#!/usr/bin/env python3
"""
Car Finder: search local dealer inventory, shortlist what you like, then
research those cars in depth.

Three phases, three commands:

    python run.py search              # broad search -> ranked report
    python run.py shortlist VIN VIN   # pin the ones worth a closer look
    python run.py research            # deep-dive the shortlist

`search` is the default, so plain `python run.py` still works.

    python run.py --sample --open     # try everything with bundled data
"""
import argparse
import datetime
import importlib
import json
import os
import sys
import webbrowser

# make the package importable wherever this file was put
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Windows consoles still default to cp1252, which can't encode the box
# characters and symbols below. Ask for UTF-8 and degrade gracefully
# rather than dying halfway through a report.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass

from carfinder import http, market, paths, store
from carfinder.config import default_config, finish_search, load_config
from carfinder.reliability import get_profile
from carfinder.scoring import _passes_hard_filters, score_and_rank
from carfinder.sources import get_source

# Everything the tool remembers lives in the data folder (see paths.py),
# never next to the code: the code may be running from a temporary copy
# that is deleted afterwards, and the working directory is whatever
# project the agent happened to be in.
OUT_DIR = paths.output_dir()


def _optional(name):
    """Import carfinder.<name>, or None if that file wasn't brought along.

    The HTML report and the setup wizard are conveniences. A run from a
    minimal copy of the code works without them.
    """
    try:
        return importlib.import_module(f"carfinder.{name}")
    except ModuleNotFoundError as e:
        if e.name != f"carfinder.{name}":
            raise
        return None


def _load_dotenv():
    """Tiny .env loader so you don't need python-dotenv."""
    path = paths.env_file()
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def _money(v):
    return f"${v:,.0f}" if isinstance(v, (int, float)) else "n/a"


def _budget_line(cfg):
    """One-line statement of where the metered call budget stands."""
    u = http.usage_summary()
    if u["limit"] is None:
        return f"{u['this_run']} API call(s) this run · {u['used']} total"
    pct = 100.0 * u["used"] / u["limit"] if u["limit"] else 0
    line = (f"{u['this_run']} API call(s) this run · "
            f"{u['used']}/{u['limit']} used, {u['remaining']} left")
    if pct >= cfg["api"]["warn_at_pct"]:
        line += "  ⚠ running low"
    return line


def _source_or_exit(use_sample):
    try:
        return get_source(use_sample=use_sample)
    except RuntimeError as e:
        print(e)
        sys.exit(1)


def _pricing_plan(listings, targets, limit):
    """Decide which models get priced against their market.

    Pricing a model costs one comparables call. A target that names a
    make and model has agreed to that cost by being in the config. A
    target that names only a make, or nothing at all, can turn up any
    number of models, so those are priced most-listings-first up to
    `limit` (None = all of them) and the rest are left unpriced.

    Returns (to_price, skipped): to_price is a list of
    (make, model, body_type, powertrain), carrying the target's own
    body type and powertrain so the comparables are the same kind of
    car the listings were; skipped is a list of (make, model, count).
    """
    named = {}
    for t in targets:
        if t.get("make") and t.get("model"):
            named[(t["make"].lower(), t["model"].lower())] = (
                t.get("body_type"), t.get("powertrain"))

    def open_target_powertrain(make):
        """The powertrain of the make-only or any-make target that a
        model nobody named must have come from."""
        for t in targets:
            if not t.get("model") and t.get("powertrain") and (
                    not t.get("make")
                    or t["make"].lower() == make.lower()):
                return t["powertrain"]
        return None

    found = {}   # (make_lower, model_lower) -> [make, model, count, bodies]
    for r in listings:
        make, model = str(r.get("make") or ""), str(r.get("model") or "")
        if not make or not model:
            continue
        entry = found.setdefault((make.lower(), model.lower()),
                                 [make, model, 0, {}])
        entry[2] += 1
        body = r.get("body_type") or ""
        entry[3][body] = entry[3].get(body, 0) + 1

    to_price, discovered = [], []
    for key, (make, model, count, bodies) in found.items():
        if key in named:
            to_price.append((make, model) + named[key])
        else:
            # Compare like with like: the body style most of its
            # listings here have.
            body = max(bodies, key=bodies.get) if bodies else ""
            discovered.append((count, make, model, body or None))
    discovered.sort(key=lambda d: (-d[0], d[1], d[2]))
    keep = discovered if limit is None else discovered[:max(0, limit)]
    to_price += [(mk, md, body, open_target_powertrain(mk))
                 for _, mk, md, body in keep]
    skipped = [(mk, md, n) for n, mk, md, _ in discovered[len(keep):]]
    return to_price, skipped


