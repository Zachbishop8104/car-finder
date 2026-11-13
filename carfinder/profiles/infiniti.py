"""Reliability profiles: Infiniti. The format and the caveats on
reading these numbers are in carfinder/reliability.py.

Infiniti sells in small numbers, so its NHTSA complaint totals are
low across the board. Read the share of a file that one component
takes, and the recall count, rather than the total."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        # 2025: 1 recall, 20 complaints.
        "make": "infiniti", "model": "qx60",
        "years": (2025, 2026),
        "generation": "L51 second gen, four-cylinder",
        "engine": "2.0L KR20DDET variable-compression turbo I4, "
                  "9-speed automatic",
        "reliability": 6.3,
        "maintenance": 5.8,
        "annual_maintenance_usd": 820,
        "insurance_factor": 1.15,
        "tire_set_usd": 1050,
        "risk": None,
        "known_issues": [
            "One recall and 20 complaints on the 2025, with no "
            "pattern yet.",
            "The V6 was replaced by the VC-Turbo four for 2025. The "
            "same engine family has a heavy engine complaint file in "
            "the QX50.",
            "Keep every oil change receipt; engine warranty claims "
            "on this family tend to hinge on them.",
        ],
        "note": "Provisional. The body is proven, the engine in it "
                "is the open question. A 2022 to 2024 V6 is the "
                "safer buy.",
    },
    {
        # 2022: 2 recalls, 23 complaints. 2023: 3 recalls, 28.
        "make": "infiniti", "model": "qx60",
        "years": (2022, 2024),
        "generation": "L51 second gen, V6",
        "engine": "3.5L VQ35DD V6, 9-speed automatic (no CVT)",
        "reliability": 7.0,
        "maintenance": 6.0,
        "annual_maintenance_usd": 780,
        "insurance_factor": 1.15,
        "tire_set_usd": 1050,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2022 and three on the 2023. "
            "Complaints are few (23 and 28) and spread out.",
            "The 9-speed can be hesitant at low speed. Drive it in "
            "stop-and-go traffic.",
            "Shares its mechanicals with the Nissan Pathfinder, so "
            "any Nissan dealer can work on it.",
        ],
        "note": "The best QX60: the long-lived V6 with a "
                "conventional automatic in place of the CVT.",
    },
    {
        # 2015: 3 recalls, 92 complaints, 23 POWER TRAIN. 2017: 2
        # recalls, 68. 2019: 2 recalls, 44, 13 POWER TRAIN.
        "make": "infiniti", "model": "qx60",
        "years": (2014, 2020),
        "generation": "L50 first gen",
        "engine": "3.5L VQ35 V6, Xtronic CVT",
        "reliability": 5.8,
        "maintenance": 5.8,
        "annual_maintenance_usd": 850,
        "insurance_factor": 1.12,
        "tire_set_usd": 950,
        "risk": "CVT judder and failure, worst on 2014 to 2016 cars; "
                "a replacement transmission is a four-figure job",
        "known_issues": [
            "POWER TRAIN is the largest named group on the 2015 (23 "
            "of 92 complaints) and on the 2019 (13 of 44).",
            "A shudder under light throttle between 15 and 30 mph "
            "is the CVT. Walk away if you feel it.",
            "Ask for records of CVT fluid changes or a replaced "
            "unit.",
        ],
        "note": "A Pathfinder in a better suit, with the same CVT "
                "problem. Later years with records only.",
    },
    {
        # 2019: 3 recalls, 146 complaints, 58 ENGINE and 32 ENGINE
        # AND ENGINE COOLING. 2021: 2 recalls, 41 complaints.
        # 2023: 1 recall, 4 complaints.
        "make": "infiniti", "model": "qx50",
        "years": (2019, 2025),
        "generation": "J55 second gen",
        "engine": "2.0L KR20DDET variable-compression turbo I4, "
                  "Xtronic CVT",
        "reliability": 5.2,
        "maintenance": 5.5,
        "annual_maintenance_usd": 880,
        "insurance_factor": 1.12,
        "tire_set_usd": 950,
        "risk": "VC-Turbo engine failure: 90 of 146 complaints on "
                "the 2019 are engine or engine cooling, and owners "
                "describe bearing failure and loss of power",
        "known_issues": [
            "62% of the 2019 file is the engine. For a low-volume "
            "car that is a lopsided distribution, not noise.",
            "An engine bearing recall covers early cars. Get "
            "written proof it was done and what the inspection "
            "found.",
            "25 of 41 complaints on the 2021 are still engine or "
            "engine cooling.",
            "A CVT sits behind it, which adds a second expensive "
            "part to worry about.",
        ],
        "note": "Avoid the early years. A clever engine that has "
                "not held up so far.",
    },
    {
        # 2016: 19 complaints; the recall endpoint returned nothing.
        "make": "infiniti", "model": "qx50",
        "years": (2014, 2017),
        "generation": "J50 first gen (formerly EX)",
        "engine": "3.7L VQ37VHR V6, 7-speed automatic",
        "reliability": 7.8,
        "maintenance": 6.3,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.1,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "19 complaints on the 2016 with nothing dominant. The "
            "recall lookup returned nothing; run the VIN yourself.",
            "Thirsty and wants premium fuel.",
            "Small inside for its class, even after the 2016 "
            "stretch.",
        ],
        "note": "An old-fashioned V6 and a conventional automatic. "
                "A much safer used buy than the QX50 that replaced "
                "it. Provisional on recalls.",
    },
    {
        # 2025: 4 recalls, 8 complaints.
        "make": "infiniti", "model": "qx80",
        "years": (2025, 2026),
        "generation": "Z63 third gen",
        "engine": "3.5L VR35DDTT twin-turbo V6, 9-speed automatic",
        "reliability": 6.3,
        "maintenance": 5.2,
        "annual_maintenance_usd": 980,
        "insurance_factor": 1.25,
        "tire_set_usd": 1500,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2025, its first year.",
            "Only 8 complaints so far, which at these sales numbers "
            "says nothing yet.",
            "Twin turbos, air suspension and a great deal of new "
            "electronics. Budget for an extended warranty.",
        ],
        "note": "Provisional. Far more complicated than the V8 "
                "truck it replaces, with no track record.",
    },
    {
        # 2015: 2 recalls, 18 complaints. 2018: 2 recalls, 9.
        # 2022: 1 recall, 2 complaints.
        "make": "infiniti", "model": "qx80",
        "years": (2014, 2024),
        "generation": "Z62 second gen",
        "engine": "5.6L VK56VD V8, 7-speed automatic",
        "reliability": 7.3,
        "maintenance": 5.5,
        "annual_maintenance_usd": 920,
        "insurance_factor": 1.2,
        "tire_set_usd": 1400,
        "risk": None,
        "known_issues": [
            "One or two recalls on each year pulled, and complaint "
            "files in the single or low double digits.",
            "The hydraulic body motion control suspension on upper "
            "trims leaks with age and is costly. Look for fluid at "
            "the struts and a car sitting unevenly.",
            "Fuel economy in the mid teens. Brakes and 22-inch "
            "tires are expensive.",
        ],
        "note": "A Nissan Patrol in a suit: a tough V8 drivetrain "
                "with luxury-priced suspension and running costs.",
    },
    {
        # 2016: 4 recalls, 39 complaints. 2018: 3 recalls, 43
        # complaints, 17 ENGINE. 2021: 3 recalls, 7 complaints.
        "make": "infiniti", "model": "q50",
        "years": (2016, 2024),
        "generation": "V37, turbo engines",
        "engine": "3.0L VR30DDTT twin-turbo V6 (2.0L turbo I4 on "
                  "base cars to 2019), 7-speed automatic",
        "reliability": 6.6,
        "maintenance": 5.8,
        "annual_maintenance_usd": 820,
        "insurance_factor": 1.2,
        "tire_set_usd": 1000,
        "risk": "Turbocharger failure on 2016 to 2018 3.0t cars; "
                "replacing a pair of turbos is a multi-thousand "
                "dollar job",
        "known_issues": [
            "ENGINE leads the 2018 file (17 of 43 complaints). "
            "Listen for a siren-like whine and look for blue smoke "
            "on a cold start.",
            "Three or four recalls on each year pulled (2016, "
            "2018, 2021).",
            "Many have been tuned. Ask directly, and check for "
            "non-factory intake or exhaust parts.",
            "Later cars are quieter in the data: 7 complaints on "
            "the 2021.",
        ],
        "note": "Fast and cheap for the power. Buy 2019 or later, "
                "stock, with oil change records.",
    },
    {
        # 2015: 3 recalls, 126 complaints, 39 POWER TRAIN and 28
        # STEERING.
        "make": "infiniti", "model": "q50",
        "years": (2014, 2015),
        "generation": "V37, V6",
        "engine": "3.7L VQ37VHR V6, 7-speed automatic",
        "reliability": 7.2,
        "maintenance": 6.2,
        "annual_maintenance_usd": 780,
        "insurance_factor": 1.15,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "126 complaints on the 2015: POWER TRAIN (39) and "
            "STEERING (28) lead.",
            "Cars with the optional steer-by-wire system have had "
            "steering recalls and odd steering feel. Check which "
            "steering the car has and that recalls are closed.",
            "The dual-screen infotainment is slow and dated.",
        ],
        "note": "The engine is the proven part. The early "
                "electronics and optional steering are not.",
    },
    {
        # 2022: 1 recall, 10 complaints, 5 ENGINE. 2023: 1 recall,
        # 4 complaints.
        "make": "infiniti", "model": "qx55",
        "years": (2022, 2025),
        "generation": "first gen (QX50 coupe body)",
        "engine": "2.0L KR20DDET variable-compression turbo I4, "
                  "Xtronic CVT; AWD standard",
        "reliability": 5.4,
        "maintenance": 5.5,
        "annual_maintenance_usd": 880,
        "insurance_factor": 1.15,
        "tire_set_usd": 1050,
        "risk": "Same VC-Turbo engine as the QX50, whose 2019 file "
                "is 62% engine complaints; failure means a "
                "replacement engine",
        "known_issues": [
            "Half of the 2022's 10 complaints are ENGINE. The file "
            "is tiny, but it points the same way as the QX50's.",
            "Check whether the engine bearing recall applies to the "
            "VIN and get proof it was completed.",
            "Less cargo and rear headroom than the QX50 for more "
            "money.",
        ],
        "note": "A QX50 with a sloping roof and the same engine "
                "worry. Provisional on its own data, scored from "
                "the QX50's.",
    },
]
