"""Reliability profiles: Genesis. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

Genesis sells in small numbers, so its NHTSA complaint files are thin
and say little on their own. These scores lean on recall campaigns,
which do not scale with sales. Genesis cars all have immobilizers, so
the Hyundai and Kia theft problem does not apply here."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        # 2019: 5 recalls, 64 complaints. 2022: 2 recalls, 32
        # complaints. 2024: no recalls listed, 3 complaints.
        "make": "genesis", "model": "g70",
        "years": (2019, 2026),
        "generation": "IK first gen (facelift 2022)",
        "engine": "2.0L turbo I4 (2.5L turbo from 2024) or 3.3L "
                  "twin-turbo V6, 8-speed automatic; RWD or AWD",
        "reliability": 7.2,
        "maintenance": 6.0,
        "annual_maintenance_usd": 780,
        "insurance_factor": 1.2,
        "tire_set_usd": 1000,
        "risk": "Recall 24V191000 covers the engine on the 2019 and "
                "2022 pulled, and 24V528000 the fuel pump. Confirm "
                "both were performed",
        "known_issues": [
            "Five recalls on the 2019, also including 21V161000 (ABS "
            "module) and 24V107000 (starter). The 2024 lists none.",
            "Complaint files are small (64 on the 2019, 32 on the "
            "2022, 3 on the 2024), with no single dominant cluster.",
            "The long powertrain warranty is original-owner only. A "
            "used buyer gets 5yr/60k unless it is certified "
            "pre-owned.",
            "Performance tires and brakes cost more than on a "
            "Sonata. Rear-seat room is tight.",
        ],
        "note": "A real sport sedan with a decent record. Later "
                "years are cleaner, and a certified car is worth the "
                "premium.",
    },
    {
        # 2021: 4 recalls, 9 complaints. 2023: 4 recalls, 9
        # complaints.
        "make": "genesis", "model": "g80",
        "years": (2021, 2026),
        "generation": "RG3 second gen",
        "engine": "2.5L turbo I4 or 3.5L twin-turbo V6, 8-speed "
                  "automatic; RWD or AWD",
        "reliability": 7.0,
        "maintenance": 5.6,
        "annual_maintenance_usd": 850,
        "insurance_factor": 1.18,
        "tire_set_usd": 1100,
        "risk": "Fuel system recalls run through this generation: "
                "23V630000 and 24V282000 (fuel pump), 21V208000 and "
                "26V229000 (fuel hoses). Confirm each on the VIN",
        "known_issues": [
            "Four recalls on both the 2021 and the 2023. A failed "
            "fuel pump means a stall at speed, so the fuel campaigns "
            "matter most.",
            "Only 9 complaints on each year pulled. That reflects "
            "low sales, not a spotless car.",
            "Recall 25V105000 on the 2023 covers the instrument "
            "display.",
            "Out of warranty, electronics and air-suspension parts "
            "are priced like a luxury car's.",
        ],
        "note": "A lot of luxury for the money and no pattern of "
                "major failures in the data. The score is provisional "
                "because the files are thin.",
    },
    {
        # 2018: 7 recalls, 100 complaints (electrical 24, steering
        # 16, engine 14).
        "make": "genesis", "model": "g80",
        "years": (2017, 2020),
        "generation": "DH first gen (the former Hyundai Genesis "
                      "sedan)",
        "engine": "3.8L Lambda II V6, 3.3L twin-turbo V6, or 5.0L "
                  "Tau V8; 8-speed automatic",
        "reliability": 7.0,
        "maintenance": 5.8,
        "annual_maintenance_usd": 820,
        "insurance_factor": 1.12,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "Seven recalls on the 2018, including 24V191000 "
            "(engine), 21V160000 (ABS module, fire risk) and "
            "24V107000 (starter). Confirm all are closed.",
            "100 complaints on the 2018, spread across electrical "
            "(24), steering (16) and engine (14). No lopsided "
            "cluster.",
            "The 3.8L V6 is the simple, durable engine. The V8 is "
            "smooth and thirsty.",
            "Warranty for a second owner is 5yr/60k, which has "
            "expired on most of these.",
        ],
        "note": "An older design with a long recall list and no "
                "single weak point. A good used buy with the 3.8L if "
                "the campaigns are done.",
    },
    {
        # 2022: 5 recalls, 97 complaints (fuel/propulsion 29, power
        # train 22). 2024: 2 recalls, 20 complaints.
        "make": "genesis", "model": "gv70",
        "years": (2022, 2026),
        "generation": "JK1 first gen (facelift 2026)",
        "engine": "2.5L turbo I4 or 3.5L twin-turbo V6, 8-speed "
                  "automatic, AWD; an Electrified GV70 is also sold",
        "reliability": 6.9,
        "maintenance": 5.8,
        "annual_maintenance_usd": 820,
        "insurance_factor": 1.18,
        "tire_set_usd": 1050,
        "risk": "Two fuel pump recalls on the 2022 (23V630000 and "
                "24V282000): a failed pump stalls the engine. Confirm "
                "both were performed",
        "known_issues": [
            "Fuel/propulsion is the largest cluster on the 2022 (29 "
            "of 97), matching the two fuel pump campaigns.",
            "Five recalls on the first-year 2022, two of them on "
            "front seat belts (21V796000, 23V094000). The 2024 has "
            "two.",
            "Recall 26V229000 covers fuel hoses on both years "
            "pulled.",
            "The Electrified GV70 has no oil service and lower "
            "upkeep. Ask for a battery health report on a used one.",
        ],
        "note": "The best-selling Genesis and a pleasant one. Buy a "
                "2023 or later with the fuel recalls closed.",
    },
    {
        # 2021: 5 recalls, 62 complaints. 2023: 4 recalls, 44
        # complaints. 2025: 3 recalls, 20 complaints.
        "make": "genesis", "model": "gv80",
        "years": (2021, 2026),
        "generation": "JX1 first gen (facelift 2025)",
        "engine": "2.5L turbo I4 or 3.5L twin-turbo V6, 8-speed "
                  "automatic, AWD",
        "reliability": 6.8,
        "maintenance": 5.5,
        "annual_maintenance_usd": 880,
        "insurance_factor": 1.2,
        "tire_set_usd": 1200,
        "risk": "Fuel system recalls on every year pulled: 23V630000 "
                "and 24V282000 (fuel pump), 21V208000 and 26V229000 "
                "(fuel hoses). Confirm each on the VIN",
        "known_issues": [
            "Five recalls on the 2021, four on the 2023 and three on "
            "the 2025. The count is falling but not gone.",
            "Electrical is the largest complaint cluster on all "
            "three years pulled (15, 12 and 5).",
            "Driver-assist complaints show up too: forward collision "
            "avoidance is 10 of 62 on the 2021.",
            "Large wheels and tires are expensive, and repair costs "
            "after warranty are full luxury prices.",
        ],
        "note": "Handsome and much cheaper than the Germans, with a "
                "steady stream of recalls. Buy certified, or with "
                "warranty left.",
    },
    {
        # 2023: 6 recalls, 5 complaints.
        "make": "genesis", "model": "g90",
        "years": (2023, 2026),
        "generation": "RS4 second gen",
        "engine": "3.5L twin-turbo V6, with a 48-volt electric "
                  "supercharger on the top trim; 8-speed automatic, "
                  "AWD",
        "reliability": 6.6,
        "maintenance": 4.8,
        "annual_maintenance_usd": 1000,
        "insurance_factor": 1.28,
        "tire_set_usd": 1300,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2023, including 24V282000 (fuel "
            "pump), 25V833000 (driver-assist electronics) and two on "
            "front seat belts. Confirm all are closed.",
            "Only 5 complaints on the 2023. Almost none are on the "
            "road, so that number means little.",
            "Air suspension, rear-wheel steering and the electric "
            "supercharger are costly to fix out of warranty.",
        ],
        "note": "A flagship at a discount, with flagship repair "
                "bills later. Provisional: there is too little data "
                "to score it firmly.",
    },
    {
        # 2018: 4 recalls, 16 complaints.
        "make": "genesis", "model": "g90",
        "years": (2017, 2022),
        "generation": "HI first gen (facelift 2020)",
        "engine": "3.3L twin-turbo V6 or 5.0L Tau V8, 8-speed "
                  "automatic; RWD or AWD",
        "reliability": 7.2,
        "maintenance": 5.2,
        "annual_maintenance_usd": 920,
        "insurance_factor": 1.2,
        "tire_set_usd": 1150,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2018, including 24V191000 (engine) "
            "and 24V107000 (starter). Confirm both are closed.",
            "Only 16 complaints on the 2018. Sales were tiny, so "
            "treat that as thin data and not as proof.",
            "Parts are scarce outside Genesis dealers and priced "
            "like a luxury car's.",
            "Second-owner warranty is 5yr/60k and has expired on "
            "most of these.",
        ],
        "note": "Quiet, conventional and heavily depreciated. A "
                "comfortable used buy if you can live with dealer-"
                "only service. Provisional on thin data.",
    },
]
