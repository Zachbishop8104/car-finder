"""
Deep research on a specific car, from free public sources.

This module fetches facts. It deliberately does not interpret them;
that's Claude's job, working from the JSON this produces. Keeping the
split clean means the numbers are always real and the narrative is
always grounded in them.

Sources (all free, no key, no terms-of-service problem):

  NHTSA vPIC        decode the VIN into the exact engine, transmission,
                    trim, drive type and assembly plant. This is the
                    part that makes research specific: "Camry
                    reliability" is meaningless, "2021 Camry 2.5L
                    A25A-FKS AWD" is answerable.
  NHTSA recalls     open safety recalls for that year/make/model.
  NHTSA complaints  owner-filed complaints, aggregated by component so
                    patterns show up instead of anecdotes.
  FuelEconomy.gov   EPA mileage and annual fuel cost, for the TCO model.

Complaint text is summarized rather than dumped, a popular model can
have hundreds of filings and the raw feed would swamp everything else.
"""
import re

from . import http

VPIC_DECODE = "https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/{vin}"
NHTSA_RECALLS = "https://api.nhtsa.gov/recalls/recallsByVehicle"
NHTSA_COMPLAINTS = "https://api.nhtsa.gov/complaints/complaintsByVehicle"
NHTSA_MODELS = "https://api.nhtsa.gov/products/vehicle/models"
FE_MODELS = "https://www.fueleconomy.gov/ws/rest/vehicle/menu/model"
FE_MENU = "https://www.fueleconomy.gov/ws/rest/vehicle/menu/options"
FE_VEHICLE = "https://www.fueleconomy.gov/ws/rest/vehicle/{id}"

# The EPA splits a model into separate entries per drivetrain and trim
# group: "Camry AWD LE/SE", "Legacy AWD", "3 4-Door 4WD". Asking for the
# plain model name gets you whichever single entry happens to match
# exactly, which for a 2021 Camry is the front-drive V6. So we list the
# real names first and match against them.
MAX_FE_MODELS = 4
MAX_FE_OPTIONS_PER_MODEL = 3
MAX_FE_VARIANTS = 10

# vPIC returns ~140 mostly-empty fields. These are the ones that matter
# for judging an engine and how hard it will be to live with.
VIN_FIELDS = [
    "Make", "Model", "ModelYear", "Trim", "Series", "BodyClass",
    "DriveType", "EngineCylinders", "DisplacementL", "EngineHP",
    "EngineConfiguration", "EngineModel", "FuelTypePrimary",
    "TransmissionStyle", "TransmissionSpeeds", "ElectrificationLevel",
    "TurboCharger", "Manufacturer", "PlantCity", "PlantState",
    "PlantCountry", "VehicleType", "ErrorCode", "ErrorText",
]

MAX_COMPLAINT_SAMPLES = 6
COMPLAINT_SUMMARY_CHARS = 420
MAX_RECALLS = 15

# NHTSA answers "this vehicle has no recalls/complaints" with HTTP 400 and
# a valid empty result body. Treat that as data, not failure.
NHTSA_EMPTY = (400,)


def _trim(text, limit):
    text = " ".join(str(text or "").split())
    return text if len(text) <= limit else text[:limit].rstrip() + "…"


def decode_vin(vin):
    """Exact build data for one VIN. Never changes, so cached forever."""
    data = http.get_json(
        VPIC_DECODE.format(vin=vin), {"format": "json"}, ttl=http.TTL_REFERENCE * 12
    )
    results = data.get("Results") or []
    if not results:
        raise http.FetchError(f"vPIC returned nothing for VIN {vin}")
    raw = results[0]
    out = {k: raw.get(k) for k in VIN_FIELDS if raw.get(k) not in (None, "", "Not Applicable")}
    # ErrorCode "0" means a clean decode; anything else is worth surfacing.
    out["decode_clean"] = str(raw.get("ErrorCode", "")).startswith("0")
    return out


# ------------------------------------------------- NHTSA's model names
#
# NHTSA does not file a car under the name a dealer lists it by. The
# same vehicle can be "SIENNA HYBRID" (every 2021+ Sienna), "GLS-CLASS"
# or "GLE 350 4MATIC" (Mercedes), "430I" or "4 SERIES" (BMW), "RX 350"
# (Lexus), "F-150 SUPER CREW" (trucks, by cab), "SILVERADO 2500" (no
# "HD"), "WRANGLER" (no "Unlimited"), "AUDI Q5". Asking for the listing
# name returns an empty result that looks exactly like a clean record.
#
# So ask NHTSA which names it uses for that make and year, pick the ones
# that are this model, and pull every one of them.

