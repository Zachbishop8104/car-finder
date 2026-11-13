"""Reliability profiles: Jeep. The format and the caveats on reading
these numbers are in carfinder/reliability.py."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "jeep", "model": "grand cherokee",
        "years": (2015, 2016),
        "generation": "WK2 fourth gen, early facelift years",
        "engine": "3.6L Pentastar V6, 5.7L Hemi V8 or 3.0L EcoDiesel, "
                  "8-speed automatic",
        "reliability": 5.3,
        "maintenance": 6.3,
        "annual_maintenance_usd": 800,
        "insurance_factor": 1.02,
        "tire_set_usd": 880,
        "risk": "Ten recalls on the 2015 and 1,372 complaints with 130 "
                "crash reports, the years of the rollaway shifter "
                "recall (16V240000)",
        "known_issues": [
            "Ten recall campaigns on the 2015, including 16V240000 on "
            "the automatic transmission controls. Run the VIN and "
            "confirm every one is closed.",
            "1,372 complaints on the 2015, led by power train (353) "
            "and seats (317). The seat entries are mostly active "
            "head restraints firing without a crash.",
            "Quadra-Lift air suspension is expensive when it leaks. "
            "Watch the car sit overnight, or buy one on steel springs.",
            "The 3.0L EcoDiesel carries its own engine and fuel-pump "
            "campaigns (20V475000, 22V406000). Skip it unless the "
            "service history is complete.",
        ],
        "note": "The weakest WK2 years. A 2017 or later of the same "
                "generation has a clearly shorter file for similar "
                "money.",
    },
    {
        "make": "jeep", "model": "grand cherokee",
        "years": (2017, 2021),
        "generation": "WK2 fourth gen, late years",
        "engine": "3.6L Pentastar V6 or 5.7L Hemi V8, 8-speed "
                  "automatic",
        "reliability": 6.0,
        "maintenance": 6.4,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.03,
        "tire_set_usd": 880,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2017 and seven on the 2019. Ordinary "
            "for a Jeep, and far below the generation that replaced "
            "it.",
            "371 complaints on the 2019, led by service brakes (117) "
            "and electrical (84). Two brake campaigns cover it "
            "(22V426000, 24V838000); check both are done.",
            "The 5.7L Hemi is known for lifter and camshaft wear. A "
            "ticking idle on a V8 car is a reason to walk away.",
            "Listen for a tick from the 3.6L too (rocker arms), and "
            "check the oil filter housing for leaks.",
        ],
        "note": "The Grand Cherokee to buy used. By the end of its run "
                "the WK2 was a sorted design, and the V6 with steel "
                "springs is the low-risk version.",
    },
    {
        "make": "jeep", "model": "grand cherokee",
        "years": (2022, 2024),
        "generation": "WL fifth gen",
        "engine": "3.6L Pentastar V6, 2.0L turbo I4 or the 4xe plug-in "
                  "hybrid, 8-speed automatic",
        "reliability": 4.8,
        "maintenance": 5.8,
        "annual_maintenance_usd": 860,
        "insurance_factor": 1.05,
        "tire_set_usd": 900,
        "risk": "Twenty recalls on the 2023 and 378 complaints, 176 of "
                "them electrical: the worst combined record of any "
                "vehicle profiled here",
        "known_issues": [
            "Twenty recall campaigns on the 2023, spanning the "
            "steering column, rear coil springs, backup camera and "
            "more. Recall count is volume-independent; twenty is "
            "extraordinary.",
            "378 complaints with electrical at 176 (47% of the file), "
            "engine 81 and suspension 58.",
            "The 4xe plug-in adds a high-voltage system to all of "
            "that, and its repairs are dealer-only.",
            "Depreciated 15.2%/yr in one Michigan market (Aug 2026) on top.",
            "It is a genuinely good vehicle to drive and sit in. The "
            "ownership record is the problem.",
        ],
        "note": "Avoid. Twenty recalls and a 47%-electrical complaint "
                "file is the clearest 'no' among these profiles.",
    },
    {
        "make": "jeep", "model": "grand cherokee",
        "years": (2025, 2026),
        "generation": "WL fifth gen, later years",
        "engine": "3.6L Pentastar V6, or the 2.0L Hurricane turbo I4 "
                  "added for 2026; 8-speed automatic",
        "reliability": 5.0,
        "maintenance": 5.8,
        "annual_maintenance_usd": 860,
        "insurance_factor": 1.06,
        "tire_set_usd": 920,
        "risk": "Six recalls on the 2026 already and four on the 2025, "
                "on a design whose 2023 collected twenty",
        "known_issues": [
            "Four recalls on the 2025 and six on the 2026, with both "
            "years still young enough to collect more.",
            "37 complaints on the 2026 so far, 25 of them engine. "
            "That is the first year of the new four-cylinder turbo, "
            "so favor the V6.",
            "81 complaints on the 2025, led by electrical (32) and "
            "engine (24): the same shape as the 2022 to 2024 cars.",
        ],
        "note": "Slightly better than the 2022 to 2024 cars on paper, "
                "but it is the same vehicle and the file is still "
                "filling. Buy with the full warranty or not at all.",
    },
    {
        "make": "jeep", "model": "grand cherokee 4xe",
        "years": (2022, 2026),
        "generation": "WL fifth gen plug-in hybrid",
        "engine": "2.0L turbo I4 plug-in hybrid, 17 kWh battery, "
                  "8-speed automatic, 4WD",
        "reliability": 3.9,
        "maintenance": 4.6,
        "annual_maintenance_usd": 900,
        "insurance_factor": 1.12,
        "tire_set_usd": 950,
        "risk": "Traction-battery recall on the 2024 (24V720000) and a "
                "2023 plug-in complaint file that is 48% electrical, "
                "with three fire reports",
        "known_issues": [
            "97 complaints on the 2023 plug-in, 47 of them electrical "
            "and three reporting fire.",
            "Two recalls filed on the 2024 4xe by name: 24V720000 "
            "(traction battery) and 25V766000 (engine). The shared "
            "Grand Cherokee campaigns apply on top.",
            "Ask the dealer whether the battery recall remedy is "
            "done. Until it is, the usual instruction is to park "
            "outside and not charge.",
            "Out of warranty, high-voltage repairs are dealer-only "
            "and priced accordingly. Budget for an extended plan.",
        ],
        "note": "Avoid. It takes the worst-recorded Jeep and adds a "
                "plug-in system with its own battery recall.",
    },
    {
        "make": "jeep", "model": "grand cherokee l",
        "years": (2021, 2026),
        "generation": "WL fifth gen, three-row",
        "engine": "3.6L Pentastar V6 or 5.7L Hemi V8 (through 2023), "
                  "8-speed automatic",
        "reliability": 5.3,
        "maintenance": 5.8,
        "annual_maintenance_usd": 870,
        "insurance_factor": 1.06,
        "tire_set_usd": 950,
        "risk": "Two separate rear coil spring recalls (26V051000 and "
                "26V562000), and suspension is 39 of 100 complaints "
                "on the 2023",
        "known_issues": [
            "Four recalls on the 2021, six on the 2023 and two on "
            "the 2025. NHTSA files the L apart from the two-row, "
            "whose 2023 carries twenty.",
            "100 complaints on the 2023: suspension 39, electrical "
            "24, forward collision avoidance 12. Confirm both rear "
            "spring campaigns are closed.",
            "97 complaints on the 2021, led by electrical (28), "
            "steering (20) and collision-avoidance false alarms (20).",
            "Same screens and electronics as the two-row. Test every "
            "display, camera and power feature before you sign.",
        ],
        "note": "Shorter file than the two-row Grand Cherokee but the "
                "same hardware. A cautious buy, and only with the V6.",
    },
    {
        "make": "jeep", "model": "wrangler",
        "years": (2015, 2017),
        "generation": "JK",
        "engine": "3.6L Pentastar V6, 5-speed automatic or 6-speed "
                  "manual, part-time 4WD",
        "reliability": 6.3,
        "maintenance": 7.0,
        "annual_maintenance_usd": 700,
        "insurance_factor": 0.98,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "Five recalls on the 2016, four of them air bag "
            "campaigns. Check the passenger inflator recall "
            "(19V018000) is closed.",
            "465 complaints on the 2016, led by service brakes (139), "
            "engine (88) and air bags (78).",
            "Solid front axle: worn steering parts cause a violent "
            "shimmy at highway speed. Drive it at 60 mph over a "
            "rough patch.",
            "Most are modified. Lifts and oversize tires wear ball "
            "joints and gears; a stock one is worth paying more for.",
        ],
        "note": "Crude and thirsty, but simple, and parts are "
                "everywhere. The late JK is the lowest-risk used "
                "Wrangler.",
    },
    {
        "make": "jeep", "model": "wrangler",
        "years": (2018, 2023),
        "generation": "JL (some 2018s are the old JK; check the VIN)",
        "engine": "3.6L Pentastar V6 or 2.0L turbo I4, 8-speed "
                  "automatic or 6-speed manual; 3.0L diesel optional",
        "reliability": 4.9,
        "maintenance": 6.5,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.0,
        "tire_set_usd": 1100,
        "risk": "Steering is 1,117 of 1,830 complaints on the 2018 "
                "(61%), and the 2018, 2021 and 2023 carry fourteen, "
                "fifteen and fourteen recalls",
        "known_issues": [
            "Fourteen recalls on the 2018 and fifteen on the 2021, "
            "including frame welds (18V675000) and three clutch "
            "campaigns on the manual.",
            "1,830 complaints on the 2018 with steering at 1,117. "
            "Loose, wandering steering and highway shimmy are the "
            "pattern; test drive at speed.",
            "962 complaints on the 2021: electrical 310, steering "
            "255, engine 224. Check the start-stop auxiliary battery "
            "and every dash warning.",
            "Manual cars: confirm the clutch recalls (21V028000, "
            "23V116000) are done. They concern an overheating "
            "pressure plate.",
        ],
        "note": "Holds its value and nothing else does what it does, "
                "but the record is poor. Later years of the run are "
                "better than 2018.",
    },
    {
        "make": "jeep", "model": "wrangler",
        "years": (2024, 2026),
        "generation": "JL facelift",
        "engine": "3.6L Pentastar V6 or 2.0L turbo I4, 8-speed "
                  "automatic or 6-speed manual",
        "reliability": 5.2,
        "maintenance": 6.5,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.02,
        "tire_set_usd": 1150,
        "risk": "Eleven recalls on the 2024 already, covering tail "
                "lights, wiring, the instrument cluster and the "
                "power steering pump",
        "known_issues": [
            "Eleven recalls on the 2024 and four on the 2025. The "
            "facelift did not shorten the list.",
            "The complaints endpoint returned an error for 2024 and "
            "2025, so there is no component breakdown behind this "
            "score.",
            "Steering pump recall 26V363000 reaches back to 2021 "
            "cars as well. Confirm it is closed.",
            "The new 12.3-inch screen runs most functions. Check it "
            "boots fast and the cameras work.",
        ],
        "note": "Provisional: scored on recall count and the earlier "
                "JL record. Expect the same ownership experience as "
                "a 2021 to 2023.",
    },
    {
        "make": "jeep", "model": "wrangler 4xe",
        "years": (2021, 2026),
        "generation": "JL plug-in hybrid",
        "engine": "2.0L turbo I4 plug-in hybrid, 17 kWh battery, "
                  "8-speed automatic, 4WD",
        "reliability": 3.9,
        "maintenance": 4.8,
        "annual_maintenance_usd": 850,
        "insurance_factor": 1.08,
        "tire_set_usd": 1150,
        "risk": "Four separate traction-battery recall campaigns sit "
                "on the 2023 Wrangler file (22V768000, 23V303000, "
                "23V787000, 25V741000)",
        "known_issues": [
            "NHTSA files the 4xe under Wrangler. The 2023 carries "
            "fourteen recalls, four of them on the high-voltage "
            "battery.",
            "378 complaints on the 2023 Wrangler: electrical 201 "
            "(53%), engine 109, fuel and propulsion 66.",
            "Ask for proof the latest battery recall is closed. Open "
            "battery recalls usually mean park outside and do not "
            "charge.",
            "Electric range is about 21 miles. Without home charging "
            "it is a heavier, thirstier Wrangler.",
        ],
        "note": "Avoid unless it is under warranty and every battery "
                "campaign is closed. The gas Wrangler is the safer "
                "buy.",
    },
    {
        "make": "jeep", "model": "gladiator",
        "years": (2020, 2023),
        "generation": "JT first gen",
        "engine": "3.6L Pentastar V6, 8-speed automatic or 6-speed "
                  "manual; 3.0L diesel 2021 to 2023",
        "reliability": 5.4,
        "maintenance": 6.5,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.02,
        "tire_set_usd": 1100,
        "risk": "Steering is 182 of 485 complaints on the 2020 (38%), "
                "the same loose-steering pattern as the Wrangler it "
                "is built from",
        "known_issues": [
            "Seven recalls on the 2020 and six on the 2023, including "
            "the driveshaft (19V636000) and three clutch campaigns "
            "on the manual.",
            "485 complaints on the 2020: electrical 183 and steering "
            "182 lead. Drive it on the highway and feel for wander.",
            "The 2023 is much quieter at 57 complaints. Later years "
            "of this run are the better buy.",
            "Diesel cars have a fuel-pump recall (23V263000). "
            "Confirm it is done.",
        ],
        "note": "A Wrangler with a bed, and a Wrangler's record. Buy "
                "a 2022 or 2023 over a 2020.",
    },
    {
        "make": "jeep", "model": "gladiator",
        "years": (2024, 2026),
        "generation": "JT facelift",
        "engine": "3.6L Pentastar V6, 8-speed automatic (6-speed "
                  "manual on the 2024 only)",
        "reliability": 6.0,
        "maintenance": 6.6,
        "annual_maintenance_usd": 740,
        "insurance_factor": 1.03,
        "tire_set_usd": 1150,
        "risk": None,
        "known_issues": [
            "One recall on the 2025 (26V363000, power steering pump) "
            "and 18 complaints with no component leading.",
            "The diesel was dropped for 2024 and the manual gearbox "
            "for 2025, which removes the two most recalled parts of "
            "the earlier truck.",
            "Still a solid-axle Jeep: check for highway wander and "
            "for water leaks around the roof panels.",
        ],
        "note": "The cleanest Gladiator years so far. The file is "
                "young, so treat the score as a floor that still has "
                "to hold.",
    },
    {
        "make": "jeep", "model": "cherokee",
        "years": (2015, 2018),
        "generation": "KL, before the facelift",
        "engine": "2.4L Tigershark I4 or 3.2L Pentastar V6, 9-speed "
                  "automatic",
        "reliability": 4.2,
        "maintenance": 6.2,
        "annual_maintenance_usd": 780,
        "insurance_factor": 1.0,
        "tire_set_usd": 760,
        "risk": "Power train is 1,007 of 1,794 complaints on the 2015 "
                "(56%): the 9-speed automatic shifts harshly, drops "
                "to neutral and fails",
        "known_issues": [
            "Eleven recalls on the 2015 and six on the 2017, "
            "including the transmission (16V529000) and the rear "
            "differential (20V343000).",
            "1,794 complaints on the 2015 and 1,343 on the 2017, "
            "both led by power train. The problem did not go away "
            "with updates.",
            "The 2.4L burns oil and can stall when it runs low. "
            "Check the dipstick on the lot, and prefer the V6.",
            "Drive it cold and in traffic. Any flare, bang or "
            "hesitation between gears is the fault, not a quirk.",
        ],
        "note": "Avoid. One of the most complained-about drivetrains "
                "of its decade, and cheap prices reflect it.",
    },
    {
        "make": "jeep", "model": "cherokee",
        "years": (2019, 2023),
        "generation": "KL facelift",
        "engine": "2.4L Tigershark I4, 3.2L V6 or 2.0L turbo I4, "
                  "9-speed automatic",
        "reliability": 4.8,
        "maintenance": 6.2,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.0,
        "tire_set_usd": 780,
        "risk": "Power train is 841 of 1,685 complaints on the 2019 "
                "(50%), and two later power train recalls (25V011000, "
                "26V290000) cover these years",
        "known_issues": [
            "Eleven recalls on the 2019. The 2021 is down to four, "
            "with 184 complaints, but 110 of those are still power "
            "train.",
            "4WD cars: the power transfer unit can fail and leave "
            "the car without drive or without park. Confirm the "
            "power train recalls are closed.",
            "Engine is 460 complaints on the 2019. The 2.4L uses "
            "oil; the V6 is the engine to have.",
            "Production ended with the 2023, so the newest ones are "
            "already orphans for trim and body parts.",
        ],
        "note": "Better than the early KL, still below average. A "
                "2021 or later V6 is the only version worth a look.",
    },
    {
        "make": "jeep", "model": "cherokee",
        "years": (2026, 2026),
        "generation": "KM, all-new hybrid",
        "engine": "1.6L turbo I4 hybrid, AWD",
        "reliability": 5.5,
        "maintenance": 6.0,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.04,
        "tire_set_usd": 820,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2026 in its first year: brake "
            "lights, stability control, backup camera and tire "
            "pressure monitoring.",
            "Only 10 complaints so far, which says nothing either "
            "way on a car this new.",
            "First year of a new platform and a new hybrid system. "
            "A long powertrain warranty matters more than the trim.",
        ],
        "note": "Provisional. Shares nothing but the name with the "
                "old Cherokee; four recalls in year one is not an "
                "encouraging start.",
    },
    {
        "make": "jeep", "model": "compass",
        "years": (2015, 2016),
        "generation": "MK first gen",
        "engine": "2.0L or 2.4L World I4, CVT or 6-speed automatic",
        "reliability": 5.2,
        "maintenance": 7.2,
        "annual_maintenance_usd": 640,
        "insurance_factor": 0.98,
        "tire_set_usd": 640,
        "risk": None,
        "known_issues": [
            "One recall on the 2016 (16V907000, engine) but 294 "
            "complaints, 136 of them engine: stalling and loss of "
            "power.",
            "Avoid the CVT. The 6-speed automatic fitted to most "
            "2.4L cars is the durable choice.",
            "Check front suspension bushings and ball joints, and "
            "look for water in the footwells and cargo area.",
        ],
        "note": "An old, cheap design that feels it. Fine as basic "
                "transport with the 6-speed automatic, nothing more.",
    },
    {
        "make": "jeep", "model": "compass",
        "years": (2017, 2021),
        "generation": "MP second gen (a few 2017s are the old MK)",
        "engine": "2.4L Tigershark I4, 6-speed or 9-speed automatic; "
                  "AWD available",
        "reliability": 4.9,
        "maintenance": 6.6,
        "annual_maintenance_usd": 680,
        "insurance_factor": 1.0,
        "tire_set_usd": 700,
        "risk": "Engine is 477 of 952 complaints on the 2018 (50%): "
                "the 2.4L burns oil and stalls when the level drops",
        "known_issues": [
            "Six recalls on the 2018 and 952 complaints, with engine "
            "(477) and electrical (382) far ahead of the rest.",
            "Check the oil level before the test drive. A low "
            "dipstick on a car that was just serviced is the "
            "warning sign.",
            "The 2020 is calmer (one recall, 143 complaints) but "
            "engine still leads at 79.",
            "Start-stop faults and dead batteries are common. Ask "
            "when the battery was last replaced.",
        ],
        "note": "Skip these years. The 2023 and later 2.0L turbo "
                "cars fix the engine that fills this file.",
    },
    {
        "make": "jeep", "model": "compass",
        "years": (2022, 2025),
        "generation": "MP facelift",
        "engine": "2.0L turbo I4 (2023+) or 2.4L Tigershark, 8-speed "
                  "automatic; AWD available",
        "reliability": 6.4,
        "maintenance": 6.8,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.0,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2023 and 45 complaints, led by "
            "electrical (13). Unremarkable, and dramatically better "
            "than its Grand Cherokee sibling.",
            "The 2023 switch to the 2.0L turbo fixed the old 2.4L's "
            "worst trait, which was being far too slow.",
            "Depreciated 14.6%/yr in one Michigan market (Aug 2026).",
            "Interior is cramped for the exterior size.",
        ],
        "note": "The only Stellantis vehicle here that survives its "
                "own data. Mid-pack on everything.",
    },
    {
        "make": "jeep", "model": "compass",
        "years": (2026, 2026),
        "generation": "MP facelift, final year",
        "engine": "2.0L turbo I4, 8-speed automatic, AWD",
        "reliability": 6.4,
        "maintenance": 6.8,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.0,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "One recall on the 2026 (26V531000, backup camera) and "
            "five complaints so far.",
            "Mechanically the same car as the 2023 to 2025, so it "
            "inherits that score.",
            "Interior is cramped for the exterior size.",
        ],
        "note": "A carry-over year of a now-sorted design. Buy on "
                "price; the 2025 is the same car.",
    },
    {
        "make": "jeep", "model": "renegade",
        "years": (2015, 2018),
        "generation": "BU first gen",
        "engine": "2.4L Tigershark I4 with 9-speed automatic, or 1.4L "
                  "turbo with 6-speed manual",
        "reliability": 5.0,
        "maintenance": 6.2,
        "annual_maintenance_usd": 700,
        "insurance_factor": 0.98,
        "tire_set_usd": 640,
        "risk": "Engine is 174 of 431 complaints on the 2016 (40%): "
                "the 2.4L burns oil and stalls when the level drops",
        "known_issues": [
            "Only two recalls on the 2016, but 431 complaints led by "
            "engine (174) and electrical (119).",
            "Check the oil level cold before you drive it, and ask "
            "how often the owner topped it up.",
            "The 9-speed automatic hunts and bangs on early cars. "
            "Drive it in stop-and-go traffic.",
            "Built in Italy on a Fiat platform, so some parts take "
            "longer to arrive than for a US-built Jeep.",
        ],
        "note": "Charming and flawed. The complaint file is all "
                "engine and electrical; shop the 2019 or later "
                "instead.",
    },
    {
        "make": "jeep", "model": "renegade",
        "years": (2019, 2023),
        "generation": "BU facelift",
        "engine": "1.3L turbo I4 (2.4L on early base trims), 9-speed "
                  "automatic",
        "reliability": 5.8,
        "maintenance": 6.0,
        "annual_maintenance_usd": 700,
        "insurance_factor": 0.99,
        "tire_set_usd": 660,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2019 (three of them air bag) and "
            "two on the 2022.",
            "80 complaints on the 2019 and 28 on the 2022, both led "
            "by electrical. Far quieter than the early cars.",
            "The 1.3L turbo needs the exact oil specification and "
            "on-time changes. Ask for the records.",
            "Discontinued after 2023 in the US, so trim and body "
            "parts will get slower to find.",
        ],
        "note": "The better Renegade, and an acceptable small "
                "runabout if the price reflects that it is an "
                "orphan.",
    },
    {
        "make": "jeep", "model": "wagoneer",
        "years": (2022, 2023),
        "generation": "WS first gen, launch years",
        "engine": "5.7L Hemi V8 mild hybrid or 3.0L Hurricane twin "
                  "turbo I6 (2023), 8-speed automatic",
        "reliability": 4.7,
        "maintenance": 5.2,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.15,
        "tire_set_usd": 1300,
        "risk": "Ten recalls on the 2022 and a complaint file that is "
                "58% electrical (125 of 215)",
        "known_issues": [
            "Ten recalls on the 2022, covering seats, the air bag "
            "module, the backup camera, the roof and exterior trim.",
            "215 complaints on the 2022: electrical 125, engine 54, "
            "service brakes 38. Screens going black and no-starts "
            "are the usual story.",
            "Sit in it for ten minutes with everything on. Every "
            "screen, camera and power seat should work first time.",
            "Tires and brakes for a 6,000 lb truck are priced to "
            "match.",
        ],
        "note": "A first-year luxury truck with a first-year record. "
                "Only worth it at a steep discount with warranty "
                "left.",
    },
    {
        "make": "jeep", "model": "wagoneer",
        "years": (2024, 2026),
        "generation": "WS first gen",
        "engine": "3.0L Hurricane twin turbo I6, 8-speed automatic",
        "reliability": 5.0,
        "maintenance": 5.0,
        "annual_maintenance_usd": 980,
        "insurance_factor": 1.16,
        "tire_set_usd": 1300,
        "risk": "Eight recalls on the 2024, and engine is 32 of its "
                "58 complaints, on a twin turbo six with no long "
                "record yet",
        "known_issues": [
            "Eight recalls on the 2024, still including the backup "
            "camera, exterior trim and the roof.",
            "58 complaints on the 2024, led by engine (32) and "
            "electrical (27).",
            "The Hurricane six is new and complex. Keep it under "
            "factory or extended powertrain cover.",
        ],
        "note": "Fewer electrical complaints than the launch years, "
                "but the engine is unproven. A warranty purchase "
                "only.",
    },
    {
        "make": "jeep", "model": "grand wagoneer",
        "years": (2022, 2026),
        "generation": "WS first gen",
        "engine": "6.4L Hemi V8 (2022 to 2023) or 3.0L Hurricane "
                  "high-output twin turbo I6, 8-speed automatic",
        "reliability": 4.6,
        "maintenance": 4.6,
        "annual_maintenance_usd": 1150,
        "insurance_factor": 1.3,
        "tire_set_usd": 1500,
        "risk": "Ten recalls on the 2022 and eight on the 2024, on a "
                "six-figure truck with air suspension and seven "
                "screens to go wrong",
        "known_issues": [
            "Ten recalls on the 2022 and eight on the 2024, the same "
            "campaigns as the Wagoneer.",
            "Electrical leads both years: 23 of 63 complaints on the "
            "2022 and 23 of 37 on the 2024.",
            "Air suspension is standard. Watch it raise and lower, "
            "and check it has not sagged after sitting overnight.",
            "Resale has been weak, which helps a used buyer and "
            "hurts the next sale.",
        ],
        "note": "Lovely inside and expensive in every other way. "
                "Lease-return examples with warranty are the only "
                "sane entry.",
    },
    {
        "make": "jeep", "model": "wagoneer s",
        "years": (2024, 2026),
        "generation": "first gen, battery electric",
        "engine": "Dual-motor electric AWD, 100 kWh battery",
        "reliability": 4.8,
        "maintenance": 4.8,
        "annual_maintenance_usd": 450,
        "insurance_factor": 1.25,
        "tire_set_usd": 1200,
        "risk": "Five recalls on the 2024 and six on the 2025, and "
                "electrical is 39 of 56 complaints on the 2025 (70%)",
        "known_issues": [
            "Recalls on the 2025 cover headlights, brake lights, the "
            "liftgate hinge, the instrument cluster and the "
            "transmission (25V574000).",
            "56 complaints on the 2025 with electrical at 39: "
            "software faults, charging faults and dead screens.",
            "EV: routine service is cheap, but anything high-voltage "
            "is dealer-only. Check the battery warranty transfers.",
            "Confirm it charges on both a home charger and a DC "
            "fast charger before you buy.",
        ],
        "note": "Provisional. A first-year EV on a new platform with "
                "a recall list already. Lease it, do not own it.",
    },
    {
        "make": "jeep", "model": "patriot",
        "years": (2015, 2017),
        "generation": "MK first gen",
        "engine": "2.0L or 2.4L World I4, CVT or 6-speed automatic",
        "reliability": 5.0,
        "maintenance": 7.2,
        "annual_maintenance_usd": 640,
        "insurance_factor": 0.97,
        "tire_set_usd": 620,
        "risk": None,
        "known_issues": [
            "One recall on the 2016 (16V907000, engine) and 460 "
            "complaints, 225 of them engine: stalling and loss of "
            "power.",
            "Avoid the CVT; overheating and whine are well known. "
            "The 6-speed automatic is the one to have.",
            "Check for water leaks at the dome light and sunroof, "
            "and for worn front suspension parts.",
        ],
        "note": "Very cheap for a reason. Acceptable as a beater "
                "with the 6-speed automatic and a clean underside.",
    },
]

# Listing feeds sometimes name a body style as its own model. These are
# the same vehicles, so they reuse the profiles above.
_ALIASES = {
    "wrangler": ("wrangler unlimited",),
    "wrangler 4xe": ("wrangler unlimited 4xe",),
    "wagoneer": ("wagoneer l",),
    "grand wagoneer": ("grand wagoneer l",),
}
PROFILES += [dict(p, model=alias) for p in list(PROFILES)
             for alias in _ALIASES.get(p["model"], ())]
