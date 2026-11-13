# Car Finder

An agent skill and standalone CLI that finds cars in local dealer
inventory, ranks them against what they should cost in your market, and
researches the ones you shortlist: VIN-decoded build, recalls, owner
complaints, local depreciation and 5-year cost of ownership.

It works for any make, model, body type or drivetrain, new or used:
sedans, SUVs, trucks, hybrids and EVs.

## Table of contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick start](#quick-start)
- [Usage](#usage)
- [Configuration](#configuration)
- [Where your data lives](#where-your-data-lives)
- [How ranking works](#how-ranking-works)
- [API budget](#api-budget)
- [Reliability profiles](#reliability-profiles)
- [Data sources and privacy](#data-sources-and-privacy)
- [Limitations](#limitations)
- [Project structure](#project-structure)
- [Packaging](#packaging)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Research any car from its VIN, with no setup.** Paste a VIN from
  any listing and get its recalls, complaints, exact engine and build,
  EPA mileage and 5-year cost. No API key, no config, nothing to
  install.
- **Market-relative ranking.** Each car is priced against local
  comparables of the same year and trim, so "cheap" means below market
  for its spec, not the roughest car in the price band.
- **Flags that can't be outvoted.** Known failure patterns, cars that
  have sat for months, and suspiciously deep discounts are flagged rather
  than folded into a score a low price could cancel out.
- **Research on the exact car.** NHTSA VIN decode (engine, transmission,
  plant), open recalls, complaints grouped by component, and EPA mileage
  matched to the car's drivetrain and engine.
- **5-year cost of ownership.** Depreciation fitted from listings in
  your own market, plus fuel or electricity, insurance, maintenance,
  tires and registration, with every assumption listed.
- **Quota-aware.** Responses are cached, metered calls are counted, and
  the tool stops rather than spend past your plan limit.
- **Demo mode.** `--sample` runs the whole pipeline on bundled data with
  no key and no network calls to the listings API.

## Requirements

- Python 3.10 or newer. Nothing else to install: the code uses only the
  standard library. (PyYAML is used to read `config.yaml` if it happens
  to be installed; a built-in reader does it otherwise.)
- A free [Marketcheck API key](https://developers.marketcheck.com/),
  only for searching dealer inventory. Researching a car by VIN and
  `--sample` do not need it.

## Installation

### As a CLI

```bash
git clone https://github.com/Zachbishop8104/car-finder.git
```

```bash
cd car-finder
```

### As an agent skill

Copy or link the folder into your agent's skills directory. `SKILL.md`
at the root is the skill definition. For Claude Code:

```bash
cp -r car-finder ~/.claude/skills/car-finder
```

On Windows:

```bash
cmd /c mklink /J "%USERPROFILE%\.claude\skills\car-finder" "%CD%"
```

Some skill marketplaces deliver skills through a connection instead of
installing a folder. That works too: `SKILL.md` tells the agent which
files to run from a temporary copy, and your setup and results persist
in the data folder.

Then ask the agent to find you a car. It runs the three phases below,
resolves your picks to VINs, and writes its analysis from the research
data rather than from memory.

## Quick start

Research a car you already found. No key, no config, no setup: paste
the VIN from the listing, with its asking price and mileage:

```bash
python run.py research 1HGCM82633A004352 --price 24990 --miles 38000
```

See what a search looks like, on demo data:

```bash
python run.py --sample search --open
```

Search real dealer inventory. This needs a free Marketcheck key in
`MARKETCHECK_API_KEY`. Give the search on the command line:

```bash
python run.py search --zip 60601 --target Toyota:Camry --price-max 30000
```

or answer a few questions once (location, budget, body type, models to
track, API key) and reuse them:

```bash
python run.py setup
```

```bash
python run.py search
```

## Usage

The workflow is three phases: search wide, shortlist by hand, research
the survivors in depth.

| Command | What it does |
|---|---|
| `python run.py setup` | Interactive wizard; writes `config.yaml` and `.env` |
| `python run.py search` | Pull inventory, price against comparables, rank |
| `python run.py shortlist VIN [VIN ...]` | Pin cars from the last search |
| `python run.py shortlist` | Show the current shortlist |
| `python run.py research [VIN ...]` | Deep-dive the shortlist, or specific VINs from the last search |
| `python run.py research VIN --price N --miles N` | Research any 17-character VIN; no key or config needed |
| `python run.py search --zip Z --target MAKE:MODEL ...` | Search without a config file (`search --help` lists the options) |
| `python run.py search --zip Z --body-type SUV --price-max 25000` | Search every make: no `--target` means any make that fits |
| `python run.py search --year-min 2019 --powertrain hybrid` | Narrow a saved search for one run by model year or powertrain |
| `python run.py usage` | Show the API call budget (`--reset`, `--set N`) |
| `python run.py where` | Show where config, results and cache are kept |
| `python run.py clear-cache` | Drop cached responses (the next search pays full price) |

| Flag | Effect |
|---|---|
| `--sample` | Use bundled demo data; no API key needed |
| `--cached-only` | Never spend an API call; serve cached responses only |
| `--config PATH` | Use a different config file (relative paths are tried in the working directory, then the data folder) |
| `--open` | Open the HTML report when the search finishes |

Outputs are written to `output/` in the [data folder](#where-your-data-lives):

| File | Contents |
|---|---|
| `latest.html` | Ranked report to read |
| `latest.json` | The same data, structured, with a `by_vin` index |
| `results_*.html` / `results_*.csv` | Dated archive, one pair per search |
| `shortlist.json` | Your pinned cars |
| `research.html` | Research report to read (`research --open` opens it) |
| `research.md` / `research.json` | The same research facts, as text and structured |
| `research/<VIN>.json` | Each car ever researched, kept on its own |

Nothing piles up:

| What | Kept |
|---|---|
| `latest.*`, `research.*`, `shortlist.json` | Always; each run replaces the last |
| Dated `results_*` pairs | The newest 10 (`output.keep_reports`) |
| `research/<VIN>.json` | The newest 50 cars (`output.keep_research`) |
| Cached API responses | Until they expire: 6 hours for listings, a week for comparables, 30 days for recalls, complaints and mileage. Expired ones are deleted once a day |

Only files the tool wrote, matching those exact names, are ever
deleted, and only inside the data folder's `output/` and `.cache/`.

## Configuration

`python run.py setup` writes `config.yaml`; re-run it any time and your
current answers become the defaults. You can also copy
`config.example.yaml` and edit it by hand.

| Section | Keys | Notes |
|---|---|---|
| `search` | `zip`, `radius_miles`, `price_min`, `price_max`, `miles_min`, `miles_max`, `year_min`, `year_max`, `body_type`, `drivetrain`, `powertrain`, `car_types` | Only `zip` is required. `body_type`, `drivetrain` and `powertrain` may be `""` for no preference. `powertrain` is `gas`, `hybrid`, `plug-in hybrid`, `electric` or `diesel`, or several separated by commas. `car_types` is any of `used`, `certified`, `new`. |
| `targets` | list of optional `make`, optional `model`, optional `body_type`, optional `powertrain` | One API call per entry per search. Leave out `make`, or write `targets: []`, to search every make that fits the filters. A per-target `body_type` or `powertrain` overrides the global one. |
| `scoring` | `weight_value`, `weight_mileage`, `weight_reliability`, `weight_maintenance` | Should sum to about 1.0. |
| `ownership` | `years`, `annual_miles`, `fuel_price_per_gallon`, `baseline_insurance_annual`, `tire_replacement_interval_miles`, `annual_registration_usd`, `maintenance_escalation_per_10k` | Replace the insurance baseline with a real quote; it matters more than any other input. |
| `api` | `call_limit`, `warn_at_pct`, `max_requests_per_second`, `price_models` | Your Marketcheck plan's limits. `price_models` is how many models to price when a search names none (see [API budget](#api-budget)). |
| `output` | `max_results`, `open_report_when_done`, `keep_reports`, `keep_research` | `open_report_when_done` opens the HTML report after a search or research run. The two `keep_` values set how many dated reports and researched cars are kept. |

The API key lives in `.env` in the data folder as `MARKETCHECK_API_KEY`
(see `.env.example`), or in the environment under the same name.

## Where your data lives

The code and your data are kept apart, so the code can be updated,
moved, or run from a temporary copy without losing your setup, your
results, or the cache that protects your API quota.

Your data folder holds `config.yaml`, `.env`, `output/` and `.cache/`.
It is, in order:

1. `$CAR_FINDER_HOME`, if that environment variable is set.
2. The code's own folder, if a `config.yaml` sits next to `run.py`. Use
   this for a self-contained checkout: copy `config.example.yaml` to
   `config.yaml` there and everything stays in one place. Those files
   are gitignored.
3. `~/.car-finder/` otherwise. This is what `setup` uses on a fresh
   install.

```bash
python run.py where
```

prints which one is in use and what is in it.

## How ranking works

Each car scores 0-100 from four components:

| Component | Default weight | What it measures |
|---|---|---|
| value | 45% | Price against what this year and trim should cost locally |
| mileage | 30% | Fewer miles is better, within your band |
| reliability | 15% | Dependability of that generation and engine |
| maintenance | 10% | How cheap and easy it is to fix |

Price and mileage lead because they are known for every car, so a model
with a reliability profile and one without compete on the same basis.

- **New cars** are priced against their own MSRP rather than a pool of
  used comparables.
- **Missing data is never invented.** If a car has no reliability
  profile or too few comparables, that weight is redistributed, the
  score is pulled toward neutral, and the car is marked as partially
  scored.
- **Deep discounts stop earning credit.** Past roughly 15% under market
  the value score stops rising, and past 25% it falls: that is what a
  branded title or a repaired wreck looks like in the price.

## API budget

The Marketcheck free tier is the scarce resource, so the tool tracks it.

- A search costs one call per target, plus one per model priced
  against its market. Comparables are cached for a week.
- A target that names a make and model is always priced. A search that
  names no model (a whole make, or any make) can find many models, so
  only the `api.price_models` with the most listings are priced
  (default 3). The rest are listed unpriced, and the search prints how
  many it found and what pricing them would cost. `--price-models N`
  sets the number for one run.
- Everything is cached in `.cache/` in the data folder; repeating a
  search inside the cache window costs nothing.
- `--cached-only` guarantees no call is spent, which is the right mode
  while changing scoring or report code.
- The tool stops at `api.call_limit` rather than spending past it.
- NHTSA and FuelEconomy.gov are free and never counted.

## Reliability profiles

Search, market pricing, depreciation, recalls, complaints, EPA mileage
and cost of ownership work for any car. None of that needs a profile.

A profile adds a dependability and repair-ease score to the ranking and
a hand-written list of that generation's known problems. The repo ships
589 profiles covering 304 models from 35 makes, mostly model years
2015 to 2026: cars, SUVs, trucks, minivans, hybrids and EVs. A car
without one is marked `unrated` and scored on the components that
exist.

The recall and complaint counts quoted in profiles were fetched from
NHTSA and name the model year they are for; they drift as new recalls
are filed, and the research phase always pulls the current figures. The
scores, and the notes on what tends to fail, are a judgement drawn from
those figures and from each generation's widely reported problems.
Profiles that rest on thin data say "provisional".

Profiles live one file per make in `carfinder/profiles/`, keyed by
model and year range, and are loaded only for the makes being searched.
They are a reading of public NHTSA data, not a professional inspection,
and the depreciation figures quoted in a few of them come from a single
market. Edit
them, and add your own: the research phase gives you the material. Copy
an existing entry and fill it in.

## Data sources and privacy

| Source | Used for | Key |
|---|---|---|
| [Marketcheck](https://www.marketcheck.com/apis/) | Dealer listings and comparables | Your own, free tier available |
| [NHTSA vPIC](https://vpic.nhtsa.dot.gov/api/) | VIN decode | None |
| [NHTSA](https://www.nhtsa.gov/nhtsa-datasets-and-apis) | Recalls and complaints | None |
| [FuelEconomy.gov](https://www.fueleconomy.gov/feg/ws/) | EPA mileage and energy cost | None |

- Only read-only GET requests to those hosts. Nothing else is contacted.
- What leaves your machine: your search parameters (ZIP, radius, price
  and mileage range, make, model) and the VINs being looked up.
- Your API key is read from the environment or `.env` and sent only to
  Marketcheck.
- All files are written inside the data folder: `config.yaml`, `.env`,
  `output/` and `.cache/`. Nothing is written next to the code unless
  you chose that folder as your data folder.
- It does not scrape Cars.com, Autotrader or CarGurus. That violates
  their terms and breaks constantly; a listings API is the supported
  route to the same inventory.

## Limitations

- US market only: US ZIP codes, NHTSA and EPA data.
- It does not check title history, accident history or service records.
  The Carfax flags in the listing feed are carried through as raw data
  and are not a title check.
- Insurance is your configured baseline times a per-model factor, not a
  quote.
- Electric cars are costed from the EPA's national-average annual energy
  estimate, and plug-in hybrids as if they never charge. Both are stated
  in the output.
- Recalls and complaints are per model year, not per VIN. Confirm open
  recalls on the specific car with the dealer or NHTSA.
- The Marketcheck free tier caps the search radius at 100 miles.

This is a research aid. Get an independent pre-purchase inspection and a
title history report before buying.

## Project structure

```
car-finder/
├── SKILL.md                # agent skill definition
├── run.py                  # CLI entry point
├── config.example.yaml     # configuration template
├── .env.example            # API key template
├── requirements.txt
├── carfinder/
│   ├── paths.py            # where code and user data live
│   ├── config.py           # loads config.yaml
│   ├── setup.py            # interactive wizard
│   ├── http.py             # GET + cache + call budget
│   ├── sources.py          # Marketcheck API and sample data
│   ├── market.py           # expected price, depreciation curve
│   ├── reliability.py      # profile loading and lookup
│   ├── profiles/           # per-generation profiles, one file per make
│   ├── scoring.py          # filtering and ranking
│   ├── research.py         # NHTSA and EPA lookups
│   ├── tco.py              # 5-year cost of ownership
│   ├── store.py            # latest / seen / shortlist JSON
│   └── report.py           # HTML, CSV and research markdown
├── data/                   # bundled demo listings and comparables
├── tests/                  # unit tests (not shipped in the package)
├── scripts/
│   └── package.py          # builds dist/car-finder.zip
└── .github/                # CI workflow, issue and pull request templates
```

## Packaging

```bash
python scripts/package.py
```

Writes `dist/car-finder.zip` with a single top-level `car-finder/`
folder, the shape skill marketplaces expect. Only git-visible files are
included, and the build refuses to run if a personal config, `.env`, a
binary or something that looks like a real API key would be shipped.

## Development

```bash
python -m unittest discover -s tests -v
```

The tests use only the standard library, need no API key and make no
network calls. They run on every pull request.

## Contributing

Issues and pull requests are welcome, especially new or corrected
reliability profiles. [CONTRIBUTING.md](CONTRIBUTING.md) covers setup,
the ground rules and how profiles are sourced. Please follow the
[Code of Conduct](CODE_OF_CONDUCT.md), and report security problems
privately as described in [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE)