# Words NHTSA appends that do not make it a different vehicle.
_BODY_WORDS = {
    "regular", "super", "crew", "cab", "quad", "mega", "double", "extended",
    "king", "access", "supercab", "supercrew", "class", "coupe", "sedan",
    "convertible", "cabriolet", "hatchback", "wagon", "van", "cargo",
    "passenger", "sportback", "awd", "fwd", "rwd", "wd", "matic", "xdrive",
    "sdrive", "edrive", "swb", "lwb", "door", "seat", "kwh", "battery",
    "sd",       # Ford's Super Duty: "F-250 SD"
}
_POWER_WORDS = {
    "hybrid": "hybrid", "hev": "hybrid",
    "phev": "plug-in hybrid", "plug": "plug-in hybrid",
    "prime": "plug-in hybrid", "xe": "plug-in hybrid",
    "energi": "plug-in hybrid",
    "bev": "electric", "ev": "electric", "electric": "electric",
    "diesel": "diesel",
}
# Words a listing appends that NHTSA usually leaves off.
_LISTING_EXTRAS = {"unlimited", "hd", "class", "super", "duty", "in"} \
    | set(_POWER_WORDS)


def _name_tokens(name, make=""):
    """A model name as comparable tokens: "RX350" -> ["rx", "350"]."""
    text = re.sub(r"\(.*?\)", " ", str(name or "").lower())
    tokens = re.findall(r"[a-z]+|\d+", text)
    lead = re.findall(r"[a-z]+|\d+", str(make or "").lower())
    if lead and tokens[:len(lead)] == lead and len(tokens) > len(lead):
        tokens = tokens[len(lead):]          # "AUDI Q5" -> q5
    return tokens


def _name_powertrains(tokens):
    return {_POWER_WORDS[t] for t in tokens if t in _POWER_WORDS}


def _is_variant_of(cand, base):
    """Is NHTSA name `cand` the model `base`, give or take a cab style,
    body style, powertrain word or trim badge ("350", "450h")?"""
    if cand[:len(base)] != base:
        return False
    prev_digit = False
    for tok in cand[len(base):]:
        if tok.isdigit():
            prev_digit = True
            continue
        ok = (tok in _BODY_WORDS or tok in _POWER_WORDS or tok == "in"
              or (prev_digit and len(tok) <= 2))    # the h in 450h
        if not ok:
            return False
        prev_digit = False
    return True


def _is_bmw_series(cand, base):
    """BMW files a "4 Series" as 430I, M440I and so on."""
    if len(base) != 2 or base[1] != "series" or not base[0].isdigit():
        return False
    rest = cand[1:] if cand[:1] == ["m"] else cand
    return (bool(rest) and rest[0].isdigit() and len(rest[0]) == 3
            and rest[0].startswith(base[0])
            and all(len(t) <= 2 or t in _BODY_WORDS for t in rest[1:]))


def nhtsa_models(make, year):
    """Every model name NHTSA files this make and year under."""
    data = http.get_json(
        NHTSA_MODELS,
        {"modelYear": year, "make": make, "issueType": "r", "max": 1000},
        ttl=http.TTL_REFERENCE, ok_statuses=NHTSA_EMPTY,
    )
    names = []
    for row in data.get("results") or []:
        name = str(row.get("model") or "").strip()
        # NHTSA marks its own duplicate entries this way.
        if name and not name.lower().startswith("redundant") \
                and name not in names:
            names.append(name)
    return names


