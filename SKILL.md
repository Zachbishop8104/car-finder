---
name: car-finder
description: Research any car from its VIN with no setup (recalls, owner complaints, exact engine and build, EPA mileage, reliability profile, 5-year cost of ownership), or search local dealer inventory for new and used cars and rank them against local market prices. Use when the user asks to find a car, is car shopping, wants to compare specific vehicles, asks whether a car is a good deal or reliable, or wants to know what a car will cost to own.
---

# Car Finder

## What this skill needs and touches

Tell the user this before the first live run; none of it is hidden.

- **Python 3.10+, and nothing else to install.** The code uses only the
  standard library. (If PyYAML happens to be installed it is used to
  read `config.yaml`; otherwise a built-in reader does it.)
- **Network, read-only GETs to three services:** `api.marketcheck.com`
  (dealer listings), `api.nhtsa.gov` / `vpic.nhtsa.dot.gov` (VIN decode,
  recalls, complaints) and `www.fueleconomy.gov` (EPA mileage). Nothing
  else is contacted and nothing is uploaded beyond the search parameters
  (ZIP, radius, price and mileage range, make/model) and VINs being
  looked up.
- **One optional credential:** `MARKETCHECK_API_KEY`, the user's own
  free key, read from the environment or from `.env` in the data
  folder. It is sent only to `api.marketcheck.com`, and only searching
  dealer inventory needs it. Researching a car by VIN and `--sample`
  need no key and make no Marketcheck calls. The only other environment
  variable read is the
  optional `CAR_FINDER_HOME`, which relocates the data folder.
- **Files:** the tool keeps the user's own data in one folder,
  `~/.car-finder/` by default: `config.yaml`, `.env`, `output/` and
  `.cache/`. The cache and call counter there are what protect the API
  quota, so it has to persist between sessions. Nothing else on the
  machine is read or modified.

`python run.py where` prints the data folder, whether a config exists
there and whether a key is set (never the key itself). Run it first.
File names like `output/latest.json` below are inside the data folder;
every command also prints the full paths it wrote.

## Running it

**If these files are a folder on disk** (an installed skill or a
checkout), run `run.py` in place by its full path. The working directory
doesn't matter.

**If the skill was loaded through a marketplace connection and there is
no folder**, write the files you need, unchanged, into one fresh
temporary directory, keeping their relative paths, and run `run.py` from
there. Reuse that one copy for the whole conversation instead of
rewriting it per command, and delete it when the car work is done. Never
copy the code into the user's project, a skill folder or the data
folder.

You don't need every file. Fetch only these:

| for | files |
|---|---|
| every command | `run.py`, and in `carfinder/`: `__init__.py`, `paths.py`, `config.py`, `http.py`, `sources.py`, `market.py`, `scoring.py`, `reliability.py`, `store.py` |
| reliability scores | `carfinder/profiles/<make>.py` for each make being searched or researched (`toyota.py`, `ford.py`, `mercedes_benz.py`, `land_rover.py`; lowercase, non-letters become `_`). No file for a make just means those cars are unrated |
| `research`, including a pasted VIN | `carfinder/research.py`, `carfinder/tco.py`, plus the profile file for the car's make (the listing or the user will have named it) |
| an HTML/CSV report for the user to open | `carfinder/report.py` (without it only the JSON is written) |
| `--sample` demo | `data/sample_listings.json`, `data/sample_comparables.json`, `config.example.yaml` |

`carfinder/setup.py` is an interactive wizard for a human at a terminal;
you never need it.

## Zero setup: research one car by its VIN

If the user already has a car in mind (a dealer listing, a car on a
lot, a private sale), this is the whole job and it needs no API key, no
config and no questions beyond the VIN:

```bash
python run.py research 1HGCM82633A004352 --price 24990 --miles 38000
```

It decodes the VIN with NHTSA to get the year, make, model, engine and
build, then pulls recalls, owner complaints and EPA mileage, attaches
the reliability profile for that generation if there is one, and
estimates 5-year cost of ownership. `--price` and `--miles` are the
asking price and odometer reading from the listing. Without `--price`
the cost estimate is skipped and the output says so; ask the user for
the price rather than guessing one. Several VINs can be given at once
(without `--price`/`--miles`) to compare recall and complaint records.

