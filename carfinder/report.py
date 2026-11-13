"""Write results to a CSV and a self-contained HTML report."""
import csv
import html
import os
import re

CSV_FIELDS = [
    "score", "year", "make", "model", "trim", "price", "miles",
    "market_expected", "market_delta_usd", "car_type", "drivetrain",
    "generation", "reliability", "maintenance", "unrated", "is_new",
    "price_drop", "dealer_name", "dealer_city", "dealer_state",
    "distance", "vin", "url",
]


def _flatten(r):
    """CSV wants a flat row; the JSON keeps the nested structure."""
    row = dict(r)
    mk = r.get("market") or {}
    row["market_expected"] = mk.get("expected")
    row["market_delta_usd"] = mk.get("delta_usd")
    return row


def write_csv(listings, path):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS, extrasaction="ignore")
        w.writeheader()
        for r in listings:
            w.writerow(_flatten(r))


def _fmt_money(v):
    return f"${v:,.0f}" if isinstance(v, (int, float)) else "n/a"


def _fmt_miles(v):
    return f"{v:,.0f} mi" if isinstance(v, (int, float)) else "n/a"


def _fmt_liters(v):
    """vPIC reports displacement like 2.998832712; show it as 3.0L."""
    try:
        return f"{float(v):.1f}L"
    except (TypeError, ValueError):
        return ""


def _fmt_dist(v):
    return f"{v:.0f} mi away" if isinstance(v, (int, float)) else ""


def _market_cell(r):
    mk = r.get("market")
    if not mk:
        return ('<span class="nodata">not priced</span>'
                '<div class="dist">too few comparables</div>')
    delta = mk["delta_usd"]
    pct = mk["delta_pct"] * 100
    if delta > 250:
        cls, sign = "good", "under"
    elif delta < -250:
        cls, sign = "bad", "over"
    else:
        cls, sign = "flat", "at"
    if cls == "flat":
        return f'<span class="flat">at market</span>'
    n = mk["sample_size"]
    basis = ("vs. sticker price" if n == 1 and "MSRP" in str(mk.get("basis"))
             else f'{n} comparable{"s" if n != 1 else ""}')
    return (f'<span class="{cls}">{_fmt_money(abs(delta))} {sign}</span>'
            f'<div class="dist">{abs(pct):.0f}% · {basis}</div>')


def write_html(listings, path, search, source_label, generated_at):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    rows = []
    for i, r in enumerate(listings, 1):
        title = f'{r.get("year","")} {r.get("make","")} {r.get("model","")} {r.get("trim","")}'.strip()
        url = r.get("url") or "#"
        loc = ", ".join(x for x in [r.get("dealer_city"), r.get("dealer_state")] if x)
        note = r.get("note", "")
        caution = bool(r.get("risk"))
        score = r.get("score", 0)

        badges = ""
        if r.get("is_new"):
            badges += '<span class="badge new">NEW</span>'
        if r.get("price_drop"):
            badges += f'<span class="badge drop">−{_fmt_money(r["price_drop"])}</span>'
        if r.get("unrated"):
            badges += '<span class="badge unrated">UNRATED</span>'

        missing = r.get("missing_components") or []
        labels = {"value": "market price", "mileage": "mileage",
                  "reliability": "reliability", "maintenance": "repair cost"}
        partial = (f'<div class="dist">Partial score: no '
                   f'{", ".join(labels.get(m, m) for m in missing)} data'
                   f'</div>') if missing else ""

        flags = r.get("flags") or []
        flagged = "".join(
            f'<div class="flag">⚠ {html.escape(f[:1].upper() + f[1:])}</div>'
            for f in flags)

        rel = r.get("reliability")
        rows.append(f"""
        <tr class="{'caution' if caution else ''}">
          <td class="rank">{i}</td>
          <td class="score"><div class="bar" style="--w:{score}%"></div><span>{score}</span></td>
          <td class="title"><a href="{html.escape(url)}" target="_blank">{html.escape(title)}</a>{badges}
              <div class="note">{html.escape(note)}</div>{flagged}
              <div class="vin">{html.escape(r.get('vin',''))}</div>{partial}</td>
          <td class="price">{_fmt_money(r.get('price'))}</td>
          <td class="mkt">{_market_cell(r)}</td>
          <td>{_fmt_miles(r.get('miles'))}</td>
          <td>{html.escape(str(r.get('car_type','')).title())}</td>
          <td class="rel">{f'{rel}/10' if rel is not None else 'n/a'}</td>
          <td>{html.escape(loc)}<div class="dist">{_fmt_dist(r.get('distance'))}</div></td>
        </tr>""")

    s = search
    body = str(s.get("body_type") or "").strip().lower()
    drive = str(s.get("drivetrain") or "").strip()
    kind = (body + "s") if body else "all body types"
    kind = f"{drive} {kind}" if drive else kind[:1].upper() + kind[1:]
    pt = s.get("powertrain")
    pt = ", ".join(pt) if isinstance(pt, (list, tuple)) else str(pt or "")
    if pt.strip():
        kind += f" · {pt.strip()}"
    lo, hi = s.get("year_min"), s.get("year_max")
    if lo and hi:
        kind += f" · {lo}-{hi}"
    elif lo:
        kind += f" · {lo} or newer"
    elif hi:
        kind += f" · {hi} or older"
    subtitle = (
        f'{html.escape(kind)} · '
        f'${s["price_min"]:,}-${s["price_max"]:,} · '
        f'≤{s["miles_max"]:,} mi · within {s["radius_miles"]} mi of {s["zip"]}'
    )
    n_new = sum(1 for r in listings if r.get("is_new"))
    body_rows = "".join(rows) if rows else (
        '<tr><td colspan="9" class="empty">No matches this run. '
        'Try a wider radius, price range or mileage limit.</td></tr>'
    )

    doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Car Finder results</title>