def nhtsa_names(make, model, year, powertrain=None):
    """The NHTSA model names to look this car up under.

    powertrain is one of sources.POWERTRAINS when the listing says, and
    keeps a gas car from collecting the hybrid version's recalls (and
    the reverse) where NHTSA files the two separately.

    Returns (names, note). names is never empty: when NHTSA's list can't
    be read, or nothing in it looks like this model, it falls back to
    the listing's own name and the note says so.
    """
    plain = str(model or "").strip()
    try:
        known = nhtsa_models(make, year)
    except http.FetchError as e:
        return [plain], f"could not read NHTSA's model list ({e})"
    if not known:
        return [plain], (f"NHTSA lists no {make} models at all for {year}")

    base = _name_tokens(plain, make)
    listing_power = _name_powertrains(base)
    cands = [(n, _name_tokens(n, make)) for n in known]

    def matches(tokens):
        return [n for n, c in cands
                if _is_variant_of(c, tokens) or _is_bmw_series(c, tokens)]

    found = matches(base)
    # The listing may carry a word NHTSA doesn't ("Unlimited", "HD",
    # "Hybrid", the 1500 in "ProMaster 1500"). Drop those from the end.
    trimmed = list(base)
    while not found and len(trimmed) > 1 and (
            trimmed[-1] in _LISTING_EXTRAS or trimmed[-1].isdigit()):
        trimmed.pop()
        found = matches(trimmed)
    if not found:
        return [plain], (
            f"none of NHTSA's {len(known)} {make} model names for {year} "
            f"matched {plain!r}")

    want = powertrain or (sorted(listing_power)[0] if listing_power else None)
    if want:
        by_power = {n: _name_powertrains(_name_tokens(n, make)) for n in found}
        if want == "gas":
            keep = [n for n in found if not by_power[n]]
        else:
            # Its own powertrain's names, plus the plain ones: recalls
            # on the shared body are filed under the plain name.
            keep = [n for n in found if not by_power[n] or want in by_power[n]]
        # If that leaves nothing (every 2021+ Sienna is "SIENNA HYBRID"),
        # the split doesn't exist for this model; use them all.
        found = keep or found
    return found, None


MAX_RECALL_NAMES = 16


def _spellings(name, make=""):
    """Ways NHTSA's recall file might spell one model name.

    The recall file has no index to ask, and it disagrees with the
    complaint file: "F-150" not "F-150 SUPER CREW", "MODEL Y" not
    "MODEL Y 5-SEAT", "GLS 450" or "GLS450" not "GLS-CLASS", "MUSTANG
    MACH E" without the hyphen, "Q5" not "AUDI Q5". So derive the likely
    spellings and try them all; the lookups are free and cached.
    """
    out = []

    def add(text):
        text = " ".join(str(text).split())
        if text and text.upper() not in (o.upper() for o in out):
            out.append(text)

    text = re.sub(r"\s+", " ", str(name or "")).strip()
    add(text)
    bare = re.sub(r"\(.*?\)", " ", text)            # "(5 DOOR)", "(Super Crew)"
    add(bare)
    words = bare.split()
    if make and len(words) > 1 and words[0].lower() == str(make).lower():
        words = words[1:]                            # "AUDI Q5" -> "Q5"
        add(" ".join(words))
    # Drop trailing cab, body and seat words: "F-150 SUPER CREW" -> "F-150".
    core = list(words)
    while len(core) > 1 and (
            set(re.findall(r"[a-z]+", core[-1].lower())) <= _BODY_WORDS
            and re.search(r"[a-z]", core[-1].lower())):
        core.pop()
        add(" ".join(core))
    for form in list(out):
        if "-" in form:
            add(form.replace("-", " "))              # "MACH-E" -> "MACH E"
        parts = form.split()
        if len(parts) >= 2 and parts[1][:1].isdigit() and parts[0].isalpha():
            add(parts[0] + " " + parts[1])           # "GLE 350 4MATIC" -> "GLE 350"
            add(parts[0] + parts[1])                 # -> "GLE350"
        if re.search(r"\bsuper duty\b", form, re.I):
            add(re.sub(r"\bsuper duty\b", "SD", form, flags=re.I))
            add(re.sub(r"\s*\bsuper duty\b", "", form, flags=re.I))
    return out


