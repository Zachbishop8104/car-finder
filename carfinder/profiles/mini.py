"""Reliability profiles: Mini. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

Model 'cooper' means the 2-door and 4-door Hardtop. NHTSA files it under
COOPER, COOPER S and HARDTOP depending on the year; counts quoted here
are the union of those names.
"""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "mini", "model": "cooper",
        "years": (2025, 2026),
        "generation": "fourth gen (F66)",
        "engine": "1.5L turbo I3 (Cooper) or 2.0L turbo I4 (Cooper S), "
                  "7-speed dual-clutch automatic",
        "reliability": 6.5,
        "maintenance": 5.4,
        "annual_maintenance_usd": 820,
        "insurance_factor": 1.05,
        "tire_set_usd": 800,
        "risk": None,
        "known_issues": [
            "Four recalls across the 2025 Cooper and Cooper S, the first "
            "year.",
            "Only four complaints on the 2025 so far, three about brakes.",
            "No manual gearbox is offered, and nearly every control is on "
            "the round centre screen. Try it before buying.",
            "Mini parts and labour are BMW-priced. An independent BMW and "
            "Mini specialist is the way to keep bills sensible.",
        ],
        "note": "Too new for a firm number. It is a heavy update of the "
                "previous car, so the engines are proven.",
    },
    {
        "make": "mini", "model": "cooper",
        "years": (2019, 2024),
        "generation": "third gen (F56), facelift",
        "engine": "1.5L turbo I3 (Cooper) or 2.0L turbo I4 (Cooper S); "
                  "manual or automatic",
        "reliability": 7.0,
        "maintenance": 5.4,
        "annual_maintenance_usd": 820,
        "insurance_factor": 1.05,
        "tire_set_usd": 750,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2019 and none found on the 2022.",
            "14 complaints on the 2019 and seven on the 2022: small files "
            "with no lopsided component.",
            "Upper engine mounts and front control arm bushings are the "
            "usual wear items. Listen for a clunk when pulling away.",
            "Mini parts and labour are BMW-priced. An independent BMW and "
            "Mini specialist is the way to keep bills sensible.",
        ],
        "note": "The dependable years of the modern Mini, and much better "
                "than the brand's older reputation.",
    },
    {
        "make": "mini", "model": "cooper",
        "years": (2015, 2018),
        "generation": "third gen (F56)",
        "engine": "1.5L turbo I3 (Cooper) or 2.0L turbo I4 (Cooper S); "
                  "manual or automatic",
        "reliability": 6.4,
        "maintenance": 5.4,
        "annual_maintenance_usd": 850,
        "insurance_factor": 1.05,
        "tire_set_usd": 750,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2015 Cooper and Cooper S and four on the "
            "2016.",
            "74 complaints on the 2015, led by engine (17) and fuel system "
            "(13); 38 on the 2016.",
            "Upper engine mounts fail early on these years, and manual cars "
            "can need a clutch by 60,000 miles. Check both.",
            "Mini parts and labour are BMW-priced. An independent BMW and "
            "Mini specialist is the way to keep bills sensible.",
        ],
        "note": "A big step up from the older Minis, with a longer file than "
                "the 2019 and later cars.",
    },
    {
        "make": "mini", "model": "countryman",
        "years": (2025, 2026),
        "generation": "third gen (U25)",
        "engine": "2.0L turbo I4, 7-speed dual-clutch automatic, AWD; SE is "
                  "electric",
        "reliability": 6.3,
        "maintenance": 5.2,
        "annual_maintenance_usd": 880,
        "insurance_factor": 1.08,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2025, the first year.",
            "18 complaints on the 2025, led by electrical (8) and service "
            "brakes (7).",
            "It shares its platform with the BMW X1, whose file is dominated "
            "by a recalled brake control unit. Confirm no campaign is open "
            "on the car you are looking at.",
            "Mini parts and labour are BMW-priced. An independent BMW and "
            "Mini specialist is the way to keep bills sensible.",
        ],
        "note": "Too new for a firm number. Bigger and more grown-up than "
                "before, with the BMW X1's early brake complaints.",
    },
    {
        "make": "mini", "model": "countryman",
        "years": (2017, 2024),
        "generation": "second gen (F60)",
        "engine": "1.5L turbo I3 or 2.0L turbo I4, automatic or manual; SE "
                  "is a plug-in hybrid",
        "reliability": 6.8,
        "maintenance": 5.2,
        "annual_maintenance_usd": 880,
        "insurance_factor": 1.05,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2017, two on the 2019 and none found on the "
            "2022.",
            "Seven complaints on the 2017, 11 on the 2019 and two on the "
            "2022: very small files.",
            "The three-cylinder is slow in a car this heavy. The plug-in SE "
            "has campaigns of its own; check that VIN separately.",
            "Mini parts and labour are BMW-priced. An independent BMW and "
            "Mini specialist is the way to keep bills sensible.",
        ],
        "note": "BMW X1 mechanicals and a quiet record. The sensible Mini.",
    },
    {
        "make": "mini", "model": "countryman",
        "years": (2015, 2016),
        "generation": "first gen (R60)",
        "engine": "1.6L I4 or 1.6L turbo I4 (Cooper S), 6-speed manual or "
                  "automatic",
        "reliability": 4.8,
        "maintenance": 4.8,
        "annual_maintenance_usd": 1000,
        "insurance_factor": 1.05,
        "tire_set_usd": 800,
        "risk": "The 1.6L engines of this generation, the turbo above all, "
                "have a long record of timing chain, oil leak and thermostat "
                "housing repairs",
        "known_issues": [
            "69 complaints on the 2015 across the Cooper and Cooper S "
            "Countryman files, led by engine (17) and fuel system (12). No "
            "recalls came back under those names, which may be a naming gap.",
            "Listen for a rattle on a cold start (timing chain) and check "
            "the oil level; these engines use oil between changes.",
            "Clutch and dual-mass flywheel wear is common on manual cars.",
            "Mini parts and labour are BMW-priced. An independent BMW and "
            "Mini specialist is the way to keep bills sensible.",
        ],
        "note": "The old Mini engine in its last years. Avoid unless it is "
                "very cheap and has a thick folder of receipts.",
    },
]
