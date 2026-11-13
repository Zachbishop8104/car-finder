"""Reliability profiles: Mercedes-Benz. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

NHTSA files Mercedes recalls under the trim name (C 300, GLC 300, GLE
350) and complaints under the class name (C-CLASS, GLC-CLASS). Recall
counts quoted here are for the volume trim named; AMG and plug-in
versions have their own files and are not covered.
"""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "mercedes-benz", "model": "c-class",
        "years": (2022, 2026),
        "generation": "W206",
        "engine": "2.0L turbo I4 with 48-volt mild hybrid (C 300), 9-speed "
                  "automatic",
        "reliability": 6.0,
        "maintenance": 4.6,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.2,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "Nine recalls on the 2022 C 300 and nine on the 2023, led by "
            "electrical system and two fuel system campaigns on each.",
            "26 complaints on the 2022 and 26 on the 2023, with forward "
            "collision avoidance (11) leading the 2023.",
            "Nearly every control is on the central touchscreen. Check that "
            "the software is current and nothing lags.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "Pleasant and modern, with more campaigns than a new design "
                "should need. Too few complaints yet to call it good or bad.",
    },
    {
        "make": "mercedes-benz", "model": "c-class",
        "years": (2019, 2021),
        "generation": "W205 facelift",
        "engine": "2.0L turbo I4 (C 300), 9-speed automatic",
        "reliability": 6.3,
        "maintenance": 4.6,
        "annual_maintenance_usd": 1000,
        "insurance_factor": 1.2,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "17 recalls on the 2019 C 300, five of them electrical. That is "
            "a long list for a car in its fifth year of production.",
            "80 complaints on the 2019, against 456 on the 2015: engine "
            "still leads (19) but the file is far smaller.",
            "The facelift brought a revised engine that has not shown the "
            "piston trouble of the 2015 to 2018 cars.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "The years to buy if you want this body style. Check every "
                "recall against the VIN; there are a lot of them.",
    },
    {
        "make": "mercedes-benz", "model": "c-class",
        "years": (2015, 2018),
        "generation": "W205",
        "engine": "2.0L turbo I4 (C 300), 7-speed or 9-speed automatic",
        "reliability": 5.3,
        "maintenance": 4.6,
        "annual_maintenance_usd": 1050,
        "insurance_factor": 1.2,
        "tire_set_usd": 950,
        "risk": "Engine is the top complaint component on the 2015 (134 of "
                "456) and the 2016 (100 of 322); the early 2.0L turbo has a "
                "documented pattern of piston failure that needs a new "
                "engine",
        "known_issues": [
            "11 recalls on the 2015 C 300 and 13 on the 2016, including "
            "three steering campaigns on each.",
            "456 complaints on the 2015 and 322 on the 2016, led by engine, "
            "with structure (79) and fuel system (72) next on the 2015.",
            "Listen for a rough idle or misfire on a cold start and check "
            "for a stored misfire code. Walk away from any car with either.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "The risky years of the C-Class. A 2019 or later car costs "
                "more and is worth it.",
    },
    {
        "make": "mercedes-benz", "model": "e-class",
        "years": (2024, 2026),
        "generation": "W214",
        "engine": "2.0L turbo I4 (E 350) or 3.0L turbo I6 (E 450), 48-volt "
                  "mild hybrid, 9-speed automatic",
        "reliability": 6.3,
        "maintenance": 4.4,
        "annual_maintenance_usd": 1050,
        "insurance_factor": 1.25,
        "tire_set_usd": 1150,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2024 E 350, the first year.",
            "28 complaints on the 2024, with electrical the largest group "
            "(15).",
            "The cabin is mostly screens. Check every display and the driver "
            "assistance functions on a test drive.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "Too new for a firm number. A quiet start on recalls, with "
                "the electrics the thing to watch.",
    },
    {
        "make": "mercedes-benz", "model": "e-class",
        "years": (2017, 2023),
        "generation": "W213",
        "engine": "2.0L turbo I4 (E 300, E 350) or 3.0L six (E 400, E 450), "
                  "9-speed automatic",
        "reliability": 6.4,
        "maintenance": 4.4,
        "annual_maintenance_usd": 1100,
        "insurance_factor": 1.22,
        "tire_set_usd": 1100,
        "risk": None,
        "known_issues": [
            "Seven recalls on the 2018 E 300, six on the 2020 E 350 and 12 "
            "on the 2021.",
            "68 complaints on the 2018, 21 on the 2020 and 20 on the 2021, "
            "with engine and electrical leading and no lopsided component.",
            "From 2021 the six-cylinder E 450 uses a 48-volt mild hybrid "
            "system with a record of battery failures. The four-cylinder is "
            "the simpler car.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "A solid big sedan with an average file for the brand. Air "
                "suspension, where fitted, is the cost to plan for.",
    },
    {
        "make": "mercedes-benz", "model": "e-class",
        "years": (2015, 2016),
        "generation": "W212 facelift",
        "engine": "3.5L V6 (E 350), 7-speed automatic",
        "reliability": 7.2,
        "maintenance": 5.0,
        "annual_maintenance_usd": 1050,
        "insurance_factor": 1.2,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2015 E 350 and 57 complaints, led by air "
            "bags (13) with no lopsided component.",
            "The non-turbo V6 and 7-speed automatic are older, simpler and "
            "longer-lived than what replaced them.",
            "Engine mounts and, on cars with air suspension, the air springs "
            "are the usual age-related repairs.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "The last of the simple E-Classes and the most dependable "
                "Mercedes profiled here. Buy on condition and service "
                "history.",
    },
    {
        "make": "mercedes-benz", "model": "glc",
        "years": (2023, 2026),
        "generation": "X254",
        "engine": "2.0L turbo I4 with 48-volt mild hybrid (GLC 300), 9-speed "
                  "automatic",
        "reliability": 5.9,
        "maintenance": 4.6,
        "annual_maintenance_usd": 1050,
        "insurance_factor": 1.18,
        "tire_set_usd": 1100,
        "risk": None,
        "known_issues": [
            "12 recalls on the 2023 GLC 300 (three for the fuel system) and "
            "eight on the 2024.",
            "65 complaints on the 2023, with electrical the largest group "
            "(30); 33 on the 2024.",
            "Check that the software is current and that every fuel system "
            "recall is closed.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "A comfortable, popular SUV whose first two years already "
                "carry 20 campaigns between them. Best bought with warranty "
                "left.",
    },
    {
        "make": "mercedes-benz", "model": "glc",
        "years": (2016, 2022),
        "generation": "X253",
        "engine": "2.0L turbo I4 (GLC 300), 9-speed automatic",
        "reliability": 5.8,
        "maintenance": 4.6,
        "annual_maintenance_usd": 1050,
        "insurance_factor": 1.15,
        "tire_set_usd": 1000,
        "risk": "Twelve or more recalls on every year checked (12 on the "
                "2016, 12 on the 2018, 16 on the 2020), and 2016 to 2019 "
                "cars share the early 2.0L turbo with a documented piston "
                "failure pattern",
        "known_issues": [
            "12 recalls on the 2016, 12 on the 2018 and 16 on the 2020. Four "
            "on each of the first two are structure campaigns.",
            "141 complaints on the 2016, led by engine (40) and service "
            "brakes (29); engine also leads the 2018 (32 of 99) and 2020 (28 "
            "of 81).",
            "On full steering lock when cold the front tires skip and "
            "judder. It is a known trait of the 4MATIC cars, not a fault, "
            "but it wears tires.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "Nice to drive and to sit in, with a recall list that never "
                "shortened. A 2020 or later car avoids the early engine.",
    },
    {
        "make": "mercedes-benz", "model": "gle",
        "years": (2023, 2026),
        "generation": "W167, later years",
        "engine": "2.0L turbo I4 (GLE 350) or 3.0L turbo I6 with 48-volt "
                  "mild hybrid (GLE 450), 9-speed automatic",
        "reliability": 5.9,
        "maintenance": 4.0,
        "annual_maintenance_usd": 1200,
        "insurance_factor": 1.28,
        "tire_set_usd": 1300,
        "risk": None,
        "known_issues": [
            "Three recalls on the 2023 GLE 350 and three on the 2024, "
            "against 27 on the 2020.",
            "31 complaints on the 2023 and 52 on the 2024, with no lopsided "
            "component.",
            "Six-cylinder cars use a 48-volt mild hybrid system whose "
            "battery has a record of failing and leaving the car unable to "
            "start. Ask whether it has been replaced.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "Much calmer than the launch years. Still an expensive "
                "vehicle to keep once the warranty ends.",
    },
    {
        "make": "mercedes-benz", "model": "gle",
        "years": (2020, 2022),
        "generation": "W167, early years",
        "engine": "2.0L turbo I4 (GLE 350) or 3.0L turbo I6 with 48-volt "
                  "mild hybrid (GLE 450), 9-speed automatic",
        "reliability": 4.8,
        "maintenance": 4.0,
        "annual_maintenance_usd": 1250,
        "insurance_factor": 1.28,
        "tire_set_usd": 1300,
        "risk": "27 recalls on the 2020 launch year and 14 on the 2021, and "
                "the 48-volt battery on six-cylinder cars is known to fail "
                "and leave the car unable to start",
        "known_issues": [
            "27 recalls on the 2020 GLE 350, the highest count of any "
            "vehicle in these European profiles; 14 on the 2021.",
            "125 complaints on the 2020, led by engine (44) and electrical "
            "(37). The complaints endpoint returned nothing for the 2021.",
            "Run the VIN through the recall lookup and confirm every "
            "campaign is closed before you travel to see one.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "A first-year design with a very heavy recall list. Buy a "
                "2023 or later instead unless the price is far lower.",
    },
    {
        "make": "mercedes-benz", "model": "gle",
        "years": (2016, 2019),
        "generation": "W166",
        "engine": "3.5L V6 (GLE 350), 7-speed or 9-speed automatic",
        "reliability": 6.4,
        "maintenance": 4.4,
        "annual_maintenance_usd": 1200,
        "insurance_factor": 1.25,
        "tire_set_usd": 1200,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2016 GLE 350 and seven on the 2018.",
            "107 complaints on the 2016, spread across fuel system (22), "
            "electrical (19), steering (16) and engine (16); 57 on the 2018.",
            "The non-turbo V6 is the simple, long-lived choice. Air "
            "suspension and the diesel's emissions parts are the expensive "
            "items.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "An older design (a renamed ML) and the more dependable GLE. "
                "Dated inside, but far fewer campaigns than its replacement.",
    },
    {
        "make": "mercedes-benz", "model": "gla",
        "years": (2021, 2026),
        "generation": "H247",
        "engine": "2.0L turbo I4 (GLA 250), 8-speed dual-clutch automatic",
        "reliability": 6.3,
        "maintenance": 5.0,
        "annual_maintenance_usd": 900,
        "insurance_factor": 1.1,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "Nine recalls on the 2021 GLA 250, the first year, and one on "
            "the 2023.",
            "23 complaints on the 2021 and eight on the 2023: small files, "
            "with engine the largest group on both.",
            "The dual-clutch gearbox can be jerky at parking speeds. Drive "
            "it in slow traffic before deciding.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "The cheapest Mercedes SUV to run, with a file that "
                "shortened quickly after the first year.",
    },
    {
        "make": "mercedes-benz", "model": "gla",
        "years": (2015, 2020),
        "generation": "X156",
        "engine": "2.0L turbo I4 (GLA 250), 7-speed dual-clutch automatic",
        "reliability": 6.2,
        "maintenance": 5.0,
        "annual_maintenance_usd": 900,
        "insurance_factor": 1.1,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2016 GLA 250 and 12 on the 2018.",
            "54 complaints on the 2016 and 53 on the 2018, with engine and "
            "electrical leading and no lopsided component.",
            "The dual-clutch gearbox needs its fluid changed on schedule and "
            "can shudder if it has not been. Ask for the record.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "A small hatchback on stilts with an average file. Ride and "
                "cabin space are the usual reasons people sell them.",
    },
    {
        "make": "mercedes-benz", "model": "glb",
        "years": (2022, 2026),
        "generation": "X247, later years",
        "engine": "2.0L turbo I4 (GLB 250), 8-speed dual-clutch automatic",
        "reliability": 6.4,
        "maintenance": 5.0,
        "annual_maintenance_usd": 900,
        "insurance_factor": 1.1,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "One recall on the 2023 GLB 250, against 20 on the 2020.",
            "13 complaints on the 2023, a small file with engine (4) the "
            "largest group.",
            "The optional third row is for children only. Check that both "
            "rear rows fold and latch properly.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "A practical, boxy small SUV that settled down after a rough "
                "launch.",
    },
    {
        "make": "mercedes-benz", "model": "glb",
        "years": (2020, 2021),
        "generation": "X247, early years",
        "engine": "2.0L turbo I4 (GLB 250), 8-speed dual-clutch automatic",
        "reliability": 5.5,
        "maintenance": 5.0,
        "annual_maintenance_usd": 920,
        "insurance_factor": 1.1,
        "tire_set_usd": 950,
        "risk": "Twenty recalls on the 2020 launch year and eleven on the "
                "2021",
        "known_issues": [
            "20 recalls on the 2020 GLB 250 (five structure, four air bags) "
            "and 11 on the 2021.",
            "64 complaints on the 2020, led by structure (15) and electrical "
            "(14).",
            "Confirm every campaign is closed against the VIN; with this "
            "many it is easy for one to be missed.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "The launch years carry a very long recall list. Buy a 2022 "
                "or later unless every campaign is documented.",
    },
    {
        "make": "mercedes-benz", "model": "cla",
        "years": (2026, 2026),
        "generation": "third gen",
        "engine": "electric at launch (about 85 kWh battery, RWD or AWD); a "
                  "48-volt hybrid follows",
        "reliability": 6.0,
        "maintenance": 4.6,
        "annual_maintenance_usd": 650,
        "insurance_factor": 1.2,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "NHTSA returned no recalls or complaints for the 2026 yet. That "
            "is an empty file on a brand-new car, not a clean record.",
            "It is an all-new platform with new motors, battery and "
            "software, so there is no history to lean on.",
            "The electric version needs little servicing; check which "
            "drivetrain a listing actually has.",
        ],
        "note": "Provisional: no data yet. Scored at the brand's recent "
                "average until a file builds up.",
    },
    {
        "make": "mercedes-benz", "model": "cla",
        "years": (2020, 2025),
        "generation": "C118",
        "engine": "2.0L turbo I4 (CLA 250), 7-speed dual-clutch automatic",
        "reliability": 6.2,
        "maintenance": 5.0,
        "annual_maintenance_usd": 900,
        "insurance_factor": 1.15,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "11 recalls on the 2020 CLA 250, the first year. No recalls came "
            "back for the 2022.",
            "25 complaints on the 2020 and four on the 2022: small files.",
            "Low and stiffly sprung, so check the wheels for kerb and "
            "pothole damage and the front bumper for scrapes.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "Stylish and reasonably dependable after its first year. "
                "Rear seat and ride comfort are the compromises.",
    },
    {
        "make": "mercedes-benz", "model": "cla",
        "years": (2015, 2019),
        "generation": "C117",
        "engine": "2.0L turbo I4 (CLA 250), 7-speed dual-clutch automatic",
        "reliability": 6.0,
        "maintenance": 5.0,
        "annual_maintenance_usd": 920,
        "insurance_factor": 1.15,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "Seven recalls on the 2015 CLA 250 and 10 on the 2017.",
            "158 complaints on the 2015, led by engine (42); only 28 on the "
            "2017.",
            "The dual-clutch gearbox is jerky at low speed on early cars and "
            "needs its fluid changed on schedule.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "Cheap to buy now. Later years of this shape have a much "
                "shorter file than the 2015.",
    },
    {
        "make": "mercedes-benz", "model": "gls",
        "years": (2020, 2026),
        "generation": "X167",
        "engine": "3.0L turbo I6 (GLS 450) or 4.0L turbo V8 (GLS 580), "
                  "48-volt mild hybrid, 9-speed automatic",
        "reliability": 5.2,
        "maintenance": 3.8,
        "annual_maintenance_usd": 1400,
        "insurance_factor": 1.32,
        "tire_set_usd": 1450,
        "risk": "22 recalls on the 2020 launch year and 12 on the 2021, and "
                "the 48-volt battery is known to fail and leave the car "
                "unable to start",
        "known_issues": [
            "22 recalls on the 2020 GLS 450, 12 on the 2021 and five on the "
            "2023.",
            "39 complaints on the 2020 and 38 on the 2021, with electrical "
            "the largest group on both (18 and 17).",
            "Air suspension is standard and is a certain cost as the car "
            "ages. A 2023 or later has far fewer campaigns.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "A superb family hauler when it works, with a launch-year "
                "record to avoid. Buy late and buy with warranty.",
    },
    {
        "make": "mercedes-benz", "model": "gls",
        "years": (2017, 2019),
        "generation": "X166",
        "engine": "3.0L turbo V6 (GLS 450) or 4.7L turbo V8 (GLS 550), "
                  "9-speed automatic",
        "reliability": 5.8,
        "maintenance": 4.0,
        "annual_maintenance_usd": 1350,
        "insurance_factor": 1.3,
        "tire_set_usd": 1350,
        "risk": None,
        "known_issues": [
            "Eight recalls on the 2017 GLS 450 and three on the 2018.",
            "42 complaints on the 2017, with six fires reported, and 22 on "
            "the 2018. No single component dominates.",
            "Air suspension is standard. Check the car sits level and listen "
            "for the compressor running constantly.",
            "Mercedes parts and dealer labour are expensive, and many "
            "repairs need dealer-level software. Budget for a specialist and "
            "keep an emergency fund once the warranty ends.",
        ],
        "note": "An older design (a renamed GL) with fewer campaigns than "
                "its replacement, but air suspension and age make it costly.",
    },
]