def recall_names(make, model, complaint_names, listing=None, vin_decode=None):
    """Every model name worth asking the recall file about."""
    listing, vd = listing or {}, vin_decode or {}
    names = []

    def add_all(source):
        for n in _spellings(source, make):
            if n.upper() not in (x.upper() for x in names):
                names.append(n)

    plain = str(model or "").strip()
    add_all(plain)
    # The listing's own extras off the end: "Wrangler Unlimited",
    # "Silverado 2500HD", "RAV4 Hybrid".
    stem = re.sub(r"(?i)(\s+(unlimited|hybrid|plug-in hybrid|phev|prime|"
                  r"energi|4xe)|(?<=\d)hd)\s*$", "", plain)
    add_all(stem)
    # The Ram 1500 Classic's recalls are in the plain 1500's file.
    add_all(re.sub(r"(?i)\s+classic\s*$", "", stem))
    for n in complaint_names or []:
        add_all(n)
    # Luxury makes file recalls by badge ("GLS 450", "430I", "RX350"),
    # which is the listing's trim or the VIN's series, not its model.
    base = re.sub(r"(?i)[\s-]*class$", "", stem).strip()
    for extra in (listing.get("trim"), vd.get("Series"), vd.get("Trim"),
                  vd.get("Model")):
        words = str(extra or "").split()
        if not words:
            continue
        first = words[0]
        if first.lower() == base.lower() and len(words) > 1:
            first = words[1]                         # trim "GLS 450 4MATIC"
        if re.fullmatch(r"\d{2,3}[a-zA-Z]{0,2}", first):
            if re.fullmatch(r"\d\s*series", base, re.I):
                add_all(first)                       # BMW: "430i"
            elif base and len(base) <= 4:
                add_all(f"{base} {first}")           # "GLS 450", and "GLS450"
        elif re.fullmatch(r"[a-zA-Z]?\d{3}[a-zA-Z]{1,2}", first):
            add_all(first)                           # "M440i"
    return names[:MAX_RECALL_NAMES]


def _unique(items, key):
    seen, out = set(), []
    for it in items:
        k = it.get(key) or id(it)
        if k not in seen:
            seen.add(k)
            out.append(it)
    return out


def _nhtsa_pull(url, make, names, year, key):
    """Results for every name, merged, plus which names had any."""
    items, with_data = [], []
    for name in names:
        data = http.get_json(
            url, {"make": make, "model": name, "modelYear": year},
            ttl=http.TTL_REFERENCE, ok_statuses=NHTSA_EMPTY,
        )
        got = data.get("results") or []
        if got:
            with_data.append(name)
        items.extend(got)
    return _unique(items, key), with_data


def recalls(make, model, year, names=None):
    names = names or [model]
    items, with_data = _nhtsa_pull(NHTSA_RECALLS, make, names, year,
                                   "NHTSACampaignNumber")
    return {
        "count": len(items),
        "nhtsa_names_tried": list(names),
        "nhtsa_names_with_data": with_data,
        "items": [
            {
                "campaign": r.get("NHTSACampaignNumber"),
                "component": r.get("Component"),
                "reported": r.get("ReportReceivedDate"),
                "summary": _trim(r.get("Summary"), 500),
                "consequence": _trim(r.get("Consequence"), 300),
                "remedy": _trim(r.get("Remedy"), 300),
            }
            for r in items[:MAX_RECALLS]
        ],
        "truncated": max(0, len(items) - MAX_RECALLS),
    }


def complaints(make, model, year, names=None):
    names = names or [model]
    items, with_data = _nhtsa_pull(NHTSA_COMPLAINTS, make, names, year,
                                   "odiNumber")

    by_component = {}
    for c in items:
        for comp in str(c.get("components") or "unknown").split(","):
            comp = comp.strip() or "unknown"
            by_component[comp] = by_component.get(comp, 0) + 1

    ranked = sorted(by_component.items(), key=lambda kv: kv[1], reverse=True)

    def _date(c):
        return c.get("dateComplaintFiled") or ""

    recent = sorted(items, key=_date, reverse=True)[:MAX_COMPLAINT_SAMPLES]

    return {
        "count": len(items),
        "nhtsa_names_tried": list(names),
        "nhtsa_names_with_data": with_data,
        "by_component": dict(ranked[:10]),
        "top_component": ranked[0][0] if ranked else None,
        "crashes": sum(1 for c in items if c.get("crash")),
        "fires": sum(1 for c in items if c.get("fire")),
        "injuries": sum(int(c.get("numberOfInjuries") or 0) for c in items),
        "samples": [
            {
                "filed": c.get("dateComplaintFiled"),
                "components": c.get("components"),
                "miles": c.get("odometer"),
                "summary": _trim(c.get("summary"), COMPLAINT_SUMMARY_CHARS),
            }
            for c in recent
        ],
    }


def _fe_text(node, tag, cast=None):
    el = node.find(tag)
    if el is None or el.text is None:
        return None
    if cast:
        try:
            return cast(el.text)
        except ValueError:
            return None
    return el.text


def _norm(s):
    return "".join(ch for ch in str(s or "").lower() if ch.isalnum())


def _is_awd(text):
    t = str(text or "").lower()
    return "awd" in t or "4wd" in t or "all-wheel" in t or "4-wheel" in t