Read `output/research.json` and write the analysis as described under
Phase 3 below. Two things differ from a researched shortlist: there is
no market price comparison, because nothing was searched, and
depreciation uses the generic rate unless a Marketcheck key and a saved
search exist. Both are stated in the output; say them to the user.

Use the search loop below when the user wants to find cars rather than
check one.

## First run

Searching dealer inventory needs a Marketcheck key and a search to run.
Run `python run.py where`. If it says the config isn't created yet, this
person hasn't been set up. For a one-off search you can pass the
criteria as options and skip the config file entirely:

```bash
python run.py search --zip 60601 --target Toyota:Camry --target Honda:CR-V --price-max 30000 --miles-max 80000
```

(`--radius`, `--price-min`, `--body-type`, `--drivetrain`,
`--year-min`, `--year-max`, `--powertrain` and `--condition
used,certified,new` are also accepted; `python run.py search --help`
lists them. The same options override a saved config for one run.)

`--powertrain` takes `gas`, `hybrid`, `plug-in hybrid`, `electric` or
`diesel`, or several separated by commas. Leave out `--target` to search
every make that fits the filters, which is how "SUVs under $25k near
me" is run:

```bash
python run.py search --zip 60601 --body-type SUV --price-max 25000 --year-min 2019 --powertrain hybrid
```

For someone who will search more than once, ask them the
questions conversationally and
write `config.yaml` into the data folder yourself, using
`config.example.yaml` as the template: ZIP, search radius, price range,
max mileage, body type, drivetrain, and which models to track. Any make
and model works: sedans, SUVs, trucks, EVs, new or used. Leave
`body_type` or `drivetrain` as `""` for no preference, and give a target
its own `body_type` when the shortlist mixes kinds (a pickup and a
sedan, say).

Write the ZIP in quotes (`zip: "02134"`). It is text, and a ZIP that
starts with 0 must not be read as a number.

For the API key, point them at https://developers.marketcheck.com/ and
have them put `MARKETCHECK_API_KEY=...` in the `.env` file in the data
folder themselves, rather than pasting it into the chat. Until they do,
research individual cars by VIN, or use `--sample` to show the search.

If the code is a folder on disk they can instead run `python run.py
setup` in their own terminal; it asks the same questions and writes both
files.

Never put their ZIP, budget or API key anywhere but `config.yaml` and
`.env` in the data folder.

## The loop

A three-phase loop. Each phase is a shell command that writes JSON; you
read the JSON and do the talking. **The Python fetches facts, you
interpret them.** Never substitute recalled knowledge for a number the
tool can produce, and never present a number the tool didn't produce as
if it did.

`--sample` uses bundled data, needs no API key and no config, and is the
right way to demo the loop or test a change.

## Phase 1: Search

```bash
python run.py search
```

Reads `config.yaml`, pulls Marketcheck inventory, prices every car
against local comparables, ranks, and writes:

| file | what it's for |
|---|---|
| `output/latest.json` | **read this**: every ranked listing, plus `by_vin` |
| `output/latest.html` | for the user to open |
| `output/results_*.html`, `.csv` | dated archive; only the newest 10 are kept |

### Give the user their report

The report is in the data folder (`~/.car-finder/output` by default),
which most people will never find on their own. After every search and
every research run:

- Give the user the full path of the HTML report. The command prints it
  (`Report:`); `python run.py where` shows the folder.
- Offer to open it, and do it if they say yes: re-run with `--open`
  (free after a search, since the results are cached), or open the file
  yourself if you can. `output.open_report_when_done: true` in the
  config makes that the default.

Search writes `latest.html`; research writes `research.html`.

If the user's criteria differ from `config.yaml`, edit the config first
and say what you changed. Common edits: `price_max`, `miles_max`,
`radius_miles`, `year_min` / `year_max`, `powertrain`, and the `targets`
list. For a one-off change, pass the option on the command line instead
of editing the file.

