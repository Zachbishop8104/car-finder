"""Reliability profiles: Mitsubishi. The format and the caveats on
reading these numbers are in carfinder/reliability.py.

Two things apply to every used Mitsubishi. Sales are low, so small
complaint files prove little. And the 10-year/100,000-mile powertrain
warranty is for the first owner only: a second owner gets the
remainder of 5 years/60,000 miles."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        # 2022: 7 recalls, 219 complaints, 77 STRUCTURE (75 of them
        # mention the hood). 2023: 2 recalls, 50 complaints.
        "make": "mitsubishi", "model": "outlander",
        "years": (2022, 2026),
        "generation": "GN fourth gen (shared with Nissan Rogue)",
        "engine": "2.5L PR25DD I4 (Nissan), CVT; three rows",
        "reliability": 6.8,
        "maintenance": 6.8,
        "annual_maintenance_usd": 600,
        "insurance_factor": 1.0,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "Seven recalls on the 2022, the launch year; two on the "
            "2023.",
            "77 of 219 complaints on the 2022 are STRUCTURE, nearly "
            "all about the hood fluttering at highway speed. Watch "
            "the hood on a fast test drive.",
            "It uses the Nissan 2.5L, not the troubled 1.5L turbo "
            "from the Rogue. The CVT still wants fluid changes.",
            "A used buyer does not get the 10-year powertrain "
            "warranty. Check what is actually left.",
        ],
        "note": "Good value and well equipped. Prefer 2023 and "
                "later, after the launch-year recalls. The plug-in "
                "hybrid is a different car, not covered here.",
    },
    {
        # 2016: 8 recalls, 171 complaints, 71 POWER TRAIN. 2018: 6
        # recalls, 58 complaints. 2020: 3 recalls, 32 complaints.
        "make": "mitsubishi", "model": "outlander",
        "years": (2014, 2020),
        "generation": "GF third gen",
        "engine": "2.4L 4B12 I4 with CVT, or 3.0L V6 with 6-speed "
                  "automatic on GT",
        "reliability": 6.2,
        "maintenance": 6.8,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.0,
        "tire_set_usd": 780,
        "risk": "CVT failure on four-cylinder cars: 71 of 171 "
                "complaints on the 2016 are POWER TRAIN, and a "
                "replacement is a four-figure job",
        "known_issues": [
            "POWER TRAIN is 42% of the 2016 file. Hesitation, "
            "whining and overheating warnings are the usual signs.",
            "Eight recalls on the 2016, six on the 2018, three on "
            "the 2020. Run the VIN.",
            "The V6 GT uses a conventional 6-speed automatic and "
            "avoids the CVT.",
            "Later cars are quieter: 32 complaints on the 2020.",
        ],
        "note": "Cheap three-row seating. 2018 and later, or the "
                "V6, and only with CVT service records.",
    },
    {
        # 2019: 1 recall, 47 complaints. 2021: 1 recall, 19.
        # 2023: 7 complaints; the recall endpoint returned nothing.
        "make": "mitsubishi", "model": "outlander sport",
        "years": (2018, 2026),
        "generation": "GA first gen, later years",
        "engine": "2.0L 4B11 or 2.4L 4B12 I4, CVT",
        "reliability": 6.6,
        "maintenance": 7.2,
        "annual_maintenance_usd": 540,
        "insurance_factor": 1.0,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "One recall on each of the 2019 and 2021. Complaints "
            "are few and falling: 47, then 19, then 7 on the 2023.",
            "A 2011 design sold with small updates ever since: "
            "noisy, slow with the 2.0L, dated safety tech.",
            "Ask for CVT fluid service on anything past 60k miles.",
        ],
        "note": "Old, simple and cheap. Dull to drive, but most of "
                "its faults were found years ago.",
    },
    {
        # 2016: 8 recalls, 163 complaints, 65 POWER TRAIN.
        "make": "mitsubishi", "model": "outlander sport",
        "years": (2011, 2017),
        "generation": "GA first gen, early years",
        "engine": "2.0L 4B11 or 2.4L 4B12 I4, CVT (5-speed manual "
                  "on base cars)",
        "reliability": 5.8,
        "maintenance": 7.2,
        "annual_maintenance_usd": 580,
        "insurance_factor": 1.0,
        "tire_set_usd": 680,
        "risk": "CVT failure: 65 of 163 complaints on the 2016 are "
                "POWER TRAIN, and a replacement can cost more than "
                "the car is worth",
        "known_issues": [
            "POWER TRAIN is 40% of the 2016 file.",
            "Eight recalls on the 2016. Check every one is closed.",
            "The base 5-speed manual avoids the CVT entirely.",
        ],
        "note": "Very cheap, and the CVT is why. A manual, or a "
                "2018 and later car, is the better bet.",
    },
    {
        # 2018: 2 recalls, 19 complaints. 2019: 1 recall, 13.
        # 2022: 8 complaints, 2023: 5; the recall endpoint returned
        # nothing for either.
        "make": "mitsubishi", "model": "eclipse cross",
        "years": (2018, 2025),
        "generation": "GK first gen",
        "engine": "1.5L 4B40 turbo I4, CVT",
        "reliability": 6.9,
        "maintenance": 6.8,
        "annual_maintenance_usd": 570,
        "insurance_factor": 1.0,
        "tire_set_usd": 780,
        "risk": None,
        "known_issues": [
            "Small files throughout: 19 complaints on the 2018, 13 "
            "on the 2019, 8 on the 2022. Electrical leads each.",
            "Two recalls on the 2018 and one on the 2019. The "
            "lookup returned none for 2022 or 2023; check by VIN.",
            "A small direct-injection turbo: change the oil on "
            "time and ask for proof the last owner did.",
            "There was no 2021 model. The 2022 facelift has the "
            "better cabin and cargo space.",
        ],
        "note": "Nothing alarming in the data, but there is not "
                "much data. Provisional.",
    },
    {
        # 2015: 2 recalls, 39 complaints. 2017: 2 recalls, 28
        # complaints, 14 AIR BAGS. 2019: 5 complaints, 2021: 2,
        # 2024: 4; NHTSA returned nothing at all for the 2023.
        "make": "mitsubishi", "model": "mirage",
        "years": (2014, 2024),
        "generation": "sixth gen",
        "engine": "1.2L 3A92 three-cylinder, CVT or 5-speed manual",
        "reliability": 6.8,
        "maintenance": 8.0,
        "annual_maintenance_usd": 430,
        "insurance_factor": 1.05,
        "tire_set_usd": 420,
        "risk": None,
        "known_issues": [
            "14 of 28 complaints on the 2017 are AIR BAGS. Confirm "
            "the airbag recall work is recorded.",
            "Two recalls on each of the 2015 and 2017. NHTSA "
            "returned nothing for the 2023, which is a gap in the "
            "data and not a clean record.",
            "Under 80 hp. Merging and hills take planning, and the "
            "engine is loud doing it.",
            "Light build and basic crash protection next to any "
            "larger car at the same price.",
        ],
        "note": "About the cheapest car to buy, fuel and maintain. "
                "Slow and thin, but the mechanicals are simple. "
                "Provisional for later years.",
    },
]
