"""Reliability profiles: Porsche. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

Porsche sells in small numbers, so the complaint files are small. Recall
counts are the better guide.
"""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "porsche", "model": "macan",
        "years": (2019, 2026),
        "generation": "first gen, facelift (gas)",
        "engine": "2.0L turbo I4 or 2.9L and 3.0L turbo V6; 7-speed "
                  "dual-clutch automatic, AWD",
        "reliability": 7.2,
        "maintenance": 3.8,
        "annual_maintenance_usd": 1300,
        "insurance_factor": 1.3,
        "tire_set_usd": 1450,
        "risk": None,
        "known_issues": [
            "One recall on the 2019, one on the 2021 and none found on the "
            "2023.",
            "21 complaints on the 2019 (10 for exterior lighting), 12 on the "
            "2021 and six on the 2023: small files.",
            "The battery-electric Macan sold from 2024 is a different "
            "vehicle and is not covered by this profile.",
            "Porsche parts and labour are among the most expensive of any "
            "brand here. Brakes and tires alone cost several times what they "
            "do on a mainstream SUV.",
        ],
        "note": "A short file for a performance SUV. Dependable for what it "
                "is, and expensive to service whatever happens.",
    },
    {
        "make": "porsche", "model": "macan",
        "years": (2015, 2018),
        "generation": "first gen",
        "engine": "2.0L turbo I4 (from 2017) or 3.0L and 3.6L turbo V6; "
                  "7-speed dual-clutch automatic, AWD",
        "reliability": 6.5,
        "maintenance": 3.8,
        "annual_maintenance_usd": 1400,
        "insurance_factor": 1.3,
        "tire_set_usd": 1400,
        "risk": "V6 cars are known for oil leaks at the timing cover, a "
                "large labour bill, and for transfer case failures",
        "known_issues": [
            "Two recalls on the 2015 and six on the 2017, including two fuel "
            "pump campaigns.",
            "28 complaints on the 2015 and 63 on the 2017, with air bags the "
            "largest group on the 2017 (21).",
            "Look for oil at the front of the engine and feel for shudder or "
            "binding in tight low-speed turns (transfer case).",
            "Porsche parts and labour are among the most expensive of any "
            "brand here. Brakes and tires alone cost several times what they "
            "do on a mainstream SUV.",
        ],
        "note": "Great to drive, with two known expensive faults. Buy only "
                "with proof that both have been checked or fixed.",
    },
    {
        "make": "porsche", "model": "cayenne",
        "years": (2019, 2026),
        "generation": "third gen",
        "engine": "3.0L turbo V6, 2.9L turbo V6 (S), 4.0L turbo V8 or "
                  "plug-in hybrid; 8-speed automatic, AWD",
        "reliability": 6.8,
        "maintenance": 3.6,
        "annual_maintenance_usd": 1500,
        "insurance_factor": 1.35,
        "tire_set_usd": 1600,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2019, the first year, five on the 2021, one "
            "on the 2023 and four on the 2024.",
            "50 complaints on the 2019, led by air bags (12) and electrical "
            "(11); 21 on the 2021 and five each on the 2023 and 2024.",
            "Air suspension and the plug-in hybrid's battery are the big "
            "costs out of warranty. The base V6 on steel springs is the "
            "cheapest to keep.",
            "Porsche parts and labour are among the most expensive of any "
            "brand here. Brakes and tires alone cost several times what they "
            "do on a mainstream SUV.",
        ],
        "note": "A sound large luxury SUV by the numbers. The bills are high "
                "even when nothing breaks.",
    },
    {
        "make": "porsche", "model": "cayenne",
        "years": (2015, 2018),
        "generation": "second gen, facelift",
        "engine": "3.6L V6, 3.6L turbo V6 (S), 4.8L turbo V8, diesel (2015 "
                  "to 2016) or plug-in hybrid; 8-speed automatic, AWD",
        "reliability": 6.6,
        "maintenance": 3.6,
        "annual_maintenance_usd": 1550,
        "insurance_factor": 1.3,
        "tire_set_usd": 1500,
        "risk": "The transfer case is a known failure on this generation, "
                "felt as shudder or jerking under light acceleration",
        "known_issues": [
            "Two recalls on the 2015 and two on the 2017.",
            "14 complaints on the 2015 and 19 on the 2017: small files with "
            "no lopsided component.",
            "Diesel models were part of the emissions settlement. Confirm "
            "the fix was done.",
            "Porsche parts and labour are among the most expensive of any "
            "brand here. Brakes and tires alone cost several times what they "
            "do on a mainstream SUV.",
        ],
        "note": "Short NHTSA files, but an old, complex vehicle. Budget for "
                "the transfer case and for suspension work.",
    },
]
