"""
Interactive first-run setup.

Asks what you're looking for and writes config.yaml (your search) and
.env (your API key) into the data folder (see paths.py), so nothing
personal ever lands in the code.

Re-running is safe: existing answers become the defaults, so you can
change one thing and press Enter through the rest.
"""
import os
import sys

from .reliability import all_profiles
from .sources import MAX_RADIUS

CONFIG_TEMPLATE = """\
# ============================================================
# Car Finder: your search configuration
#
# Written by `python run.py setup`. Safe to hand-edit afterwards;
# re-running setup will use these values as its defaults.
#
# See config.example.yaml, next to the code, for the template.
# ============================================================

search:
  zip: "{zip}"
  radius_miles: {radius}
  price_min: {price_min}
  price_max: {price_max}
  miles_min: 0
  miles_max: {miles_max}
  body_type: "{body_type}"
  drivetrain: "{drivetrain}"
  # gas, hybrid, plug-in hybrid, electric, diesel, or "" for any
  powertrain: "{powertrain}"
{years}
  # Which listing conditions to include: used, certified, new
  car_types:
{car_types}

# The models to search for. "model" is optional; leave it out to search
# everything from that make matching your filters. With no targets at
# all, every make that fits the filters above is searched.
{targets}

# How results get ranked. Weights should sum to ~1.0.
#
# Price and mileage lead on purpose: they're known for every car, so a
# model with a reliability profile and one without still compete on the
# same basis. Reliability breaks near-ties rather than deciding the list,
# and anything with a known problem gets flagged regardless of rank.
#
# Raise weight_reliability if you'd rather the first pass actively steer
# you toward models you've profiled.
scoring:
  weight_value: {w_val}         # price vs. what this spec should cost locally
  weight_mileage: {w_mil}       # fewer miles scores higher
  weight_reliability: {w_rel}   # dependability of that generation + engine
  weight_maintenance: {w_mnt}   # cheaper/easier to fix scores higher

# Inputs to the 5-year cost-of-ownership estimate (`run.py research`).
ownership:
  years: 5
  annual_miles: {annual_miles}
  fuel_price_per_gallon: {fuel_price}
  baseline_insurance_annual: {insurance}   # your real premium, not an average
  tire_replacement_interval_miles: 45000
  annual_registration_usd: {registration}
  maintenance_escalation_per_10k: 0.06

# Marketcheck plan limits. The free tier is 500 calls total, 5 req/sec.
# Check where you stand with:  python run.py usage
api:
  call_limit: {call_limit}            # refuse to spend past this; null = unlimited
  warn_at_pct: 80
  max_requests_per_second: 4
  # When a search names no model, how many of the models it finds to
  # price against the market, at one call each.
  price_models: {price_models}

output:
  max_results: 100
  open_report_when_done: {open_report}
"""

BODY_TYPES = ["Sedan", "SUV", "Pickup", "Coupe", "Hatchback", "Wagon",
              "Minivan", "Convertible", ""]
# Makes whose name is two words, so "Land Rover Defender" doesn't become
# make "Land", model "Rover Defender".
TWO_WORD_MAKES = {"land rover", "alfa romeo", "aston martin"}
POWERTRAIN_CHOICES = [
    ("gas", "petrol only, including mild hybrids"),
    ("hybrid", "self-charging hybrid"),
    ("plug-in hybrid", "hybrid you can charge"),
    ("electric", "battery only"),
    ("diesel", ""),
    ("", "no preference"),
]
DRIVETRAINS = [
    ("AWD", "all-wheel drive (best for snow)"),
    ("FWD", "front-wheel drive"),
    ("RWD", "rear-wheel drive"),
    ("", "no preference"),
]


# ------------------------------------------------------------ prompting

class Abort(Exception):
    """User pressed Ctrl-C."""


class NoInput(Abort):
    """stdin ran dry, not a terminal, or a script piped too few answers."""


def _input(prompt):
    """Read one answer. Works interactively or from piped input, so the
    wizard can be scripted and tested."""
    try:
        # A piped first answer can carry a byte-order mark; drop it.
        return input(prompt).lstrip("﻿")
    except EOFError:
        raise NoInput()
    except KeyboardInterrupt:
        raise Abort()


