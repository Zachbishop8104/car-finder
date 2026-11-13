"""Reliability profiles: Ford. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

Recall and complaint counts quoted here were pulled from NHTSA's public
API in Nov 2026 and each names the model year it is for. NHTSA files
truck complaints by cab style and some EVs under a different name, so
where the complaints endpoint returned nothing the profile says so and
the score is provisional."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    # ---------------------------------------------------------- Escape
    {
        "make": "ford", "model": "escape",
        "years": (2026, 2026),
        "generation": "fourth gen, facelifted, final model year",
        "engine": "1.5L EcoBoost turbo I3 or 2.0L turbo I4; hybrid "
                  "uses a 2.5L",
        "reliability": 5.9,
        "maintenance": 7.2,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.0,
        "tire_set_usd": 700,
        "risk": "Same car as the 2023 to 2025, which carried eight "
                "recalls on the 2024 alone",
        "known_issues": [
            "Two recalls already on the 2026, and only three complaints "
            "so far. That is too little time on the road to call it "
            "clean.",
            "Mechanically identical to the 2023 to 2025 car, so read "
            "that record (eight recalls on the 2024) as this one's.",
            "The Escape has been discontinued. Parts will be around for "
            "years, but expect resale to stay weak.",
        ],
        "note": "The last Escape, and the same car as the 2023 to 2025. "
                "Scored the same as those years; provisional because "
                "the 2026 file is nearly empty.",
    },
    {
        "make": "ford", "model": "escape",
        "years": (2023, 2025),
        "generation": "fourth gen, facelifted",
        "engine": "1.5L EcoBoost turbo I3 or 2.0L turbo I4; hybrid "
                  "uses a 2.5L",
        "reliability": 5.9,
        "maintenance": 7.2,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.0,
        "tire_set_usd": 700,
        "risk": "Eight recalls on the 2024, a very high campaign count "
                "for a single model year",
        "known_issues": [
            "Eight recalls on the 2024 alone, including 24V634000 "
            "(fuel injectors) and 24V850000 (instrument cluster). "
            "Recall count does not scale with sales volume, so eight "
            "is a genuinely bad number.",
            "76 complaints led by electrical (27), collision "
            "avoidance (19) and lane departure (18).",
            "Depreciated 22.3%/yr in one Michigan market (Aug 2026), the "
            "worst measured for these profiles.",
            "The 1.5L three-cylinder EcoBoost has a long history of "
            "coolant intrusion on earlier versions. Verify which "
            "engine the specific car has.",
        ],
        "note": "Cheap to buy for a reason. Weak resale where it was measured "
                "and one of the worst recall records here.",
    },
    {
        "make": "ford", "model": "escape",
        "years": (2020, 2022),
        "generation": "fourth gen, early build",
        "engine": "1.5L EcoBoost turbo I3 or 2.0L turbo I4, 8-speed "
                  "automatic; hybrid and plug-in use a 2.5L",
        "reliability": 5.3,
        "maintenance": 7.0,
        "annual_maintenance_usd": 650,
        "insurance_factor": 1.0,
        "tire_set_usd": 700,
        "risk": "23 recalls on the 2020 and 19 on the 2022, with fuel "
                "system the top complaint on the 2022",
        "known_issues": [
            "23 recalls on the 2020 and 19 on the 2022. Run the VIN at "
            "nhtsa.gov/recalls and make the seller show every one "
            "closed.",
            "1,552 complaints on the 2020, led by structure (606) and "
            "power train (243). Structure at that share is one defect, "
            "not general wear: check the door and liftgate hardware.",
            "239 complaints on the 2022 with fuel system (64) on top. "
            "Fuel leaking near a hot engine is the fire route, so walk "
            "away from any car that smells of fuel.",
        ],
        "note": "The launch years of this body are the ones to avoid. "
                "A 2023 or later has a shorter recall list for similar "
                "money.",
    },
    {
        "make": "ford", "model": "escape",
        "years": (2017, 2019),
        "generation": "third gen, facelifted",
        "engine": "1.5L or 2.0L EcoBoost turbo I4, or the base 2.5L "
                  "non-turbo; 6-speed automatic",
        "reliability": 4.8,
        "maintenance": 6.8,
        "annual_maintenance_usd": 720,
        "insurance_factor": 0.98,
        "tire_set_usd": 680,
        "risk": "Coolant leaks into the cylinders on the 1.5L and 2.0L "
                "EcoBoost, and the usual fix is a replacement engine",
        "known_issues": [
            "2,708 complaints on the 2017, and engine is 1,587 of them "
            "with engine cooling another 513. A share that lopsided is "
            "the coolant intrusion fault, not a sales-volume effect.",
            "Only 4 recalls on the 2017, so the recall list does not "
            "cover the engine. A failure out of warranty is your bill.",
            "Before buying: check the coolant level cold, look for "
            "white exhaust smoke at startup, and ask for any misfire "
            "codes in the history.",
            "The base 2.5L non-turbo avoids the problem entirely. It "
            "is slow and is the one to buy.",
        ],
        "note": "Avoid the EcoBoost engines in these years unless the "
                "engine has already been replaced with paperwork. The "
                "2.5L S trim is a much safer car.",
    },
    {
        "make": "ford", "model": "escape",
        "years": (2015, 2016),
        "generation": "third gen, pre-facelift",
        "engine": "1.6L or 2.0L EcoBoost turbo I4, or the base 2.5L "
                  "non-turbo; 6-speed automatic",
        "reliability": 5.2,
        "maintenance": 6.9,
        "annual_maintenance_usd": 700,
        "insurance_factor": 0.97,
        "tire_set_usd": 680,
        "risk": "The 1.6L EcoBoost can overheat and crack its cylinder "
                "head, and the 2015 file has 20 fire complaints",
        "known_issues": [
            "9 recalls and 1,149 complaints on the 2015, led by power "
            "train (286) and engine (239), with 20 fires reported.",
            "The 6-speed automatic is the power train cluster: "
            "shudder, slipping and harsh shifts. Drive it warm and "
            "feel for a flare between second and third.",
            "The 1.6L turbo is the engine to avoid. The 2.5L is the "
            "dependable one, the 2.0L sits in between.",
        ],
        "note": "Old enough now that condition matters more than the "
                "badge. Buy the 2.5L, check the transmission, and "
                "confirm every recall is closed.",
    },
    # ---------------------------------------------------- Bronco Sport
    {
        "make": "ford", "model": "bronco sport",
        "years": (2026, 2026),
        "generation": "first gen, facelifted",
        "engine": "1.5L EcoBoost turbo I3 or 2.0L EcoBoost turbo I4, "
                  "8-speed automatic; AWD standard",
        "reliability": 5.6,
        "maintenance": 7.0,
        "annual_maintenance_usd": 650,
        "insurance_factor": 1.0,
        "tire_set_usd": 740,
        "risk": "Six recalls on the 2026 already, on top of fourteen "
                "on the 2023 version of the same car",
        "known_issues": [
            "Six recalls on the 2026 with the model year barely over. "
            "Only 8 complaints so far, which is time on the road, not "
            "proof of a fix.",
            "Same engines and platform as the 2021 to 2025 car, which "
            "logged fourteen recalls on the 2023.",
            "Standard AWD and real capability. Buy it with the factory "
            "warranty intact and use the dealer for everything.",
        ],
        "note": "Same verdict as the earlier years: likeable, capable, "
                "and recalled too often. Scored the same, and "
                "provisional until the 2026 file fills in.",
    },
    {
        "make": "ford", "model": "bronco sport",
        "years": (2021, 2025),
        "generation": "first gen",
        "engine": "1.5L EcoBoost turbo I3 or 2.0L EcoBoost turbo I4, "
                  "8-speed automatic; AWD standard",
        "reliability": 5.6,
        "maintenance": 7.0,
        "annual_maintenance_usd": 650,
        "insurance_factor": 1.0,
        "tire_set_usd": 740,
        "risk": "Fourteen recalls on the 2023 with five fire-related "
                "complaints and a fuel-system cluster; the 2025 "
                "already carries seven",
        "known_issues": [
            "Fourteen recalls on the 2023. That is not a volume "
            "artifact: it is fourteen separate defect campaigns.",
            "150 complaints with electrical (37), engine (32) and "
            "fuel system (29) leading, plus five fires.",
            "The 2025 has already accumulated seven recalls, "
            "including two separate instrument-cluster campaigns and "
            "one engine campaign. The pattern is not improving.",
            "Standard AWD and real capability. It is a likeable "
            "vehicle with a bad reliability record.",
        ],
        "note": "The most recall-prone vehicle profiled here after "
                "the Grand Cherokee. Avoid unless you love it enough "
                "to live with the dealer.",
    },
    # -------------------------------------------------------- Maverick
    {
        "make": "ford", "model": "maverick",
        "years": (2026, 2026),
        "generation": "first gen, facelifted",
        "engine": "2.5L hybrid (AWD available) or 2.0L EcoBoost "
                  "turbo I4",
        "reliability": 6.2,
        "maintenance": 7.4,
        "annual_maintenance_usd": 580,
        "insurance_factor": 0.98,
        "tire_set_usd": 700,
        "risk": "Seven recalls on the 2026 already, following fifteen "
                "on the 2024",
        "known_issues": [
            "Seven recalls on the 2026 and only 7 complaints so far. "
            "The recall habit of the earlier years has carried over.",
            "Same truck underneath as the 2022 to 2025, so the "
            "fifteen-recall 2024 is the record to read.",
            "The hybrid can now be had with AWD, which removes the "
            "main reason to pick the thirstier 2.0L turbo.",
        ],
        "note": "Still the small truck to buy, still recalled too "
                "often. Scored the same as 2022 to 2025; provisional "
                "until the 2026 file fills in.",
    },
    {
        "make": "ford", "model": "maverick",
        "years": (2022, 2025),
        "generation": "first gen",
        "engine": "2.5L hybrid or 2.0L EcoBoost turbo I4",
        "reliability": 6.2,
        "maintenance": 7.4,
        "annual_maintenance_usd": 580,
        "insurance_factor": 0.98,
        "tire_set_usd": 700,
        "risk": "Fifteen recalls on the 2024, a very high campaign "
                "count for a vehicle this new",
        "known_issues": [
            "Fifteen recalls on the 2024, including 24V185000 (fuel "
            "tank assembly) and several exterior-lighting campaigns.",
            "67 complaints led by power train (16) and electrical "
            "(12).",
            "Depreciated 10.9%/yr in one Michigan market (Aug 2026), among "
            "the best domestic numbers. Small trucks hold value.",
            "The hybrid returns genuinely good economy for a pickup, "
            "and the bed makes it far more useful than any crossover.",
        ],
        "note": "Best resale of the domestic vehicles measured, "
                "dragged down by a heavy recall count. If you want a "
                "truck bed, this is the one.",
    },
    # ----------------------------------------------------------- F-150
    {
        "make": "ford", "model": "f-150",
        "years": (2021, 2026),
        "generation": "fourteenth gen",
        "engine": "2.7L or 3.5L EcoBoost twin-turbo V6, 5.0L V8, or "
                  "the 3.5L PowerBoost hybrid; 10-speed automatic",
        "reliability": 6.3,
        "maintenance": 7.0,
        "annual_maintenance_usd": 780,
        "insurance_factor": 1.08,
        "tire_set_usd": 1100,
        "risk": "29 recalls on the 2021, the launch year of this "
                "generation, and 13 on the 2023",
        "known_issues": [
            "29 recalls on the 2021 and 13 on the 2023. Buy a 2023 or "
            "later if the budget allows, and run the VIN either way.",
            "NHTSA files F-150 complaints by cab style. The 2021 "
            "SuperCrew file alone holds 1,058, led by power train "
            "(333), electrical (130) and exterior lighting (120).",
            "The 10-speed automatic is the power train cluster: harsh "
            "or delayed shifts. Drive it cold and through stop-and-go "
            "before you sign.",
            "The PowerBoost hybrid adds a lot of hardware to a truck "
            "that already has a long recall list. The 2.7L and 5.0L "
            "are the simpler choices.",
        ],
        "note": "A good truck with a rough launch. Parts and "
                "mechanics are everywhere, which keeps a middling "
                "record livable. Avoid the 2021.",
    },
    {
        "make": "ford", "model": "f-150",
        "years": (2015, 2020),
        "generation": "thirteenth gen, aluminum body",
        "engine": "2.7L or 3.5L EcoBoost twin-turbo V6, 5.0L V8 or "
                  "base V6; 6-speed automatic, 10-speed from 2017",
        "reliability": 6.8,
        "maintenance": 7.2,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.05,
        "tire_set_usd": 1050,
        "risk": "Cam phaser rattle on the 2017 to 2020 3.5L EcoBoost "
                "and harsh shifting on the 10-speed are both common, "
                "and neither is cheap out of warranty",
        "known_issues": [
            "Recalls by year: 14 on the 2016, 19 on the 2018, 9 on "
            "the 2019 and 11 on the 2020. The 2018 is the worst of "
            "the run.",
            "In the base 2018 F-150 complaint file, power train is 73 "
            "of 104. That file is only part of the truck's total "
            "(NHTSA splits it by cab), but the share points at the "
            "10-speed.",
            "On a 3.5L EcoBoost, listen for a rattle in the first two "
            "seconds of a cold start. That is the cam phasers.",
            "The aluminum body does not rust but costs more to "
            "repair after a crash. Check for poor panel repairs.",
        ],
        "note": "The safest used F-150 here is a 2015 to 2016 with "
                "the 6-speed, or any year with the 2.7L or 5.0L. "
                "Cheap to keep running by full-size truck standards.",
    },
    # ------------------------------------------------- F-150 Lightning
    {
        "make": "ford", "model": "f-150 lightning",
        "years": (2022, 2026),
        "generation": "first gen, battery electric",
        "engine": "dual-motor electric, AWD; 98 kWh standard or "
                  "131 kWh extended-range battery",
        "reliability": 6.0,
        "maintenance": 6.8,
        "annual_maintenance_usd": 450,
        "insurance_factor": 1.2,
        "tire_set_usd": 1300,
        "risk": "Nine recalls on file for the 2022 and nine for the "
                "2023, and any battery work out of warranty is very "
                "expensive",
        "known_issues": [
            "Nine recalls on the 2022 and nine on the 2023. NHTSA's "
            "complaints endpoint returned nothing for the Lightning, "
            "which is a naming gap in the API, not a clean record.",
            "Routine maintenance is low (no oil, few brake jobs), but "
            "the truck is heavy and eats tires. Budget for them.",
            "Towing and cold weather each cut range sharply. If you "
            "tow, test your real route before committing.",
            "Ask for a battery health report and confirm the eight "
            "year battery warranty is still running on the VIN.",
        ],
        "note": "Provisional: scored from the recall list and the "
                "known shape of the truck, with no complaint data. "
                "Works well as a commuter truck, less well for towing.",
    },
    # ------------------------------------------------------ Super Duty
    # The "f-250" entries are copied to the other Super Duty names a
    # listings feed uses; see the loop at the bottom of this file.
    {
        "make": "ford", "model": "f-250",
        "years": (2023, 2026),
        "generation": "Super Duty, fifth gen",
        "engine": "6.8L or 7.3L gas V8, or the 6.7L Power Stroke "
                  "diesel V8; 10-speed automatic",
        "reliability": 6.2,
        "maintenance": 6.0,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.1,
        "tire_set_usd": 1400,
        "risk": "16 recalls on the 2023 F-250, the first year of "
                "this generation",
        "known_issues": [
            "16 recalls on the 2023 F-250. NHTSA returned no "
            "complaint file for it under this name, so the complaint "
            "side is unknown rather than clean.",
            "The 7.3L gas V8 is the simple choice. It has had "
            "reports of lifter and cam wear, so listen for a tick "
            "at idle and ask about oil changes.",
            "The diesel costs far more to service and repair. Buy it "
            "only if you tow heavy and often.",
        ],
        "note": "Provisional: scored from the recall count. A strong "
                "work truck with a long first-year recall list. "
                "Applies to the F-350 as well.",
    },
    {
        "make": "ford", "model": "f-250",
        "years": (2017, 2022),
        "generation": "Super Duty, fourth gen, aluminum body",
        "engine": "6.2L gas V8 (7.3L from 2020) or the 6.7L Power "
                  "Stroke diesel V8; 6-speed, 10-speed from 2020",
        "reliability": 6.4,
        "maintenance": 6.0,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.1,
        "tire_set_usd": 1400,
        "risk": "Front-end shake at highway speed (the so-called "
                "death wobble) on the solid front axle, and on the "
                "diesel a failed fuel pump can take out the whole "
                "fuel system",
        "known_issues": [
            "12 recalls on the 2019 F-250, and the same count on the "
            "2019 F-350.",
            "The 2019 complaint file under this name is tiny (8), "
            "but steering (5) and suspension (4) are nearly all of "
            "it. That is the front-end shake.",
            "Drive it over 60 mph across expansion joints. Any "
            "violent shake in the wheel means steering damper, "
            "track bar or ball joint work.",
            "On a diesel, ask for fuel filter service records. "
            "Contaminated fuel is what kills the injection pump.",
        ],
        "note": "The 6.2L gas truck is the dependable one and the "
                "cheapest to own. Applies to the F-350 as well.",
    },
    {
        "make": "ford", "model": "f-250",
        "years": (2015, 2016),
        "generation": "Super Duty, third gen, steel body",
        "engine": "6.2L gas V8 or the 6.7L Power Stroke diesel V8; "
                  "6-speed automatic",
        "reliability": 6.6,
        "maintenance": 6.2,
        "annual_maintenance_usd": 920,
        "insurance_factor": 1.05,
        "tire_set_usd": 1350,
        "risk": "On the diesel a failed high-pressure fuel pump can "
                "contaminate the whole fuel system, a repair that "
                "runs to five figures",
        "known_issues": [
            "4 recalls on the 2016 F-250. The complaint file under "
            "this name is nearly empty, so the score is provisional.",
            "The steel body rusts where the later aluminum one does "
            "not. Check cab corners, rockers and the bed supports.",
            "The 6.2L gas V8 with the 6-speed is a simple, proven "
            "pairing. Most of these trucks have worked hard, so buy "
            "on service records.",
        ],
        "note": "Provisional. An old-school work truck that is easy "
                "to keep going in gas form. Applies to the F-350 as "
                "well.",
    },
    # ---------------------------------------------------------- Ranger
    {
        "make": "ford", "model": "ranger",
        "years": (2024, 2026),
        "generation": "fifth gen (second US generation)",
        "engine": "2.3L EcoBoost turbo I4 or 2.7L EcoBoost V6 (3.0L "
                  "in the Raptor); 10-speed automatic",
        "reliability": 6.2,
        "maintenance": 7.2,
        "annual_maintenance_usd": 640,
        "insurance_factor": 1.02,
        "tire_set_usd": 950,
        "risk": "13 recalls on the 2024, the first year of the "
                "redesign",
        "known_issues": [
            "13 recalls on the 2024. NHTSA returned no complaint "
            "file for it, so the complaint side is unknown.",
            "First years of a redesign are the risky ones on recent "
            "Fords. A 2025 or later should be the better buy.",
            "The 2.3L is carried over from the previous truck and "
            "is the proven engine of the three.",
        ],
        "note": "Provisional: scored from the recall count. A much "
                "nicer truck than the one it replaced, with a launch "
                "year to be careful of.",
    },
    {
        "make": "ford", "model": "ranger",
        "years": (2019, 2023),
        "generation": "fourth gen (first US return)",
        "engine": "2.3L EcoBoost turbo I4, 10-speed automatic",
        "reliability": 7.0,
        "maintenance": 7.4,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.0,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "11 recalls on the 2019, the launch year. Later years of "
            "this truck are the calmer buy.",
            "272 complaints on the 2019, led by power train (92) and "
            "electrical (41). The power train share is the 10-speed: "
            "harsh or hunting shifts.",
            "One engine and one transmission for the whole run, "
            "which makes it simple to shop and to fix.",
        ],
        "note": "A sound midsize truck with one known annoyance in "
                "the transmission. Prefer a 2021 or later.",
    },
    # -------------------------------------------------------- Explorer
    {
        "make": "ford", "model": "explorer",
        "years": (2025, 2026),
        "generation": "sixth gen, facelifted",
        "engine": "2.3L EcoBoost turbo I4 or 3.0L EcoBoost V6; "
                  "10-speed automatic, rear-drive based",
        "reliability": 5.5,
        "maintenance": 6.3,
        "annual_maintenance_usd": 780,
        "insurance_factor": 1.05,
        "tire_set_usd": 950,
        "risk": "20 recalls on the 2025, six model years into this "
                "platform",
        "known_issues": [
            "20 recalls on the 2025. A facelift should have a short "
            "list; this one does not.",
            "111 complaints on the 2025, led by electrical (25), "
            "service brakes (20) and power train (16).",
            "The big touchscreen runs nearly everything. Check every "
            "camera view and the driver-assist features on the test "
            "drive.",
        ],
        "note": "Better inside than the 2020 to 2024 car, but the "
                "recall record has not improved. Buy with warranty.",
    },
    {
        "make": "ford", "model": "explorer",
        "years": (2020, 2024),
        "generation": "sixth gen",
        "engine": "2.3L EcoBoost turbo I4, 3.0L EcoBoost V6 or 3.3L "
                  "hybrid; 10-speed automatic, rear-drive based",
        "reliability": 4.8,
        "maintenance": 6.2,
        "annual_maintenance_usd": 800,
        "insurance_factor": 1.05,
        "tire_set_usd": 950,
        "risk": "33 recalls on the 2020 and 24 on the 2022, the "
                "longest recall lists of any Ford profiled here",
        "known_issues": [
            "33 recalls on the 2020 and 24 on the 2022. Recall count "
            "does not scale with sales, so these are bad numbers.",
            "1,254 complaints on the 2020 with power train at 506, "
            "well ahead of electrical (187) and engine (118).",
            "The power train cluster covers the 10-speed and the "
            "rear axle mounting. Feel for clunks on takeoff and "
            "when shifting between drive and reverse.",
            "Check that the rear camera works every time. Camera "
            "failures have been recalled more than once.",
        ],
        "note": "The 2020 is one of the worst launch years in this "
                "file. If you want this body, buy the newest you can "
                "and confirm every recall is closed.",
    },
    {
        "make": "ford", "model": "explorer",
        "years": (2015, 2019),
        "generation": "fifth gen, front-drive based",
        "engine": "3.5L V6, 2.3L EcoBoost turbo I4 or 3.5L EcoBoost "
                  "V6; 6-speed automatic",
        "reliability": 5.8,
        "maintenance": 6.4,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.02,
        "tire_set_usd": 900,
        "risk": "The 3.5L V6 water pump is driven by the timing "
                "chain inside the engine, so a leaking pump is a "
                "major job and can ruin the engine if ignored",
        "known_issues": [
            "14 recalls on the 2017 and 1,716 complaints, with "
            "structure at 665, far ahead of everything else. The "
            "recalls include loose exterior trim and rear suspension "
            "links that can fracture, so confirm both are closed.",
            "Exhaust smell in the cabin under hard acceleration is a "
            "long-running complaint on these years. Drive it hard "
            "with the windows up and the fan on recirculate.",
            "Check the coolant level and look for coolant in the "
            "oil. Either one points at the water pump.",
            "On AWD cars the power transfer unit runs hot and cooks "
            "its fluid. Ask if it has ever been changed.",
        ],
        "note": "Roomy and cheap used, with two expensive weak "
                "points. A documented water pump replacement is "
                "worth paying extra for.",
    },
    # ---------------------------------------------------------- Bronco
    {
        "make": "ford", "model": "bronco",
        "years": (2021, 2026),
        "generation": "sixth gen",
        "engine": "2.3L EcoBoost turbo I4 or 2.7L EcoBoost V6 (3.0L "
                  "in the Raptor); 7-speed manual or 10-speed auto",
        "reliability": 5.5,
        "maintenance": 6.5,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.12,
        "tire_set_usd": 1200,
        "risk": "20 recalls on the 2021 and 18 on the 2023, and "
                "early 2.7L V6 engines had valve failures that "
                "needed a replacement engine",
        "known_issues": [
            "20 recalls on the 2021 and 18 on the 2023. The count "
            "has not come down as the truck has aged.",
            "232 complaints on the 2021 with engine on top at 70. "
            "On a 2021 2.7L, ask whether the engine was replaced.",
            "236 complaints on the 2023 with visibility and wipers "
            "at 91, a lopsided share that points at one defect.",
            "Removable roofs leak and whistle. Check the headliner "
            "and carpets for water marks.",
        ],
        "note": "Bought for how it looks and what it can do "
                "off-road, not for dependability. The 2.3L is the "
                "safer engine.",
    },
    # ------------------------------------------------------ Expedition
    {
        "make": "ford", "model": "expedition",
        "years": (2025, 2026),
        "generation": "fifth gen",
        "engine": "3.5L EcoBoost twin-turbo V6, 10-speed automatic",
        "reliability": 6.0,
        "maintenance": 6.2,
        "annual_maintenance_usd": 850,
        "insurance_factor": 1.12,
        "tire_set_usd": 1150,
        "risk": None,
        "known_issues": [
            "6 recalls on the 2025 already, the first year of the "
            "redesign, and 39 complaints with no single component "
            "standing out.",
            "Engine and transmission carry over from the previous "
            "truck, so the cam phaser and 10-speed history below "
            "still applies.",
            "Too new for a long-term read. Keep it under factory "
            "warranty.",
        ],
        "note": "Provisional: a first-year redesign with a short "
                "record so far. Nothing alarming yet, nothing "
                "proven either.",
    },
    {
        "make": "ford", "model": "expedition",
        "years": (2018, 2024),
        "generation": "fourth gen, aluminum body",
        "engine": "3.5L EcoBoost twin-turbo V6, 10-speed automatic",
        "reliability": 5.9,
        "maintenance": 6.2,
        "annual_maintenance_usd": 870,
        "insurance_factor": 1.1,
        "tire_set_usd": 1100,
        "risk": "Cam phaser rattle on the 3.5L EcoBoost and harsh "
                "shifting on the 10-speed are both common on the "
                "2018 to 2020 trucks and costly out of warranty",
        "known_issues": [
            "11 recalls on the 2019 and 12 on the 2022.",
            "533 complaints on the 2019, led by power train (224), "
            "seat belts (119) and engine (108). The power train "
            "share is the 10-speed.",
            "Listen for a rattle in the first two seconds of a cold "
            "start. That is the cam phasers, and the repair means "
            "opening the front of the engine.",
            "By the 2022 the file is down to 119 complaints with no "
            "dominant component. Later years are the better buy.",
        ],
        "note": "Prefer a 2021 or later. The early trucks have a "
                "transmission and timing problem that the later "
                "ones mostly left behind.",
    },
    {
        "make": "ford", "model": "expedition",
        "years": (2015, 2017),
        "generation": "third gen, facelifted, steel body",
        "engine": "3.5L EcoBoost twin-turbo V6, 6-speed automatic",
        "reliability": 6.7,
        "maintenance": 6.4,
        "annual_maintenance_usd": 840,
        "insurance_factor": 1.05,
        "tire_set_usd": 1050,
        "risk": None,
        "known_issues": [
            "3 recalls on the 2016, a short list for a Ford.",
            "217 complaints on the 2016, led by service brakes (52), "
            "engine (37) and power train (36). Check for a hard or "
            "sinking brake pedal.",
            "The older 3.5L EcoBoost stretches timing chains if oil "
            "changes were skipped. Ask for records.",
        ],
        "note": "An old design by the end, which is why it is "
                "calmer than the truck that replaced it. The 6-speed "
                "is the more trusted transmission.",
    },
    # ------------------------------------------------------------ Edge
    {
        "make": "ford", "model": "edge",
        "years": (2019, 2024),
        "generation": "second gen, facelifted",
        "engine": "2.0L EcoBoost turbo I4 or 2.7L EcoBoost V6 (ST); "
                  "8-speed automatic",
        "reliability": 6.4,
        "maintenance": 7.0,
        "annual_maintenance_usd": 660,
        "insurance_factor": 1.0,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "4 recalls on the 2020, a short list by recent Ford "
            "standards.",
            "331 complaints on the 2020 with power train at 193, "
            "more than half the file. That is the 8-speed "
            "automatic: harsh shifts, slipping and warning lights.",
            "Drive it long enough to get the transmission fully "
            "warm, and ask if it has had a software update or a "
            "replacement.",
        ],
        "note": "Fewer recalls than most Fords of its age, with one "
                "clear weak point in the transmission. Fine if it "
                "shifts cleanly.",
    },
    {
        "make": "ford", "model": "edge",
        "years": (2015, 2018),
        "generation": "second gen, pre-facelift",
        "engine": "2.0L EcoBoost turbo I4, 3.5L V6 or 2.7L EcoBoost "
                  "V6 (Sport); 6-speed automatic",
        "reliability": 5.6,
        "maintenance": 6.9,
        "annual_maintenance_usd": 700,
        "insurance_factor": 0.98,
        "tire_set_usd": 850,
        "risk": "Coolant leaks into the cylinders on the 2.0L "
                "EcoBoost, and the usual fix is a replacement engine",
        "known_issues": [
            "7 recalls on the 2016 and 932 complaints, with engine "
            "at 337 and engine cooling another 91.",
            "Service brakes are second at 176. Check the pedal feel "
            "and look at the front brake hoses for cracks or leaks.",
            "Check the coolant level cold and look for white smoke "
            "at startup on any 2.0L car.",
            "The 3.5L non-turbo V6 avoids the coolant problem and "
            "is the one to look for.",
        ],
        "note": "Comfortable and cheap used. The 2.0L turbo is the "
                "gamble; the 3.5L V6 is the sensible pick.",
    },
    # --------------------------------------------------------- Mustang
    {
        "make": "ford", "model": "mustang",
        "years": (2024, 2026),
        "generation": "seventh gen (S650)",
        "engine": "2.3L EcoBoost turbo I4 or 5.0L V8; 6-speed "
                  "manual (V8) or 10-speed automatic",
        "reliability": 6.6,
        "maintenance": 7.0,
        "annual_maintenance_usd": 720,
        "insurance_factor": 1.3,
        "tire_set_usd": 1050,
        "risk": None,
        "known_issues": [
            "12 recalls on the 2024, the first year of this body.",
            "85 complaints on the 2024 with electrical at 41, close "
            "to half. The new all-screen dash is where the trouble "
            "is, not the engines.",
            "Both engines carry over from the previous car and are "
            "well understood.",
            "Insurance is the real running cost. Get a quote before "
            "you fall for one.",
        ],
        "note": "Proven engines under a new body with first-year "
                "electrical bugs. A 2025 or later is the safer buy.",
    },
    {
        "make": "ford", "model": "mustang",
        "years": (2015, 2023),
        "generation": "sixth gen (S550)",
        "engine": "2.3L EcoBoost turbo I4, 5.0L V8 or (to 2017) "
                  "3.7L V6; 6-speed manual, 6-speed or 10-speed auto",
        "reliability": 7.3,
        "maintenance": 7.2,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.3,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "6 recalls on the 2017 and 8 on the 2020, modest for a "
            "Ford.",
            "269 complaints on the 2017, led by the rear camera "
            "(64), structure (41) and door latches (29). Engine is "
            "only 27. The drivetrain is not the weak point.",
            "Many have been driven hard or modified. Look for an "
            "aftermarket tune, mismatched tires and curb damage, "
            "and prefer an unmodified car.",
            "On 2018 and later V8s, ask about oil consumption "
            "between changes.",
        ],
        "note": "A dependable sports car if you find one that was "
                "not abused. Insurance costs more than repairs.",
    },
    # ---------------------------------------------------- Mustang Mach-E
    {
        "make": "ford", "model": "mustang mach-e",
        "years": (2021, 2026),
        "generation": "first gen, battery electric",
        "engine": "single-motor RWD or dual-motor AWD electric; "
                  "standard or extended-range battery",
        "reliability": 6.2,
        "maintenance": 6.8,
        "annual_maintenance_usd": 380,
        "insurance_factor": 1.2,
        "tire_set_usd": 1000,
        "risk": "13 recalls on the 2021, and early cars had "
                "high-voltage battery contactors that overheat and "
                "cut power while driving",
        "known_issues": [
            "13 recalls on the 2021 and 6 on the 2023. The later "
            "cars are clearly calmer.",
            "353 complaints on the 2021 with electrical at 156 and "
            "forward collision avoidance at 106. The 2023 file is "
            "129, again led by electrical (53).",
            "Loss of power after fast charging or hard acceleration "
            "is the contactor fault. Confirm that recall is closed "
            "on a 2021 or 2022.",
            "Maintenance is low (no oil, little brake wear). Ask "
            "for a battery health report and check that the eight "
            "year battery warranty is still running.",
        ],
        "note": "A good electric crossover once past the first two "
                "years. Buy a 2023 or later, or a 2021 to 2022 with "
                "the battery recalls done.",
    },
    # ---------------------------------------------------------- Fusion
    {
        "make": "ford", "model": "fusion",
        "years": (2017, 2020),
        "generation": "second gen, facelifted",
        "engine": "2.5L I4, 1.5L or 2.0L EcoBoost turbo I4, or the "
                  "2.0L hybrid; 6-speed automatic (eCVT on hybrid)",
        "reliability": 6.2,
        "maintenance": 7.5,
        "annual_maintenance_usd": 600,
        "insurance_factor": 1.0,
        "tire_set_usd": 700,
        "risk": "Coolant leaks into the cylinders on the 1.5L "
                "EcoBoost (and less often the 2.0L), and the usual "
                "fix is a replacement engine",
        "known_issues": [
            "Only 2 recalls on the 2018, but 445 complaints with "
            "engine at 206 and engine cooling another 88. The "
            "recall list does not cover the engine fault.",
            "Check the coolant level cold and look for white smoke "
            "at startup on any EcoBoost car.",
            "The base 2.5L and the hybrid are the dependable "
            "versions and worth seeking out.",
        ],
        "note": "Two different cars under one name. The 2.5L and "
                "the hybrid are solid, cheap sedans; the 1.5L turbo "
                "is the one to skip.",
    },
    {
        "make": "ford", "model": "fusion",
        "years": (2015, 2016),
        "generation": "second gen, pre-facelift",
        "engine": "2.5L I4, 1.5L or 2.0L EcoBoost turbo I4, or the "
                  "2.0L hybrid; 6-speed automatic (eCVT on hybrid)",
        "reliability": 5.8,
        "maintenance": 7.5,
        "annual_maintenance_usd": 620,
        "insurance_factor": 0.98,
        "tire_set_usd": 700,
        "risk": "Coolant leaks into the cylinders on the 1.5L "
                "EcoBoost, and the usual fix is a replacement engine",
        "known_issues": [
            "13 recalls on the 2015, a long list for a sedan.",
            "1,066 complaints on the 2015, led by engine (280), "
            "steering (181) and power train (157).",
            "Steering that high is unusual. Feel for a wheel that "
            "goes heavy or loose, and check the steering recalls "
            "are closed on the VIN.",
            "The base 2.5L and the hybrid avoid the turbo engine "
            "trouble.",
        ],
        "note": "More recalls and more steering complaints than the "
                "later cars. Buy the 2.5L or the hybrid, and only "
                "with the recall work done.",
    },
    # -------------------------------------------------------- EcoSport
    {
        "make": "ford", "model": "ecosport",
        "years": (2018, 2022),
        "generation": "second gen (only US generation)",
        "engine": "1.0L EcoBoost turbo I3 (FWD) or 2.0L I4 (AWD); "
                  "6-speed automatic",
        "reliability": 4.6,
        "maintenance": 7.0,
        "annual_maintenance_usd": 640,
        "insurance_factor": 0.98,
        "tire_set_usd": 600,
        "risk": "Engine failures dominate the complaint file: sudden "
                "loss of oil pressure, with a replacement engine as "
                "the usual outcome",
        "known_issues": [
            "728 complaints on the 2018, with engine at 357 and "
            "engine cooling at 311. Almost the whole file is one "
            "problem.",
            "The 2020 is the same shape: 404 complaints, engine 174 "
            "and engine cooling 179, plus 9 fires.",
            "Only 2 recalls on the 2018 and 3 on the 2020, so do "
            "not read the short recall list as a clean record. One "
            "of them is an engine oil campaign: confirm it is done.",
            "An oil pressure warning means stop at once. Ask for "
            "proof of on-time oil changes with the right oil, and "
            "whether the engine has been replaced.",
        ],
        "note": "Cheap for a reason. The complaint file is among "
                "the most lopsided here and it points at the engine. "
                "Avoid unless the engine is new with paperwork.",
    },
    # -------------------------------------------------- Transit Connect
    {
        "make": "ford", "model": "transit connect",
        "years": (2015, 2023),
        "generation": "second gen",
        "engine": "2.5L I4 with 6-speed automatic; 2.0L I4 with "
                  "8-speed automatic from 2019",
        "reliability": 6.6,
        "maintenance": 7.3,
        "annual_maintenance_usd": 640,
        "insurance_factor": 1.0,
        "tire_set_usd": 650,
        "risk": None,
        "known_issues": [
            "10 recalls on the 2016 and 8 on the 2020. Not short, "
            "so run the VIN.",
            "104 complaints on the 2016 spread evenly across brakes "
            "(17), structure (14), visibility (14) and electrical "
            "(14). No single weak point stands out.",
            "On the 2020 the file is small (32) with power train "
            "on top at 10. That is the 8-speed, so check it shifts "
            "cleanly.",
            "Most were work vans. Judge the individual van: sliding "
            "door tracks, rear door hinges and service history.",
        ],
        "note": "A simple, useful small van with no dominant fault. "
                "The 2.5L with the 6-speed is the one to trust.",
    },
    # ----------------------------------------------------------- Focus
    {
        "make": "ford", "model": "focus",
        "years": (2015, 2018),
        "generation": "third gen, facelifted",
        "engine": "2.0L I4 or 1.0L EcoBoost turbo I3; 6-speed "
                  "dual-clutch automatic or manual",
        "reliability": 4.5,
        "maintenance": 7.2,
        "annual_maintenance_usd": 680,
        "insurance_factor": 1.0,
        "tire_set_usd": 620,
        "risk": "The dual-clutch automatic shudders, slips and "
                "fails, and clutch packs and control modules are "
                "often replaced more than once",
        "known_issues": [
            "10 recalls on the 2016 and 1,196 complaints, with power "
            "train at 678. More than half the file is the "
            "transmission.",
            "On an automatic, pull away gently from a stop on a "
            "slight hill. Any shudder or hesitation is the fault.",
            "The manual cars (including the ST and RS) do not have "
            "this problem and are a different proposition.",
        ],
        "note": "Avoid the automatic. With a manual gearbox it is a "
                "decent, cheap small car.",
    },
    # ---------------------------------------------------------- Fiesta
    {
        "make": "ford", "model": "fiesta",
        "years": (2015, 2019),
        "generation": "sixth gen",
        "engine": "1.6L I4 or 1.0L EcoBoost turbo I3; 6-speed "
                  "dual-clutch automatic or manual",
        "reliability": 4.6,
        "maintenance": 7.3,
        "annual_maintenance_usd": 650,
        "insurance_factor": 0.98,
        "tire_set_usd": 560,
        "risk": "Same dual-clutch automatic as the Focus: shudder, "
                "slipping and repeat clutch replacements",
        "known_issues": [
            "179 complaints on the 2016 with power train at 101, "
            "more than half the file.",
            "NHTSA's recall endpoint returned nothing for the 2016 "
            "Fiesta, which is not the same as no recalls. Run the "
            "VIN.",
            "The manual cars, including the ST, avoid the "
            "transmission problem.",
        ],
        "note": "Provisional on recalls. Avoid the automatic; the "
                "manual is a cheap and cheerful runabout.",
    },
    # ---------------------------------------------------------- Taurus
    {
        "make": "ford", "model": "taurus",
        "years": (2015, 2019),
        "generation": "sixth gen",
        "engine": "3.5L V6, 2.0L EcoBoost turbo I4 or 3.5L EcoBoost "
                  "V6 (SHO); 6-speed automatic",
        "reliability": 7.0,
        "maintenance": 6.8,
        "annual_maintenance_usd": 680,
        "insurance_factor": 1.0,
        "tire_set_usd": 800,
        "risk": "The 3.5L V6 water pump is driven by the timing "
                "chain inside the engine, so a leaking pump is a "
                "major job and can ruin the engine if ignored",
        "known_issues": [
            "4 recalls on the 2017 and only 44 complaints, with "
            "electrical on top at 11. A quiet file.",
            "Check the coolant level and look for coolant in the "
            "oil. Budget for a water pump on a high-mileage car "
            "with no record of one.",
            "Many are former police or fleet cars. Idle hours are "
            "hard on an engine, so check the history.",
        ],
        "note": "A big, old-fashioned sedan with a calm record and "
                "one expensive known job. Good value if the water "
                "pump has been done.",
    },
]

# A listings feed may call the Super Duty trucks by several names. The
# F-250 and F-350 share engines, transmissions and front ends, so the
# same profiles are listed under each name.
for _p in [p for p in PROFILES if p["model"] == "f-250"]:
    for _name in ("f-250 super duty", "f-350", "f-350 super duty"):
        PROFILES.append(dict(_p, model=_name))
del _p, _name
