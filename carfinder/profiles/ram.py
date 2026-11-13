"""Reliability profiles: Ram. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

NHTSA files recent Ram pickups under cab-style names ("1500 CREW
CAB") and does not separate the 1500 Classic from the new-body 1500
in its complaint data, so the counts below name the file they came
from."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "ram", "model": "1500",
        "years": (2015, 2018),
        "generation": "DS fourth gen",
        "engine": "3.6L Pentastar V6, 5.7L Hemi V8 or 3.0L EcoDiesel "
                  "V6, 8-speed automatic",
        "reliability": 5.6,
        "maintenance": 7.0,
        "annual_maintenance_usd": 720,
        "insurance_factor": 1.03,
        "tire_set_usd": 1000,
        "risk": "The 5.7L Hemi is known for lifter and camshaft "
                "failure, a repair that runs into the thousands, and "
                "the 2016 carries seventeen recalls",
        "known_issues": [
            "Seventeen recalls on the 2016 and fifteen on the 2018, "
            "covering the tailgate latch, curtain air bag inflators, "
            "rear axle and steering.",
            "1,567 complaints on the 2016, spread across steering "
            "(317), engine (293) and service brakes (289), with 36 "
            "fire reports.",
            "Listen to a Hemi at cold idle. A steady tick that does "
            "not fade is lifter wear, and broken exhaust manifold "
            "bolts sound similar.",
            "The EcoDiesel has its own engine and EGR cooler "
            "campaigns (20V475000, 19V757000). Buy one only with "
            "full records.",
        ],
        "note": "A comfortable, cheap-to-fix truck with a long "
                "recall list. The V6 is the low-risk engine; a quiet "
                "Hemi with service records is acceptable.",
    },
    {
        "make": "ram", "model": "1500",
        "years": (2019, 2024),
        "generation": "DT fifth gen",
        "engine": "3.6L Pentastar V6 or 5.7L Hemi V8 with eTorque "
                  "mild hybrid, 8-speed automatic; 3.0L EcoDiesel "
                  "through 2023",
        "reliability": 5.0,
        "maintenance": 6.6,
        "annual_maintenance_usd": 780,
        "insurance_factor": 1.06,
        "tire_set_usd": 1100,
        "risk": "Thirty recalls on the 2019 file and sixteen on the "
                "2022, plus the Hemi's known lifter and camshaft "
                "failures",
        "known_issues": [
            "Thirty recalls on the 2019 (the file also holds the "
            "Classic), fourteen on the 2020 and sixteen on the 2022. "
            "Run the VIN; expect several open.",
            "1,503 complaints on the 2019 file: electrical 383, "
            "steering 342, engine 235. The first year is the one to "
            "avoid.",
            "642 complaints on the 2022 Crew Cab file, led by engine "
            "(254) and electrical (203).",
            "Check the big touchscreen, the backup camera (five "
            "campaigns on the 2022) and the rear window for leaks.",
        ],
        "note": "The nicest half-ton to sit in and one of the most "
                "recalled. Skip 2019; a 2021 or later V6 is the "
                "defensible choice.",
    },
    {
        "make": "ram", "model": "1500",
        "years": (2025, 2026),
        "generation": "DT facelift",
        "engine": "3.6L Pentastar V6 or 3.0L Hurricane twin turbo I6, "
                  "8-speed automatic; 5.7L Hemi returns for 2026",
        "reliability": 4.8,
        "maintenance": 6.0,
        "annual_maintenance_usd": 820,
        "insurance_factor": 1.08,
        "tire_set_usd": 1150,
        "risk": "Eight recalls on the 2025 already, and electrical is "
                "202 of 381 complaints on the 2025 Crew Cab file "
                "(53%)",
        "known_issues": [
            "Eight recalls on the 2025: wheel hubs (24V794000), "
            "headlights, two instrument cluster campaigns, brake "
            "lights and more.",
            "381 complaints on the 2025 Crew Cab: electrical 202, "
            "engine 80, exterior lighting 61. The facelift brought "
            "new electronics and new faults.",
            "The Hurricane six replaces the Hemi and has no long "
            "record yet. Keep it under powertrain warranty.",
        ],
        "note": "A new engine and new electrical system in one step, "
                "and the file shows it. Wait a year or buy with "
                "warranty.",
    },
    {
        "make": "ram", "model": "1500 classic",
        "years": (2019, 2024),
        "generation": "DS fourth gen, sold beside the new truck",
        "engine": "3.6L Pentastar V6 or 5.7L Hemi V8, 8-speed "
                  "automatic",
        "reliability": 5.8,
        "maintenance": 7.2,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.02,
        "tire_set_usd": 950,
        "risk": "The 5.7L Hemi is known for lifter and camshaft "
                "failure, a repair that runs into the thousands",
        "known_issues": [
            "NHTSA returned the same complaint file for the Classic "
            "as for the new-body 1500, so there is no separate count "
            "to quote.",
            "It is the 2013 to 2018 truck kept in production: old "
            "electronics, fewer screens, and a decade of fixes "
            "already made.",
            "Listen to a Hemi at cold idle for a steady tick, and "
            "look for broken exhaust manifold bolts.",
            "Many were work or fleet trucks. Check for idle hours, "
            "towing wear and a rusted rear bumper and bed seams.",
        ],
        "note": "Provisional. Scored from the earlier DS record; the "
                "simpler truck and usually the safer used buy than a "
                "2019 or 2020 new-body 1500.",
    },
    {
        "make": "ram", "model": "2500",
        "years": (2015, 2018),
        "generation": "DJ fourth gen heavy duty",
        "engine": "5.7L or 6.4L Hemi V8, or 6.7L Cummins turbo "
                  "diesel, 6-speed automatic",
        "reliability": 6.2,
        "maintenance": 6.0,
        "annual_maintenance_usd": 900,
        "insurance_factor": 1.08,
        "tire_set_usd": 1300,
        "risk": None,
        "known_issues": [
            "Fourteen recalls on the 2016, including two on the "
            "steering linkage (19V021000, 18E096000) and the "
            "tailgate latch.",
            "261 complaints on the 2016, with no single component "
            "dominating: power train 64, engine 54, steering 43.",
            "Solid front axle: worn track bar and steering parts "
            "cause a violent highway shimmy. Drive it at speed over "
            "bumps.",
            "On a Cummins, ask for emissions-system history (DPF, "
            "EGR, DEF). Deleted or tuned trucks are a legal and "
            "warranty problem.",
        ],
        "note": "A sound work truck. The Cummins outlasts the truck "
                "around it; the automatic behind it and the front "
                "end are what to inspect.",
    },
    {
        "make": "ram", "model": "2500",
        "years": (2019, 2024),
        "generation": "DJ fifth gen heavy duty",
        "engine": "6.4L Hemi V8 with 8-speed automatic, or 6.7L "
                  "Cummins turbo diesel with 6-speed automatic",
        "reliability": 5.6,
        "maintenance": 5.8,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.1,
        "tire_set_usd": 1350,
        "risk": "2019 and 2020 Cummins trucks carry a high-pressure "
                "fuel pump recall (21V880000); a failed pump sends "
                "metal through the whole fuel system",
        "known_issues": [
            "Twelve recalls on the 2019, ten on the 2020 and twelve "
            "on the 2022.",
            "Fuel system leads the complaint file on the 2019 and "
            "2020. On a diesel from those years, get proof the fuel "
            "pump recall was done.",
            "Recall 22V835000 covers transmission fluid leaking "
            "from the dipstick tube under heat. Confirm it is "
            "closed.",
            "182 complaints on the 2022 Crew Cab file, led by "
            "electrical (61) and power train (50).",
        ],
        "note": "Capable and comfortable, with a real diesel fuel "
                "pump problem in 2019 and 2020. A 2021 or later, or "
                "the gas 6.4L, avoids it.",
    },
    {
        "make": "ram", "model": "2500",
        "years": (2025, 2026),
        "generation": "DJ fifth gen facelift",
        "engine": "6.4L Hemi V8 or revised 6.7L Cummins turbo diesel, "
                  "8-speed automatic",
        "reliability": 5.5,
        "maintenance": 5.6,
        "annual_maintenance_usd": 980,
        "insurance_factor": 1.12,
        "tire_set_usd": 1400,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2025, including two on the "
            "instrument cluster and two on transmission software.",
            "68 complaints on the 2025 Crew Cab file, 41 of them "
            "electrical and 16 exterior lighting.",
            "The diesel gained a new 8-speed automatic and a revised "
            "engine for 2025. Both are too new to judge.",
        ],
        "note": "Provisional. Early faults are electrical, not "
                "mechanical, but the new diesel drivetrain has no "
                "record yet.",
    },
    {
        "make": "ram", "model": "3500",
        "years": (2015, 2018),
        "generation": "D2 fourth gen heavy duty",
        "engine": "6.4L Hemi V8 or 6.7L Cummins turbo diesel, 6-speed "
                  "automatic (Aisin optional)",
        "reliability": 6.2,
        "maintenance": 5.8,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.1,
        "tire_set_usd": 1400,
        "risk": None,
        "known_issues": [
            "Sixteen recalls on the 2016, including the steering "
            "linkage (19V021000) and wheel lug nuts (21V398000).",
            "134 complaints on the 2016, led by steering (29) and "
            "wheels (21).",
            "Most have towed heavy. Check the rear axle, the fifth "
            "wheel or gooseneck mounts, and transmission fluid "
            "condition.",
            "On a Cummins, ask for emissions-system history and "
            "walk away from deleted or tuned trucks.",
        ],
        "note": "A durable tow rig if it was maintained. Buy on "
                "condition and records, not on mileage alone.",
    },
    {
        "make": "ram", "model": "3500",
        "years": (2019, 2024),
        "generation": "D2 fifth gen heavy duty",
        "engine": "6.4L Hemi V8 with 8-speed automatic, or 6.7L "
                  "Cummins turbo diesel with 6-speed automatic",
        "reliability": 5.5,
        "maintenance": 5.6,
        "annual_maintenance_usd": 1000,
        "insurance_factor": 1.12,
        "tire_set_usd": 1450,
        "risk": "2019 and 2020 Cummins trucks carry a high-pressure "
                "fuel pump recall (21V880000), and power train is "
                "115 of 191 complaints on the 2022 (60%)",
        "known_issues": [
            "Fourteen recalls on the 2019 and twelve on the 2022.",
            "On a 2019 or 2020 diesel, get proof the fuel pump "
            "recall was done. Fuel system leads that year's "
            "complaints.",
            "191 complaints on the 2022 with power train at 115. "
            "Recall 22V835000 (transmission fluid leak under heat) "
            "is the related campaign.",
            "Test the trailer brake controller, exhaust brake and "
            "every camera with a trailer plugged in if you can.",
        ],
        "note": "Strong truck, weak spots in the diesel fuel pump "
                "and the 6-speed automatic. The Aisin-equipped "
                "trucks and 2021 or later diesels are the better "
                "picks.",
    },
    {
        "make": "ram", "model": "3500",
        "years": (2025, 2026),
        "generation": "D2 fifth gen facelift",
        "engine": "6.4L Hemi V8 or revised 6.7L Cummins turbo diesel, "
                  "8-speed automatic",
        "reliability": 5.5,
        "maintenance": 5.4,
        "annual_maintenance_usd": 1020,
        "insurance_factor": 1.14,
        "tire_set_usd": 1500,
        "risk": None,
        "known_issues": [
            "Five recalls on the 2025, two of them on the instrument "
            "cluster.",
            "43 complaints on the 2025: electrical 28 and service "
            "brakes 19 lead.",
            "New 8-speed automatic and revised diesel for 2025, "
            "both without a track record.",
        ],
        "note": "Provisional. The same early pattern as the 2025 "
                "Ram 2500: electrical niggles, mechanical verdict "
                "still open.",
    },
    {
        "make": "ram", "model": "promaster",
        "years": (2015, 2022),
        "generation": "first gen (Fiat Ducato based)",
        "engine": "3.6L Pentastar V6, 6-speed automatic (9-speed for "
                  "2022), front-wheel drive",
        "reliability": 5.4,
        "maintenance": 6.4,
        "annual_maintenance_usd": 820,
        "insurance_factor": 1.05,
        "tire_set_usd": 850,
        "risk": "The 6-speed 62TE automatic is the weak point under "
                "load, with a park pawl recall (23V301000) on 2019 "
                "to 2021 vans",
        "known_issues": [
            "Fifteen recalls on the 2016, nine on the 2019 and eight "
            "on the 2021. Four of the 2016's are seat campaigns, so "
            "read the list against how the van is fitted out.",
            "Power train leads the 2019 complaints (24 of 60). Check "
            "for harsh shifts, slipping and the fluid's color and "
            "smell.",
            "Radiator fan circuit recall 25V720000 covers 2018 to "
            "2026 vans. Confirm it is closed.",
            "Most are ex-fleet or camper conversions. Ask what it "
            "carried, and check the front suspension and sliding "
            "door hardware.",
        ],
        "note": "Cheap to buy and easy to load, with a transmission "
                "that dislikes heavy work. Fine for light duty with "
                "fluid changes on record.",
    },
    {
        "make": "ram", "model": "promaster",
        "years": (2023, 2026),
        "generation": "first gen facelift",
        "engine": "3.6L Pentastar V6, 9-speed automatic, front-wheel "
                  "drive; a battery electric version from 2024",
        "reliability": 5.3,
        "maintenance": 6.2,
        "annual_maintenance_usd": 820,
        "insurance_factor": 1.06,
        "tire_set_usd": 880,
        "risk": "Steering is 40 of 99 complaints on the 2023, with "
                "five fire reports, and a power steering wiring "
                "recall (26V621000) covers 2022 to 2026 vans",
        "known_issues": [
            "Six recalls on the 2023 and five on the 2025, including "
            "the radiator fan circuit (25V720000).",
            "99 complaints on the 2023: steering 40, electrical 25, "
            "engine cooling 15. Sudden loss of power steering is the "
            "common report.",
            "The electric van has its own drive software recall "
            "(25V665000) and a short range; it suits fixed local "
            "routes only.",
        ],
        "note": "The 9-speed fixes the old transmission complaint, "
                "but the steering and cooling recalls are fresh. "
                "Confirm every campaign is closed.",
    },
    {
        "make": "ram", "model": "promaster city",
        "years": (2015, 2022),
        "generation": "first gen (Fiat Doblo based)",
        "engine": "2.4L Tigershark I4, 9-speed automatic, front-wheel "
                  "drive",
        "reliability": 5.8,
        "maintenance": 6.4,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.0,
        "tire_set_usd": 620,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2016 and one on the 2019.",
            "58 complaints on the 2016, led by engine (19), "
            "electrical (15) and power train (15). Only five on the "
            "2019.",
            "The 2.4L uses oil between changes. Check the level "
            "before the test drive.",
            "Early 9-speed automatics shift roughly. Later software "
            "helps; drive it in traffic.",
        ],
        "note": "A handy small van with an average record. Prefer a "
                "2018 or later, and expect body parts to be slow now "
                "that it is discontinued.",
    },
]

# Listing feeds often name the ProMaster by its weight class or body.
# These are the same van, so they reuse the profiles above.
_ALIASES = {
    "promaster": ("promaster 1500", "promaster 2500", "promaster 3500",
                  "promaster cargo van", "promaster window van"),
    "promaster city": ("promaster city cargo van",
                       "promaster city wagon"),
}
PROFILES += [dict(p, model=alias) for p in list(PROFILES)
             for alias in _ALIASES.get(p["model"], ())]