def ask(question, default=None, hint=None):
    suffix = f" [{default}]" if default not in (None, "") else ""
    if hint:
        print(f"  {hint}")
    answer = _input(f"  {question}{suffix}: ").strip()
    return answer or (str(default) if default is not None else "")


def ask_year(question, default=None):
    """A model year, or None when the answer is blank or "any"."""
    while True:
        raw = ask(question, default if default else "any").strip().lower()
        if raw in ("", "any", "none"):
            return None
        if raw.isdigit() and 1981 <= int(raw) <= 2100:
            return int(raw)
        print("    ! enter a four-digit year, or press Enter for any")


def ask_int(question, default=None, lo=None, hi=None, hint=None):
    while True:
        raw = ask(question, default, hint)
        hint = None  # only show it the first time
        cleaned = raw.replace(",", "").replace("$", "").strip().lower()
        if cleaned.endswith("k") and cleaned[:-1].replace(".", "").isdigit():
            cleaned = str(int(float(cleaned[:-1]) * 1000))
        try:
            value = int(float(cleaned))
        except ValueError:
            print("    ! enter a number")
            continue
        if lo is not None and value < lo:
            print(f"    ! must be at least {lo}")
            continue
        if hi is not None and value > hi:
            print(f"    ! must be at most {hi}")
            continue
        return value


def ask_float(question, default=None, hint=None):
    while True:
        raw = ask(question, default, hint)
        hint = None
        try:
            return float(raw.replace("$", "").strip())
        except ValueError:
            print("    ! enter a number")


def ask_choice(question, options, default=None, hint=None):
    """options: list of (value, description)."""
    if hint:
        print(f"  {hint}")
    for i, (value, desc) in enumerate(options, 1):
        label = value or "(any)"
        print(f"    {i}) {label:10} {desc}")
    default_idx = None
    for i, (value, _) in enumerate(options, 1):
        if value == default:
            default_idx = i
    while True:
        raw = _input(f"  {question}"
                     f"{f' [{default_idx}]' if default_idx else ''}: ").strip()
        if not raw and default_idx:
            return options[default_idx - 1][0]
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return options[int(raw) - 1][0]
        # allow typing the value directly
        for value, _ in options:
            if raw.lower() == value.lower() and value:
                return value
        print(f"    ! pick 1-{len(options)}")


def ask_yes_no(question, default=False):
    suffix = "[Y/n]" if default else "[y/N]"
    while True:
        raw = _input(f"  {question} {suffix}: ").strip().lower()
        if not raw:
            return default
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("    ! y or n")


def header(text):
    print(f"\n{text}")
    print("─" * max(24, len(text)))


# --------------------------------------------------------------- models

def profiled_models():
    """Models we have reliability data for, so setup can say so."""
    seen, out = set(), []
    for p in all_profiles():
        key = (p["make"], p["model"])
        if key not in seen:
            seen.add(key)
            out.append((p["make"].title(), p["model"].title()))
    return out


def ask_targets(current):
    """Ask which models to track.

    Any make and model works. Some ship with a reliability profile; the
    rest are searched, priced and ranked the same way and marked
    "unrated", which is a completely normal state, not a downgrade.
    """
    known = profiled_models()

    print("  Type any 'Make Model' you want to track, comma separated.")
    print("  Examples: BMW 330i, Ford F-150, Honda CR-V, Tesla Model 3")
    print("  Or type 'any' to search every make that fits your filters.")
    print(f"  ({len(known)} models ship with reliability profiles; anything "
          f"else is")
    print("  ranked without a reliability score until you add one.)")
    print()

    default = ""
    if current:
        default = ", ".join(
            f"{t.get('make', '')} {t.get('model', '')}".strip()
            for t in current if t.get("make")
        ) or "any"

    raw = ask("Models to track", default)
    if raw.strip().lower() in ("any", "all", "*"):
        return []

    targets, unknown = [], []
    for piece in raw.split(","):
        piece = piece.strip()
        if not piece:
            continue
        # Keep whatever casing they typed. Title-casing turns CR-V
        # into Cr-V and BMW into Bmw; the API is case-insensitive, so
        # mangling it buys nothing and looks broken in the config.
        words = piece.split()
        n = 2 if " ".join(words[:2]).lower() in TWO_WORD_MAKES else 1
        make, model = " ".join(words[:n]), " ".join(words[n:])
        known_lower = {(mk.lower(), md.lower()) for mk, md in known}
        if model and (make.lower(), model.lower()) not in known_lower:
            unknown.append(f"{make} {model}")
        entry = {"make": make, "model": model}
        if entry not in targets:
            targets.append(entry)

    if unknown:
        print(f"    note: no reliability profile yet for "
              f"{', '.join(unknown)}. Those cars will be marked 'unrated'.")
    return targets


