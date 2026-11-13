"""
Reliability, maintenance and ownership-cost reference data.

Keyed by generation and engine, not by model. "Camry reliability" is a
meaningless number, the 2.5L four, the hybrid, and the AWD-specific
setup are different cars with different failure modes. Each profile
therefore carries a year range and the engine it applies to.

Scales:
  reliability  0-10, long-term dependability (higher = better)
  maintenance  0-10 EASE of repair (10 = cheap, parts everywhere)

An optional "risk" field marks a generation with a known, expensive
failure pattern. It becomes a visible warning on the listing rather than
a quiet drag on the score, so a cheap price can't outvote it, a car you
should think twice about stays legible even when it ranks well.

Cost fields feed the 5-year TCO estimate in tco.py. They are editable
estimates, not quotes, order-of-magnitude figures distilled from
published repair-cost averages. Tune them if you have better local
numbers; every one of them is just a starting point.

When a car has no profile it is NOT given an invented middle score.
It's marked unrated, ranked on the data we do have, and flagged in the
report so you know the ranking is partial.

Profiles live one file per make in carfinder/profiles/<make>.py and are
loaded on demand, so a run only needs the files for the makes it is
actually looking at. A make with no file is simply unrated.

Reading the numbers in the profiles:

  COMPLAINT COUNTS SCALE WITH SALES. NHTSA totals are higher for cars
  that sold more, so a bare total says little. Counts are compared
  within a model over time, or where one component is a lopsided share
  of that car's own file, that shape survives the volume problem.

  RECALL COUNT IS THE VOLUME-PROOF SIGNAL. A campaign is opened per
  defect, not per car, so recall counts are directly comparable between
  models. Where the two signals disagree, trust the recalls.

  DEPRECIATION FIGURES ARE FROM ONE MARKET. The %/yr numbers quoted in
  some profiles were measured from listings in a single Michigan market
  in Aug 2026. They are illustrative, not national, the research phase
  fits a curve for the user's own area, and that is the one to trust.

  HONDA SEDANS HAVE A DATA GAP. The NHTSA complaints endpoint returned
  an empty set for Accord and Civic while returning full files for
  Honda's SUVs. That is an API quirk, not a clean record, so those
  scores lean on recall campaigns and are marked provisional.
"""
import importlib
import os
import re

_PROFILE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "profiles")
_loaded = {}

# Which model years a given make/model actually offered AWD. Used as a
# hard filter: a "Camry AWD" listed as a 2018 is a data error or a lie.
AWD_AVAILABILITY = {
    ("toyota", "camry"): 2020,
    ("toyota", "avalon"): 2021,
    ("toyota", "crown"): 2023,       # AWD standard on every Crown
    ("toyota", "corolla"): 2023,     # AWD only on the hybrid, from 2023
    ("kia", "k5"): 2021,
    ("lexus", "es"): 2021,           # the AWD one is the ES 250
    ("lexus", "es hybrid"): 2021,    # ES 300h gained AWD for 2021
    ("mazda", "mazda3"): 2019,
    ("nissan", "altima"): 2019,
    ("subaru", "legacy"): 1990,   # AWD standard on every Legacy
    ("subaru", "impreza"): 1993,  # AWD standard on every Impreza
    ("subaru", "outback"): 1995,
    ("subaru", "crosstrek"): 2013,
}


# Used when a car has no profile. Deliberately has no reliability or
# maintenance number: we score what we know and say so.
UNRATED_PROFILE = {
    "generation": None,
    "engine": None,
    "reliability": None,
    "maintenance": None,
    "annual_maintenance_usd": None,
    "insurance_factor": 1.0,
    "tire_set_usd": 750,
    "known_issues": [],
    "risk": None,
    "note": "No reliability profile for this model year, so it is ranked "
            "on price and mileage only. Shortlist it to pull its recalls, "
            "complaints and running costs.",
    "unrated": True,
}


def _slug(make):
    return re.sub(r"[^a-z0-9]+", "_", str(make or "").lower()).strip("_")


def profiles_for(make):
    """Profiles for one make, or [] if there is no file for it."""
    slug = _slug(make)
    if slug not in _loaded:
        found = []
        if slug and os.path.isfile(os.path.join(_PROFILE_DIR, slug + ".py")):
            mod = importlib.import_module(f"{__package__}.profiles.{slug}")
            found = list(mod.PROFILES)
        _loaded[slug] = found
    return _loaded[slug]


def all_profiles():
    """Every profile that shipped with this copy of the code."""
    out = []
    if os.path.isdir(_PROFILE_DIR):
        for name in sorted(os.listdir(_PROFILE_DIR)):
            if name.endswith(".py") and not name.startswith("_"):
                out.extend(profiles_for(name[:-3]))
    return out


def _model_key(model):
    """Model name reduced to letters and digits, so "F-150", "F150" and
    "f 150" are one model. Feeds do not agree on the punctuation."""
    return re.sub(r"[^a-z0-9]+", "", str(model or "").lower())


# Feeds often list an electrified version as its own model ("RAV4
# Hybrid", "Accord Hybrid", "Wrangler 4xe"). It shares a generation with
# the plain model, so that profile is used when it has none of its own.
_VARIANT_SUFFIX = re.compile(
    r"\s+(plug[- ]?in hybrid|hybrid|phev|prime|energi|4xe)\s*$")


def _base_model(model):
    """The model name without a trailing powertrain word, or None."""
    name = str(model or "").strip().lower()
    base = _VARIANT_SUFFIX.sub("", name)
    return base if base and base != name else None


def get_profile(make, model, year=None):
    """Best profile for a make/model/year, or the unrated placeholder."""
    for name in (model, _base_model(model)):
        if not name:
            continue
        md = _model_key(name)
        fallback = None
        for p in profiles_for(make):
            if _model_key(p["model"]) != md:
                continue
            lo, hi = p["years"]
            if year and lo <= int(year) <= hi:
                return dict(p, unrated=False)
            fallback = fallback or p

        if fallback and not year:
            # No year to match on. The first profile for that model is
            # the least-wrong guess.
            return dict(fallback, unrated=False)

    return dict(UNRATED_PROFILE)


def awd_from_year(make, model):
    """First model year this make/model offered AWD, or None if unknown."""
    key = (str(make or "").strip().lower(), str(model or "").strip().lower())
    return AWD_AVAILABILITY.get(key)
