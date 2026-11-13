"""Reliability profiles: Rivian. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

Both are EVs from a young company. Servicing cost is low; insurance,
tires and body repair are not.
"""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "rivian", "model": "r1t",
        "years": (2022, 2024),
        "generation": "first gen",
        "engine": "dual or quad-motor AWD; roughly 105 to 149 kWh battery",
        "reliability": 5.4,
        "maintenance": 3.8,
        "annual_maintenance_usd": 550,
        "insurance_factor": 1.45,
        "tire_set_usd": 1700,
        "risk": "Body repair is unusually costly: minor rear-quarter damage "
                "can mean replacing a very large one-piece panel",
        "known_issues": [
            "12 recalls on the 2022 (four of them seat belts, two "
            "suspension) and eight on the 2023. Some are software, but "
            "several needed a shop visit.",
            "74 complaints on the 2022, led by suspension (17); 41 on the "
            "2023, led by air bags (14).",
            "Service centers are few and can be hours away. Find the nearest "
            "one and ask about wait times before you buy.",
            "Little routine servicing, but 20 to 22 inch truck tires wear "
            "fast at this weight and insurance is high.",
        ],
        "note": "A capable, likeable truck from a young company. The recall "
                "list, the thin service network and the repair bills are the "
                "price of that.",
    },
    {
        "make": "rivian", "model": "r1t",
        "years": (2025, 2026),
        "generation": "second gen",
        "engine": "dual, tri or quad-motor AWD; roughly 92 to 140 kWh "
                  "battery",
        "reliability": 5.6,
        "maintenance": 3.8,
        "annual_maintenance_usd": 520,
        "insurance_factor": 1.45,
        "tire_set_usd": 1700,
        "risk": "Body repair is unusually costly: minor rear-quarter damage "
                "can mean replacing a very large one-piece panel",
        "known_issues": [
            "Eight recalls on the 2025 already, including seat belts, "
            "lighting and electrical.",
            "Only 10 complaints on the 2025 so far, too few to show a "
            "pattern.",
            "The second gen changed the motors, wiring and software. It "
            "looks the same but shares little with the 2022 to 2024 truck.",
            "Service centers are still few. Check how far the nearest one "
            "is.",
        ],
        "note": "Too new for a firm number. Eight campaigns in the first "
                "year says the redesign did not reset the record.",
    },
    {
        "make": "rivian", "model": "r1s",
        "years": (2022, 2024),
        "generation": "first gen",
        "engine": "dual or quad-motor AWD; roughly 105 to 149 kWh battery",
        "reliability": 5.3,
        "maintenance": 3.8,
        "annual_maintenance_usd": 550,
        "insurance_factor": 1.45,
        "tire_set_usd": 1700,
        "risk": "Body repair is unusually costly, and parts and approved "
                "shops are scarce",
        "known_issues": [
            "13 recalls on the 2022 and 10 on the 2023, with seat belts, air "
            "bags and suspension the main groups.",
            "76 complaints on the 2023, led by air bags (29), electrical "
            "(16) and seats (12).",
            "Service centers are few and can be hours away. Find the nearest "
            "one and ask about wait times before you buy.",
            "Little routine servicing, but tires and insurance are both well "
            "above a gas three-row SUV.",
        ],
        "note": "The same strengths and the same drawbacks as the R1T: "
                "quick, roomy and capable, with a long recall list and a "
                "thin service network.",
    },
    {
        "make": "rivian", "model": "r1s",
        "years": (2025, 2026),
        "generation": "second gen",
        "engine": "dual, tri or quad-motor AWD; roughly 92 to 140 kWh "
                  "battery",
        "reliability": 5.5,
        "maintenance": 3.8,
        "annual_maintenance_usd": 520,
        "insurance_factor": 1.45,
        "tire_set_usd": 1700,
        "risk": "Body repair is unusually costly, and parts and approved "
                "shops are scarce",
        "known_issues": [
            "11 recalls on the 2025 already: electrical (3), exterior "
            "lighting (3) and seat belts (2) lead.",
            "55 complaints on the 2025, spread across electrical (9), "
            "forward collision avoidance (9) and exterior lighting (9).",
            "Service centers are still few. Check how far the nearest one "
            "is.",
        ],
        "note": "Too new for a firm number, and eleven campaigns in the "
                "first year is not an encouraging start.",
    },
]
