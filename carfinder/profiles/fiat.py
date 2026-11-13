"""Reliability profiles: Fiat. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

Fiat sold very few cars in the US after 2016, so the later complaint
files are close to empty. That is low volume, not a clean record."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "fiat", "model": "500",
        "years": (2015, 2019),
        "generation": "Type 312",
        "engine": "1.4L MultiAir I4 (turbo on Abarth and 2018+), "
                  "5-speed manual or 6-speed automatic",
        "reliability": 5.4,
        "maintenance": 6.0,
        "annual_maintenance_usd": 650,
        "insurance_factor": 0.98,
        "tire_set_usd": 520,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2015 and two on the 2017 and 2019.",
            "92 complaints on the 2015, led by power train (32) and "
            "electrical (26). The 2017 has 14 and the 2019 "
            "returned none.",
            "The MultiAir engine needs the exact oil grade, changed "
            "on time. A neglected one fails its valve actuator, "
            "which is an expensive part.",
            "Manual cars wear clutches early in city use. Check the "
            "bite point, and check door handles and window "
            "regulators work.",
        ],
        "note": "A fun, cheap city car with an average record and a "
                "shrinking dealer network. Buy on service history; "
                "the manual is the simpler choice.",
    },
    {
        "make": "fiat", "model": "500x",
        "years": (2016, 2018),
        "generation": "Type 334, before the facelift",
        "engine": "2.4L Tigershark I4 with 9-speed automatic, or 1.4L "
                  "turbo with 6-speed manual",
        "reliability": 5.0,
        "maintenance": 5.8,
        "annual_maintenance_usd": 720,
        "insurance_factor": 1.0,
        "tire_set_usd": 660,
        "risk": "154 complaints on the 2016 for a slow seller, split "
                "between engine (52), power train (50) and "
                "electrical (48): oil burning, stalls and a rough "
                "9-speed",
        "known_issues": [
            "One recall on the 2016 (16V529000, the 9-speed "
            "automatic).",
            "The 2.4L burns oil and can stall when low. Check the "
            "dipstick before the test drive.",
            "Drive it in traffic. Harsh or hesitant shifts from the "
            "9-speed are the known fault.",
            "Shares its platform with the Jeep Renegade, which "
            "helps with mechanical parts. Body and trim are slower.",
        ],
        "note": "The same hardware and the same faults as the early "
                "Jeep Renegade. Shop the 2019 or later instead.",
    },
    {
        "make": "fiat", "model": "500x",
        "years": (2019, 2023),
        "generation": "Type 334 facelift",
        "engine": "1.3L turbo I4, 9-speed automatic, AWD standard",
        "reliability": 5.6,
        "maintenance": 5.6,
        "annual_maintenance_usd": 720,
        "insurance_factor": 1.0,
        "tire_set_usd": 680,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2019 and one on the 2022, all air "
            "bag campaigns.",
            "Only three complaints on the 2019 and two on the 2022. "
            "So few were sold that this says little.",
            "The 1.3L turbo needs the exact oil specification and "
            "on-time changes. Ask for the records.",
            "Discontinued in the US after 2023, with few Fiat "
            "dealers left. Check where you would get it serviced.",
        ],
        "note": "Provisional: the file is too thin to score on, so "
                "this leans on the Jeep Renegade with the same "
                "engine. A reasonable car that is hard to support.",
    },
    {
        "make": "fiat", "model": "500e",
        "years": (2015, 2019),
        "generation": "Type 312 battery electric",
        "engine": "Single-motor electric, 24 kWh battery, "
                  "front-wheel drive",
        "reliability": 6.0,
        "maintenance": 5.6,
        "annual_maintenance_usd": 380,
        "insurance_factor": 1.0,
        "tire_set_usd": 520,
        "risk": None,
        "known_issues": [
            "One recall on the 2016 (16V303000): the power inverter "
            "can shut the drive system down. Confirm it is closed.",
            "Only four complaints on the 2016. It was sold in "
            "California and Oregon only, so the file is tiny.",
            "EV: about 84 miles of range when new and less now. Ask "
            "for a battery capacity reading, and note it has no DC "
            "fast charging.",
            "Outside the West Coast, few shops will touch the "
            "high-voltage system. Find one before you buy.",
        ],
        "note": "Provisional. A cheap, simple short-range EV that "
                "works as a second car near home and nowhere else.",
    },
    {
        "make": "fiat", "model": "500e",
        "years": (2024, 2026),
        "generation": "Type 332 battery electric",
        "engine": "Single-motor electric, 42 kWh battery, "
                  "front-wheel drive",
        "reliability": 6.0,
        "maintenance": 5.4,
        "annual_maintenance_usd": 380,
        "insurance_factor": 1.08,
        "tire_set_usd": 620,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2024 (air bags and headlights) and "
            "five complaints.",
            "EV: about 149 miles of range. Fine for a city, tight "
            "for a highway trip, and DC fast charging is slow by "
            "current standards.",
            "It is a new design sold in very small numbers, so "
            "there is no real record yet. Check the battery "
            "warranty transfers.",
            "Few Fiat dealers remain. Confirm one near you is "
            "trained and equipped to service it.",
        ],
        "note": "Provisional. Nothing alarming in the file, and "
                "nearly nothing in the file at all. A likeable city "
                "EV to lease.",
    },
    {
        "make": "fiat", "model": "500l",
        "years": (2015, 2020),
        "generation": "Type 330",
        "engine": "1.4L MultiAir turbo I4, 6-speed automatic "
                  "(dual-clutch on some 2015s) or 6-speed manual",
        "reliability": 4.8,
        "maintenance": 5.6,
        "annual_maintenance_usd": 740,
        "insurance_factor": 1.0,
        "tire_set_usd": 600,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2015 (both air bags) and 23 "
            "complaints. NHTSA returned nothing at all for the "
            "2018.",
            "Avoid the dual-clutch automatic on early cars. The "
            "conventional 6-speed automatic that replaced it is the "
            "one to have.",
            "The MultiAir turbo needs the exact oil, on time. Ask "
            "for records, and listen for a rough idle or misfire.",
            "Built in Serbia in small numbers. Trim, glass and body "
            "parts can take weeks.",
        ],
        "note": "Provisional. Roomy and cheap, with a poor "
                "reputation the thin NHTSA file neither confirms "
                "nor clears. Hard to recommend over a Kia Soul.",
    },
]
