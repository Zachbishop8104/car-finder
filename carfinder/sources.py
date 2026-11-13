"""
Where listings come from.

Two sources:
  1. MarketcheckSource: live dealer inventory via the Marketcheck API
     (needs a free API key; set MARKETCHECK_API_KEY in your environment
     or a .env file).
  2. SampleSource: bundled listings so you can try the tool and see
     every feature with no API key at all.

Both expose the same two methods:
  fetch()             listings matching your search criteria
  fetch_comparables() a wide pull of the same model across years and
                      mileages, used to price a car against its market
                      and to measure how it depreciates locally

Both return normalized 'listing' dicts with identical keys, so nothing
downstream cares where the data came from. Responses are cached on disk
(see http.py) so iterating on scoring doesn't burn API credits.
"""
import json
import os

from . import http

API_BASE = "https://api.marketcheck.com/v2/search/car/active"

# Marketcheck rejects a radius over 100 with HTTP 422 ("Subscribed
# package radius limit"). The exact cap is plan-dependent; 100 is what
# the developer tier allows.
MAX_RADIUS = 100

# Marketcheck normalizes all-wheel drive to "4WD": there is no "AWD"
# value in the data, so querying drivetrain=AWD silently matches nothing.
# config.yaml stays human-readable ("AWD") and we translate here.
DRIVETRAIN_QUERY = {
    "awd": "4WD",
    "all wheel drive": "4WD",
    "all-wheel drive": "4WD",
    "4wd": "4WD",
    "fwd": "FWD",
    "rwd": "RWD",
}

# Powertrain. The feed describes this in two fields with their own
# vocabularies: build.powertrain_type (Combustion, MHEV, HEV, PHEV, BEV)
# and build.fuel_type (Unleaded, Premium Unleaded, Diesel, Electric,
# "Electric / Unleaded", E85...). Config stays in plain words and is
# translated here. A mild hybrid (MHEV) counts as gas: it cannot move on
# electricity, and nobody shopping for "a hybrid" means a Wrangler with
# a belt starter. Diesel is a fuel, not a powertrain type, so it is
# asked for by fuel_type.
POWERTRAINS = ("gas", "hybrid", "plug-in hybrid", "electric", "diesel")
POWERTRAIN_ALIASES = {
    "gasoline": "gas", "petrol": "gas", "ice": "gas", "combustion": "gas",
    "hev": "hybrid",
    "phev": "plug-in hybrid", "plug in hybrid": "plug-in hybrid",
    "plugin hybrid": "plug-in hybrid", "plug-in": "plug-in hybrid",
    "ev": "electric", "bev": "electric",
}
POWERTRAIN_TYPE_QUERY = {
    "gas": ["Combustion", "MHEV"],
    "hybrid": ["HEV"],
    "plug-in hybrid": ["PHEV"],
    "electric": ["BEV"],
}

# Comparables are deliberately much wider than your search: we want the
# whole local price surface for a model, not just the slice you can afford.
#
# The price and mileage ceilings are floors for the upper bound, not
# caps: someone shopping $90k trucks needs comparables above $70k, or
# every truck looks overpriced against a pool that was cut off below it.
COMP_RADIUS_MULTIPLIER = 2
COMP_PRICE_MIN = 4000
COMP_PRICE_MAX = 70000
COMP_MILES_MAX = 160000
COMP_ROWS = 50
COMP_HEADROOM = 1.5


def _body_type(tgt_body, search):
    """Body type to query, or None for no preference."""
    return (tgt_body or search.get("body_type") or "").strip() or None


def drivetrain_param(value):
    """Translate a config drivetrain into what the API actually indexes."""
    if not value:
        return None
    return DRIVETRAIN_QUERY.get(str(value).strip().lower(), str(value).strip())


def clamp_radius(miles):
    return min(int(miles), MAX_RADIUS)


def wanted_powertrains(value):
    """Config powertrain value -> a set of POWERTRAINS, empty for "any".

    Accepts one word, a comma-separated string or a list. An unknown
    word is an error rather than a filter that silently matches nothing.
    """
    if not value:
        return set()
    items = value if isinstance(value, (list, tuple)) else str(value).split(",")
    out = set()
    for item in items:
        word = " ".join(str(item).strip().lower().split())
        if not word or word == "any":
            continue
        word = POWERTRAIN_ALIASES.get(word, word)
        if word not in POWERTRAINS:
            raise ValueError(
                f"unknown powertrain {str(item).strip()!r}; use one of: "
                + ", ".join(POWERTRAINS))
        out.add(word)
    return out


