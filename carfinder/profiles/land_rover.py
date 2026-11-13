"""Reliability profiles: Land Rover. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

Land Rover sells in small numbers, so the complaint files are small and
several came back empty. Recall counts, which do not scale with sales,
carry these scores.
"""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "land rover", "model": "range rover",
        "years": (2022, 2026),
        "generation": "fifth gen (L460)",
        "engine": "3.0L turbo I6 mild hybrid, 4.4L turbo V8 or plug-in "
                  "hybrid; 8-speed automatic",
        "reliability": 4.6,
        "maintenance": 3.0,
        "annual_maintenance_usd": 1700,
        "insurance_factor": 1.45,
        "tire_set_usd": 1700,
        "risk": "Ten or eleven recalls on each of its first three model "
                "years, on a vehicle where every repair is expensive",
        "known_issues": [
            "10 recalls on the 2022, 11 on the 2023 and 10 on the 2024.",
            "23 complaints on the 2023, led by service brakes (8), and 11 on "
            "the 2024. NHTSA's complaints endpoint returned nothing for the "
            "2022: an API gap, not a clean record.",
            "Air suspension is standard and is a certain cost as the car "
            "ages. Check it raises, lowers and holds height overnight.",
            "Land Rover parts and labour are expensive and dealers are few. "
            "Do not buy one without warranty cover or a repair fund.",
        ],
        "note": "A magnificent thing to ride in, with one of the heaviest "
                "recall records in these profiles. Lease it or buy it with "
                "warranty.",
    },
    {
        "make": "land rover", "model": "range rover",
        "years": (2015, 2021),
        "generation": "fourth gen (L405)",
        "engine": "3.0L supercharged V6 or 5.0L supercharged V8 (3.0L turbo "
                  "I6 from 2020; diesel offered); 8-speed automatic",
        "reliability": 4.2,
        "maintenance": 3.0,
        "annual_maintenance_usd": 1800,
        "insurance_factor": 1.4,
        "tire_set_usd": 1500,
        "risk": "Air suspension, and on the 5.0L V8 the timing chains and "
                "plastic coolant pipes, are expensive repeat failures out of "
                "warranty",
        "known_issues": [
            "13 recalls on the 2016, five of them for door latches; four on "
            "the 2018 and five on the 2020.",
            "NHTSA's complaints endpoint returned nothing for these years: "
            "an API gap, not a clean record.",
            "Air suspension is standard and is a certain cost as the car "
            "ages. Check it raises, lowers and holds height overnight.",
            "Land Rover parts and labour are expensive and dealers are few. "
            "Do not buy one without warranty cover or a repair fund.",
        ],
        "note": "Provisional: scored from recalls and the well-documented "
                "faults of this generation. Cheap to buy used for good "
                "reason.",
    },
    {
        "make": "land rover", "model": "range rover sport",
        "years": (2023, 2026),
        "generation": "third gen (L461)",
        "engine": "3.0L turbo I6 mild hybrid, 4.4L turbo V8 or plug-in "
                  "hybrid; 8-speed automatic",
        "reliability": 4.7,
        "maintenance": 3.0,
        "annual_maintenance_usd": 1650,
        "insurance_factor": 1.45,
        "tire_set_usd": 1700,
        "risk": "Seven or eight recalls on each of its first two model "
                "years, on a vehicle where every repair is expensive",
        "known_issues": [
            "Seven recalls on the 2023 and eight on the 2024.",
            "23 complaints on the 2023 and 18 on the 2024, with electrical "
            "the largest group on both (13 and 8).",
            "Air suspension is standard and is a certain cost as the car "
            "ages. Check it raises, lowers and holds height overnight.",
            "Land Rover parts and labour are expensive and dealers are few. "
            "Do not buy one without warranty cover or a repair fund.",
        ],
        "note": "Too new for a firm number, and the early signs match the "
                "brand's record. Best owned under warranty.",
    },
    {
        "make": "land rover", "model": "range rover sport",
        "years": (2015, 2022),
        "generation": "second gen (L494)",
        "engine": "3.0L supercharged V6 or 5.0L supercharged V8 (3.0L turbo "
                  "I6 from 2020; diesel offered); 8-speed automatic",
        "reliability": 4.3,
        "maintenance": 3.0,
        "annual_maintenance_usd": 1750,
        "insurance_factor": 1.4,
        "tire_set_usd": 1500,
        "risk": "Air suspension, and on the 5.0L V8 the timing chains and "
                "plastic coolant pipes, are expensive repeat failures out of "
                "warranty",
        "known_issues": [
            "11 recalls on the 2016, five of them for door latches; five on "
            "the 2018 and eight on the 2020.",
            "80 complaints on the 2016, led by steering (24) and engine "
            "(14); 33 on the 2018 and 50 on the 2020, where electrical leads "
            "(20).",
            "Air suspension is standard and is a certain cost as the car "
            "ages. Check it raises, lowers and holds height overnight.",
            "Land Rover parts and labour are expensive and dealers are few. "
            "Do not buy one without warranty cover or a repair fund.",
        ],
        "note": "Fast, handsome and unreliable. A full dealer history and a "
                "warranty are the minimum.",
    },
    {
        "make": "land rover", "model": "range rover evoque",
        "years": (2020, 2026),
        "generation": "second gen (L551)",
        "engine": "2.0L turbo I4 (mild hybrid on some), 9-speed automatic, "
                  "AWD",
        "reliability": 5.0,
        "maintenance": 3.8,
        "annual_maintenance_usd": 1250,
        "insurance_factor": 1.25,
        "tire_set_usd": 1050,
        "risk": None,
        "known_issues": [
            "15 recalls on the 2020, the first year (five air bags, four "
            "electrical), and three on the 2022.",
            "NHTSA's complaints endpoint returned nothing for these years: "
            "an API gap, not a clean record.",
            "The 9-speed automatic can hunt and thump at low speed. Drive it "
            "in town before deciding.",
            "Land Rover parts and labour are expensive and dealers are few. "
            "Do not buy one without warranty cover or a repair fund.",
        ],
        "note": "Provisional: scored from recalls only. The 2020 launch year "
                "is the one to avoid.",
    },
    {
        "make": "land rover", "model": "range rover evoque",
        "years": (2015, 2019),
        "generation": "first gen (L538)",
        "engine": "2.0L turbo I4, 9-speed automatic, AWD",
        "reliability": 4.8,
        "maintenance": 3.8,
        "annual_maintenance_usd": 1300,
        "insurance_factor": 1.25,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "One recall on the 2016 and two on the 2018.",
            "NHTSA's complaints endpoint returned nothing for these years: "
            "an API gap, not a clean record. The short recall list should "
            "not be read as a good record.",
            "The 9-speed automatic is known for harsh, hesitant shifts. Ask "
            "for gearbox software updates and the service record.",
            "Land Rover parts and labour are expensive and dealers are few. "
            "Do not buy one without warranty cover or a repair fund.",
        ],
        "note": "Provisional. Stylish and cheap used, with a poor reputation "
                "that the thin NHTSA file does not capture.",
    },
    {
        "make": "land rover", "model": "discovery",
        "years": (2017, 2026),
        "generation": "fifth gen (L462)",
        "engine": "3.0L supercharged V6 or diesel (to 2020); 2.0L turbo I4 "
                  "or 3.0L turbo I6 mild hybrid (from 2021); 8-speed "
                  "automatic",
        "reliability": 4.6,
        "maintenance": 3.2,
        "annual_maintenance_usd": 1500,
        "insurance_factor": 1.3,
        "tire_set_usd": 1300,
        "risk": "Air suspension and electrical faults are common out of "
                "warranty, and repairs are dealer-priced",
        "known_issues": [
            "Three recalls on the 2017, four on the 2018 and six each on the "
            "2020 and 2022.",
            "37 complaints on the 2018, 20 on the 2020 and 11 on the 2022, "
            "with electrical the largest or joint largest group on all "
            "three.",
            "Most have air suspension. Check it raises, lowers and holds "
            "height overnight, and test every seat-folding motor.",
            "Land Rover parts and labour are expensive and dealers are few. "
            "Do not buy one without warranty cover or a repair fund.",
        ],
        "note": "Hugely practical and a poor bet out of warranty. It sells "
                "in small numbers, so the complaint files understate the "
                "trouble.",
    },
    {
        "make": "land rover", "model": "defender",
        "years": (2020, 2026),
        "generation": "L663",
        "engine": "2.0L turbo I4, 3.0L turbo I6 mild hybrid or 5.0L "
                  "supercharged V8; 8-speed automatic",
        "reliability": 4.8,
        "maintenance": 3.4,
        "annual_maintenance_usd": 1400,
        "insurance_factor": 1.3,
        "tire_set_usd": 1400,
        "risk": "Eight to ten recalls on every model year checked (2020, "
                "2021, 2023, 2024)",
        "known_issues": [
            "Eight recalls on the 2020, 10 on the 2021, 10 on the 2023 and "
            "eight on the 2024.",
            "97 complaints on the 2023, with electrical close to half (45); "
            "60 on the 2020, led by exterior lighting (23).",
            "Check for water leaks at the roof and tailgate, and that every "
            "screen and camera works.",
            "Land Rover parts and labour are expensive and dealers are few. "
            "Do not buy one without warranty cover or a repair fund.",
        ],
        "note": "Capable and desirable, with a recall list that has not "
                "shortened in five years. Own it with a warranty.",
    },
]
