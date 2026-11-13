"""Load and validate the config file.

The config is YAML (config.yaml) or JSON (config.json). PyYAML is used
when it is installed, but nothing has to be installed: the small reader
below handles the plain YAML this tool's own template and setup wizard
write (nested keys, lists, quoted and bare scalars, comments).
"""
import copy
import json
import os
import re

DEFAULTS = {
    "output": {
        "max_results": 100,
        "open_report_when_done": False,
        # Housekeeping: how many dated search reports (results_*.html
        # and .csv) and how many researched cars to keep. Older ones
        # are deleted. latest.html and research.html are always kept.
        "keep_reports": 10,
        "keep_research": 50,
    },
    # Price and mileage lead, because they exist for every car, so a
    # model with a reliability profile and one without still compete on
    # the same basis. Reliability is a tiebreaker, not the decider;
    # known problems surface as flags instead of a silent score penalty.
    "scoring": {
        "weight_value": 0.45,
        "weight_mileage": 0.30,
        "weight_reliability": 0.15,
        "weight_maintenance": 0.10,
    },
    "api": {
        "call_limit": 500,
        "warn_at_pct": 80,
        "max_requests_per_second": 4,
        # A search that names no model (a whole make, or no make at all)
        # can turn up many models, and pricing each one against its
        # market costs one call. This is how many get priced without
        # being asked; the rest are listed unpriced.
        "price_models": 3,
    },
    "ownership": {
        "years": 5,
        "annual_miles": 12000,
        "fuel_price_per_gallon": 3.35,
        "baseline_insurance_annual": 1650,
        "tire_replacement_interval_miles": 45000,
        "annual_registration_usd": 180,
        "maintenance_escalation_per_10k": 0.06,
    },
}


# ------------------------------------------------------- plain YAML reader

def _strip_comment(line):
    """Drop a trailing # comment, leaving any # inside quotes alone."""
    quote = None
    for i, ch in enumerate(line):
        if quote:
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
        elif ch == "#" and (i == 0 or line[i - 1] in " \t"):
            return line[:i]
    return line


def _scalar(text):
    t = text.strip()
    if t == "" or t in ("~", "null", "Null", "NULL"):
        return None
    if len(t) >= 2 and t[0] == t[-1] and t[0] in "\"'":
        body = t[1:-1]
        if t[0] == '"':
            return body.replace('\\"', '"').replace("\\\\", "\\")
        return body.replace("''", "'")
    if t.startswith("[") and t.endswith("]"):
        inner = t[1:-1].strip()
        return [_scalar(x) for x in _split_flow(inner)] if inner else []
    if t in ("true", "True", "TRUE"):
        return True
    if t in ("false", "False", "FALSE"):
        return False
    if re.fullmatch(r"[-+]?\d+", t):
        # A leading zero means it is a code, not a quantity: the ZIP
        # 02134 must not become the number 2134.
        if len(t.lstrip("+-")) > 1 and t.lstrip("+-").startswith("0"):
            return t
        return int(t)
    if re.fullmatch(r"[-+]?(\d+\.\d*|\.\d+|\d+)([eE][-+]?\d+)?", t):
        return float(t)
    return t


def _split_flow(inner):
    """Split "a, 'b, c', d" on the commas that are outside quotes."""
    parts, cur, quote = [], "", None
    for ch in inner:
        if quote:
            cur += ch
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            cur += ch
        elif ch == ",":
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    parts.append(cur)
    return parts


def _key_value(content):
    """Split "key: value" into (key, value text), or None if it isn't one."""
    m = re.match(r"""^("[^"]*"|'[^']*'|[^\s:#'"\[\]{}][^:]*?)\s*:(\s+(.*))?$""",
                 content)
    if not m:
        return None
    key = m.group(1).strip()
    if key[:1] in "\"'":
        key = key[1:-1]
    return key, (m.group(3) or "")


def _parse_block(lines, i, indent):
    """Parse the block starting at lines[i], whose lines sit at `indent`.
    Returns (value, index of the first line after the block)."""
    if lines[i][1].startswith("- ") or lines[i][1] == "-":
        out = []
        while i < len(lines) and lines[i][0] == indent and (
                lines[i][1].startswith("- ") or lines[i][1] == "-"):
            rest = lines[i][1][1:].strip()
            inner = indent + 1 + (len(lines[i][1]) - 1
                                  - len(lines[i][1][1:].lstrip()))
            if rest and _key_value(rest):
                # A mapping written inline after the dash. Treat the
                # rest of the line as the first line of a nested block.
                lines[i] = (inner, rest)
                item, i = _parse_block(lines, i, inner)
            elif rest:
                item, i = _scalar(rest), i + 1
            elif i + 1 < len(lines) and lines[i + 1][0] > indent:
                item, i = _parse_block(lines, i + 1, lines[i + 1][0])
            else:
                item, i = None, i + 1
            out.append(item)
        return out, i

    out = {}
    while i < len(lines) and lines[i][0] == indent:
        kv = _key_value(lines[i][1])
        if not kv:
            raise ValueError(f"can't read this config line: {lines[i][1]!r}")
        key, value = kv
        i += 1
        if value.strip():
            out[key] = _scalar(value)
        elif i < len(lines) and (
                lines[i][0] > indent
                or (lines[i][0] == indent and lines[i][1].startswith("-"))):
            out[key], i = _parse_block(lines, i, lines[i][0])
        else:
            out[key] = None
    return out, i