def powertrain_of(rec):
    """Which of POWERTRAINS a listing is, or None when the feed doesn't
    say. None means "can't tell", and is never a reason to drop a car."""
    kind = str(rec.get("powertrain_type") or "").strip().upper()
    fuel = str(rec.get("fuel_type") or "").strip().lower()
    if kind == "BEV":
        return "electric"
    if kind == "PHEV":
        return "plug-in hybrid"
    if kind == "HEV":
        return "hybrid"
    if kind in ("COMBUSTION", "MHEV"):
        return "diesel" if "diesel" in fuel else "gas"
    # No powertrain type. The fuel alone settles the unambiguous cases.
    if fuel == "electric":
        return "electric"
    if "diesel" in fuel:
        return "diesel"
    if fuel and "electric" not in fuel:
        return "gas"
    return None


def powertrain_matches(rec, wanted):
    kind = powertrain_of(rec)
    return not wanted or kind is None or kind in wanted


def powertrain_params(wanted):
    """API parameters for a powertrain filter, or {} when it can only be
    applied client-side (diesel mixed with something else: the API takes
    fuel type and powertrain type as two separate, AND-ed filters)."""
    if not wanted:
        return {}
    if wanted == {"diesel"}:
        return {"fuel_type": "Diesel"}
    if "diesel" in wanted:
        return {}
    kinds = []
    for name in POWERTRAINS:
        if name in wanted:
            kinds.extend(POWERTRAIN_TYPE_QUERY[name])
    return {"powertrain_type": ",".join(kinds)}


def year_range_param(search):
    """Marketcheck's year_range value ("2019-2023"), or None for any year."""
    lo, hi = search.get("year_min"), search.get("year_max")
    if not lo and not hi:
        return None
    return f"{int(lo or 1981)}-{int(hi or 2100)}"


def target_label(tgt):
    """How to name a target in messages: "Toyota Camry", "any SUV"."""
    name = f"{tgt.get('make') or ''} {tgt.get('model') or ''}".strip()
    if name:
        return name
    return f"any {tgt.get('body_type')}" if tgt.get("body_type") else "any make"


def _normalize(raw):
    """Turn a Marketcheck record into our flat listing shape."""
    build = raw.get("build", {}) or {}
    dealer = raw.get("dealer", {}) or {}
    return {
        "vin": (raw.get("vin") or "").upper(),
        "year": build.get("year"),
        "make": build.get("make", ""),
        "model": build.get("model", ""),
        "trim": build.get("trim", ""),
        "drivetrain": build.get("drivetrain", ""),
        "body_type": build.get("body_type", ""),
        "transmission": build.get("transmission", ""),
        "engine": build.get("engine", ""),
        "fuel_type": build.get("fuel_type"),
        "powertrain_type": build.get("powertrain_type"),
        "price": raw.get("price"),
        "miles": raw.get("miles"),
        "car_type": raw.get("inventory_type", ""),
        "days_on_market": raw.get("dom"),
        "dealer_name": dealer.get("name", ""),
        "dealer_city": dealer.get("city", ""),
        "dealer_state": dealer.get("state", ""),
        "distance": raw.get("dist"),
        "url": raw.get("vdp_url", ""),
        "photo": (raw.get("media", {}) or {}).get("photo_links", [None])[0],
        # Colour: the marketing name plus the API's normalized bucket.
        # The bucket ("Gray", "Blue") is what you can actually filter on;
        # the marketing name is what the window sticker says.
        "exterior_color": raw.get("exterior_color"),
        "exterior_color_group": raw.get("base_ext_color"),
        "interior_color": raw.get("interior_color"),
        "interior_color_group": raw.get("base_int_color"),
        # Carfax summary flags. DO NOT read carfax_clean_title as a title
        # brand check, it came back False on 40 of 51 cars in one real pull, and the
        # one car in it known to be flood-branded (disclosed
        # "clear flood" on the dealer's own page) has it as None, not
        # False. It tracks whether a Carfax clean-title guarantee is
        # attached, not whether the title is clean. Carried through as
        # raw data only; nothing should branch on it.
        "carfax_clean_title": raw.get("carfax_clean_title"),
        "carfax_1_owner": raw.get("carfax_1_owner"),
        "msrp": raw.get("msrp"),
        "stock_no": raw.get("stock_no"),
    }


