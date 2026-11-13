"""Regenerate the demo data for --sample: data/sample_listings.json and
data/sample_comparables.json.

The demo has to be internally consistent, because it is the first thing
a new user sees. Both files therefore come from one set of price curves:
every model gets an age curve and trim multipliers, the comparables are
drawn from that curve with a little noise, and each demo listing is
priced a chosen amount above or below what the curve says its year, trim
and mileage should cost. That is how the demo shows a real mix: a good
deal, an overpriced car, cars at market, one that is suspiciously cheap
and has sat for months, one with a known-problem flag, one with no
reliability profile, and one outside the budget.

Listings and dealers are invented. VINs are placeholders, so the demo
cannot be mistaken for real inventory.

Deterministic: same seed, same output. Run it from anywhere:

    python data/generate_sample_comparables.py
"""
import json
import os
import random

CURRENT_YEAR = 2026
FIRST_YEAR, LAST_YEAR = 2019, 2025
MILEAGE_COEF = 0.055      # $/mile off the age curve
NORM_MILES_PER_YEAR = 12000
PRICE_NOISE = 0.02
PER_TRIM_PER_YEAR = 2     # comparables per trim per model year
EXTRA_SAME_TRIM = 3       # more for each demo listing's own year and trim
random.seed(20261113)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# make, model -> body, drivetrain, price of a new one, annual retention,
# and trims as (name, multiplier).
MODELS = {
    ("Toyota", "Camry"): ("Sedan", "AWD", 34000, 0.915, [
        ("LE AWD", 0.94), ("SE AWD", 0.98), ("XLE AWD", 1.04),
        ("XSE AWD", 1.08)]),
    ("Subaru", "Legacy"): ("Sedan", "AWD", 33500, 0.900, [
        ("Base", 0.93), ("Premium", 0.98), ("Sport", 1.03),
        ("Limited", 1.08)]),
    ("Mazda", "Mazda3"): ("Sedan", "AWD", 31500, 0.905, [
        ("Select AWD", 0.95), ("Preferred AWD", 1.00),
        ("Premium AWD", 1.06)]),
    ("Nissan", "Altima"): ("Sedan", "AWD", 32000, 0.875, [
        ("S AWD", 0.94), ("SV AWD", 0.99), ("SR AWD", 1.03),
        ("SL AWD", 1.07)]),
    ("Honda", "CR-V"): ("SUV", "AWD", 37000, 0.915, [
        ("LX AWD", 0.93), ("EX AWD", 0.99), ("EX-L AWD", 1.04),
        ("Touring AWD", 1.09)]),
    ("Ford", "F-150"): ("Pickup", "4WD", 56000, 0.905, [
        ("XL 4WD", 0.86), ("XLT 4WD", 0.97), ("Lariat 4WD", 1.12),
        ("Platinum 4WD", 1.25)]),
    ("Tesla", "Model 3"): ("Sedan", "AWD", 46000, 0.860, [
        ("Standard Range", 0.90), ("Long Range AWD", 1.03),
        ("Performance AWD", 1.15)]),
    ("Jaguar", "F-PACE"): ("SUV", "AWD", 62000, 0.830, [
        ("P250", 0.92), ("P250 S", 1.00), ("P340 S", 1.10)]),
}

# Chicago-area dealers, to match ZIP 60601 in config.example.yaml.
CITIES = [
    ("Chicago", "IL", 4), ("Oak Park", "IL", 9), ("Evanston", "IL", 13),
    ("Skokie", "IL", 14), ("Elmhurst", "IL", 17), ("Orland Park", "IL", 24),
    ("Arlington Heights", "IL", 26), ("Schaumburg", "IL", 27),
    ("Naperville", "IL", 30), ("Joliet", "IL", 38),
]

