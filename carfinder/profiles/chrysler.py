"""Reliability profiles: Chrysler. The format and the caveats on
reading these numbers are in carfinder/reliability.py."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "chrysler", "model": "pacifica",
        "years": (2017, 2020),
        "generation": "RU first gen",
        "engine": "3.6L Pentastar V6, 9-speed automatic",
        "reliability": 4.9,
        "maintenance": 6.4,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.0,
        "tire_set_usd": 760,
        "risk": "1,547 complaints on the 2017 led by engine (527) and "
                "power train (474): stalling while driving and a "
                "9-speed automatic that shifts badly",
        "known_issues": [
            "Eleven recalls on the 2017 and twelve on the 2018, "
            "including a loose battery ground that can cause a "
            "stall (19V348000).",
            "1,547 complaints on the 2017 and 901 on the 2018. The "
            "2020 falls to 176 with five recalls, so later is "
            "better.",
            "Drive it for twenty minutes in traffic. Hesitation, "
            "flare between gears or a stumble at low speed are the "
            "known faults.",
            "Test both sliding doors, the liftgate and the "
            "start-stop system; each has its own complaint cluster.",
        ],
        "note": "The best minivan to sit in and a poor one to own in "
                "its first two years. A 2020 is a different "
                "proposition from a 2017.",
    },
    {
        "make": "chrysler", "model": "pacifica",
        "years": (2021, 2026),
        "generation": "RU first gen, facelift",
        "engine": "3.6L Pentastar V6, 9-speed automatic; AWD "
                  "available",
        "reliability": 5.4,
        "maintenance": 6.3,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.02,
        "tire_set_usd": 800,
        "risk": "Ten recalls on the 2022, eleven on the 2024 and nine "
                "on the 2025: the campaign count is not coming down",
        "known_issues": [
            "Recalls on the 2022 and 2025 include three side "
            "curtain air bag campaigns each. Run the VIN and expect "
            "open ones.",
            "222 complaints on the 2022: power train 74, engine 68, "
            "electrical 64. Fewer than the early vans, same shape.",
            "Several campaigns apply only to wheelchair-accessible "
            "conversions; NHTSA files them under the same model.",
            "AWD adds a transfer unit and rear drive module. Check "
            "for leaks and for vibration under acceleration.",
        ],
        "note": "Improved but still below the Sienna and Odyssey on "
                "record. Buy for the seats and the price, and keep "
                "it under warranty.",
    },
    {
        "make": "chrysler", "model": "pacifica hybrid",
        "years": (2017, 2020),
        "generation": "RU first gen plug-in hybrid",
        "engine": "3.6L V6 plug-in hybrid, 16 kWh battery, "
                  "electrically variable transmission",
        "reliability": 4.0,
        "maintenance": 4.8,
        "annual_maintenance_usd": 800,
        "insurance_factor": 1.05,
        "tire_set_usd": 780,
        "risk": "Twelve fire reports among 225 complaints on the 2018 "
                "plug-in, and recalls for an engine shutdown "
                "(23V010000) and a 12-volt post fault (20V334000)",
        "known_issues": [
            "225 complaints on the 2018 plug-in: electrical 84, "
            "hybrid propulsion 75, engine 63, with 12 fire reports.",
            "Recall 23V010000 covers 2017 to 2023 plug-ins: a "
            "transmission wiring connector can short and shut the "
            "engine off. Get proof it is closed.",
            "PHEV: about 32 miles of electric range when new. Ask "
            "for a battery health check and confirm the hybrid "
            "warranty status.",
            "High-voltage and transmission work is dealer-only. "
            "Price an extended plan into the deal.",
        ],
        "note": "Avoid the early plug-ins. The idea is excellent "
                "and the fuel savings are real, but the fire and "
                "shutdown history is not worth it.",
    },
    {
        "make": "chrysler", "model": "pacifica hybrid",
        "years": (2021, 2026),
        "generation": "RU first gen plug-in hybrid, facelift",
        "engine": "3.6L V6 plug-in hybrid, 16 kWh battery, "
                  "electrically variable transmission",
        "reliability": 4.5,
        "maintenance": 4.8,
        "annual_maintenance_usd": 800,
        "insurance_factor": 1.06,
        "tire_set_usd": 800,
        "risk": "A battery fire recall (26V362000) covers 2020 to "
                "2022 plug-ins and the engine shutdown recall "
                "(23V010000) runs through 2023",
        "known_issues": [
            "116 complaints on the 2022 plug-in: power train 55, "
            "engine 53, electrical 40. Sudden shutdowns are the "
            "common report.",
            "The recall endpoint returned an error for the plug-in "
            "by name, so campaigns are read from the shared "
            "Pacifica file.",
            "Until the battery recall is closed, the usual "
            "instruction is to park outside and not charge. Ask "
            "the dealer for the VIN status in writing.",
            "The 2024 is quieter (26 complaints, 17 of them "
            "engine), but it is early.",
        ],
        "note": "Provisional on recall count. Still the only "
                "plug-in minivan, and still a car to buy only with "
                "every campaign closed and warranty remaining.",
    },
    {
        "make": "chrysler", "model": "voyager",
        "years": (2020, 2026),
        "generation": "RU first gen (a lower-trim Pacifica)",
        "engine": "3.6L Pentastar V6, 9-speed automatic",
        "reliability": 5.6,
        "maintenance": 6.6,
        "annual_maintenance_usd": 720,
        "insurance_factor": 0.98,
        "tire_set_usd": 720,
        "risk": None,
        "known_issues": [
            "One recall on the 2020, five on the 2022 and seven on "
            "the 2024, mostly shared with the Pacifica (curtain air "
            "bags, backup camera).",
            "Complaint files are tiny (13 on the 2020, 6 on the "
            "2022) because few were sold to private buyers. That is "
            "low volume, not a clean record.",
            "2022 to 2024 vans were fleet-only, so most used ones "
            "are ex-rental. Check for interior wear and get the "
            "service history.",
            "Same engine and 9-speed as the Pacifica. Drive it in "
            "traffic and feel for hesitation or rough shifts.",
        ],
        "note": "A Pacifica with fewer features to break. Scored "
                "from the Pacifica's record of the same years, "
                "nudged up for the simpler equipment.",
    },
    {
        "make": "chrysler", "model": "300",
        "years": (2015, 2023),
        "generation": "LX second gen, facelifted",
        "engine": "3.6L Pentastar V6 or 5.7L Hemi V8, 8-speed "
                  "automatic; AWD available on the V6",
        "reliability": 7.0,
        "maintenance": 7.0,
        "annual_maintenance_usd": 680,
        "insurance_factor": 1.15,
        "tire_set_usd": 880,
        "risk": None,
        "known_issues": [
            "Three recalls on the 2016 and two each on the 2019 and "
            "2022. A short list.",
            "Small complaint files: 76 on the 2016, 61 on the 2019 "
            "(electrical 22, air bags 22) and five on the 2022.",
            "On the 5.7L, listen for a steady lifter tick at cold "
            "idle. The V6 has no such pattern.",
            "Check the infotainment screen for delamination and "
            "ghost touches, and the front suspension bushings for "
            "clunks.",
        ],
        "note": "An old design that got reliable by standing still. "
                "The V6 is a comfortable, inexpensive big sedan with "
                "a quiet record.",
    },
    {
        "make": "chrysler", "model": "200",
        "years": (2015, 2017),
        "generation": "UF second gen",
        "engine": "2.4L Tigershark I4 or 3.6L Pentastar V6, 9-speed "
                  "automatic",
        "reliability": 4.0,
        "maintenance": 6.2,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.03,
        "tire_set_usd": 660,
        "risk": "1,994 complaints on the 2015 with 100 crash reports: "
                "electrical 756, power train 695, engine 607. Stalls "
                "and 9-speed transmission failures",
        "known_issues": [
            "Eight recalls on the 2015, two of them on the automatic "
            "transmission (16V529000, 15V090000).",
            "The 2016 is far quieter (two recalls, 346 complaints), "
            "so the first year is the one to rule out.",
            "The 2.4L burns oil and can stall when low. Check the "
            "dipstick before the test drive.",
            "Drive it cold. Harsh shifts, a drop to neutral or a "
            "transmission warning light are the known failures.",
        ],
        "note": "Avoid the 2015 outright. A 2016 or 2017 V6 is "
                "tolerable if it is very cheap, but there are better "
                "sedans at the same money.",
    },
    {
        "make": "chrysler", "model": "town & country",
        "years": (2015, 2016),
        "generation": "RT fifth gen",
        "engine": "3.6L Pentastar V6, 6-speed automatic",
        "reliability": 5.7,
        "maintenance": 7.4,
        "annual_maintenance_usd": 670,
        "insurance_factor": 0.98,
        "tire_set_usd": 660,
        "risk": "The 62TE 6-speed automatic is the weak point: power "
                "train leads the complaints on both the 2015 (113) "
                "and the 2016 (187)",
        "known_issues": [
            "Four recalls on the 2015 and five on the 2016.",
            "383 complaints on the 2015 and 527 on the 2016, led by "
            "power train both years.",
            "Check transmission fluid condition and shift quality, "
            "and look for an oil leak from the filter housing on "
            "top of the engine.",
            "Test both power sliding doors and the liftgate, and "
            "look for rust on the rocker panels.",
        ],
        "note": "A Grand Caravan in a better suit. Cheap, easy to "
                "fix and worth buying only on transmission "
                "condition.",
    },
]

# Listing feeds spell this model both ways.
_ALIASES = {
    "town & country": ("town and country",),
}
PROFILES += [dict(p, model=alias) for p in list(PROFILES)
             for alias in _ALIASES.get(p["model"], ())]