def _gather_comparables(source, to_price, search):
    """One wide pull per model, reused for both pricing and depreciation."""
    comps = {}
    for make, model, body_type, powertrain in to_price:
        key = (make.lower(), model.lower())
        if key not in comps:
            comps[key] = source.fetch_comparables(make, model, search,
                                                  body_type, powertrain)
    return comps


def _search_summary(search):
    """The filters in one line, for the console."""
    parts = [f"within {search['radius_miles']} mi of {search['zip']}",
             f"${search['price_min']:,}-${search['price_max']:,}",
             f"≤{search['miles_max']:,} mi"]
    lo, hi = search.get("year_min"), search.get("year_max")
    if lo and hi:
        parts.append(f"{lo}-{hi}")
    elif lo:
        parts.append(f"{lo} or newer")
    elif hi:
        parts.append(f"{hi} or older")
    for key in ("body_type", "drivetrain"):
        if search.get(key):
            parts.append(str(search[key]))
    if search.get("powertrain"):
        pt = search["powertrain"]
        parts.append(", ".join(pt) if isinstance(pt, list) else str(pt))
    return " · ".join(parts)


# --------------------------------------------------------------- search

def cmd_search(args, cfg):
    from carfinder.sources import target_label

    search, targets = cfg["search"], cfg["targets"]
    current_year = datetime.date.today().year

    source, label = _source_or_exit(args.sample)
    print("Car Finder: searching…")
    what = ("demo listings" if args.sample
            else ", ".join(target_label(t) for t in targets))
    print(f"  {what} · {_search_summary(search)}\n")

    listings = source.fetch(search, targets, cfg["output"]["max_results"])

    # The demo listings are a fixed set, whatever the config's targets
    # say, and its comparables are free: price all of them.
    limit = getattr(args, "price_models", None)
    if limit is None:
        limit = None if args.sample else cfg["api"].get("price_models", 3)
    # Only models with a car that survives the filters are worth a call.
    eligible = [r for r in listings if _passes_hard_filters(r, search)[0]]
    to_price, unpriced = _pricing_plan(
        eligible, [] if args.sample else targets, limit)

    print(f"  pulling comparables for market pricing "
          f"({len(to_price)} model{'s' if len(to_price) != 1 else ''})…")
    comps = _gather_comparables(source, to_price, search)
    n_comps = sum(len(v) for v in comps.values())

    ranked, rejected = score_and_rank(
        listings, search, cfg["scoring"], comps, current_year
    )
    fresh, drops = store.update_seen(ranked, OUT_DIR)

    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    html_path = os.path.join(OUT_DIR, f"results_{stamp}.html")
    csv_path = os.path.join(OUT_DIR, f"results_{stamp}.csv")
    latest = os.path.join(OUT_DIR, "latest.html")

    report = _optional("report")
    if report:
        report.write_csv(ranked, csv_path)
        report.write_html(ranked, html_path, search, label, ts)
        report.write_html(ranked, latest, search, label, ts)
    json_path = store.write_run(ranked, OUT_DIR, search, label, ts)
    # Dated reports are an archive, not a log: keep the newest few.
    store.keep_newest(OUT_DIR, r"results_\d{8}_\d{6}\.(html|csv)",
                      2 * cfg["output"].get("keep_reports", 10))

    print(f"\nDone. Pulled {len(listings)} listings ({n_comps} comparables), "
          f"{len(ranked)} matched your filters.")
    if rejected:
        reasons = {}
        for r in rejected:
            reasons[r["rejected_because"]] = reasons.get(r["rejected_because"], 0) + 1
        print("  filtered out: " + ", ".join(f"{v} {k}" for k, v in reasons.items()))
    if unpriced:
        # Never spend quota on models nobody asked to have priced. Say
        # what was left out and exactly what pricing it would cost.
        left = http.usage_summary().get("remaining")
        shown = ", ".join(f"{mk} {md} ({n})" for mk, md, n in unpriced[:8])
        more = f", and {len(unpriced) - 8} more" if len(unpriced) > 8 else ""
        total = len(to_price) + len(unpriced)
        print(f"\n  Market pricing: {len(to_price)} of {total} models priced "
              f"(most listings first). Not priced:\n    {shown}{more}")
        print(f"  Pricing a model costs 1 API call"
              + (f"; you have {left} left" if left is not None else "")
              + f". To price them all, re-run with --price-models {total}\n"
              f"  (the listings are cached, so only the extra "
              f"{len(unpriced)} call{'s' if len(unpriced) != 1 else ''} "
              f"would be spent).")
    if fresh:
        print(f"  {len(fresh)} new since your last run")
    if drops:
        print(f"  {len(drops)} price drop(s): " + ", ".join(
            f'{r["year"]} {r["model"]} −{_money(r["price_drop"])}' for r in drops[:4]))

    if ranked:
        print("\nTop picks:")
        for i, r in enumerate(ranked[:5], 1):
            title = f"{r.get('year','')} {r.get('make','')} {r.get('model','')} {r.get('trim','')}".strip()
            mk = r.get("market")
            vs = ""
            if mk and abs(mk["delta_usd"]) > 250:
                vs = f' · {_money(abs(mk["delta_usd"]))} {"under" if mk["delta_usd"] > 0 else "over"} market'
            flags = " [NEW]" if r.get("is_new") else ""
            print(f"  {i}. [{r['score']:>5}] {title}{flags}")
            print(f"          {_money(r.get('price'))} · "
                  f"{r.get('miles', 0):,.0f} mi{vs}")
            print(f"          {r.get('vin','')}")
            for warning in r.get("flags") or []:
                print(f"          ! {warning}")
    else:
        print("\nNo matches. Try widening radius/price/mileage in config.yaml.")

    print()
    if report:
        print(f"Report:      {html_path}")
        print(f"Spreadsheet: {csv_path}")
    print(f"Data:        {json_path}")
    if not args.sample:
        print(f"Budget:      {_budget_line(cfg)}")
    if ranked:
        print(f"\nNext: python run.py shortlist {ranked[0]['vin']} <more VINs…>")

    if report and (args.open or cfg["output"].get("open_report_when_done")):
        webbrowser.open("file://" + os.path.abspath(latest))


