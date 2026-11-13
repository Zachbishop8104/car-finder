"""
Filtering + ranking.

Every surviving listing gets a 0-100 composite score. Four components:

  reliability   long-term dependability for that generation and engine
  value         price relative to what this exact spec should cost
                locally, NOT "cheapest in the band". The cheapest car
                in a price band is usually the rough one: worst trim,
                highest wear, accident history. Below-market-for-its-
                spec is the signal that actually means "good buy".
  mileage       fewer miles is better within your band
  maintenance   how cheap and easy it is to fix

When a component has no data, an unrated model, or too few
comparables to price against, its weight is redistributed across the
components we do have, and the listing is flagged so the report can say
the ranking is partial. We never invent a middle-of-the-road number and
let it quietly move a car up the list.
"""
from . import market
from .reliability import awd_from_year, get_profile

# Legacy config key -> current one.
ALIASES = {"weight_price": "weight_value"}

# Thresholds for the "look closer at this one" flags. A car that is both
# far under market and has been sitting for months is the classic shape
# of a branded title, flood history, or a repaired wreck: the listing
# looks like a bargain precisely because nobody who inspected it bought it.
STALE_DAYS = 120
SUSPICIOUS_UNDER_PCT = 0.15
ABSURD_UNDER_PCT = 0.25

# A score built from one surviving component is not comparable to one
# built from all four, but it looks identical on the page. Shrink toward
# neutral in proportion to how much of the weight we actually had, so a
# car known only by its odometer can't outrank a fully evaluated one.
NEUTRAL_SCORE = 0.5


def _canonical_drivetrain(text):
    """Collapse the many spellings feeds use into AWD / FWD / RWD.

    Returns None when there's nothing to compare, an empty config value
    (no preference) or a listing that didn't report one. Unknown means
    "don't filter on this", never "reject".
    """
    t = str(text or "").strip().lower()
    if not t:
        return None
    if any(k in t for k in ("awd", "4wd", "all wheel", "all-wheel",
                            "4 wheel", "4-wheel", "four wheel", "4x4")):
        return "AWD"
    # "4x2" is deliberately not here: on a pickup it means rear-drive,
    # on a crossover front-drive. Unknown is safer than a wrong reject.
    if any(k in t for k in ("fwd", "front wheel", "front-wheel")):
        return "FWD"
    if any(k in t for k in ("rwd", "rear wheel", "rear-wheel")):
        return "RWD"
    return None


def _passes_hard_filters(rec, search):
    """Drop anything that clearly doesn't match, even if the API was loose."""
    price = rec.get("price")
    miles = rec.get("miles")
    if price is None or miles is None:
        return False, "missing price or mileage"
    if not (search["price_min"] <= price <= search["price_max"]):
        return False, "outside price band"
    if not (search["miles_min"] <= miles <= search["miles_max"]):
        return False, "outside mileage band"

    # Model year. Enforced here whether or not the source could filter
    # on it. A listing with no year is kept: unknown is not a mismatch.
    year = rec.get("year")
    try:
        year = int(year) if year else None
    except (TypeError, ValueError):
        year = None
    lo, hi = search.get("year_min"), search.get("year_max")
    if year and ((lo and year < int(lo)) or (hi and year > int(hi))):
        return False, "outside model-year range"

    # Drivetrain sanity. Feeds are inconsistent here: Marketcheck reports
    # all-wheel-drive cars as "4WD" with no "AWD" value in the data at
    # all, while others say "AWD" / "All Wheel Drive". For a passenger car
    # the distinction is academic, anything driving all four wheels
    # counts, so both normalize to AWD.
    want = _canonical_drivetrain(search.get("drivetrain"))
    got = _canonical_drivetrain(rec.get("drivetrain"))
    if want and got and want != got:
        return False, f"not {want}"

    # AWD availability by model-year (e.g. a "2018 Camry AWD" cannot exist).
    first = awd_from_year(rec.get("make"), rec.get("model"))
    year = rec.get("year") or 0
    if want == "AWD" and first and year and int(year) < first:
        return False, f"{rec.get('make')} {rec.get('model')} had no AWD in {year}"
    rec["awd_year_verified"] = bool(first)

    return True, None


def _flags(rec, pricing, profile):
    """Things worth a second look before you drive out to see it."""
    out = []

    # A known failure pattern for this generation. Deliberately a flag
    # rather than a score penalty: a good enough price could always
    # outvote the penalty, and then the warning silently disappears.
    if profile.get("risk"):
        out.append(profile["risk"])

    dom = rec.get("days_on_market")
    stale = isinstance(dom, (int, float)) and dom > STALE_DAYS
    # Only a high-confidence price gets to imply something is wrong with
    # the car. A cross-trim estimate showing 20% off is far more likely
    # to be a bad comparison than a bad title.
    cheap = (bool(pricing) and pricing.get("confidence") == "high"
             and pricing["delta_pct"] > SUSPICIOUS_UNDER_PCT)

    if stale:
        out.append(f"on the lot {int(dom)} days")
    if cheap:
        out.append(f"{pricing['delta_pct'] * 100:.0f}% under market")
    if stale and cheap:
        out.append("cheap and unsold for months: check the title and "
                   "accident history before anything else")
    return out