def _epa_model_names(make, model, year, want_awd):
    """EPA's own model names that correspond to ours, AWD ones first."""
    menu = http.get_xml(
        FE_MODELS, {"year": year, "make": make}, ttl=http.TTL_REFERENCE * 12
    )
    names = [_fe_text(i, "value") for i in menu.findall("menuItem")]
    names = [n for n in names if n]

    # Mazda calls the Mazda3 just "3", Kia calls the K5 "K5", drop a
    # leading make name from our model before matching.
    target = _norm(model)
    if target.startswith(_norm(make)):
        target = target[len(_norm(make)):] or _norm(model)

    hits = [n for n in names if _norm(n).startswith(target)]
    if not hits:
        hits = [n for n in names if target and target in _norm(n)]

    if want_awd:
        awd = [n for n in hits if _is_awd(n)]
        if awd:
            # Keep non-AWD names as a fallback behind the AWD ones.
            hits = awd + [n for n in hits if not _is_awd(n)]
    return hits


def fuel_economy(make, model, year, displacement=None, want_awd=True):
    """EPA mileage for the variants of this year/make/model.

    Returns every variant we found plus a best guess. The guess prefers
    an entry with the same driven wheels as the car (all-wheel-drive
    entries for an AWD car, two-wheel-drive ones otherwise) and then the
    closest engine displacement to the VIN decode, but the variants
    list is there so you can check it picked the right one.

    For electric and plug-in cars `mpg_combined` is MPGe, which is not a
    number you can divide gallons by. Those carry `kwh_per_100mi` and the
    EPA's own `annual_fuel_cost_usd`, and tco.py uses that instead.
    """
    try:
        candidates = _epa_model_names(make, model, year, want_awd)
    except http.FetchError:
        candidates = [model]
    if not candidates:
        return {"variants": [], "best_match": None,
                "note": f"No EPA model matching '{model}' for {year} {make}."}

    variants = []
    for name in candidates[:MAX_FE_MODELS]:
        if len(variants) >= MAX_FE_VARIANTS:
            break
        try:
            menu = http.get_xml(
                FE_MENU, {"year": year, "make": make, "model": name},
                ttl=http.TTL_REFERENCE * 12,
            )
        except http.FetchError:
            continue
        options = [
            {"label": _fe_text(i, "text"), "id": _fe_text(i, "value")}
            for i in menu.findall("menuItem")
        ]
        for opt in [o for o in options if o["id"]][:MAX_FE_OPTIONS_PER_MODEL]:
            try:
                v = http.get_xml(
                    FE_VEHICLE.format(id=opt["id"]), ttl=http.TTL_REFERENCE * 12
                )
            except http.FetchError:
                continue
            variants.append({
                "epa_model": name,
                "label": opt["label"],
                "id": opt["id"],
                "mpg_combined": _fe_text(v, "comb08", int),
                "mpg_city": _fe_text(v, "city08", int),
                "mpg_highway": _fe_text(v, "highway08", int),
                "annual_fuel_cost_usd": _fe_text(v, "fuelCost08", int),
                "displacement_l": _fe_text(v, "displ", float),
                "cylinders": _fe_text(v, "cylinders", int),
                "drive": _fe_text(v, "drive"),
                "transmission": _fe_text(v, "trany"),
                # "Regular Gasoline", "Premium Gasoline", "Diesel",
                # "Electricity"; atv_type is "EV", "Plug-in Hybrid",
                # "Hybrid", "Diesel" or absent for a plain petrol car.
                "fuel_type": _fe_text(v, "fuelType1"),
                "atv_type": _fe_text(v, "atvType"),
                "kwh_per_100mi": _fe_text(v, "combE", float) or None,
            })

    if not variants:
        return {"variants": [], "best_match": None,
                "note": f"EPA listed {candidates[:3]} but returned no mileage data."}

    awd = [v for v in variants if _is_awd(v.get("drive")) or _is_awd(v.get("epa_model"))]
    two_wd = [v for v in variants if v not in awd]
    if want_awd:
        pool = awd or variants
    else:
        pool = two_wd or variants

    best = pool[0]
    if displacement:
        try:
            target = float(displacement)
            best = min(pool, key=lambda v: abs((v["displacement_l"] or 99) - target))
        except (TypeError, ValueError):
            pass

    if want_awd and not awd:
        matched = "no AWD variant in EPA data; using two-wheel-drive figures"
    elif not want_awd and not two_wd:
        matched = "only AWD variants in EPA data; using those figures"
    else:
        matched = "AWD variant" if want_awd else "two-wheel-drive variant"
        if displacement and best.get("displacement_l"):
            matched += ", closest engine displacement"

    return {"variants": variants, "best_match": best, "matched_on": matched}