def parse_simple_yaml(text):
    """Read block-style YAML: nested mappings, lists, plain scalars.

    Not a full YAML parser. Anchors, multi-line strings and nested flow
    collections are out of scope; a file that needs them should be read
    with PyYAML installed, or written as JSON.
    """
    lines = []
    for raw in text.replace("\t", "    ").splitlines():
        line = _strip_comment(raw).rstrip()
        if not line.strip() or line.strip() in ("---", "..."):
            continue
        lines.append((len(line) - len(line.lstrip()), line.strip()))
    if not lines:
        return {}
    value, end = _parse_block(lines, 0, lines[0][0])
    if end != len(lines):
        raise ValueError(
            f"can't read this config line (check its indentation): "
            f"{lines[end][1]!r}")
    return value


def _read(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        text = f.read()
    if path.lower().endswith(".json"):
        return json.loads(text) if text.strip() else {}
    try:
        import yaml
    except ModuleNotFoundError:
        return parse_simple_yaml(text)
    cfg = yaml.safe_load(text) or {}
    # PyYAML reads an unquoted `zip: 02134` as the octal number 1116,
    # and the real ZIP cannot be recovered from that. Take it from the
    # text instead.
    raw_zip = re.search(r"(?m)^[ \t]+zip:[ \t]*([0-9]{1,5})[ \t]*(#.*)?$", text)
    if raw_zip and isinstance(cfg, dict) and isinstance(cfg.get("search"), dict) \
            and not isinstance(cfg["search"].get("zip"), str):
        cfg["search"]["zip"] = raw_zip.group(1)
    return cfg


# ----------------------------------------------------------------- loading

def _fill_defaults(cfg):
    for section, defaults in DEFAULTS.items():
        if not isinstance(cfg.get(section), dict):
            cfg[section] = {}
        for k, v in defaults.items():
            cfg[section].setdefault(k, v)

    # weight_price was the old name for weight_value; keep old configs working
    scoring = cfg["scoring"]
    if "weight_price" in scoring and "weight_value" not in scoring:
        scoring["weight_value"] = scoring.pop("weight_price")
    return cfg


def default_config():
    """A config with no search in it: the ownership, scoring and API
    defaults only. Enough for commands that don't search, such as
    researching a VIN the user pasted."""
    cfg = _fill_defaults({})
    cfg["search"] = None
    cfg["targets"] = []
    return copy.deepcopy(cfg)


def finish_search(search):
    """Fill the optional search keys. Blank body type or drivetrain
    means "any"."""
    # A ZIP is text. Written without quotes it arrives as a number that
    # has lost its leading zeros (02134 -> 2134), so put them back.
    zip_code = search.get("zip")
    if isinstance(zip_code, bool) or isinstance(zip_code, float):
        raise ValueError(f"zip {zip_code!r} is not a ZIP code; write it "
                         f"in quotes, like zip: \"02134\".")
    zip_code = str(zip_code or "").strip()
    if zip_code.isdigit() and len(zip_code) < 5:
        zip_code = zip_code.zfill(5)
    if not re.fullmatch(r"\d{5}(-\d{4})?", zip_code):
        raise ValueError(f"zip {zip_code!r} is not a 5-digit ZIP code; "
                         f"write it in quotes, like zip: \"02134\".")
    search["zip"] = zip_code
    search.setdefault("radius_miles", 50)
    search.setdefault("price_min", 0)
    search.setdefault("price_max", 1000000)
    search.setdefault("miles_min", 0)
    search.setdefault("miles_max", 300000)
    search.setdefault("body_type", "")
    search.setdefault("drivetrain", "")
    search.setdefault("powertrain", "")
    search.setdefault("year_min", None)
    search.setdefault("year_max", None)
    search.setdefault("car_types", ["used"])
    for key in ("year_min", "year_max"):
        if search[key] in ("", 0):
            search[key] = None
    lo, hi = search["year_min"], search["year_max"]
    if lo and hi and int(lo) > int(hi):
        raise ValueError(f"year_min ({lo}) is after year_max ({hi}).")
    return search


def load_config(path="config.yaml"):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Could not find {path}."
        )
    cfg = _read(path)
    if not isinstance(cfg, dict):
        raise ValueError(f"{os.path.basename(path)} is not a config file.")
    _fill_defaults(cfg)

    name = os.path.basename(path)
    if not isinstance(cfg.get("search"), dict) or not cfg["search"].get("zip"):
        raise ValueError(f"{name} must define 'search' with a 'zip'.")
    # No targets means an open search: every make that fits the filters.
    cfg["targets"] = [t for t in (cfg.get("targets") or [])
                      if isinstance(t, dict)] or [{}]

    finish_search(cfg["search"])
    return cfg
