# Contributing to Car Finder

Thanks for helping. Bug reports, fixes, and new or corrected reliability
profiles are all welcome.

By taking part you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
Contributions are accepted under the project's [MIT License](LICENSE).

## Ways to contribute

- **Report a bug** or **suggest a feature** with the
  [issue forms](../../issues/new/choose).
- **Fix or add a reliability profile.** This is the most useful kind of
  contribution; see [Reliability profiles](#reliability-profiles) below.
- **Send a pull request** for a bug fix or a small improvement. For
  anything large, open an issue first so we can agree on the approach
  before you spend time on it.

Security problems should not go in a public issue. See
[SECURITY.md](SECURITY.md).

## Getting set up

You need Python 3.10 or newer. There is nothing to install: the code
uses only the standard library.

```bash
git clone https://github.com/Zachbishop8104/car-finder.git
```

```bash
cd car-finder
```

```bash
python run.py --sample search
```

The last command runs the whole pipeline on bundled demo data with no
API key and no config.

## Running the tests

```bash
python -m unittest discover -s tests -v
```

The tests need no API key and make no network calls. They also run on
every pull request, on the oldest and newest supported Python versions.

## Making a change

1. Fork the repository and create a branch from `master`.
2. Make your change. Keep it focused: one fix or feature per pull
   request.
3. Add or update a test when you change behaviour.
4. Run the tests and `python scripts/package.py`.
5. Open a pull request and fill in the template.

`master` is protected. Changes land through pull requests, and the
checks must pass before merging.

### Ground rules for code

- **Standard library only.** Adding a dependency means every user has
  to install something. Open an issue before proposing one.
- **Never spend API quota in tests or by default.** Use `--sample` or
  `--cached-only` while developing. Any new call to the Marketcheck API
  must be counted and capped like the existing ones in
  `carfinder/http.py`.
- **User data stays in the data folder.** Config, keys, results and the
  cache live where `carfinder/paths.py` says, never next to the code.
- **Keep modules optional where they already are.** `run.py` loads the
  report, setup and research modules lazily so a minimal copy of the
  code still works. Don't add imports that break that.
- **Don't invent numbers.** When data is missing, the tool says so and
  scores what it has. A lookup that fails must not read as a clean
  result.
- **No personal data in commits.** No real ZIP codes, API keys, VINs of
  real cars, or names of real dealerships in code, comments, tests or
  demo data.

### Style

Match the code around you. Comments explain why, not what. Keep lines
under about 80 characters. There is no formatter or linter to run.

### Commit messages

Write a short summary line in the imperative ("Fix year filter for open
searches"), then a blank line and a few lines on what changed and why
if it isn't obvious.

## Reliability profiles

Profiles live one file per make in `carfinder/profiles/`. The format
and the caveats on reading the numbers are documented at the top of
`carfinder/reliability.py`.

A profile is one person's reading of public data, so it has to be
checkable:

- **Base it on NHTSA data.** Recall campaign numbers and complaint
  counts must come from NHTSA's recall and complaint records for that
  model year, not from memory or a forum post. `python run.py research
  <VIN>` pulls them for you.
- **Say where a number comes from** in the profile text: the model year
  and, for recalls, the campaign number.
- **Remember that complaint totals scale with sales.** Compare within a
  model, or point to one component being a lopsided share of that car's
  own file.
- **Use the `risk` field sparingly.** It is for a known, expensive
  failure pattern, and it becomes a warning on every listing of that
  car.
- **In the pull request, list the model years you checked** so a
  reviewer can repeat the lookup.

Year ranges for one model must not overlap, and every profile needs all
the fields the existing ones have. The tests check both.

## Reviews and releases

The maintainer reviews pull requests as time allows; this is a
spare-time project. You may be asked for changes. Once merged, a change
ships the next time the packaged skill is rebuilt with
`python scripts/package.py`.
