"""
What a car *should* cost, and what it will be worth later.

Both answers come from the same place: a wide pull of comparable
listings for the same make and model in your own market. That matters
more than a national average, a Legacy in Michigan is not priced like
a Legacy in Arizona.

  expected_price()      fits price against age and mileage, so we can
                        say "this one is $1,900 under market" instead of
                        "this one is the cheapest in the band". The
                        cheapest listing in a band is usually the rough
                        one; below-market-for-its-spec is the real signal.

  depreciation_curve()  medians by model year give an observed local
                        retention rate, which we project forward.

No numpy, the regression is a 3-parameter ordinary least squares solved
with Gaussian elimination, which is about 30 lines and no dependency.
"""
import statistics

# Three tiers, most-trusted first. Rare configurations (an AWD Mazda3,
# say) can have single-digit comparables in a whole metro area, which is
# too thin to regress but not too thin to say anything at all.
MIN_FOR_REGRESSION = 12   # full fit on age + mileage
MIN_FOR_WINDOW = 6        # median of nearby model years, adjusted
MIN_FOR_MEDIAN = 4        # median of the same model year

YEAR_WINDOW = 1
# Used only to shift a comp onto the target car's age/mileage in the
# windowed tier. Deliberately generic: if we had enough data to
# estimate these we'd be in the regression tier instead.
FALLBACK_RETENTION = 0.87
FALLBACK_MILEAGE_COEF = 0.06

# Sanity clamp: no single listing is 40% off market. A number that
# extreme means bad data (salvage title, stripped trim, typo'd price).
MAX_DELTA = 0.40

# A mileage slope needs the comps to actually span some mileage. Four
# new cars all within a few hundred miles of each other describe trim,
# not wear, and the slope through them is noise.
MIN_MILEAGE_SPREAD = 5000

# How far past the comps' mileage range a fit may be evaluated, as a
# fraction of that range. Beyond this it is extrapolation.
EXTRAPOLATION_MARGIN = 0.15


def _trim_key(trim):
    """Normalized trim for like-for-like matching, or None if unknown."""
    t = str(trim or "").strip().lower()
    return t or None


def _same_year_estimate(rows, age, miles, trim=None):
    """Expected price from same-model-year comps, fitted on mileage.

    This is the most trustworthy estimate available and it is tried
    first. Comps from the same year share a generation, so the main
    things left to explain are trim and wear. Both have to be handled or
    the answer is worse than no answer:

    TRIM. Same model year is not the same car. A base Corolla Cross L
    priced against four XLE/XSE comps produced a $40,298 "expected" on a
    car whose own window sticker said $27,239, a fabricated $12.7k
    discount, at the top of the rankings, marked high confidence. So the
    same-trim pool is tried first and a cross-trim answer is never
    better than a median, never a fit.

    MILEAGE. A slope is only meaningful inside the mileage range the
    comps actually cover, and only if they cover a range at all. Fitting
    four cars between 4.8k and 17.7k miles and then evaluating at 0 is
    extrapolation, which is exactly what the regression tier below
    already refuses to do for age.

    Returns (expected, sample_size, quality), where quality is one of
    "trim-fit", "trim-median", "mixed-median", or None.
    """
    same = [(m, p, t) for a_, m, p, t in rows if a_ == age]
    if len(same) < MIN_FOR_MEDIAN:
        return None, 0, None

    # Prefer comps of the same trim. Only that pool earns a fit.
    key = _trim_key(trim)
    pool = [(m, p) for m, p, t in same if key and _trim_key(t) == key]
    matched = len(pool) >= MIN_FOR_MEDIAN
    if not matched:
        # Trims are mixed, so the spread across this pool is mostly
        # equipment, not wear. A median is the only defensible read.
        prices = [p for _, p, _ in same]
        return statistics.median(prices), len(same), "mixed-median"

    n = len(pool)
    prices = [p for _, p in pool]
    mileages = [m for m, _ in pool]
    lo_m, hi_m = min(mileages), max(mileages)

    # No fit without real mileage spread, and no fit outside the range
    # the comps cover. Either way fall back to the same-trim median,
    # which is still a genuinely like-for-like number.
    if hi_m - lo_m < MIN_MILEAGE_SPREAD:
        return statistics.median(prices), n, "trim-median"
    margin = (hi_m - lo_m) * EXTRAPOLATION_MARGIN
    if not (lo_m - margin <= miles <= hi_m + margin):
        return statistics.median(prices), n, "trim-median"

    sx = sum(mileages)
    sy = sum(prices)
    sxx = sum(m * m for m in mileages)
    sxy = sum(m * p for m, p in pool)
    denom = n * sxx - sx * sx
    if abs(denom) < 1e-9:
        return statistics.median(prices), n, "trim-median"

    slope = (n * sxy - sx * sy) / denom
    expected = (sy - slope * sx) / n + slope * miles

    # Even inside the mileage range a steep slope on a small n can land
    # somewhere silly. Keep the fit near the observed price range.
    lo, hi = min(prices), max(prices)
    if not (lo * 0.85 <= expected <= hi * 1.15):
        return statistics.median(prices), n, "trim-median"
    return expected, n, "trim-fit"