def _norm(value, lo, hi, higher_is_better):
    """Scale value into 0..1. Guards against divide-by-zero."""
    if hi == lo:
        return 0.5
    frac = max(0.0, min(1.0, (value - lo) / (hi - lo)))
    return frac if higher_is_better else (1.0 - frac)


# How much of a low-confidence market delta to believe when ranking. If
# an estimate isn't solid enough to warn about, it isn't solid enough to
# put a car at the top of the list either.
LOW_CONFIDENCE_WEIGHT = 0.5


def _value_score(pricing):
    """Map a market delta onto 0..1, with at-market = 0.5.

    Credit for being under market stops at SUSPICIOUS_UNDER_PCT and
    reverses past ABSURD_UNDER_PCT. A car 35% below its comparables is
    not a 35% better buy, that is roughly what a branded title, flood
    history or a botched repair looks like in the price. Rewarding it
    linearly puts damaged cars at the top of the list, directly
    contradicting the warning flag on the same row.
    """
    delta = pricing["delta_pct_clamped"]
    if delta > SUSPICIOUS_UNDER_PCT:
        excess = delta - SUSPICIOUS_UNDER_PCT
        delta = SUSPICIOUS_UNDER_PCT
        if pricing["delta_pct_clamped"] > ABSURD_UNDER_PCT:
            delta -= pricing["delta_pct_clamped"] - ABSURD_UNDER_PCT
        del excess

    raw = 0.5 + delta / (2 * market.MAX_DELTA)
    raw = max(0.0, min(1.0, raw))
    if pricing.get("confidence") != "high":
        raw = 0.5 + (raw - 0.5) * LOW_CONFIDENCE_WEIGHT
    return raw


def _weights(scoring):
    w = {}
    for key, value in scoring.items():
        w[ALIASES.get(key, key)] = value
    return {
        "reliability": float(w.get("weight_reliability", 0.35)),
        "value": float(w.get("weight_value", 0.30)),
        "mileage": float(w.get("weight_mileage", 0.20)),
        "maintenance": float(w.get("weight_maintenance", 0.15)),
    }


def score_and_rank(listings, search, scoring, comps_by_model=None,
                   current_year=None):
    """Filter, score and sort listings best-first.

    comps_by_model maps (make_lower, model_lower) -> comparable listings.
    Pass it to enable market-relative value scoring; without it, value is
    simply treated as unavailable and its weight is redistributed.
    """
    comps_by_model = comps_by_model or {}
    kept, rejected = [], []
    for r in listings:
        ok, why = _passes_hard_filters(r, search)
        (kept if ok else rejected).append(r if ok else dict(r, rejected_because=why))
    if not kept:
        return [], rejected

    m_lo, m_hi = search["miles_min"], search["miles_max"]
    w = _weights(scoring)

    for r in kept:
        prof = get_profile(r.get("make"), r.get("model"), r.get("year"))
        comps = comps_by_model.get(
            (str(r.get("make", "")).lower(), str(r.get("model", "")).lower()), []
        )
        pricing = market.expected_price(r, comps, current_year) if comps else None

        parts = {
            "mileage": _norm(r["miles"], m_lo, m_hi, higher_is_better=False),
            "reliability": (prof["reliability"] / 10.0
                            if prof["reliability"] is not None else None),
            "maintenance": (prof["maintenance"] / 10.0
                            if prof["maintenance"] is not None else None),
            "value": _value_score(pricing) if pricing else None,
        }

        available = {k: v for k, v in parts.items() if v is not None}
        total_w = sum(w[k] for k in available) or 1.0
        composite = sum(w[k] * v for k, v in available.items()) / total_w

        # Renormalizing alone treats "great on the one axis we measured"
        # as equivalent to "great on all four". Pull the score toward
        # neutral by how much of the weight was actually available, so
        # thin evidence produces a middling score rather than a confident
        # one in either direction.
        coverage = total_w / sum(w.values())
        composite = NEUTRAL_SCORE + (composite - NEUTRAL_SCORE) * coverage

        r["score"] = round(composite * 100, 1)
        r["evidence_coverage"] = round(coverage, 2)
        r["score_components"] = {
            k: (round(v, 3) if v is not None else None) for k, v in parts.items()
        }
        r["missing_components"] = sorted(set(parts) - set(available))
        r["generation"] = prof["generation"]
        r["engine_profile"] = prof["engine"]
        r["reliability"] = prof["reliability"]
        r["maintenance"] = prof["maintenance"]
        r["known_issues"] = prof["known_issues"]
        r["note"] = prof["note"]
        r["unrated"] = bool(prof.get("unrated"))
        r["market"] = pricing
        r["risk"] = prof.get("risk")
        r["flags"] = _flags(r, pricing, prof)

    kept.sort(key=lambda r: r["score"], reverse=True)
    return kept, rejected