<style>
  :root {{ color-scheme: light dark; }}
  * {{ box-sizing: border-box; }}
  body {{ font-family: -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
    margin: 0; padding: 32px; background: #0f1115; color: #e7e9ee; }}
  @media (prefers-color-scheme: light) {{
    body {{ background:#f7f8fa; color:#1a1d24; }}
    th, td {{ border-bottom-color:#e3e6ec !important; }}
    .sub, .note, th, .rank {{ color:#5b6472 !important; }}
    .meta, .dist, .vin, .foot {{ color:#6b7280 !important; }}
    .title a {{ color:#1d4ed8 !important; }}
    tr.caution .title a, .flag {{ color:#b45309 !important; }}
    .mkt .good {{ color:#15803d !important; }}
    .mkt .bad {{ color:#b91c1c !important; }}
  }}
  .wrap {{ overflow-x: auto; }}
  .foot {{ color:#6b7280; font-size:12px; line-height:1.5; margin-top:20px; max-width:760px; }}
  @media (max-width: 720px) {{
    body {{ padding: 16px; }}
    table {{ min-width: 640px; }}
  }}
  h1 {{ margin: 0 0 4px; font-size: 24px; }}
  .sub {{ color: #8b92a1; font-size: 14px; margin-bottom: 4px; }}
  .meta {{ color: #6b7280; font-size: 12px; margin-bottom: 20px; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
  th, td {{ text-align: left; padding: 10px 12px; border-bottom: 1px solid #23262f; vertical-align: top; }}
  th {{ font-size: 11px; text-transform: uppercase; letter-spacing: .05em; color: #8b92a1; }}
  .rank {{ color: #8b92a1; width: 28px; }}
  .title a {{ color: #6ea8fe; text-decoration: none; font-weight: 600; }}
  .title a:hover {{ text-decoration: underline; }}
  .note {{ font-size: 12px; color: #8b92a1; margin-top: 3px; max-width: 340px; }}
  .flag {{ font-size: 12px; color: #f59e0b; margin-top: 4px; max-width: 340px; font-weight: 600; }}
  .vin {{ font-size: 11px; color: #4b5563; font-family: ui-monospace, Menlo, Consolas, monospace; margin-top: 2px; }}
  .price {{ font-weight: 700; }}
  .rel {{ font-variant-numeric: tabular-nums; }}
  .dist {{ font-size: 11px; color: #6b7280; }}
  .mkt .good {{ color: #22c55e; font-weight: 600; }}
  .mkt .bad {{ color: #ef4444; font-weight: 600; }}
  .mkt .flat, .mkt .nodata {{ color: #8b92a1; }}
  .badge {{ font-size: 10px; font-weight: 700; letter-spacing: .04em; padding: 2px 5px;
    border-radius: 4px; margin-left: 6px; vertical-align: 2px; }}
  .badge.new {{ background: #1d4ed8; color: #fff; }}
  .badge.drop {{ background: #15803d; color: #fff; }}
  .badge.unrated {{ background: #4b5563; color: #fff; }}
  .score {{ position: relative; width: 90px; font-weight: 700; font-variant-numeric: tabular-nums; }}
  .score .bar {{ position:absolute; left:12px; top:6px; height:6px; width:var(--w);
    max-width: 66px; background: linear-gradient(90deg,#3b82f6,#22c55e); border-radius:4px; opacity:.75; }}
  .score span {{ position: relative; top: 12px; }}
  tr.caution .title a {{ color: #f59e0b; }}
  .empty {{ text-align:center; color:#8b92a1; padding: 40px; }}
</style></head>
<body>
  <h1>Car Finder: {len(listings)} match{'es' if len(listings)!=1 else ''}{f' · {n_new} new' if n_new else ''}</h1>
  <div class="sub">{subtitle}</div>
  <div class="meta">Source: {html.escape(source_label)} · generated {html.escape(generated_at)} · ranked best-first</div>
  <div class="wrap"><table>
    <thead><tr>
      <th></th><th>Score</th><th>Vehicle</th><th>Price</th><th>vs. market</th>
      <th>Miles</th><th>Type</th><th>Reliability</th><th>Location</th>
    </tr></thead>
    <tbody>{body_rows}</tbody>
  </table></div>
  <p class="foot">Score is 0 to 100 and weighs price against comparable
    local listings, mileage, reliability and repair cost. A warning marks a
    known problem or a price that looks too good; it is not folded into
    the score. This is a research aid: get an independent inspection and a
    title history report before you buy.</p>
</body></html>"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)


# ------------------------------------------------------------ research

def write_research_markdown(bundles, path):
    """A plain facts digest of the research pull.

    Deliberately just the facts, the interpretation belongs to whoever
    reads research.json, which carries the full detail this trims.
    """
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(_research_lines(bundles)) + "\n")


def _research_lines(bundles):
    """The research facts as markdown lines, shared by the .md and the
    .html so the two can never disagree."""
    out = ["# Deep research\n"]

    for b in bundles:
        L = b["listing"]
        title = f'{L.get("year","")} {L.get("make","")} {L.get("model","")} {L.get("trim","")}'.strip()
        out.append(f'\n## {title}\n')
        out.append(f'- VIN: `{b.get("vin","")}`')
        if L.get("price") is None and L.get("miles") is None:
            out.append('- Price and mileage: not given')
        else:
            out.append(f'- Price: {_fmt_money(L.get("price"))} · '
                       f'{_fmt_miles(L.get("miles"))}')
        if L.get("reliability") is not None:
            out.append(f'- Reliability profile: {L["reliability"]}/10 '
                       f'reliability, {L.get("maintenance")}/10 ease of '
                       f'repair ({L.get("generation") or "this generation"})')
            if L.get("note"):
                out.append(f'  - {L["note"]}')
        elif L.get("unrated"):
            out.append('- Reliability profile: none for this model year; '
                       'judge it from the recalls and complaints below')
        if L.get("url"):
            out.append(f'- Listing: {L["url"]}')
        for warning in L.get("flags") or []:
            out.append(f'- ⚠ {warning}')

        mk = L.get("market")
        if mk:
            out.append(f'- Market: expected {_fmt_money(mk["expected"])}, '
                       f'{_fmt_money(abs(mk["delta_usd"]))} '
                       f'{"under" if mk["delta_usd"] > 0 else "over"} '
                       f'({mk["basis"]}, n={mk["sample_size"]})')

        vd = b.get("vin_decode") or {}
        if vd:
            engine = " ".join(str(x) for x in [
                _fmt_liters(vd.get("DisplacementL")),
                vd.get("EngineConfiguration"),
                vd.get("EngineCylinders") and f'{vd["EngineCylinders"]}-cyl',
                vd.get("EngineHP") and f'{vd["EngineHP"]} hp',
            ] if x)
            out.append(f'- Decoded: {vd.get("Trim") or vd.get("Series") or "n/a"} · '
                       f'{engine or "engine unknown"} · '
                       f'{vd.get("DriveType","?")} · {vd.get("TransmissionStyle","?")}')
            if vd.get("PlantCity"):
                out.append(f'- Built: {vd.get("PlantCity")}, {vd.get("PlantCountry","")}')

        dep = b.get("depreciation")
        if dep and dep.get("curve"):
            c = dep["curve"]
            out.append(f'- Local depreciation: {c["annual_depreciation_pct"]}%/yr '
                       f'({c["years_observed"]} model years, '
                       f'{c["total_comparables"]} listings)')

        t = b.get("tco")
        if t:
            bd = t["breakdown"]
            out.append(f'- **{t["years"]}-yr cost: {_fmt_money(t["total"])}** '
                       f'({_fmt_money(t["cost_per_month"])}/mo): '
                       + ", ".join(f'{k.replace("_"," ")} {_fmt_money(v)}'
                                   for k, v in bd.items()))
            out.append(f'- Projected resale after {t["years"]} yr: '
                       f'{_fmt_money(t["projected_resale"])}')
            if t.get("assumptions"):
                out.append('- What the cost estimate assumes:')
                out.extend(f'  - {a}' for a in t["assumptions"])

        rc = b.get("recalls")
        if rc and rc.get("unverified_empty"):
            out.append('- Recalls: none found, but NOT confirmed clean. '
                       'NHTSA files recalls under its own model names '
                       '(tried: ' + ", ".join(rc.get("nhtsa_names_tried", [])[:6])
                       + '). Check the VIN at nhtsa.gov/recalls')
        elif rc:
            under = rc.get("nhtsa_names_with_data") or []
            out.append(f'- Recalls: {rc["count"]}'
                       + (f' (filed by NHTSA under {", ".join(under)})'
                          if under else ''))
            for item in rc["items"][:5]:
                out.append(f'  - `{item["campaign"]}` {item["component"]}: {item["summary"]}')

        cp = b.get("complaints")
        if cp and cp.get("unverified_empty"):
            out.append('- NHTSA complaints: none found, but NOT confirmed '
                       'clean: NHTSA has no model under a name matching '
                       'this one for that year (tried: '
                       + ", ".join(cp.get("nhtsa_names_tried", [])[:6]) + ')')
        elif cp:
            under = cp.get("nhtsa_names_with_data") or []
            out.append(f'- NHTSA complaints: {cp["count"]} '
                       f'(crashes {cp["crashes"]}, fires {cp["fires"]}, '
                       f'injuries {cp["injuries"]})'
                       + (f', filed under {", ".join(under)}' if under else ''))
            for comp, n in list(cp["by_component"].items())[:5]:
                out.append(f'  - {comp}: {n}')

        fe = b.get("fuel_economy") or {}
        best = fe.get("best_match")
        if best:
            out.append(f'- EPA: {best["mpg_combined"]} mpg combined '
                       f'({best["mpg_city"]} city / {best["mpg_highway"]} hwy) · '
                       f'{_fmt_money(best["annual_fuel_cost_usd"])}/yr fuel')
            out.append(f'  - matched "{best.get("epa_model")}" '
                       f'({best.get("displacement_l")}L, {best.get("drive")}): '
                       f'{fe.get("matched_on")}')
        elif fe.get("note"):
            out.append(f'- EPA: {fe["note"]}')

        issues = L.get("known_issues") or []
        if issues:
            out.append('- Known issues for this generation:')
            out.extend(f'  - {i}' for i in issues)

        if b.get("errors"):
            out.append('- Data gaps: ' + "; ".join(b["errors"]))
    return out


def write_research_html(bundles, path):
    """The same facts as research.md, as a page a person can open."""
    def inline(text):
        text = html.escape(text)
        text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
        text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
        return re.sub(r"(https?://[^\s<]+)", r'<a href="\1">\1</a>', text)

    body, depth = [], 0
    for line in _research_lines(bundles)[1:]:
        want = 2 if line.startswith("  - ") else 1 if line.startswith("- ") else 0
        while depth < want:
            body.append("<ul>")
            depth += 1
        while depth > want:
            body.append("</ul>")
            depth -= 1
        if want:
            body.append(f"<li>{inline(line.strip()[2:])}</li>")
        elif line.strip().startswith("## "):
            body.append(f"<h2>{inline(line.strip()[3:])}</h2>")
    body.append("</ul>" * depth)

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Car Finder research</title>
<style>
  :root {{ color-scheme: light dark; }}
  body {{ font-family: -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
    margin: 0 auto; padding: 24px 16px; max-width: 860px; line-height: 1.5;
    font-size: 15px; }}
  h1 {{ font-size: 24px; margin: 0 0 4px; }}
  h2 {{ font-size: 19px; margin: 28px 0 8px; padding-top: 16px;
    border-top: 1px solid #8884; }}
  ul {{ padding-left: 20px; margin: 4px 0; }}
  li {{ margin: 3px 0; }}
  ul ul {{ font-size: 14px; opacity: .85; }}
  code {{ font-family: ui-monospace, Menlo, Consolas, monospace; font-size: 13px; }}
  .foot {{ font-size: 12px; opacity: .7; margin-top: 28px; }}
</style></head><body>
<h1>Car Finder research: {len(bundles)} car{'s' if len(bundles) != 1 else ''}</h1>
{chr(10).join(body)}
<p class="foot">Facts from NHTSA and the EPA, plus a reliability profile
  where one exists. Recalls and complaints are for the model year, not
  this exact car. This is a research aid: get an independent inspection
  and a title history report before you buy.</p>
</body></html>
""")