# ------------------------------------------------------------ shortlist

def cmd_shortlist(args, cfg):
    if not args.vins:
        current = store.load_shortlist(OUT_DIR)
        if not current.get("listings"):
            print("Shortlist is empty. Pass VINs from the last search:\n"
                  "  python run.py shortlist 4T1G11AK5MU… 4S3BWAB6…")
            return
        print(f"Shortlist ({len(current['listings'])} cars, "
              f"saved {current.get('saved_at')}):")
        for r in current["listings"]:
            print(f"  {r['vin']}  {r.get('year')} {r.get('make')} "
                  f"{r.get('model')}, {_money(r.get('price'))}")
        return

    picked, missing = store.save_shortlist(args.vins, OUT_DIR)
    for r in picked:
        print(f"  + {r['vin']}  {r.get('year')} {r.get('make')} "
              f"{r.get('model')} {r.get('trim','')}, {_money(r.get('price'))}")
    for vin in missing:
        print(f"  ! {vin} not in the last search. Re-run search, or check the VIN")
    if picked:
        print(f"\nSaved {len(picked)} to {os.path.join(OUT_DIR, 'shortlist.json')}")
        print("Next: python run.py research")


# ------------------------------------------------------------- research

def _listing_from_vin(research, vin):
    """A listing built from nothing but a VIN, via the free NHTSA decode.

    This is what lets someone research a car they found anywhere: paste
    the VIN from the dealer's page. Returns None (after saying why) when
    the VIN can't be turned into a year, make and model.
    """
    if len(vin) != 17:
        print(f"  ! {vin} is not a 17-character VIN and is not in the "
              f"last search; skipping")
        return None
    try:
        d = research.decode_vin(vin)
    except http.FetchError as e:
        print(f"  ! {vin}: the VIN decode failed ({e}); skipping")
        return None
    year = str(d.get("ModelYear") or "")
    if not (d.get("Make") and d.get("Model") and year.isdigit()):
        print(f"  ! {vin}: NHTSA could not decode a year, make and model "
              f"from this VIN. Check it for a typo; skipping")
        return None
    make = str(d["Make"])
    return {
        "vin": vin,
        "year": int(year),
        # vPIC shouts makes ("TOYOTA"); keep short ones (BMW, GMC) as is.
        "make": make.title() if len(make) > 3 else make,
        "model": str(d["Model"]),
        "trim": d.get("Trim") or d.get("Series") or "",
        "drivetrain": d.get("DriveType") or "",
        "body_type": d.get("BodyClass") or "",
        "price": None,
        "miles": None,
        "from_vin_only": True,
    }


