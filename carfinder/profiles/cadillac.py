"""Reliability profiles: Cadillac. The format and the caveats on reading
these numbers are in carfinder/reliability.py."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "cadillac", "model": "escalade",
        "years": (2015, 2020),
        "generation": "fourth gen (K2XX)",
        "engine": "6.2L V8; 6-speed automatic on early 2015 trucks, then an "
                  "8-speed, and a 10-speed from 2018",
        "reliability": 6.4,
        "maintenance": 5.8,
        "annual_maintenance_usd": 1050,
        "insurance_factor": 1.3,
        "tire_set_usd": 1300,
        "risk": None,
        "known_issues": [
            "104 complaints on the 2016, led by engine (31), power train "
            "(22) and suspension (15). Only 22 on the 2018.",
            "4 recalls on the 2016, including 19V645000 (brake vacuum pump), "
            "and 1 on the 2018.",
            "The 8-speed automatic on 2015-2017 trucks can shudder at steady "
            "speed. The 10-speed from 2018 is the better transmission.",
            "Magnetic ride shocks and, on newer trucks, air springs are "
            "expensive to replace. Look for leaks and a sagging corner.",
        ],
        "note": "The 2018-2020 trucks with the 10-speed are the pick. "
                "Everything on it costs more than the same part on a Tahoe.",
    },
    {
        "make": "cadillac", "model": "escalade",
        "years": (2021, 2026),
        "generation": "fifth gen (T1)",
        "engine": "6.2L V8 or 3.0L Duramax diesel, 10-speed automatic; the "
                  "V-Series is supercharged",
        "reliability": 5.0,
        "maintenance": 5.4,
        "annual_maintenance_usd": 1200,
        "insurance_factor": 1.4,
        "tire_set_usd": 1500,
        "risk": "Engine is 112 of 146 complaints on the 2023, and recall "
                "25V274000 covers 6.2L V8 engines on 2021-2024 trucks for "
                "internal damage that can end in engine failure",
        "known_issues": [
            "Engine is 54 of 97 complaints on the 2021 and 112 of 146 on the "
            "2023. Three-quarters of a file on one component is as lopsided "
            "as it gets.",
            "9 recalls on the 2021 and 4 on the 2023. Confirm 25V274000 "
            "(6.2L engine) and, on a 2021, 24V797000 (transmission control "
            "valve).",
            "Almost every Escalade has the 6.2L, so the engine recall is the "
            "first thing to check on any of them. The diesel avoids it.",
            "Magnetic ride shocks and, on newer trucks, air springs are "
            "expensive to replace. Look for leaks and a sagging corner.",
        ],
        "note": "A lovely truck with a serious engine problem in the data. "
                "Do not buy a 6.2L without the recall paperwork.",
    },
    {
        "make": "cadillac", "model": "escalade esv",
        "years": (2015, 2020),
        "generation": "fourth gen (K2XX), long wheelbase",
        "engine": "6.2L V8; 6-speed automatic on early 2015 trucks, then an "
                  "8-speed, and a 10-speed from 2018",
        "reliability": 6.4,
        "maintenance": 5.8,
        "annual_maintenance_usd": 1070,
        "insurance_factor": 1.3,
        "tire_set_usd": 1300,
        "risk": None,
        "known_issues": [
            "The complaints endpoint returns the same 104 filings for the "
            "2016 ESV as for the standard Escalade, so read them as one "
            "file: engine 31, power train 22, suspension 15.",
            "3 recalls on the 2016 ESV.",
            "The 8-speed automatic on 2015-2017 trucks can shudder at steady "
            "speed. The 10-speed from 2018 is the better transmission.",
            "Magnetic ride shocks and, on newer trucks, air springs are "
            "expensive to replace. Look for leaks and a sagging corner.",
        ],
        "note": "A longer Escalade with the same strengths and costs. The "
                "2018-2020 trucks are the pick.",
    },
    {
        "make": "cadillac", "model": "escalade esv",
        "years": (2021, 2026),
        "generation": "fifth gen (T1), long wheelbase",
        "engine": "6.2L V8 or 3.0L Duramax diesel, 10-speed automatic; the "
                  "V-Series is supercharged",
        "reliability": 5.0,
        "maintenance": 5.4,
        "annual_maintenance_usd": 1220,
        "insurance_factor": 1.4,
        "tire_set_usd": 1500,
        "risk": "Engine is 68 of 96 complaints on the 2023, and recall "
                "25V274000 covers 6.2L V8 engines on 2021-2024 trucks for "
                "internal damage that can end in engine failure",
        "known_issues": [
            "Engine is 61 of 91 complaints on the 2021 and 68 of 96 on the "
            "2023, about two-thirds of the file or more.",
            "10 recalls on the 2021 and 4 on the 2023. Confirm 25V274000 "
            "(6.2L engine) and, on a 2021, 24V797000 (transmission control "
            "valve).",
            "Almost every Escalade has the 6.2L, so the engine recall is the "
            "first thing to check on any of them. The diesel avoids it.",
            "Magnetic ride shocks and, on newer trucks, air springs are "
            "expensive to replace. Look for leaks and a sagging corner.",
        ],
        "note": "Same verdict as the standard Escalade: do not buy a 6.2L "
                "without the recall paperwork.",
    },
    {
        "make": "cadillac", "model": "xt4",
        "years": (2019, 2023),
        "generation": "first gen",
        "engine": "2.0L turbo I4, 9-speed automatic; AWD available",
        "reliability": 7.0,
        "maintenance": 6.6,
        "annual_maintenance_usd": 680,
        "insurance_factor": 1.1,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "Small files: 22 complaints on the 2019 (engine 12) and 12 on "
            "the 2021.",
            "3 recalls on the 2019, including 20V668000 (automatic "
            "transmission), and 1 on the 2021.",
            "The first model year carries the most complaints and recalls. "
            "Prefer a 2020 or later.",
            "It needs premium fuel to make its rated power, and dealer labor "
            "rates are Cadillac rates.",
        ],
        "note": "A sound small luxury SUV with a thin complaint file. Not "
                "exciting, not troublesome.",
    },
    {
        "make": "cadillac", "model": "xt4",
        "years": (2024, 2026),
        "generation": "first gen, facelifted",
        "engine": "2.0L turbo I4, 9-speed automatic; AWD available",
        "reliability": 6.9,
        "maintenance": 6.5,
        "annual_maintenance_usd": 690,
        "insurance_factor": 1.12,
        "tire_set_usd": 880,
        "risk": None,
        "known_issues": [
            "33 complaints on the 2024, led by forward collision avoidance "
            "(10), service brakes (9) and electrical (8). More than the 12 "
            "on the 2021.",
            "1 recall on the 2024.",
            "The facelift added a 33-inch screen and new software. Check "
            "that every function works and that updates are current.",
            "Same engine and transmission as before, so the mechanical parts "
            "are a known quantity.",
        ],
        "note": "The same sound drivetrain with a lot of new electronics. "
                "Slightly provisional until those age.",
    },
    {
        "make": "cadillac", "model": "xt5",
        "years": (2017, 2019),
        "generation": "first gen",
        "engine": "3.6L V6, 8-speed automatic; AWD available",
        "reliability": 6.8,
        "maintenance": 6.5,
        "annual_maintenance_usd": 720,
        "insurance_factor": 1.1,
        "tire_set_usd": 880,
        "risk": None,
        "known_issues": [
            "125 complaints on the 2017 and 67 on the 2018, spread across "
            "power train, engine, electrical and steering with no single "
            "cluster.",
            "1 recall on the 2017 (16V802000, brakes). The API returned none "
            "for the 2018.",
            "The 8-speed can shift roughly or shudder at low speed. Drive it "
            "in stop-and-go traffic before deciding.",
            "The first model year has nearly twice the complaints of the "
            "second. Prefer a 2018 or 2019.",
        ],
        "note": "A comfortable midsize with an ordinary record. The 2020 "
                "update with the 9-speed is the better buy if the budget "
                "stretches.",
    },
    {
        "make": "cadillac", "model": "xt5",
        "years": (2020, 2026),
        "generation": "first gen, facelifted",
        "engine": "2.0L turbo I4 or 3.6L V6, 9-speed automatic; AWD "
                  "available",
        "reliability": 7.1,
        "maintenance": 6.5,
        "annual_maintenance_usd": 710,
        "insurance_factor": 1.1,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "Small files: 19 complaints on the 2021 and 17 on the 2023.",
            "4 recalls on the 2023, including 23V172000 (automatic "
            "transmission), 23V043000 (front half shaft) and 24V459000 "
            "(instrument panel). Confirm all three on a 2023.",
            "2 recalls on the 2021, including 21V422000 (fuel supply line).",
            "The V6 suits the car better than the 2.0L turbo.",
        ],
        "note": "Quiet in the complaints, with a few real recalls to "
                "confirm. A safe, conservative choice.",
    },
    {
        "make": "cadillac", "model": "xt6",
        "years": (2020, 2026),
        "generation": "first gen",
        "engine": "3.6L V6 or 2.0L turbo I4, 9-speed automatic; AWD "
                  "available",
        "reliability": 7.0,
        "maintenance": 6.4,
        "annual_maintenance_usd": 740,
        "insurance_factor": 1.12,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "40 complaints on the 2020, 15 on the 2022 and 16 on the 2024, "
            "with no dominant cluster.",
            "4 recalls on the 2020, including 20V668000 (automatic "
            "transmission) and 20V639000 (fuel pump). 3 on the 2022 and 2 on "
            "the 2024.",
            "On a 2024 or 2025, confirm 24V459000 (instrument panel may not "
            "light).",
            "Prefer a 2021 or later; the first year has the largest file.",
        ],
        "note": "A three-row Cadillac built on proven Traverse and Enclave "
                "parts. Unremarkable in the data, which is a compliment.",
    },
    {
        "make": "cadillac", "model": "ct4",
        "years": (2020, 2026),
        "generation": "first gen",
        "engine": "2.0L turbo I4 with an 8-speed automatic, or 2.7L turbo I4 "
                  "with a 10-speed; the Blackwing has a 3.6L twin-turbo V6",
        "reliability": 7.3,
        "maintenance": 6.5,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.2,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "Very small files: 8 complaints on the 2020, 6 on the 2022 and 7 "
            "on the 2024. Low sales explain part of that.",
            "4 recalls on the 2020, including 25V148000 (10-speed automatic) "
            "and 20V588000 (brakes). 2 on the 2022; none returned for the "
            "2024.",
            "On a 2020 or 2021 with the 10-speed, confirm 25V148000 was "
            "done.",
            "It sells in small numbers, so body and trim parts can take time "
            "to arrive.",
        ],
        "note": "A good small sport sedan with little on file against it. "
                "The thin data makes the score somewhat provisional.",
    },
    {
        "make": "cadillac", "model": "ct5",
        "years": (2020, 2026),
        "generation": "first gen",
        "engine": "2.0L turbo I4 or 3.0L twin-turbo V6, 10-speed automatic; "
                  "the Blackwing has a supercharged 6.2L V8",
        "reliability": 7.2,
        "maintenance": 6.3,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.25,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "40 complaints on the 2020, led by power train (16). Then 11 on "
            "the 2022 and 3 on the 2024.",
            "4 recalls on the 2020, including 25V148000 (10-speed automatic) "
            "and 20V588000 (brakes). 2 on the 2022; none returned for the "
            "2024.",
            "On a 2020 or 2021, confirm 25V148000 was done and test for "
            "harsh shifts.",
            "Prefer a 2021 or later; the first year carries most of the "
            "complaints.",
        ],
        "note": "A capable sedan that settled quickly after its first year.",
    },
    {
        "make": "cadillac", "model": "lyriq",
        "years": (2023, 2026),
        "generation": "first gen",
        "engine": "single motor rear-wheel drive or dual motor all-wheel "
                  "drive, 102 kWh battery",
        "reliability": 5.7,
        "maintenance": 6.0,
        "annual_maintenance_usd": 380,
        "insurance_factor": 1.3,
        "tire_set_usd": 1200,
        "risk": "8 recalls on the 2023 and 7 on the 2024, a very high "
                "campaign count for a new model",
        "known_issues": [
            "8 recalls on the 2023, including 23V367000 (high-voltage "
            "battery connections) and 22V710000 (driver display). 7 on the "
            "2024 and 4 already on the 2025.",
            "Recall 26V717000 (anti-lock brakes) covers 2023 through 2025, "
            "and 25V232000 (front stabilizer bar bolts) does too. Confirm "
            "both.",
            "119 complaints on the 2024, led by electrical (40), forward "
            "collision avoidance (39) and service brakes (30).",
            "EV running costs are low, but check the software level and that "
            "the car charges on both home and DC fast chargers.",
        ],
        "note": "Handsome and quiet, with a recall list that says the early "
                "cars were not finished. Buy the newest you can and verify "
                "every campaign.",
    },
]
