"""Reliability profiles: Volvo. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

NHTSA's complaints endpoint returned nothing for most current Volvos
(XC40 before 2024, XC60 from 2018, XC90, S60 from 2019) while returning
recall lists for all of them. Those profiles are scored from recalls and
marked provisional.
"""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "volvo", "model": "xc40",
        "years": (2019, 2026),
        "generation": "first gen",
        "engine": "2.0L turbo I4 (T4, T5; mild hybrid B5 from 2023), 8-speed "
                  "automatic",
        "reliability": 6.6,
        "maintenance": 5.4,
        "annual_maintenance_usd": 850,
        "insurance_factor": 1.08,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2019, one on the 2020, three on the 2022 "
            "and four on the 2024.",
            "14 complaints on the 2024, led by electrical (5) and service "
            "brakes (4). NHTSA's complaints endpoint returned nothing for "
            "2019, 2020 and 2022: an API gap, not a clean record.",
            "The electric version (XC40 Recharge, later EX40) is a different "
            "drivetrain and is not covered by this profile.",
            "Volvo parts and dealer labour are priced close to the German "
            "brands, and independent specialists are scarcer. Software "
            "updates often need a dealer visit.",
        ],
        "note": "Provisional on the complaint side. A short, steady recall "
                "list for a small luxury SUV, and the simplest modern Volvo.",
    },
    {
        "make": "volvo", "model": "xc60",
        "years": (2018, 2026),
        "generation": "second gen (SPA)",
        "engine": "2.0L turbo I4 (T5, B5), turbo and supercharged (T6, B6) "
                  "or plug-in hybrid (T8); 8-speed automatic",
        "reliability": 6.2,
        "maintenance": 5.0,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.1,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "Five recalls on the 2018, eight on the 2019, five on the 2021 "
            "and five on the 2023.",
            "NHTSA's complaints endpoint returned nothing for any of those "
            "years: an API gap, not a clean record.",
            "Slow or frozen centre screens and brake wear are the usual "
            "owner complaints. Check the screen boots quickly and responds.",
            "Volvo parts and dealer labour are priced close to the German "
            "brands, and independent specialists are scarcer. Software "
            "updates often need a dealer visit.",
        ],
        "note": "Provisional: scored from recalls only. A steady five or so "
                "campaigns a year, which is average for the class. The plain "
                "turbo is the simplest version to own.",
    },
    {
        "make": "volvo", "model": "xc60",
        "years": (2015, 2017),
        "generation": "first gen",
        "engine": "2.0L turbo I4 (FWD), or 2.5L turbo I5 and 3.0L turbo I6 "
                  "(AWD); 6-speed or 8-speed automatic",
        "reliability": 6.6,
        "maintenance": 5.4,
        "annual_maintenance_usd": 900,
        "insurance_factor": 1.05,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "One recall on the 2015 and three on the 2016.",
            "48 complaints on the 2015 and 39 on the 2016, with engine the "
            "largest group on both (13 and 16).",
            "The 2.0L four of 2015 to 2016 can burn oil. Check the level and "
            "ask how often it needs topping up; the five-cylinder AWD cars "
            "are the safer choice.",
            "Volvo parts and dealer labour are priced close to the German "
            "brands, and independent specialists are scarcer. Software "
            "updates often need a dealer visit.",
        ],
        "note": "An old, sturdy design with a short recall list. Engine "
                "choice matters more than year.",
    },
    {
        "make": "volvo", "model": "xc90",
        "years": (2020, 2026),
        "generation": "second gen (SPA), facelift",
        "engine": "2.0L turbo I4 (T5, B5), turbo and supercharged (T6, B6) "
                  "or plug-in hybrid (T8); 8-speed automatic",
        "reliability": 6.2,
        "maintenance": 4.6,
        "annual_maintenance_usd": 1000,
        "insurance_factor": 1.15,
        "tire_set_usd": 1150,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2021 and six on the 2023.",
            "NHTSA's complaints endpoint returned nothing for these years: "
            "an API gap, not a clean record.",
            "Air suspension, where fitted, and the plug-in hybrid's rear "
            "motor and battery are the costly items. The plain turbo on "
            "steel springs is the cheapest to keep.",
            "Volvo parts and dealer labour are priced close to the German "
            "brands, and independent specialists are scarcer. Software "
            "updates often need a dealer visit.",
        ],
        "note": "Provisional: scored from recalls only. Later cars are "
                "better sorted than the 2016 to 2017 launch years.",
    },
    {
        "make": "volvo", "model": "xc90",
        "years": (2016, 2019),
        "generation": "second gen (SPA)",
        "engine": "2.0L turbo I4 (T5), turbo and supercharged (T6) or "
                  "plug-in hybrid (T8); 8-speed automatic",
        "reliability": 5.5,
        "maintenance": 4.6,
        "annual_maintenance_usd": 1050,
        "insurance_factor": 1.15,
        "tire_set_usd": 1150,
        "risk": None,
        "known_issues": [
            "Eight recalls on the 2016, the first year, seven on the 2017 "
            "and six on the 2019.",
            "NHTSA's complaints endpoint returned nothing for these years: "
            "an API gap, not a clean record.",
            "Launch-year cars are known for touchscreen and software faults "
            "and, on the T6, oil consumption. Check the oil level and that "
            "the screen has had its updates.",
            "Volvo parts and dealer labour are priced close to the German "
            "brands, and independent specialists are scarcer. Software "
            "updates often need a dealer visit.",
        ],
        "note": "Provisional: scored from recalls only. A lovely cabin with "
                "a first-year design's teething troubles. A 2019 or later is "
                "the better buy. There was no 2015 model year.",
    },
    {
        "make": "volvo", "model": "s60",
        "years": (2019, 2025),
        "generation": "third gen (SPA)",
        "engine": "2.0L turbo I4 (T5, B5), turbo and supercharged (T6) or "
                  "plug-in hybrid (T8); 8-speed automatic",
        "reliability": 6.4,
        "maintenance": 5.0,
        "annual_maintenance_usd": 900,
        "insurance_factor": 1.1,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2019, three on the 2021 and six on the "
            "2023.",
            "NHTSA's complaints endpoint returned nothing for any of those "
            "years: an API gap, not a clean record.",
            "It shares engines and electronics with the XC60, so the same "
            "screen and software complaints apply.",
            "Volvo parts and dealer labour are priced close to the German "
            "brands, and independent specialists are scarcer. Software "
            "updates often need a dealer visit.",
        ],
        "note": "Provisional: scored from recalls only. Discontinued after "
                "2025, and it sold in small numbers, so used examples are "
                "thin.",
    },
    {
        "make": "volvo", "model": "s60",
        "years": (2015, 2018),
        "generation": "second gen",
        "engine": "2.0L turbo I4 (FWD), or 2.5L turbo I5 and 3.0L turbo I6 "
                  "(AWD); 6-speed or 8-speed automatic",
        "reliability": 6.5,
        "maintenance": 5.4,
        "annual_maintenance_usd": 880,
        "insurance_factor": 1.05,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2015 and five on the 2017.",
            "60 complaints on the 2015, led by engine (24); 17 on the 2017.",
            "The 2.0L four of 2015 to 2016 can burn oil. Check the level and "
            "ask how often it needs topping up.",
            "Volvo parts and dealer labour are priced close to the German "
            "brands, and independent specialists are scarcer. Software "
            "updates often need a dealer visit.",
        ],
        "note": "A comfortable, safe old sedan. Engine complaints lead the "
                "2015 file, so prefer a 2017 or 2018.",
    },
]