# The demo listings: make, model, year, trim, miles, condition, dollars
# over (+) or under (-) the curve, days on the lot, dealer city index.
LISTINGS = [
    ("Toyota", "Camry", 2022, "SE AWD", 31400, "certified", -1150, 18, 8),
    ("Toyota", "Camry", 2023, "XLE AWD", 24900, "used", 1650, 41, 7),
    ("Subaru", "Legacy", 2023, "Limited", 22050, "certified", 100, 12, 2),
    ("Subaru", "Legacy", 2022, "Premium", 41120, "used", -700, 33, 4),
    ("Mazda", "Mazda3", 2022, "Premium AWD", 31900, "used", 900, 27, 5),
    ("Mazda", "Mazda3", 2021, "Select AWD", 44800, "used", -450, 9, 1),
    ("Nissan", "Altima", 2022, "SR AWD", 47300, "used", -600, 52, 9),
    ("Nissan", "Altima", 2023, "SV AWD", 36800, "used", -4300, 164, 6),
    ("Honda", "CR-V", 2021, "EX AWD", 49000, "used", 300, 21, 3),
    ("Ford", "F-150", 2021, "XLT 4WD", 58200, "used", 400, 36, 8),
    ("Tesla", "Model 3", 2022, "Long Range AWD", 38500, "used", -1900, 22, 0),
    ("Jaguar", "F-PACE", 2020, "P250 S", 61000, "used", 200, 47, 7),
    # Over the demo budget on purpose, to show the "filtered out" line.
    ("Ford", "F-150", 2024, "Lariat 4WD", 21500, "used", 0, 15, 5),
]


def curve_price(make, model, year, trim, miles):
    """What the demo market says this year, trim and mileage costs."""
    _, _, new_price, retention, trims = MODELS[(make, model)]
    age = CURRENT_YEAR - year
    mult = dict(trims)[trim]
    return (new_price * (retention ** age) * mult
            - MILEAGE_COEF * (miles - NORM_MILES_PER_YEAR * age))


def powertrain(make):
    """Fuel and powertrain fields, in the listings feed's own words."""
    if make == "Tesla":
        return {"fuel_type": "Electric", "powertrain_type": "BEV"}
    return {"fuel_type": "Unleaded", "powertrain_type": "Combustion"}


def comparable(n, make, model, year, trim):
    body, drive, _, _, _ = MODELS[(make, model)]
    age = CURRENT_YEAR - year
    miles = max(1500, int(random.gauss(NORM_MILES_PER_YEAR * age,
                                       4000 + 1800 * age)))
    price = curve_price(make, model, year, trim, miles)
    price *= random.uniform(1 - PRICE_NOISE, 1 + PRICE_NOISE)
    city, state, dist = CITIES[n % len(CITIES)]
    return {
        "vin": f"COMP{n:05d}", "year": year, "make": make, "model": model,
        "trim": trim, "drivetrain": drive, "body_type": body,
        "price": int(round(price / 10) * 10), "miles": miles,
        "car_type": "used", "days_on_market": random.randint(3, 90),
        "dealer_city": city, "dealer_state": state, "distance": dist,
        **powertrain(make),
    }


comps = []
for (make, model), (_, _, _, _, trims) in MODELS.items():
    wanted = {(y, t) for mk, md, y, t, *_ in LISTINGS
              if (mk, md) == (make, model)}
    for year in range(FIRST_YEAR, LAST_YEAR + 1):
        for trim, _ in trims:
            count = PER_TRIM_PER_YEAR
            if (year, trim) in wanted:
                count += EXTRA_SAME_TRIM
            for _ in range(count):
                c = comparable(len(comps) + 1, make, model, year, trim)
                if c["price"] >= 5000:
                    comps.append(c)

listings = []
for i, (make, model, year, trim, miles, cond, over, dom, city_i) in \
        enumerate(LISTINGS, 1):
    body, drive, _, _, _ = MODELS[(make, model)]
    city, state, dist = CITIES[city_i]
    price = curve_price(make, model, year, trim, miles) + over
    listings.append({
        "vin": f"SAMPLE{i:04d}", "year": year, "make": make, "model": model,
        "trim": trim, "drivetrain": drive, "body_type": body,
        "price": int(round(price / 100) * 100) - 10, "miles": miles,
        "car_type": cond, "days_on_market": dom,
        "dealer_name": f"Demo Motors of {city}", "dealer_city": city,
        "dealer_state": state, "distance": dist,
        "url": f"https://example.com/listing/{i}", "photo": None,
        **powertrain(make),
    })


def dump(name, rows):
    path = os.path.join(REPO, "data", name)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("[\n" + ",\n".join(json.dumps(r) for r in rows) + "\n]\n")
    return path


print(f"wrote {len(listings)} listings to "
      f"{dump('sample_listings.json', listings)}")
print(f"wrote {len(comps)} comparables to "
      f"{dump('sample_comparables.json', comps)}\n")
for L in listings:
    print(f"  {L['vin']}  {L['year']} {L['make']} {L['model']} {L['trim']:16s}"
          f" ${L['price']:,}  {L['miles']:,} mi")