class MarketcheckSource:
    label = "Marketcheck live inventory"

    def __init__(self, api_key):
        self.api_key = api_key
        self.calls = 0

    def _query(self, params, ttl):
        params = dict(params, api_key=self.api_key)
        self.calls += 1
        return http.get_json(API_BASE, params, ttl=ttl)

    def fetch(self, search, targets, max_results=100):
        """Pull listings for every target, giving each target a fair share
        of the result budget.

        The share matters: pulling targets in order and truncating at the
        end means the first make eats the entire budget and the rest of
        your shortlist never appears in the report.
        """
        # car_type accepts exactly one of new/used/certified, no comma
        # lists. Rather than spend a call per condition, omit it entirely
        # and filter client-side: one call per target instead of two,
        # which halves the cost of a search against a 500-call plan.
        wanted = {str(c).lower() for c in search.get("car_types", ["used"])}
        per_target = max(5, max_results // max(1, len(targets)))
        radius = clamp_radius(search["radius_miles"])
        if radius < search["radius_miles"]:
            print(f"  note: radius capped at {MAX_RADIUS} mi by your API plan")

        listings, seen = [], set()
        for tgt in targets:
            # A target may override the global body type and powertrain.
            # Feeds don't always agree with common sense about what a
            # sedan is: Marketcheck files the Kia Stinger as a Hatchback,
            # and without this the car is silently absent from results.
            # A target with no make is an open search across every make.
            want_pt = wanted_powertrains(
                tgt.get("powertrain") or search.get("powertrain"))
            params = {
                "zip": search["zip"],
                "radius": radius,
                "price_range": f'{search["price_min"]}-{search["price_max"]}',
                "miles_range": f'{search["miles_min"]}-{search["miles_max"]}',
                "rows": COMP_ROWS,
                "sort_by": "price",
                "sort_order": "asc",
            }
            body = _body_type(tgt.get("body_type"), search)
            if body:
                params["body_type"] = body
            dt = drivetrain_param(search.get("drivetrain"))
            if dt:
                params["drivetrain"] = dt
            if tgt.get("make"):
                params["make"] = tgt["make"]
            if tgt.get("model"):
                params["model"] = tgt["model"]
            years = year_range_param(search)
            if years:
                params["year_range"] = years
            params.update(powertrain_params(want_pt))
            label = target_label(tgt)
            try:
                data = self._query(params, ttl=http.TTL_LISTINGS)
            except http.FetchError as e:
                print(f"  ! query failed for {label}: {e}")
                continue

            got, wrong_pt = [], 0
            for raw in data.get("listings", []):
                rec = _normalize(raw)
                if not rec["vin"] or rec["vin"] in seen:
                    continue
                if wanted and str(rec["car_type"]).lower() not in wanted:
                    continue
                # Checked here as well as asked of the API: the API's
                # "gas" includes diesels, and a mixed request can't be
                # expressed to it at all.
                if not powertrain_matches(rec, want_pt):
                    wrong_pt += 1
                    continue
                seen.add(rec["vin"])
                got.append(rec)
            if wrong_pt:
                print(f"  · {label}: dropped {wrong_pt} that were not "
                      f"{' or '.join(sorted(want_pt))}")

            # Say when a target contributed nothing. Silently returning
            # fewer cars hides the two most common causes, a misspelled
            # model, and filters that are simply too tight, and the call
            # was already paid for either way.
            returned = len(data.get("listings", []))
            found = data.get("num_found")
            if isinstance(found, int) and found > returned > 0:
                # One call returns at most 50 cars. Say when that is a
                # slice of something much bigger, and which slice.
                print(f"  · {label}: {found:,} match; this is the "
                      f"{returned} lowest-priced. Narrow the price, "
                      f"mileage, years or model to see the rest")
            if not returned:
                print(f"  · {label}: nothing matched. Check the spelling, "
                      f"or widen price/mileage/radius")
            elif not got:
                print(f"  · {label}: {returned} found, but none were "
                      f"{' or '.join(sorted(wanted))}")

            listings.extend(got[:per_target])

        return listings[:max_results]

    def fetch_comparables(self, make, model, search, body_type=None,
                          powertrain=None):
        """A wide pull of one model locally, for pricing and depreciation.

        body_type and powertrain must match whatever the listing search
        used (a target's own value overrides the search's), or we'd be
        pricing a car against a pool it isn't in.
        """
        price_lo = min(COMP_PRICE_MIN, int(search["price_min"] * 0.5))
        price_hi = max(COMP_PRICE_MAX,
                       int(search["price_max"] * COMP_HEADROOM))
        miles_hi = max(COMP_MILES_MAX,
                       int(search["miles_max"] * COMP_HEADROOM))
        params = {
            "car_type": "used",
            "make": make,
            "zip": search["zip"],
            "radius": clamp_radius(search["radius_miles"] * COMP_RADIUS_MULTIPLIER),
            "price_range": f"{price_lo}-{price_hi}",
            "miles_range": f"0-{miles_hi}",
            "rows": COMP_ROWS,
            # Deliberately unsorted. Sorting by miles ascending returns the
            # 50 lowest-mileage cars, which skews the pool toward newer,
            # pricier trims and inflates every expected price we derive
            # from it. An arbitrary sample beats a biased one.
        }
        body = _body_type(body_type, search)
        if body:
            params["body_type"] = body
        if model:
            params["model"] = model
        dt = drivetrain_param(search.get("drivetrain"))
        if dt:
            params["drivetrain"] = dt
        # Someone shopping hybrids should have a hybrid priced against
        # hybrids, not against the cheaper gas version of the same model.
        params.update(powertrain_params(
            wanted_powertrains(powertrain or search.get("powertrain"))))
        try:
            # Cached for a week: the shape of a model's local price
            # surface doesn't shift meaningfully day to day, and this is
            # the half of a search worth not paying for twice.
            data = self._query(params, ttl=http.TTL_COMPARABLES)
        except http.FetchError as e:
            print(f"  ! comparables failed for {make} {model}: {e}")
            return []
        return [_normalize(r) for r in data.get("listings", [])]


class SampleSource:
    """Bundled data, no API key needed. Ships with a comparables pool so
    the market-price and depreciation features work in demo mode too."""

    label = "sample data"

    def __init__(self, path=None):
        here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_dir = os.path.join(here, "data")
        self.path = path or os.path.join(self.data_dir, "sample_listings.json")
        self.calls = 0

    def _load(self, name):
        p = os.path.join(self.data_dir, name)
        if not os.path.exists(p):
            return []
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)

    def fetch(self, search, targets, max_results=100):
        with open(self.path, "r", encoding="utf-8") as f:
            listings = json.load(f)
        want_pt = wanted_powertrains(search.get("powertrain"))
        kept = [r for r in listings if powertrain_matches(r, want_pt)]
        if len(kept) < len(listings):
            print(f"  · dropped {len(listings) - len(kept)} demo listings "
                  f"that were not {' or '.join(sorted(want_pt))}")
        return kept[:max_results]

    def fetch_comparables(self, make, model, search, body_type=None,
                          powertrain=None):
        mk, md = make.lower(), (model or "").lower()
        want_pt = wanted_powertrains(
            powertrain or (search or {}).get("powertrain"))
        return [
            c for c in self._load("sample_comparables.json")
            if c.get("make", "").lower() == mk
            and (not md or c.get("model", "").lower() == md)
            and powertrain_matches(c, want_pt)
        ]


def get_source(use_sample=False):
    if use_sample:
        s = SampleSource()
        return s, s.label
    key = os.environ.get("MARKETCHECK_API_KEY", "").strip()
    if not key or key == "your_key_here":
        raise RuntimeError(
            "No MARKETCHECK_API_KEY found.\n"
            "  - Get a free key at https://developers.marketcheck.com/\n"
            "  - Then either: set MARKETCHECK_API_KEY=your_key\n"
            "    or put it in a .env file (see .env.example)\n"
            "  - Or run with --sample to try the tool with demo data."
        )
    s = MarketcheckSource(key)
    return s, s.label