# ----------------------------------------------------------------- .env

def write_env(repo_root, key):
    """Set the key in .env, leaving every other line alone.

    Only called when the key actually changed, there's no reason to
    rewrite someone's .env just to put back what was already in it.
    """
    os.makedirs(repo_root, exist_ok=True)
    path = os.path.join(repo_root, ".env")
    lines = []
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            lines = f.read().splitlines()
    else:
        lines = ["# Secrets for car-finder. Never commit this file.",
                 "# Free key: https://developers.marketcheck.com/"]

    replaced = False
    for i, line in enumerate(lines):
        if line.strip().startswith("MARKETCHECK_API_KEY"):
            lines[i] = f"MARKETCHECK_API_KEY={key}"
            replaced = True
            break
    if not replaced:
        lines.append(f"MARKETCHECK_API_KEY={key}")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip("\n") + "\n")
    return path


def existing_key(repo_root):
    path = os.path.join(repo_root, ".env")
    if not os.path.exists(path):
        return None
    for line in open(path, encoding="utf-8"):
        if line.strip().startswith("MARKETCHECK_API_KEY"):
            value = line.split("=", 1)[1].strip().strip('"').strip("'")
            if value and value != "your_key_here":
                return value
    return None


# ---------------------------------------------------------------- setup

def run_setup(config_path, repo_root, current=None):
    current = current or {}
    cur_search = current.get("search", {})
    cur_own = current.get("ownership", {})
    cur_api = current.get("api", {})
    cur_scoring = current.get("scoring", {})

    print("\nCar Finder setup")
    print("Press Enter to accept the value in [brackets]. Ctrl-C to bail.")

    try:
        header("Where are you looking?")
        zip_code = ask("ZIP code", cur_search.get("zip"))
        radius = ask_int(
            "Search radius in miles", cur_search.get("radius_miles", 60),
            lo=1, hi=MAX_RADIUS,
            hint=f"Marketcheck's free plan caps this at {MAX_RADIUS}.")

        header("Budget")
        price_min = ask_int("Minimum price", cur_search.get("price_min", 10000), lo=0)
        price_max = ask_int("Maximum price", cur_search.get("price_max", 30000),
                            lo=price_min + 1)
        miles_max = ask_int("Maximum mileage",
                            cur_search.get("miles_max", 80000), lo=1)

        header("What kind of car?")
        body_type = ask_choice(
            "Body type", [(b, "") for b in BODY_TYPES],
            cur_search.get("body_type", "Sedan"))
        # Defaults to no preference on purpose. Defaulting to AWD would
        # silently filter out every RWD and FWD car for someone who
        # pressed Enter without thinking about it.
        drivetrain = ask_choice("Drivetrain", DRIVETRAINS,
                                cur_search.get("drivetrain", ""))
        cur_pt = cur_search.get("powertrain") or ""
        if isinstance(cur_pt, (list, tuple)):
            cur_pt = ", ".join(str(x) for x in cur_pt)
        if "," in cur_pt:
            # More than one was hand-written into the config. Keep it.
            print(f"  Powertrain: keeping {cur_pt}")
            powertrain = cur_pt
        else:
            powertrain = ask_choice("Powertrain", POWERTRAIN_CHOICES, cur_pt)
        year_min = ask_year("Oldest model year", cur_search.get("year_min"))
        year_max = ask_year("Newest model year", cur_search.get("year_max"))
        if year_min and year_max and year_min > year_max:
            print("    ! oldest is after newest; swapping them")
            year_min, year_max = year_max, year_min

        conditions = []
        print("  Which listings to include:")
        defaults = cur_search.get("car_types", ["used", "certified"])
        for cond in ("used", "certified", "new"):
            if ask_yes_no(f"  include {cond}?", cond in defaults):
                conditions.append(cond)
        if not conditions:
            print("    ! need at least one; defaulting to used")
            conditions = ["used"]

        header("Which models?")
        targets = ask_targets(current.get("targets"))
        if not targets:
            print("    Searching every make that fits your filters.")

        header("Running costs")
        print("  Used for the 5-year cost-of-ownership estimate.")
        annual_miles = ask_int("Miles you drive per year",
                               cur_own.get("annual_miles", 12000), lo=1)
        fuel_price = ask_float("Fuel price per gallon",
                               cur_own.get("fuel_price_per_gallon", 3.35))
        insurance = ask_int(
            "Your annual insurance premium",
            cur_own.get("baseline_insurance_annual", 1650), lo=0,
            hint="A real number from your policy makes the whole estimate "
                 "meaningful.")
        registration = ask_int("Annual registration/plates",
                               cur_own.get("annual_registration_usd", 180), lo=0)

        header("Marketcheck API")
        print("  Free key: https://developers.marketcheck.com/")
        print("  Skip this to use --sample mode with bundled demo data.")
        have = existing_key(repo_root)
        if have:
            print(f"  A key is already saved (…{have[-4:]}).")
            key = have
            if ask_yes_no("Replace it?", False):
                key = ask("API key", "").strip() or have
        else:
            key = ask("API key (blank to skip)", "").strip()
        key_changed = bool(key) and key != have

        call_limit = ask_int("Total API calls your plan allows",
                             cur_api.get("call_limit", 500), lo=1)
        open_report = ask_yes_no("Open the HTML report automatically?",
                                 bool(current.get("output", {})
                                      .get("open_report_when_done", False)))

    except NoInput:
        print("\n\nRan out of input before finishing. Nothing was written.")
        if not sys.stdin.isatty():
            print("Setup wants an interactive terminal. Either run it from "
                  "one,\nor copy config.example.yaml to config.yaml and edit "
                  "that.")
        return 1
    except Abort:
        print("\n\nCancelled. Nothing was written.")
        return 1

    config = CONFIG_TEMPLATE.format(
        zip=zip_code,
        radius=radius,
        price_min=price_min,
        price_max=price_max,
        miles_max=miles_max,
        body_type=body_type,
        drivetrain=drivetrain,
        powertrain=powertrain,
        years="\n".join(
            f"  {key}: {value}" if value else f"  # {key}: (any)"
            for key, value in (("year_min", year_min), ("year_max", year_max))),
        price_models=cur_api.get("price_models", 3),
        car_types="\n".join(f"    - {c}" for c in conditions),
        targets=("targets:\n" + "\n".join(
            f'  - make: "{t["make"]}"'
            + (f'\n    model: "{t["model"]}"' if t["model"] else "")
            for t in targets
        )) if targets else "targets: []",
        w_val=cur_scoring.get("weight_value", 0.45),
        w_mil=cur_scoring.get("weight_mileage", 0.30),
        w_rel=cur_scoring.get("weight_reliability", 0.15),
        w_mnt=cur_scoring.get("weight_maintenance", 0.10),
        annual_miles=annual_miles,
        fuel_price=fuel_price,
        insurance=insurance,
        registration=registration,
        call_limit=call_limit,
        open_report="true" if open_report else "false",
    )

    os.makedirs(os.path.dirname(os.path.abspath(config_path)), exist_ok=True)
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(config)
    print(f"\nWrote {config_path}")

    if key_changed:
        env_path = write_env(repo_root, key)
        print(f"Wrote {env_path}")
    elif key:
        print("Left .env alone; the saved key hasn't changed.")

    n_targets = max(1, len(targets))
    named = sum(1 for t in targets if t.get("model"))
    extra = cur_api.get("price_models", 3) if named < n_targets else 0
    print(f"\nA search will cost about {n_targets} API call(s), plus up to "
          f"{named + extra} more\nthe first time it builds comparables "
          f"(those are cached for a week).")
    print("\nNext:")
    if key:
        print("  python run.py search")
    else:
        print("  python run.py --sample search     # demo data, no key needed")
    return 0
