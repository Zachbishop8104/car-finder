"""
Durable state between runs, and the machine-readable handoff that lets
Claude pick up where a search left off.

Three files live in output/:

  latest.json     every ranked listing from the most recent search,
                  keyed by VIN. This is what Claude reads, the HTML and
                  CSV are for you.
  seen.json       every VIN ever returned, with when we first saw it and
                  what it cost then. Powers "what's new since last time"
                  and price-drop detection.
  shortlist.json  the handful of VINs you actually care about, written by
                  `run.py shortlist`. This is the input to deep research.

Plus research/<VIN>.json, one file per car ever researched, and the
housekeeping that stops dated reports and old research piling up.
"""
import datetime
import json
import os
import re

LATEST = "latest.json"
SEEN = "seen.json"
SHORTLIST = "shortlist.json"


def _path(out_dir, name):
    return os.path.join(out_dir, name)


def _read_json(path, default):
    if not os.path.exists(path):
        return default
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return default


def _write_json(path, data):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, default=str)


def _now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


def keep_newest(folder, pattern, keep, by_time=False):
    """Delete all but the newest `keep` files in `folder` whose whole
    name matches `pattern`. Nothing else in the folder is ever touched.

    Newest is by name (right for date-stamped names) or, with by_time,
    by when the file was last written. Returns how many were removed.
    """
    try:
        names = [n for n in os.listdir(folder) if re.fullmatch(pattern, n)]
    except OSError:
        return 0
    names.sort(key=(lambda n: os.path.getmtime(os.path.join(folder, n)))
               if by_time else None)
    gone = 0
    for name in names[:max(0, len(names) - max(0, int(keep)))]:
        try:
            os.remove(os.path.join(folder, name))
            gone += 1
        except OSError:
            pass
    return gone


def save_research(bundles, out_dir, keep=50):
    """One file per researched car, by VIN, so researching another car
    later does not erase this one. The oldest go once there are more
    than `keep`."""
    folder = _path(out_dir, "research")
    for b in bundles:
        name = re.sub(r"[^A-Za-z0-9]", "", str(b.get("vin") or ""))
        if name:
            _write_json(os.path.join(folder, name + ".json"),
                        dict(b, saved_at=_now()))
    keep_newest(folder, r"[A-Za-z0-9]+\.json", keep, by_time=True)
    return folder


# ---------------------------------------------------------------- run

def write_run(ranked, out_dir, search, source_label, generated_at):
    """Persist the ranked results in a form other tools can consume."""
    doc = {
        "generated_at": generated_at,
        "source": source_label,
        "search": search,
        "count": len(ranked),
        "listings": ranked,
        "by_vin": {r["vin"]: r for r in ranked if r.get("vin")},
    }
    _write_json(_path(out_dir, LATEST), doc)
    return _path(out_dir, LATEST)


def load_run(out_dir):
    return _read_json(_path(out_dir, LATEST), {})


# --------------------------------------------------------------- seen

def update_seen(ranked, out_dir):
    """Record every VIN we saw and diff against previous runs.

    Mutates each listing in place with two fields the report uses:
      is_new: never appeared in an earlier run
      price_drop: dollars cheaper than the last time we saw it (or 0)

    Returns (new_listings, dropped_listings).
    """
    path = _path(out_dir, SEEN)
    seen = _read_json(path, {})
    stamp = _now()
    fresh, drops = [], []

    for r in ranked:
        vin = r.get("vin")
        if not vin:
            r["is_new"] = False
            r["price_drop"] = 0
            continue

        price = r.get("price")
        prior = seen.get(vin)

        if prior is None:
            r["is_new"] = True
            r["price_drop"] = 0
            fresh.append(r)
            seen[vin] = {
                "first_seen": stamp,
                "last_seen": stamp,
                "first_price": price,
                "last_price": price,
                "times_seen": 1,
            }
        else:
            r["is_new"] = False
            was = prior.get("last_price")
            drop = 0
            if isinstance(was, (int, float)) and isinstance(price, (int, float)):
                drop = round(was - price)
            r["price_drop"] = drop if drop > 0 else 0
            r["first_seen"] = prior.get("first_seen")
            if r["price_drop"]:
                drops.append(r)
            prior["last_seen"] = stamp
            prior["last_price"] = price
            prior["times_seen"] = prior.get("times_seen", 1) + 1

    _write_json(path, seen)
    return fresh, drops


# ---------------------------------------------------------- shortlist

def save_shortlist(vins, out_dir):
    """Pin a set of VINs for deep research, carrying over their listing data."""
    run = load_run(out_dir)
    by_vin = run.get("by_vin", {})

    picked, missing = [], []
    for vin in vins:
        vin = vin.strip().upper()
        if vin in by_vin:
            picked.append(by_vin[vin])
        else:
            missing.append(vin)

    doc = {
        "saved_at": _now(),
        "from_run": run.get("generated_at"),
        "vins": [p["vin"] for p in picked],
        "listings": picked,
    }
    _write_json(_path(out_dir, SHORTLIST), doc)
    return picked, missing


def load_shortlist(out_dir):
    return _read_json(_path(out_dir, SHORTLIST), {})
