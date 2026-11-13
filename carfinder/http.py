"""
Shared HTTP helper with an on-disk response cache.

Every external call in this project is a plain GET that returns JSON or
XML, and nearly all of them are worth caching: Marketcheck credits are
limited on the free tier, and the NHTSA / FuelEconomy data barely moves
day to day. Caching also means you can iterate on scoring without
re-spending credits on the same search.

Cache files live in .cache/ inside the data folder (see paths.py) and
are keyed by a hash of the URL and params. The API key is stripped from the key so rotating your key
doesn't invalidate everything.
"""
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from . import paths

CACHE_DIR = paths.cache_dir()
USAGE_FILE = os.path.join(CACHE_DIR, "usage.json")

# Default time-to-live per kind of data. Listings go stale fast; the
# shape of a model's local price surface does not, and a VIN decode
# never changes at all.
TTL_LISTINGS = 6 * 3600
TTL_COMPARABLES = 7 * 24 * 3600
TTL_REFERENCE = 30 * 24 * 3600

USER_AGENT = "car-finder/2.0 (personal used-car search)"

# Only these cost money. NHTSA and FuelEconomy.gov are free public APIs,
# so they are never counted against the budget or rate limited.
METERED_HOSTS = {"api.marketcheck.com"}

# Runtime limits, set from config by configure().
_limits = {
    "call_limit": None,     # None = unlimited
    "warn_at_pct": 80,
    "min_interval": 0.25,   # 4 req/s, under Marketcheck's 5 rps ceiling
    "cached_only": False,
}
_last_request_at = [0.0]
_calls_this_run = [0]


class FetchError(Exception):
    """Any failure to get usable data back from an endpoint."""


class BudgetExceeded(FetchError):
    """Refused to spend another metered call against the plan limit."""


class CacheMiss(FetchError):
    """--cached-only was set and this request wasn't already cached."""


def configure(call_limit=None, warn_at_pct=80, max_rps=4, cached_only=False):
    _limits["call_limit"] = call_limit
    _limits["warn_at_pct"] = warn_at_pct
    _limits["min_interval"] = 1.0 / max_rps if max_rps else 0.0
    _limits["cached_only"] = cached_only


def _read_usage():
    data = _cache_read_raw(USAGE_FILE) or {}
    data.setdefault("total", 0)
    data.setdefault("by_month", {})
    return data


