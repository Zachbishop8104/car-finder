"""Reliability profiles: Alfa Romeo. The format and the caveats on
reading these numbers are in carfinder/reliability.py.

Alfa sells in small numbers, so its complaint files are short. Read
the recall counts, which do not scale with sales."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "alfa romeo", "model": "giulia",
        "years": (2017, 2019),
        "generation": "Type 952, launch years",
        "engine": "2.0L turbo I4, 8-speed automatic, RWD or AWD "
                  "(Quadrifoglio: 2.9L twin turbo V6)",
        "reliability": 4.4,
        "maintenance": 3.8,
        "annual_maintenance_usd": 1150,
        "insurance_factor": 1.3,
        "tire_set_usd": 1100,
        "risk": "Nine recalls on the 2018 for a low-volume car, "
                "including a fuel pump that can fail and cut drive "
                "power (25V586000)",
        "known_issues": [
            "Seven recalls on the 2017 and nine on the 2018, "
            "covering wiring, brakes, the instrument cluster and "
            "the fuel pump.",
            "90 complaints on the 2018, led by fuel and propulsion "
            "(32), engine (21) and electrical (20). That is a lot "
            "for how few were sold.",
            "Expect warning lights, dead batteries and sensor "
            "faults. Buy only with a complete dealer service "
            "history and a pre-purchase scan.",
            "Dealers are scarce. Check how far the nearest one is "
            "before you fall for the test drive.",
        ],
        "note": "Among the best-driving sedans of its time and "
                "among the least dependable. For enthusiasts with a "
                "warranty and a second car.",
    },
    {
        "make": "alfa romeo", "model": "giulia",
        "years": (2020, 2026),
        "generation": "Type 952, updated interior and electronics",
        "engine": "2.0L turbo I4, 8-speed automatic, RWD or AWD "
                  "(Quadrifoglio: 2.9L twin turbo V6)",
        "reliability": 5.2,
        "maintenance": 3.9,
        "annual_maintenance_usd": 1100,
        "insurance_factor": 1.3,
        "tire_set_usd": 1100,
        "risk": "Nine recalls on the 2020, four of them on the "
                "brakes and one for a fuel line sensor that can "
                "crack and leak (21V878000)",
        "known_issues": [
            "Nine recalls on the 2020, falling to three on the 2022 "
            "and four on the 2024. Later cars are clearly better.",
            "The complaints endpoint returned an error for 2020, "
            "2022 and 2024, so there is no component breakdown "
            "behind this score.",
            "The 2020 update brought a better screen and "
            "electronics. Still test every function and scan for "
            "stored fault codes.",
            "Parts and labor are priced like a German luxury car, "
            "with fewer independent shops able to do the work.",
        ],
        "note": "Provisional: scored on recall counts and the "
                "earlier record. A 2022 or later with warranty is "
                "the only Giulia to consider.",
    },
    {
        "make": "alfa romeo", "model": "stelvio",
        "years": (2018, 2019),
        "generation": "Type 949, launch years",
        "engine": "2.0L turbo I4, 8-speed automatic, mostly AWD "
                  "(Quadrifoglio: 2.9L twin turbo V6)",
        "reliability": 4.3,
        "maintenance": 3.8,
        "annual_maintenance_usd": 1200,
        "insurance_factor": 1.28,
        "tire_set_usd": 1150,
        "risk": "Eleven recalls on the 2018 and 139 complaints for a "
                "low-volume car, led by engine (42) and electrical "
                "(42)",
        "known_issues": [
            "Eleven recalls on the 2018 and eight on the 2019, "
            "including brakes, wiring, the liftgate and the fuel "
            "pump (25V586000).",
            "139 complaints on the 2018 against 37 on the 2019. The "
            "first year is the one to avoid.",
            "Expect electrical faults: warning lights, a dead "
            "battery after sitting, and infotainment freezes.",
            "Check the distance to a dealer and ask for the full "
            "service history before anything else.",
        ],
        "note": "Drives better than any rival and breaks more "
                "often. Not a sensible only car outside warranty.",
    },
    {
        "make": "alfa romeo", "model": "stelvio",
        "years": (2020, 2026),
        "generation": "Type 949, updated interior and electronics",
        "engine": "2.0L turbo I4, 8-speed automatic, mostly AWD "
                  "(Quadrifoglio: 2.9L twin turbo V6)",
        "reliability": 5.3,
        "maintenance": 3.9,
        "annual_maintenance_usd": 1150,
        "insurance_factor": 1.28,
        "tire_set_usd": 1150,
        "risk": None,
        "known_issues": [
            "Six recalls each on the 2020 and 2021, three each on "
            "the 2022 and 2024.",
            "Complaint files are tiny (seven on the 2020, four each "
            "on the 2021 and 2022). Sales were low, so that is thin "
            "evidence, not a clean bill.",
            "On a 2020 or 2021, confirm the fuel line sensor recall "
            "(21V878000) and the brake campaigns are closed.",
            "Running costs are high whatever the reliability: "
            "premium fuel, expensive brakes and few independent "
            "specialists.",
        ],
        "note": "Provisional, and better than the launch years on "
                "every count fetched. Still a warranty purchase.",
    },
    {
        "make": "alfa romeo", "model": "tonale",
        "years": (2024, 2026),
        "generation": "first gen",
        "engine": "1.3L turbo plug-in hybrid with 6-speed automatic, "
                  "or 2.0L turbo I4 with 9-speed automatic from "
                  "2025; AWD",
        "reliability": 4.9,
        "maintenance": 4.4,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.2,
        "tire_set_usd": 950,
        "risk": "Six recalls on the 2024, including a brake pedal "
                "that can collapse (24V752000) and a high-voltage "
                "cable campaign on the plug-in (23V623000)",
        "known_issues": [
            "Six recalls on the 2024 and three on the 2025, shared "
            "with the Dodge Hornet built beside it.",
            "Only two complaints on the 2024 and three on the 2025. "
            "Too few were sold for that to mean anything.",
            "PHEV: about 30 miles of electric range, and "
            "high-voltage repairs are dealer-only. Confirm the "
            "battery warranty transfers.",
            "Dealers are few and it is a niche model. Price it as "
            "a car that will be hard to sell on.",
        ],
        "note": "Provisional. A new plug-in from a brand with a "
                "poor record, and six recalls in its first US year. "
                "Lease, do not buy.",
    },
]