### When the search names no model

A target with a make but no model, or a search with no targets at all,
can turn up many models. Pricing a model against its market costs one
API call each, so the tool prices only the few with the most listings
(`api.price_models`, default 3), lists the rest as "not priced", and
prints how many models it found and what pricing them would cost.

Do not choose a number for the user. When that message appears, tell
them how many models were found, that pricing each one costs one call,
and how many calls they have left (`python run.py usage`), then ask how
many they want priced. Re-run with `--price-models N`; the listings are
cached, so only the extra comparables are paid for. An unpriced car
still has its mileage and reliability scored, and shows
`missing_components: ["value"]`; say that its rank does not reflect its
price.

Then present the top matches. For each: year/make/model/trim, price,
mileage, **the VIN**, market delta, and the dealer link. Lead with the
market delta and the score, not the raw price. The whole point is that
the cheapest car is usually the worst one.

Flag anything with `unrated: true` or a non-empty `missing_components`:
its score is computed from partial data and ranks lower-confidence than
it looks.

**Always surface `flags`.** Two kinds show up here and both matter:

- A known failure pattern for that generation (`risk`), e.g. a CVT that
  fails past 90k miles. Ranking deliberately does *not* penalize these,
  so the flag is the only signal. Never omit it.
- A car well under market that has also sat on the lot for months, the
  classic shape of a branded title, flood damage, or a repaired wreck.
  It looks cheap precisely because everyone who inspected it walked away.

Say both plainly and never let a high score bury them. Ranking is led by
price and mileage on purpose: it answers "is this a fair deal on a car
you said you wanted", not "is this car a good idea". The second question
is what phase 3 answers.

End by asking which ones to look at more closely.

## Phase 2: Shortlist

```bash
python run.py shortlist VIN1 VIN2 VIN3
```

Pins the user's picks to `output/shortlist.json`. VINs must come from the
last search; anything else is reported as missing and skipped.