def _powertrain(listing, out):
    """gas / hybrid / plug-in hybrid / electric / diesel for this car, or
    None when neither the listing nor the VIN decode says."""
    kind = str(listing.get("powertrain_type") or "").upper()
    fuel = str(listing.get("fuel_type") or "").lower()
    vd = out.get("vin_decode") or {}
    level = str(vd.get("ElectrificationLevel") or "").lower()
    vfuel = str(vd.get("FuelTypePrimary") or "").lower()
    if kind == "BEV" or fuel == "electric" or "bev" in level \
            or vfuel == "electric":
        return "electric"
    if kind == "PHEV" or "phev" in level or "plug-in" in level:
        return "plug-in hybrid"
    if kind == "HEV" or "strong hev" in level or "full hev" in level:
        return "hybrid"
    if "diesel" in fuel or "diesel" in vfuel:
        return "diesel"
    if kind in ("COMBUSTION", "MHEV") or (vd and vfuel == "gasoline"
                                          and not level):
        return "gas"
    return None


def research_vehicle(listing):
    """Everything we can learn about one listing. Never raises, each
    source that fails is recorded in `errors` so partial results still
    come back useful."""
    vin = listing.get("vin", "")
    make = listing.get("make", "")
    model = listing.get("model", "")
    year = listing.get("year")

    out = {
        "vin": vin,
        "listing": listing,
        "vin_decode": None,
        "recalls": None,
        "complaints": None,
        "fuel_economy": None,
        "errors": [],
    }

    # A VIN decode is only meaningful for a real VIN, not sample data.
    if vin and len(vin) == 17:
        try:
            out["vin_decode"] = decode_vin(vin)
        except http.FetchError as e:
            out["errors"].append(f"vin_decode: {e}")
    else:
        out["errors"].append(
            "vin_decode: skipped because this is not a 17-character VIN "
            "(demo listings use placeholder VINs; a real listing's VIN "
            "is decoded to its exact engine, transmission and plant)"
        )

    if make and model and year:
        names, note = nhtsa_names(make, model, year, _powertrain(listing, out))
        r_names = recall_names(make, model, None if note else names,
                               listing, out["vin_decode"])
        for name, fn in (
            ("recalls", lambda: recalls(make, model, year, r_names)),
            ("complaints", lambda: complaints(make, model, year, names)),
        ):
            try:
                out[name] = fn()
            except http.FetchError as e:
                out["errors"].append(f"{name}: {e}")

        # An empty answer is only a clean record if we know NHTSA has
        # this model on file under a name we asked for. Otherwise it is
        # a lookup that may have missed, and it has to say so.
        cp = out.get("complaints")
        if cp is not None:
            cp["name_matched"] = note is None
            if cp["count"] == 0 and note:
                cp["unverified_empty"] = True
                out["errors"].append(
                    f"complaints: NHTSA returned nothing, but {note}. This "
                    f"is probably a model-name mismatch, NOT a clean "
                    f"record.")
        rc = out.get("recalls")
        if rc is not None and rc["count"] == 0:
            # The recall file has no list of its own model names to
            # check against, so zero can never be confirmed from here.
            rc["unverified_empty"] = True
            out["errors"].append(
                "recalls: none found under the model names tried ("
                + ", ".join(rc["nhtsa_names_tried"][:6])
                + ("…" if len(rc["nhtsa_names_tried"]) > 6 else "")
                + "). NHTSA files recalls under its own model names, so "
                  "this is NOT confirmation that there are none. Check the "
                  "VIN at nhtsa.gov/recalls.")

        displ = (out["vin_decode"] or {}).get("DisplacementL")
        want_awd = _is_awd(listing.get("drivetrain")) or _is_awd(listing.get("trim"))
        try:
            out["fuel_economy"] = fuel_economy(make, model, year, displ, want_awd)
        except http.FetchError as e:
            out["errors"].append(f"fuel_economy: {e}")
    else:
        out["errors"].append("year/make/model incomplete; skipped NHTSA lookups")

    return out