def cmd_research(args, cfg):
    from carfinder import research, tco

    price = getattr(args, "price", None)
    miles = getattr(args, "miles", None)
    if (price is not None or miles is not None) and len(args.vins) != 1:
        print("--price and --miles describe one car, so give exactly one "
              "VIN with them.")
        sys.exit(1)

    if args.vins:
        by_vin = store.load_run(OUT_DIR).get("by_vin", {})
        listings = []
        for v in (v.strip().upper() for v in args.vins):
            L = dict(by_vin[v]) if v in by_vin else _listing_from_vin(research, v)
            if L:
                listings.append(L)
        if listings and price is not None:
            listings[0]["price"] = price
        if listings and miles is not None:
            listings[0]["miles"] = miles
    else:
        listings = store.load_shortlist(OUT_DIR).get("listings", [])

    if not listings:
        print("Nothing to research. Give it a VIN from any dealer listing:\n"
              "  python run.py research <VIN> --price 24990 --miles 38000\n"
              "or build a shortlist from a search:\n"
              "  python run.py search\n"
              "  python run.py shortlist <VIN> <VIN>")
        return

    search = cfg.get("search")
    current_year = datetime.date.today().year

    # Comparables (for a local depreciation curve) need the listings
    # source. Everything else here is free and keyless, so having no
    # API key or no saved search is not a reason to stop.
    source, label = None, "NHTSA and EPA only (no listings source)"
    if args.sample or search:
        try:
            source, label = get_source(use_sample=args.sample)
        except RuntimeError:
            pass

    years = cfg["ownership"]["years"]
    print(f"Researching {len(listings)} car(s): VIN decode, recalls, "
          f"complaints, EPA mileage, depreciation, {years}-yr cost…\n")

    bundles = []
    curves = {}
    for L in listings:
        title = f'{L.get("year","")} {L.get("make","")} {L.get("model","")}'.strip()
        print(f"  · {title} ({L.get('vin','')})")

        bundle = research.research_vehicle(L)

        key = (str(L.get("make", "")).lower(), str(L.get("model", "")).lower())
        if key not in curves:
            comps = (source.fetch_comparables(L.get("make"), L.get("model"),
                                              search or {})
                     if source else [])
            curves[key] = market.depreciation_curve(comps, current_year)
        curve = curves[key]

        profile = get_profile(L.get("make"), L.get("model"), L.get("year"))
        for k in ("generation", "reliability", "maintenance", "known_issues",
                  "note", "risk"):
            L.setdefault(k, profile.get(k))
        L.setdefault("unrated", bool(profile.get("unrated")))
        if profile.get("risk") and not L.get("flags"):
            L["flags"] = [profile["risk"]]

        if isinstance(L.get("price"), (int, float)) and L["price"] > 0:
            bundle["depreciation"] = {
                "curve": curve,
                "projection": market.project_value(L["price"], curve,
                                                   years=years),
            }
            costed = L
            assumed_miles = None
            if not isinstance(L.get("miles"), (int, float)):
                # No odometer reading given. Assume average use for the
                # car's age, and say so, rather than treating it as new.
                age = max(0, current_year - int(L.get("year") or current_year))
                assumed_miles = cfg["ownership"]["annual_miles"] * age
                costed = dict(L, miles=assumed_miles)
            best = (bundle.get("fuel_economy") or {}).get("best_match") or {}
            bundle["tco"] = tco.estimate(
                costed, profile, curve, best.get("mpg_combined"),
                cfg["ownership"], epa=best,
            )
            if assumed_miles is not None:
                bundle["tco"]["assumptions"].append(
                    f"No mileage given; maintenance assumes {assumed_miles:,} "
                    f"miles on the car (average use for its age). Pass "
                    f"--miles for a better figure.")
        else:
            bundle["depreciation"] = {"curve": curve, "projection": None}
            bundle["tco"] = None
            bundle["errors"].append(
                "cost of ownership: skipped because no asking price was "
                "given. Re-run with --price (and --miles) to get it.")
        bundles.append(bundle)

        for err in bundle["errors"]:
            print(f"      ! {err}")

    json_path = os.path.join(OUT_DIR, "research.json")
    md_path = os.path.join(OUT_DIR, "research.md")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({"generated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                   "source": label, "vehicles": bundles}, f, indent=2, default=str)
    # Each car is also kept on its own, so the next run doesn't erase it.
    store.save_research(bundles, OUT_DIR,
                        cfg["output"].get("keep_research", 50))
    html_path = os.path.join(OUT_DIR, "research.html")
    report = _optional("report")
    if report:
        report.write_research_markdown(bundles, md_path)
        report.write_research_html(bundles, html_path)

    ranking = tco.compare([(b["vin"], b["tco"]) for b in bundles if b["tco"]])
    if len(ranking) == 1:
        row = ranking[0]
        print(f"\n{years}-year cost of ownership: {_money(row['total'])} "
              f"({_money(row['cost_per_month'])}/mo)")
    if len(ranking) > 1:
        print(f"\n{cfg['ownership']['years']}-year cost of ownership, cheapest first:")
        for row in ranking:
            extra = (f' (+{_money(row["premium_over_cheapest"])})'
                     if row["premium_over_cheapest"] else "")
            print(f"  {_money(row['total']):>9}  {_money(row['cost_per_month'])}/mo  "
                  f"{row['vin']}{extra}")

    print()
    if report:
        print(f"Report:  {html_path}")
        print(f"Facts:   {md_path}")
    print(f"Data:    {json_path}")
    print(f"Per car: {os.path.join(OUT_DIR, 'research', '<VIN>.json')}")
    if report and (args.open or cfg["output"].get("open_report_when_done")):
        webbrowser.open("file://" + os.path.abspath(html_path))


# ----------------------------------------------------------------- misc

def cmd_clear_cache(args, cfg):
    n = http.clear_cache()
    print(f"Cleared {n} cached response(s) from {http.CACHE_DIR}")
    print("Note: the next search will re-fetch and spend calls.")


def cmd_setup(args, cfg):
    # cfg is None here when there's no config yet, that's the normal
    # first-run path, and the wizard is what creates it.
    setup_mod = _optional("setup")
    if not setup_mod:
        print("The setup wizard isn't in this copy of the code. Copy\n"
              f"  {paths.example_config()}\nto\n  {args.config}\n"
              "and edit it instead.")
        sys.exit(1)
    sys.exit(setup_mod.run_setup(args.config, paths.home(), current=cfg))


def cmd_where(args, cfg):
    """Say where everything is. Never prints the key itself."""
    home = paths.home()
    key = os.environ.get("MARKETCHECK_API_KEY", "").strip()
    has_key = bool(key) and key != "your_key_here"
    n_cached = 0
    if os.path.isdir(http.CACHE_DIR):
        n_cached = sum(1 for n in os.listdir(http.CACHE_DIR)
                       if n.endswith(".json") and n != "usage.json")

    def state(path):
        return "" if os.path.exists(path) else "  (not created yet)"

    print(f"Data folder: {home}{state(home)}")
    print(f"Config:      {args.config}{state(args.config)}")
    print(f"API key:     {'set' if has_key else 'not set'}"
          f"  (MARKETCHECK_API_KEY, from the environment or "
          f"{paths.env_file()})")
    print(f"Output:      {OUT_DIR}{state(OUT_DIR)}")
    print(f"Cache:       {http.CACHE_DIR}  ({n_cached} cached response(s))")
    print(f"Code:        {paths.APP_DIR}")
    print(f"Template:    {paths.example_config()}"
          f"{'' if os.path.exists(paths.example_config()) else '  (not in this copy)'}")


def cmd_usage(args, cfg):
    if args.reset:
        http.set_usage(0)
        print("Call counter reset to 0.")
    elif args.set is not None:
        http.set_usage(args.set)
        print(f"Call counter set to {args.set}.")

    u = http.usage_summary()
    limit = u["limit"]
    print(f"\nMarketcheck calls used: {u['used']}"
          + (f" / {limit}  ({u['remaining']} left)" if limit else ""))
    if limit:
        width = 40
        filled = min(width, int(width * u["used"] / limit))
        print(f"  [{'█' * filled}{'·' * (width - filled)}]")
    if u["by_month"]:
        print("\n  by month:")
        for month, n in sorted(u["by_month"].items()):
            print(f"    {month}  {n}")
    targets = cfg["targets"]
    if targets:
        named = sum(1 for t in targets if t.get("make") and t.get("model"))
        extra = cfg["api"].get("price_models", 3) if named < len(targets) else 0
        print(f"\nYour saved search costs {len(targets)} call(s) for "
              f"listings plus up to {named + extra} for comparables\n"
              f"(comparables are cached for a week, so repeat searches "
              f"inside that window cost only the first number).")
    else:
        print("\nA search costs 1 call per make or model searched, plus 1 "
              "per model priced against its market.")
    print("NHTSA and FuelEconomy.gov calls are free and not counted.")
    print("\nIterating on code? Use --cached-only to spend nothing.")


def build_parser():
    # The shared flags are declared twice: once on the top-level parser
    # with real defaults, and once on every subparser with SUPPRESS so a
    # flag given before the subcommand isn't silently overwritten by the
    # subparser's default. That makes both orderings work:
    #     run.py --sample search      run.py search --sample
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--sample", action="store_true",
                        default=argparse.SUPPRESS,
                        help="use bundled demo data (no API key needed)")
    common.add_argument("--open", action="store_true",
                        default=argparse.SUPPRESS,
                        help="open the HTML report when finished")
    common.add_argument("--config", default=argparse.SUPPRESS,
                        help="path to config file")
    common.add_argument("--cached-only", action="store_true",
                        default=argparse.SUPPRESS,
                        help="never spend an API call; use cached responses "
                             "only (for iterating on code for free)")

    ap = argparse.ArgumentParser(
        description="Find, shortlist and research used cars.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    ap.add_argument("--sample", action="store_true",
                    help="use bundled demo data (no API key needed)")
    ap.add_argument("--open", action="store_true",
                    help="open the HTML report when finished")
    ap.add_argument("--config", default=None,
                    help="path to config file (default: config.yaml in "
                         "the data folder; see `where`)")
    ap.add_argument("--cached-only", action="store_true",
                    help="never spend an API call; use cached responses only")

    sub = ap.add_subparsers(dest="command")
    se = sub.add_parser("search", parents=[common],
                        help="search inventory and rank the results")
    # Each of these overrides the saved search for one run. With --zip
    # and at least one --target, no config file is needed at all.
    se.add_argument("--zip", help="ZIP code to search around")
    se.add_argument("--radius", type=int, metavar="MILES",
                    help="search radius (the free API plan caps it at 100)")
    se.add_argument("--target", action="append", metavar="MAKE[:MODEL]",
                    help="a make, or make and model, to search for, such as "
                         "Toyota:Camry or \"Land Rover:Defender\"; repeat "
                         "for more (each costs one API call)")
    se.add_argument("--price-min", type=int, metavar="USD")
    se.add_argument("--price-max", type=int, metavar="USD")
    se.add_argument("--miles-max", type=int, metavar="N")
    se.add_argument("--body-type", metavar="TYPE",
                    help="Sedan, SUV, Pickup, Coupe, Hatchback, Wagon, "
                         "Minivan or Convertible")
    se.add_argument("--drivetrain", metavar="AWD|FWD|RWD")
    se.add_argument("--condition", metavar="LIST",
                    help="comma-separated: used, certified, new")
    se.add_argument("--year-min", type=int, metavar="YEAR",
                    help="oldest model year to include")
    se.add_argument("--year-max", type=int, metavar="YEAR",
                    help="newest model year to include")
    se.add_argument("--powertrain", metavar="KIND",
                    help="gas, hybrid, plug-in hybrid, electric or diesel; "
                         "comma-separate to allow several")
    se.add_argument("--any-make", action="store_true",
                    help="ignore the saved targets and search every make "
                         "that fits the filters")
    se.add_argument("--price-models", type=int, metavar="N",
                    help="when a search names no model, how many of the "
                         "models it finds to price against the market "
                         "(1 API call each; default 3)")

    sl = sub.add_parser("shortlist", parents=[common],
                        help="pin VINs for deep research")
    sl.add_argument("vins", nargs="*", help="VINs from the last search "
                                            "(no args = show current shortlist)")

    rs = sub.add_parser("research", parents=[common],
                        help="deep-dive the shortlist")
    rs.add_argument("vins", nargs="*",
                    help="VINs to research: from the last search, or any "
                         "17-character VIN from a dealer listing (no API "
                         "key or config needed). Default: the shortlist")
    rs.add_argument("--price", type=float, metavar="USD",
                    help="asking price of the one VIN given, for the "
                         "cost-of-ownership estimate")
    rs.add_argument("--miles", type=float, metavar="N",
                    help="odometer reading of the one VIN given")

    sub.add_parser("setup", parents=[common],
                   help="interactive first-run setup (writes config.yaml)")

    sub.add_parser("where", parents=[common],
                   help="show where config, results and cache are kept")

    sub.add_parser("clear-cache", parents=[common],
                   help="drop every cached API response")

    us = sub.add_parser("usage", parents=[common],
                        help="show how much of the API budget is spent")
    us.add_argument("--reset", action="store_true",
                    help="zero the counter (do this when your quota renews)")
    us.add_argument("--set", type=int, metavar="N",
                    help="set the counter to N (to account for calls made "
                         "before tracking existed)")
    return ap


COMMANDS = {
    "search": cmd_search,
    "shortlist": cmd_shortlist,
    "research": cmd_research,
    "setup": cmd_setup,
    "where": cmd_where,
    "clear-cache": cmd_clear_cache,
    "usage": cmd_usage,
}


# These only touch saved results or the cache, so they work before
# (or without) a config: a shortlist made in demo mode, for one.
NO_CONFIG_NEEDED = {"shortlist", "clear-cache"}

SEARCH_OPTIONS = {
    "zip": "zip", "radius": "radius_miles", "price_min": "price_min",
    "price_max": "price_max", "miles_max": "miles_max",
    "body_type": "body_type", "drivetrain": "drivetrain",
    "year_min": "year_min", "year_max": "year_max",
    "powertrain": "powertrain",
}


def _parse_targets(values):
    """--target Toyota:Camry (or just --target Toyota) -> config targets."""
    out = []
    for v in values or []:
        make, _, model = v.partition(":")
        if make.strip():
            t = {"make": make.strip()}
            if model.strip():
                t["model"] = model.strip()
            out.append(t)
    return out


def _apply_search_options(args, cfg):
    """Let `search` options override the saved search for this run."""
    for opt, key in SEARCH_OPTIONS.items():
        value = getattr(args, opt, None)
        if value is not None:
            cfg["search"][key] = value
    if getattr(args, "condition", None):
        cfg["search"]["car_types"] = [
            c.strip().lower() for c in args.condition.split(",") if c.strip()]
    targets = _parse_targets(getattr(args, "target", None))
    if targets:
        cfg["targets"] = targets
    elif getattr(args, "any_make", False):
        cfg["targets"] = [{}]


def _config_from_options(args, command):
    """A config for a run that has no config file, or None if this
    command can't do without one.

    `research` needs none: a pasted VIN is researched from free public
    data. `search` needs none when the criteria are given as options.
    """
    cfg = default_config()
    if command in ("research", "usage"):
        return cfg
    if command == "search" and getattr(args, "zip", None):
        # No --target means an open search across every make.
        cfg["search"] = {"zip": str(args.zip)}
        cfg["targets"] = [{}]
        return cfg
    return None


def main():
    args = build_parser().parse_args()
    # No --config means the one in the data folder. A relative --config
    # is tried against the working directory first, then the data folder.
    if not args.config:
        args.config = paths.config_file()
        as_json = os.path.splitext(args.config)[0] + ".json"
        if not os.path.exists(args.config) and os.path.exists(as_json):
            args.config = as_json
    elif not os.path.isabs(args.config) and not os.path.exists(args.config):
        args.config = os.path.join(paths.home(), args.config)
    _load_dotenv()
    command = args.command or "search"

    if command == "where":
        cmd_where(args, None)
        return

    # The demo needs no setup at all: with --sample and no config yet,
    # fall back to the template that ships with the code.
    if (getattr(args, "sample", False) and not os.path.exists(args.config)
            and os.path.exists(paths.example_config())):
        args.config = paths.example_config()

    # setup is the one command that runs without a config, it's what
    # creates one. Everything else points you at it when there isn't one.
    try:
        cfg = load_config(args.config)
    except FileNotFoundError:
        if command == "setup":
            cmd_setup(args, None)
            return
        if command in NO_CONFIG_NEEDED:
            COMMANDS[command](args, None)
            return
        cfg = _config_from_options(args, command)
    except ValueError as e:
        print(f"Config problem: {e}")
        sys.exit(1)
    if cfg is None:
        print(f"No saved search yet at {args.config}\n\n"
              f"To research one car you found, no setup is needed:\n"
              f"  python run.py research <VIN> --price 24990 --miles 38000\n\n"
              f"To search dealer inventory, either give the search here:\n"
              f"  python run.py search --zip 60601 --target Toyota:Camry "
              f"--price-max 30000\n"
              f"  python run.py search --zip 60601 --body-type SUV "
              f"--price-max 25000     (any make)\n"
              f"or save one:\n"
              f"  python run.py setup        # answer a few questions\n"
              f"or copy {paths.example_config()}\n"
              f"to that path and edit it.")
        sys.exit(1)

    if command == "search":
        from carfinder.sources import wanted_powertrains
        try:
            _apply_search_options(args, cfg)
            finish_search(cfg["search"])
            # Catch a misspelled powertrain before it costs an API call.
            wanted_powertrains(cfg["search"].get("powertrain"))
            for t in cfg["targets"]:
                wanted_powertrains(t.get("powertrain"))
        except ValueError as e:
            print(f"Search problem: {e}")
            sys.exit(1)

    api = cfg["api"]
    http.configure(
        call_limit=api.get("call_limit"),
        warn_at_pct=api.get("warn_at_pct", 80),
        max_rps=api.get("max_requests_per_second", 4),
        cached_only=getattr(args, "cached_only", False),
    )
    http.prune_cache()   # drops expired cache files, at most once a day

    try:
        COMMANDS[command](args, cfg)
    except http.BudgetExceeded as e:
        print(f"\nStopped: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