If the user picks by position ("the first two") or by description ("the
Camry and the Legacy"), resolve that to VINs yourself from
`latest.json`. Don't make them type a VIN.

## Phase 3: Research

```bash
python run.py research          # the whole shortlist
python run.py research VIN      # one car from the last search
python run.py research VIN --price 24990 --miles 38000   # any VIN at all
```

Pulls, per car: NHTSA vPIC VIN decode, NHTSA recalls, NHTSA complaints,
EPA mileage, a local depreciation curve, and a 5-year TCO. Writes
`output/research.json` (**read this**), `output/research.md` and
`output/research.html` (for the user to open; add `--open`). Those three
hold the cars from this run only. Every car is also kept on its own as
`output/research/<VIN>.json`, so a car researched earlier is still there
to read or compare; the newest 50 are kept.

### How to read the research JSON

**`vin_decode`**: the exact car. Engine model, displacement, HP,
transmission, assembly plant, decoded trim. This is what makes the
analysis specific: reason about "the A25A-FKS 2.5L", not "a Camry". If
`decode_clean` is false the VIN failed its check digit. Say so; it may
be a typo in the listing.

**`recalls`**: open safety recalls for that year/make/model. An open
recall is **not** a reason to reject a car; the fix is free at any
dealer. It *is* something to confirm was done before purchase. Say which
ones and what they affect.

**An empty result is not a clean record.** NHTSA files a car under its
own model names, which are often not the dealer's: every 2021+ Sienna
is "SIENNA HYBRID", a Mercedes GLS is "GLS 450", a BMW 4 Series is
"430I", an F-150's complaints are split by cab. The tool looks up
NHTSA's names for the make and year and tries the likely spellings;
`nhtsa_names_tried` and `nhtsa_names_with_data` on `recalls` and
`complaints` show what it asked for and what answered. When
`unverified_empty` is true, nothing came back and the tool could not
confirm that is because there is nothing. Never tell the user such a car
has "no recalls" or "no complaints". Say that none were found under the
names tried, name them, and tell the user to check the VIN at
nhtsa.gov/recalls. For recalls, zero is always reported this way,
because the recall file offers no list of its model names to check
against.

The counts are for the model year across the names that matched, so a
figure can include a sibling version (a hybrid and its gas twin, every
cab style of a truck). Say what it covers when it matters.

**`complaints`**: owner filings. Read `by_component`, not `count`.
Raw counts scale with how many of that model were sold, so a Camry will
always out-complain a Legacy and that means nothing on its own. What
matters is the *shape*: a cluster in POWER TRAIN on a CVT car is a real
signal; a cluster in AIR BAGS usually traces back to a recall already in
the `recalls` list. Cross-reference the two before drawing a conclusion.

**`fuel_economy`**: check `best_match.epa_model` and `matched_on`. The
EPA splits one model into separate entries per drivetrain and trim
("Camry AWD LE/SE", "F150 Pickup 2WD"), so the matcher picks by driven
wheels and engine displacement. `matched_on` says which it used. If it
reports falling back to two-wheel-drive figures for an all-wheel-drive
car, the mpg is optimistic. Say so. For an electric car `mpg_combined`
is MPGe; quote `kwh_per_100mi` instead and never compare MPGe to a
petrol car's mpg as if they were the same unit.

**`depreciation.curve`**: fitted from local listings across model
years. `annual_depreciation_pct` is observed, not assumed. If the curve
is null there weren't enough comparables and the projection fell back to
a generic rate; say so rather than quoting it as measured.

**`tco`**: the 5-year picture. Always surface `assumptions`; the
insurance figure is a configured baseline, not a quote, and the user
should replace it with a real one. Electric cars are costed from the
EPA's annual energy estimate rather than the configured fuel price, and
plug-in hybrids as if they never charge. Both are stated in
`assumptions`, so read them out. Compare cars on `total` and
`cost_per_month`, and point out when a cheaper sticker loses to a more
expensive car on 5-year cost. That's usually the most useful thing in
the whole report.

**`errors`**: sources that failed. State the gaps plainly instead of
filling them in from memory.

### Writing the analysis

Give the user a recommendation, not a data dump; they can read
`research.md` for the raw facts. Structure it around the decision:
what each car is good at, what would make you walk away, and what to
verify in person or in the service records. Concrete beats hedged.

The reliability scores and known-issue notes in the profiles are the
author's reading of public NHTSA data, not a professional inspection.
Always recommend an independent pre-purchase inspection and a title
history check before money changes hands; nothing here checks either.

Where a known issue exists for that generation (`known_issues` on the
listing), turn it into an action: "confirm the CVT fluid was serviced"
beats "CVTs can be unreliable."

## Maintaining the data

`carfinder/profiles/<make>.py` holds the per-generation profiles:
reliability, repair ease, annual maintenance cost, tire cost, insurance
factor, known issues. When the code is a folder on disk and research
turns up a model with no profile, offer to add one, based on what the
research actually found. When the code is only a temporary copy there is
nowhere to keep a new profile, so don't offer.

`config.yaml`'s `ownership` block drives the TCO. `baseline_insurance_annual`
is the input most worth making real.

## Notes

- **The API budget is the scarce resource.** The free tier is 500 calls
  total. A search costs one call per target plus one per model priced
  (comparables are cached a week), so about 6 calls with the example
  config.
  `python run.py usage` shows what's left; the tool hard-stops rather
  than spending past `api.call_limit`.
- **Don't re-run `search` to "refresh" unless the user asks.** Results
  are cached and a repeat costs real quota. If you only need the data,
  read `output/latest.json`; it's already there.
- When changing scoring or report code, test with `--cached-only`, which
  cannot spend a call.
- `python run.py clear-cache` forces fresh data and makes the next search
  pay full price. Only suggest it when data staleness is the problem.
  Expired cache entries are removed on their own, once a day; nothing
  needs clearing to save space.
- Don't scrape Cars.com, Autotrader, or CarGurus. They block it and it
  violates their terms; the Marketcheck API is the supported path to the
  same inventory.
- NHTSA and FuelEconomy.gov need no key and have no meaningful limits.
