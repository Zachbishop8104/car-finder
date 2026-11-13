"""Reliability profiles: Polestar. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

The Polestar 2 is an EV built on Volvo's compact platform. NHTSA files
it under the model name POLESTAR 2; dealer feeds list it as model 2.
"""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "polestar", "model": "2",
        "years": (2024, 2026),
        "generation": "first gen, rear-drive update",
        "engine": "single-motor RWD or dual-motor AWD; roughly 79 to 82 kWh "
                  "battery",
        "reliability": 6.6,
        "maintenance": 5.0,
        "annual_maintenance_usd": 420,
        "insurance_factor": 1.25,
        "tire_set_usd": 1100,
        "risk": None,
        "known_issues": [
            "Five recalls and 25 complaints on the 2024, against 306 "
            "complaints on the 2022.",
            "Back over prevention (the rear camera) is still the top "
            "complaint component on the 2024 (13 of 25).",
            "Servicing is light and mostly done through Volvo dealers, but "
            "Polestar's own network is small. Check where the nearest "
            "service point is.",
            "Battery warranty is 8 years or 100,000 miles. Body and glass "
            "parts can be slow to arrive.",
        ],
        "note": "The better Polestar 2: more range, a new rear motor and a "
                "much shorter complaint file.",
    },
    {
        "make": "polestar", "model": "2",
        "years": (2021, 2023),
        "generation": "first gen",
        "engine": "single-motor FWD or dual-motor AWD; 64 to 78 kWh battery",
        "reliability": 6.2,
        "maintenance": 5.0,
        "annual_maintenance_usd": 420,
        "insurance_factor": 1.25,
        "tire_set_usd": 1100,
        "risk": None,
        "known_issues": [
            "Five recalls on the 2021 and four each on the 2022 and 2023.",
            "Back over prevention is a lopsided share of complaints: 114 of "
            "148 on the 2021, 209 of 306 on the 2022 and 87 of 117 on the "
            "2023. The rear camera goes blank; confirm the recall fix is "
            "installed.",
            "Outside the camera, the file is short. Electrical is a distant "
            "second on the 2022 (47).",
            "Servicing is light, but service points are few and body parts "
            "can be slow. Battery warranty is 8 years or 100,000 miles.",
        ],
        "note": "One well-known fault, the rear camera, accounts for most of "
                "the file. With that fixed it is a solid, well-built EV.",
    },
]