def _cache_read_raw(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def _bump_usage():
    data = _read_usage()
    month = time.strftime("%Y-%m")
    data["total"] += 1
    data["by_month"][month] = data["by_month"].get(month, 0) + 1
    _calls_this_run[0] += 1
    try:
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(USAGE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except OSError:
        pass
    return data["total"]


def usage_summary():
    """Where the metered call budget stands."""
    data = _read_usage()
    limit = _limits["call_limit"]
    used = data["total"]
    return {
        "used": used,
        "limit": limit,
        "remaining": (limit - used) if limit else None,
        "this_run": _calls_this_run[0],
        "by_month": data["by_month"],
    }


def set_usage(total):
    """Seed or reset the counter, use when your quota renews, or to
    account for calls made before tracking existed."""
    data = _read_usage()
    data["total"] = max(0, int(total))
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(USAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return data["total"]


def calls_this_run():
    return _calls_this_run[0]


def _throttle():
    """Keep total request rate under the plan's ceiling."""
    gap = _limits["min_interval"]
    if gap <= 0:
        return
    wait = gap - (time.time() - _last_request_at[0])
    if wait > 0:
        time.sleep(wait)
    _last_request_at[0] = time.time()


def _cache_path(url, params):
    safe = {k: v for k, v in (params or {}).items() if k != "api_key"}
    blob = url + "?" + urllib.parse.urlencode(sorted(safe.items()))
    digest = hashlib.sha256(blob.encode()).hexdigest()[:32]
    return os.path.join(CACHE_DIR, digest + ".json")


def _cache_read(path, ttl):
    if ttl <= 0 or not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            entry = json.load(f)
    except (OSError, ValueError):
        return None
    if time.time() - entry.get("ts", 0) > ttl:
        return None
    return entry.get("body")


def _cache_write(path, body, ttl=TTL_REFERENCE):
    try:
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            # ts and ttl first, so prune_cache can read them from the
            # head of the file without parsing a megabyte of listings.
            json.dump({"ts": time.time(), "ttl": ttl, "body": body}, f)
    except OSError:
        pass  # a cache failure should never break a run


def prune_cache(every=24 * 3600):
    """Delete cached responses that have expired, at most once a day.

    An expired entry is never served again, so it is only disk space.
    Entries written before the ttl was recorded are given 30 days. Only
    this module's own <hash>.json files are touched; usage.json, the
    call counter, is not one of them. Returns how many were removed.
    """
    stamp = os.path.join(CACHE_DIR, "pruned")
    now = time.time()
    try:
        if now - os.path.getmtime(stamp) < every:
            return 0
    except OSError:
        pass
    try:
        names = os.listdir(CACHE_DIR)
        open(stamp, "w").close()
    except OSError:
        return 0
    n = 0
    for name in names:
        if not re.fullmatch(r"[0-9a-f]{32}\.json", name):
            continue
        path = os.path.join(CACHE_DIR, name)
        try:
            with open(path, "r", encoding="utf-8") as f:
                m = re.match(r'\{"ts": ([\d.]+)(?:, "ttl": ([\d.]+))?',
                             f.read(80))
            ts = float(m.group(1)) if m else os.path.getmtime(path)
            ttl = float(m.group(2)) if m and m.group(2) else TTL_REFERENCE
            if now - ts > ttl:
                os.remove(path)
                n += 1
        except (OSError, ValueError):
            pass
    return n


def fetch(url, params=None, ttl=TTL_REFERENCE, timeout=30,
          accept="application/json", ok_statuses=()):
    """GET a URL and return the raw response body as text, cached on disk.

    ok_statuses lists HTTP error codes whose response body should still be
    treated as a real answer. NHTSA needs this: asking about a vehicle
    with zero recalls returns 400 with a perfectly valid
    {"Count":0,"results":[]} payload. Kept opt-in so a genuine 400 from
    another API (a bad Marketcheck key, say) still fails loudly.
    """
    path = _cache_path(url, params)
    cached = _cache_read(path, ttl)
    if cached is not None:
        return cached

    metered = urllib.parse.urlparse(url).hostname in METERED_HOSTS
    if metered:
        if _limits["cached_only"]:
            raise CacheMiss(
                "--cached-only is set and this request isn't cached; "
                "skipping rather than spending a call"
            )
        limit = _limits["call_limit"]
        if limit is not None and _read_usage()["total"] >= limit:
            raise BudgetExceeded(
                f"API call budget exhausted ({limit} calls). Raise "
                f"api.call_limit in config.yaml, or run "
                f"`python run.py usage --reset` when your quota renews."
            )

    _throttle()
    if metered:
        # Counted before the result is known: a 4xx still consumed a call
        # on the provider's side, and over-counting is the safe direction
        # to be wrong in when the budget is the scarce resource.
        _bump_usage()

    full = url
    if params:
        full += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        full, headers={"User-Agent": USER_AGENT, "Accept": accept}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        # Read the body before deciding: APIs put the actual reason in
        # there, and a bare "HTTP 422" tells you nothing about which
        # parameter it objected to.
        try:
            body = e.read().decode("utf-8", errors="replace")
        except Exception:
            body = ""
        if e.code not in ok_statuses:
            detail = f": {' '.join(body.split())[:300]}" if body.strip() else ""
            if e.code == 429:
                raise FetchError(
                    f"rate limit hit{detail}. Cached results still work; "
                    f"wait and re-run, or check your plan's quota."
                ) from e
            raise FetchError(f"HTTP {e.code} from {url}{detail}") from e
        if not body.strip():
            raise FetchError(f"HTTP {e.code} with empty body from {url}") from e
    except Exception as e:  # timeouts, DNS, connection resets
        raise FetchError(f"{type(e).__name__} from {url}: {e}") from e

    _cache_write(path, body, ttl)
    return body


def get_json(url, params=None, ttl=TTL_REFERENCE, timeout=30, ok_statuses=()):
    body = fetch(url, params, ttl=ttl, timeout=timeout, ok_statuses=ok_statuses)
    try:
        return json.loads(body)
    except ValueError as e:
        raise FetchError(f"Non-JSON response from {url}") from e


def get_xml(url, params=None, ttl=TTL_REFERENCE, timeout=30):
    """FuelEconomy.gov speaks XML natively, so parse it rather than
    asking for a JSON representation that may or may not be offered."""
    body = fetch(url, params, ttl=ttl, timeout=timeout, accept="application/xml")
    try:
        return ET.fromstring(body)
    except ET.ParseError as e:
        raise FetchError(f"Malformed XML from {url}") from e


def clear_cache():
    """Delete every cached response. Returns how many files were removed."""
    if not os.path.isdir(CACHE_DIR):
        return 0
    n = 0
    for name in os.listdir(CACHE_DIR):
        if name.endswith(".json"):
            try:
                os.remove(os.path.join(CACHE_DIR, name))
                n += 1
            except OSError:
                pass
    return n