def _solve3(a, b):
    """Solve a 3x3 linear system by Gaussian elimination with partial
    pivoting. Returns None if the matrix is singular."""
    m = [list(row) + [rhs] for row, rhs in zip(a, b)]
    n = 3
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(m[r][col]))
        if abs(m[piv][col]) < 1e-12:
            return None
        m[col], m[piv] = m[piv], m[col]
        for r in range(col + 1, n):
            f = m[r][col] / m[col][col]
            for c in range(col, n + 1):
                m[r][c] -= f * m[col][c]
    x = [0.0] * n
    for r in reversed(range(n)):
        s = m[r][n] - sum(m[r][c] * x[c] for c in range(r + 1, n))
        x[r] = s / m[r][r]
    return x


def _fit(rows):
    """OLS of price on (age_years, miles_per_10k). Returns coefficients."""
    n = len(rows)
    sx = [0.0] * 3
    sxx = [[0.0] * 3 for _ in range(3)]
    sxy = [0.0] * 3
    for age, miles, price, _ in rows:
        feats = (1.0, float(age), miles / 10000.0)
        for i in range(3):
            sx[i] += feats[i]
            sxy[i] += feats[i] * price
            for j in range(3):
                sxx[i][j] += feats[i] * feats[j]
    del n, sx
    return _solve3(sxx, sxy)


def _usable(comps, current_year):
    rows = []
    for c in comps:
        price, miles, year = c.get("price"), c.get("miles"), c.get("year")
        if not isinstance(price, (int, float)) or price <= 0:
            continue
        if not isinstance(miles, (int, float)) or miles < 0:
            continue
        if not year:
            continue
        rows.append((max(0, current_year - int(year)), float(miles),
                     float(price), c.get("trim")))
    return rows


def expected_price(listing, comps, current_year):
    """Model-implied price for this exact car, plus how far off it is.

    Returns a dict with expected, delta_usd (positive = a deal),
    delta_pct, basis, and sample size, or None if there isn't enough
    comparable data to say anything honest.
    """
    price = listing.get("price")
    miles = listing.get("miles")
    year = listing.get("year")
    if not all(isinstance(v, (int, float)) for v in (price, miles)) or not year:
        return None

    # A new car has a published price for its exact trim and equipment:
    # the window sticker. That beats any comp pool, and it is the only
    # thing that reads a 0-mile base trim correctly when the only
    # same-year comps on the market are used higher trims.
    msrp = listing.get("msrp")
    if (listing.get("car_type") == "new"
            and isinstance(msrp, (int, float)) and msrp > 0):
        delta_usd = msrp - price
        delta_pct = delta_usd / msrp
        return {
            "expected": round(msrp),
            "delta_usd": round(delta_usd),
            "delta_pct": round(delta_pct, 4),
            "delta_pct_clamped": round(
                max(-MAX_DELTA, min(MAX_DELTA, delta_pct)), 4),
            "basis": "MSRP for this exact trim (new car)",
            "confidence": "high",
            "sample_size": 1,
            "pool_size": len(comps),
        }

    rows = _usable(comps, current_year)
    if len(rows) < MIN_FOR_MEDIAN:
        return None

    age = max(0, current_year - int(year))
    ages = [a for a, _, _, _ in rows]
    expected = None
    basis = None
    used = len(rows)
    quality = None

    # 1. Same model year, matched on trim where possible and fitted on
    #    mileage. Most trustworthy, no age extrapolation, and no
    #    pricing an L against a pool of XSEs.
    same_year, n_same, quality = _same_year_estimate(
        rows, age, miles, listing.get("trim"))
    if same_year:
        expected = same_year
        used = n_same
        basis = {
            "trim-fit": f"same-year, same-trim comps fitted on mileage "
                        f"(n={n_same})",
            "trim-median": f"median of {n_same} same-year, same-trim comps",
            "mixed-median": f"median of {n_same} same-year comps across "
                            f"mixed trims",
        }[quality]

    # 2. Otherwise regress on age + mileage, but only interpolating.
    #    Extrapolating past the oldest or newest comp is where this model
    #    goes badly wrong.
    if (expected is None or expected <= 0) and len(rows) >= MIN_FOR_REGRESSION \
            and min(ages) <= age <= max(ages):
        coef = _fit(rows)
        if coef:
            expected = coef[0] + coef[1] * age + coef[2] * (miles / 10000.0)
            basis = "regression on age + mileage"

    if (expected is None or expected <= 0) and len(rows) >= MIN_FOR_WINDOW:
        # Too thin to regress: take nearby model years and shift each comp
        # onto our car's age and mileage before taking the median.
        window = [(a, m, p) for a, m, p, _ in rows if abs(a - age) <= YEAR_WINDOW]
        if len(window) >= MIN_FOR_MEDIAN:
            adjusted = [
                p * (FALLBACK_RETENTION ** (age - a))
                + FALLBACK_MILEAGE_COEF * (m - miles)
                for a, m, p in window
            ]
            expected = statistics.median(adjusted)
            used = len(window)
            basis = (f"median of {len(window)} comps within "
                     f"±{YEAR_WINDOW} model year, age/mileage adjusted")

    if expected is None or expected <= 0:
        return None

    delta_usd = expected - price
    delta_pct = delta_usd / expected if expected else 0.0
    clamped = max(-MAX_DELTA, min(MAX_DELTA, delta_pct))

    return {
        "expected": round(expected),
        "delta_usd": round(delta_usd),
        "delta_pct": round(delta_pct, 4),
        "delta_pct_clamped": round(clamped, 4),
        "basis": basis,
        # Only a like-for-like estimate is trustworthy enough to act on.
        # Every other path mixes trims, across model years in the lower
        # tiers, within one year in "mixed-median", and that is exactly
        # what manufactures a 20% "discount" out of an L priced against
        # a pool of XSEs.
        "confidence": "high" if quality in ("trim-fit", "trim-median") else "low",
        "sample_size": used,
        "pool_size": len(rows),
    }


def depreciation_curve(comps, current_year, min_per_year=3):
    """Observed local price-by-model-year for one model.

    Returns median price per year, the implied average annual retention
    rate, and the sample behind each point. None if the data is too thin
    to be worth reporting.
    """
    by_year = {}
    for c in comps:
        price, year = c.get("price"), c.get("year")
        if isinstance(price, (int, float)) and price > 0 and year:
            by_year.setdefault(int(year), []).append(float(price))

    points = [
        {
            "year": y,
            "age": max(0, current_year - y),
            "median_price": round(statistics.median(ps)),
            "sample": len(ps),
        }
        for y, ps in sorted(by_year.items())
        if len(ps) >= min_per_year
    ]
    if len(points) < 3:
        return None

    # Retention between consecutive points, normalized to a per-year rate.
    # Consecutive *points* are not necessarily consecutive *years*, thin
    # model years get dropped above, so a pair can straddle a three-year
    # gap. Treating that drop as one year's worth of depreciation is how
    # a Camry ends up looking like it loses 20% a year.
    ratios = []
    ordered = sorted(points, key=lambda p: p["age"])
    for newer, older in zip(ordered, ordered[1:]):
        gap = older["age"] - newer["age"]
        if gap <= 0 or older["median_price"] <= 0 or newer["median_price"] <= 0:
            continue
        total = older["median_price"] / newer["median_price"]
        if not 0 < total < 1.0:
            continue
        annual = total ** (1.0 / gap)
        if 0.5 < annual < 1.0:  # ignore nonsense from thin or mixed-trim years
            ratios.append(annual)
    if not ratios:
        return None

    product = 1.0
    for r in ratios:
        product *= r
    retention = product ** (1.0 / len(ratios))

    return {
        "points": points,
        "annual_retention": round(retention, 4),
        "annual_depreciation_pct": round((1 - retention) * 100, 1),
        "years_observed": len(points),
        "total_comparables": sum(p["sample"] for p in points),
    }


def project_value(price, curve, years=5):
    """What this car is likely worth after `years`, per the local curve.

    Falls back to a conservative generic rate when we have no curve, and
    says which one it used so nothing looks more precise than it is.
    """
    if curve and curve.get("annual_retention"):
        rate = curve["annual_retention"]
        basis = "local market curve"
    else:
        rate = 0.87  # broad used-car default
        basis = "generic 13%/yr fallback"

    value = price * (rate ** years)
    return {
        "years": years,
        "projected_value": round(value),
        "total_depreciation": round(price - value),
        "annual_retention": round(rate, 4),
        "basis": basis,
    }
