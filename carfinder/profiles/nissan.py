"""Reliability profiles: Nissan. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

NHTSA files some Nissans under body or battery names (FRONTIER CREW
CAB, LEAF (40 KWH BATTERY)), so a count quoted here is for the file
named in the text, not always the whole model line."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "nissan", "model": "altima",
        "years": (2019, 2026),
        "generation": "L34 sixth gen",
        "engine": "2.5L PR25DD I4",
        "reliability": 6.3,
        "maintenance": 6.5,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.0,
        "tire_set_usd": 700,
        "known_issues": [
            "Xtronic CVT is the known long-term risk: failures cluster past "
            "roughly 90k miles and replacement is a four-figure job.",
            "Resale is weak, which cuts both ways: cheap to buy, costly to "
            "sell.",
        ],
        "risk": "Xtronic CVT is a known failure point past ~90k miles; "
                "replacement is a four-figure job",
        "note": "Fits the budget easily, but the CVT is the 'pain to fix' "
                "scenario. Only with clean records and a strong price.",
    },
    {
        # 2016: 556 complaints, 235 POWER TRAIN, 4 recalls.
        # 2015: 956 complaints, 10 recalls.
        "make": "nissan", "model": "altima",
        "years": (2013, 2018),
        "generation": "L33 fifth gen",
        "engine": "2.5L QR25DE I4 (or 3.5L V6), Xtronic CVT",
        "reliability": 5.2,
        "maintenance": 6.5,
        "annual_maintenance_usd": 680,
        "insurance_factor": 1.0,
        "tire_set_usd": 650,
        "risk": "Xtronic CVT failure: 235 of the 556 complaints on the "
                "2016 are POWER TRAIN, and a replacement transmission "
                "can cost more than the car is worth",
        "known_issues": [
            "235 of 556 complaints on the 2016 are POWER TRAIN (42%). "
            "Ask for proof the CVT was replaced or its fluid changed.",
            "Ten recalls on the 2015 and four on the 2016. Run the VIN "
            "for open campaigns before paying.",
            "270 exterior lighting complaints on the 2015: the low "
            "beams are dim. Test drive it at night.",
            "On the drive, any shudder, whine or flare in revs from "
            "the transmission is a reason to walk away.",
        ],
        "note": "Cheap for a reason. The CVT in these years is the "
                "weakest part of the car and the costliest to fix.",
    },
    {
        # 683 complaints on the 2023 with 265 ENGINE and 116 ENGINE
        # AND ENGINE COOLING. That is not a volume artifact.
        "make": "nissan", "model": "rogue",
        "years": (2021, 2026),
        "generation": "T33 third gen",
        "engine": "1.5L KR15DDT variable-compression turbo three-"
                  "cylinder, Xtronic CVT",
        "reliability": 5.2,
        "maintenance": 6.0,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.0,
        "tire_set_usd": 720,
        "risk": "VC-Turbo three-cylinder: 265 engine and 116 engine-"
                "cooling complaints on the 2023 alone, plus the "
                "Xtronic CVT behind it. One of the worst complaint files "
        "profiled here",
        "known_issues": [
            "The 2023 has 683 NHTSA complaints. 265 are ENGINE and a "
            "further 116 ENGINE AND ENGINE COOLING, which puts 56% of "
            "the file on the powertrain. No sales-volume argument "
            "explains a distribution that lopsided.",
            "The variable-compression 1.5L turbo triple is a complex, "
            "low-production-history design. Repairs are dealer work.",
            "Xtronic CVT behind it, the same family as the Altima's "
            "already flagged in this tool.",
            "Six recalls on the 2023 across seats, seat belts and "
            "airbag inflators.",
            "It will look like excellent value on price and mileage. "
            "That is exactly why the flag matters.",
        ],
        "note": "Avoid. Ruled out on the data rather than on taste.",
    },
    {
        # 2017: 602 complaints, 5 recalls. 2019: 340 complaints, 3
        # recalls. 2015: 554 complaints, 9 recalls.
        "make": "nissan", "model": "rogue",
        "years": (2014, 2020),
        "generation": "T32 second gen",
        "engine": "2.5L QR25DE I4, Xtronic CVT",
        "reliability": 5.6,
        "maintenance": 6.5,
        "annual_maintenance_usd": 660,
        "insurance_factor": 1.0,
        "tire_set_usd": 700,
        "risk": "Xtronic CVT failure past roughly 80k miles; 140 "
                "POWER TRAIN complaints on the 2015 and 123 on the "
                "2017, and the fix is a replacement transmission",
        "known_issues": [
            "CVT judder, slipping and outright failure. Ask for "
            "service records showing a fluid change or a replaced "
            "unit.",
            "On the 2019, 126 SERVICE BRAKES and 101 FORWARD COLLISION "
            "AVOIDANCE complaints out of 340: the automatic braking "
            "can trigger with nothing in the road.",
            "Nine recalls on the 2015, five on the 2017. Check the VIN "
            "for open ones.",
        ],
        "note": "The engine is fine; the transmission is the gamble. "
                "Buy only with CVT paperwork and a low price.",
    },
    {
        # 2026: 1 recall (seats, shared with the Kicks), 20 complaints.
        "make": "nissan", "model": "sentra",
        "years": (2026, 2026),
        "generation": "B19 ninth gen",
        "engine": "2.0L MR20DD I4, Xtronic CVT",
        "reliability": 6.6,
        "maintenance": 7.0,
        "annual_maintenance_usd": 540,
        "insurance_factor": 1.02,
        "tire_set_usd": 620,
        "risk": None,
        "known_issues": [
            "One recall on the 2026 already, for seats. Confirm it "
            "was done before delivery.",
            "20 complaints on the 2026 with no pattern yet. Too new "
            "to read either way.",
            "Carries over the 2.0L and CVT from the previous car, so "
            "the same advice applies: change the CVT fluid on time.",
        ],
        "note": "New body on a known powertrain. Provisional score, "
                "taken from the car it replaces.",
    },
    {
        # 2021: 3 recalls, 133 complaints. 2023: 1 recall, 20.
        "make": "nissan", "model": "sentra",
        "years": (2020, 2025),
        "generation": "B18 eighth gen",
        "engine": "2.0L MR20DD I4, Xtronic CVT",
        "reliability": 6.6,
        "maintenance": 7.0,
        "annual_maintenance_usd": 540,
        "insurance_factor": 1.02,
        "tire_set_usd": 620,
        "risk": None,
        "known_issues": [
            "Three recalls on the 2021, two of them for the same tie "
            "rod. Make sure both steering campaigns are closed.",
            "40 STEERING and 40 FORWARD COLLISION AVOIDANCE "
            "complaints out of 133 on the 2021. The 2023 file is far "
            "smaller (20 complaints, 1 recall).",
            "The CVT is better than the older Sentra's but still a "
            "replace-not-repair part. Fluid changes every 30k to 40k "
            "miles are cheap insurance.",
        ],
        "note": "A real improvement on the car before it. Prefer "
                "2022 and later, after the steering recalls.",
    },
    {
        # 2017: 231 complaints, 76 POWER TRAIN, 48 ENGINE, 3 recalls.
        "make": "nissan", "model": "sentra",
        "years": (2013, 2019),
        "generation": "B17 seventh gen",
        "engine": "1.8L MRA8DE I4, Xtronic CVT",
        "reliability": 5.0,
        "maintenance": 6.8,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.02,
        "tire_set_usd": 560,
        "risk": "Xtronic CVT failure, often before 100k miles; 76 of "
                "231 complaints on the 2017 are POWER TRAIN and a "
                "replacement can exceed the value of the car",
        "known_issues": [
            "The small CVT in this generation is the least durable "
            "Nissan fitted. Budget for one, or buy the rare manual.",
            "76 POWER TRAIN and 48 ENGINE complaints out of 231 on "
            "the 2017.",
            "Three recalls on the 2017, including a brake light "
            "switch campaign covering 2016 to 2019.",
        ],
        "note": "Very cheap to buy and often very cheap for a reason. "
                "Without CVT records, skip it.",
    },
    {
        # 2021: 3 recalls, 32 complaints. 2024: 1 recall, 97
        # complaints, 53 ENGINE and 34 POWER TRAIN.
        "make": "nissan", "model": "versa",
        "years": (2020, 2026),
        "generation": "N18 third gen",
        "engine": "1.6L HR16DE I4, Xtronic CVT (5-speed manual on "
                  "base cars)",
        "reliability": 6.2,
        "maintenance": 7.5,
        "annual_maintenance_usd": 480,
        "insurance_factor": 1.02,
        "tire_set_usd": 520,
        "risk": None,
        "known_issues": [
            "97 complaints on the 2024, 53 ENGINE and 34 POWER TRAIN. "
            "Most describe the car dropping into limp mode or "
            "stalling. Ask the dealer for the update history.",
            "The 2021 file is much quieter: 32 complaints, 3 recalls.",
            "The manual gearbox avoids the CVT question entirely, if "
            "you can find one.",
        ],
        "note": "Honest cheap transport. The limp-mode complaints on "
                "later cars are the thing to ask about.",
    },
    {
        # 2016: 81 complaints; the recall endpoint returned nothing.
        "make": "nissan", "model": "versa",
        "years": (2012, 2019),
        "generation": "N17 second gen",
        "engine": "1.6L HR16DE I4, Xtronic CVT (5-speed manual or "
                  "4-speed automatic on base cars)",
        "reliability": 5.6,
        "maintenance": 7.5,
        "annual_maintenance_usd": 520,
        "insurance_factor": 1.02,
        "tire_set_usd": 480,
        "risk": "Xtronic CVT failure on higher-mileage cars; a "
                "replacement costs a large share of what the car is "
                "worth",
        "known_issues": [
            "81 complaints on the 2016, led by AIR BAGS (21) and "
            "POWER TRAIN (20).",
            "The recall lookup returned nothing for the 2016. That is "
            "not a clean record: run the VIN yourself.",
            "Base cars with the 5-speed manual or the old 4-speed "
            "automatic dodge the CVT and are the safer buy.",
        ],
        "note": "Basic and cheap to keep going, except for the CVT. "
                "Provisional on recalls.",
    },
    {
        # 2025: 4 recalls, 43 complaints, spread thin.
        "make": "nissan", "model": "kicks",
        "years": (2025, 2026),
        "generation": "P16 second gen",
        "engine": "2.0L MR20DD I4, Xtronic CVT; AWD optional",
        "reliability": 6.6,
        "maintenance": 7.0,
        "annual_maintenance_usd": 520,
        "insurance_factor": 1.0,
        "tire_set_usd": 680,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2025, its first year. Check each "
            "against the VIN.",
            "43 complaints on the 2025 with no component standing "
            "out: electrical (7) and wipers (7) lead.",
            "The 2025 'Kicks Play' is the old car sold alongside. "
            "Check which one a listing actually is.",
        ],
        "note": "Bigger and better equipped than the old Kicks. First "
                "years of a new body, so the score is provisional.",
    },
    {
        # 2019: 1 recall, 135 complaints. 2022: 24 complaints; the
        # recall endpoint returned nothing.
        "make": "nissan", "model": "kicks",
        "years": (2018, 2024),
        "generation": "P15 first gen",
        "engine": "1.6L HR16DE I4, Xtronic CVT; front-wheel drive "
                  "only",
        "reliability": 6.7,
        "maintenance": 7.5,
        "annual_maintenance_usd": 490,
        "insurance_factor": 1.0,
        "tire_set_usd": 600,
        "risk": None,
        "known_issues": [
            "On the 2019, 43 of 135 complaints are FORWARD COLLISION "
            "AVOIDANCE: automatic braking firing with no obstacle. "
            "Ask whether the radar software was updated.",
            "No AWD on this generation at any price.",
            "Light duty for a CVT (about 120 hp), which helps it "
            "last, but change the fluid on schedule anyway.",
        ],
        "note": "Slow, simple and cheap to run. One of the safer used "
                "Nissans, mostly because it asks little of its CVT.",
    },
    {
        # 2022: 5 recalls, 137 complaints. 2023: 1 recall, 107.
        "make": "nissan", "model": "pathfinder",
        "years": (2022, 2026),
        "generation": "R53 fifth gen",
        "engine": "3.5L VQ35DD V6, 9-speed automatic (no CVT)",
        "reliability": 7.0,
        "maintenance": 6.5,
        "annual_maintenance_usd": 640,
        "insurance_factor": 1.03,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "Five recalls on the 2022, the launch year; one on the "
            "2023. Later years are the easier buy.",
            "SERVICE BRAKES is the largest named cluster on the 2022 "
            "(35 of 137 complaints).",
            "The 9-speed can shift roughly at low speed. Drive it in "
            "traffic before deciding.",
        ],
        "note": "Dropping the CVT for a conventional automatic fixed "
                "the old Pathfinder's biggest problem.",
    },
    {
        # 2015: 5 recalls, 321 complaints. 2017: 2 recalls, 188
        # complaints, 83 ENGINE. 2019: 2 recalls, 76 complaints.
        "make": "nissan", "model": "pathfinder",
        "years": (2013, 2020),
        "generation": "R52 fourth gen",
        "engine": "3.5L VQ35 V6, Xtronic CVT",
        "reliability": 5.6,
        "maintenance": 6.2,
        "annual_maintenance_usd": 720,
        "insurance_factor": 1.03,
        "tire_set_usd": 850,
        "risk": "CVT judder and failure, worst on 2013 to 2016 cars; "
                "a replacement transmission is a four-figure job",
        "known_issues": [
            "321 complaints on the 2015 with POWER TRAIN (77) and "
            "ENGINE (74) leading; 188 on the 2017 with 83 ENGINE.",
            "A shudder between 15 and 30 mph on light throttle is the "
            "CVT. Do not accept 'they all do that'.",
            "Later cars are calmer: 76 complaints and 2 recalls on "
            "the 2019.",
        ],
        "note": "A three-row family car pulled by a CVT that was not "
                "up to the weight. 2017 and later, with records, or "
                "not at all.",
    },
    {
        # 2025: 2 recalls, 26 complaints.
        "make": "nissan", "model": "murano",
        "years": (2025, 2026),
        "generation": "fourth gen",
        "engine": "2.0L KR20DDET variable-compression turbo I4, "
                  "9-speed automatic",
        "reliability": 6.0,
        "maintenance": 6.0,
        "annual_maintenance_usd": 680,
        "insurance_factor": 1.05,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "Two recalls and 26 complaints on the 2025, with "
            "electrical (8), engine (6) and power train (6) leading. "
            "Small numbers, very early.",
            "The VC-Turbo engine family has a poor record in the "
            "Rogue and Infiniti QX50. Keep the warranty paperwork.",
            "No CVT any more, which removes the old Murano's main "
            "worry.",
        ],
        "note": "Provisional. A complicated engine with a short "
                "history, in a new body.",
    },
    {
        # 2015: 5 recalls, 205 complaints. 2017: 3 recalls, 107.
        # 2021: 17 complaints; the recall endpoint returned nothing.
        "make": "nissan", "model": "murano",
        "years": (2015, 2024),
        "generation": "Z52 third gen",
        "engine": "3.5L VQ35DE V6, Xtronic CVT",
        "reliability": 6.6,
        "maintenance": 6.3,
        "annual_maintenance_usd": 650,
        "insurance_factor": 1.03,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "The launch year is the rough one: 5 recalls and 205 "
            "complaints on the 2015, 53 of them POWER TRAIN.",
            "Complaints fall away later (107 on the 2017, 17 on the "
            "2021).",
            "The V6 is long-proven. The CVT copes better here than "
            "in Nissan's four-cylinder cars but still wants fluid "
            "changes; ask for them in the records.",
        ],
        "note": "A comfortable, aging design. 2017 and later with CVT "
                "service history is a reasonable buy.",
    },
    {
        # 2022: 6 recalls, 112 complaints filed under FRONTIER.
        # 2023: 1 recall; 68 complaints under FRONTIER CREW CAB.
        "make": "nissan", "model": "frontier",
        "years": (2022, 2026),
        "generation": "D41 third gen",
        "engine": "3.8L VQ38DD V6, 9-speed automatic",
        "reliability": 7.2,
        "maintenance": 7.0,
        "annual_maintenance_usd": 600,
        "insurance_factor": 1.03,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2022, the first year of the new "
            "body; one on the 2023.",
            "On the 2023 crew cab, 31 of 68 complaints are "
            "ELECTRICAL SYSTEM. Check every screen, camera and "
            "switch on the test drive.",
            "A naturally aspirated V6 and a conventional automatic: "
            "no turbo, no CVT.",
        ],
        "note": "Simple by current truck standards. Prefer 2023 and "
                "later, after the launch-year recalls.",
    },
    {
        # 2020: 2 recalls; 23 complaints under FRONTIER CREW CAB.
        "make": "nissan", "model": "frontier",
        "years": (2020, 2021),
        "generation": "D40 second gen, new powertrain",
        "engine": "3.8L VQ38DD V6, 9-speed automatic",
        "reliability": 7.4,
        "maintenance": 7.2,
        "annual_maintenance_usd": 580,
        "insurance_factor": 1.03,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2020. 23 complaints on the 2020 crew "
            "cab, 12 of them POWER TRAIN: drive it long enough to "
            "feel every gear.",
            "Old cabin and old safety tech; no automatic emergency "
            "braking.",
        ],
        "note": "The old truck's proven frame with the new truck's "
                "engine. A small complaint file, so provisional.",
    },
    {
        # 2017: 1 recall, 38 complaints filed under FRONTIER.
        "make": "nissan", "model": "frontier",
        "years": (2011, 2019),
        "generation": "D40 second gen",
        "engine": "4.0L VQ40DE V6 (or 2.5L QR25DE I4), 5-speed "
                  "automatic or manual",
        "reliability": 7.8,
        "maintenance": 7.8,
        "annual_maintenance_usd": 560,
        "insurance_factor": 1.0,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "One recall and 38 complaints on the 2017, with fuel "
            "system (10) the largest group.",
            "Thirsty for its size, and the cabin dates from 2005.",
            "Check the frame and rear leaf spring mounts for rust on "
            "trucks from salted-road states.",
        ],
        "note": "An old design that had its faults worked out long "
                "ago. One of the better used Nissans.",
    },
    {
        # 2017: 3 recalls, 172 complaints, 90 ENGINE. 2019: 4
        # recalls, 49 complaints. 2021: 5 recalls. 2022: 4 recalls.
        "make": "nissan", "model": "titan",
        "years": (2016, 2024),
        "generation": "A61 second gen",
        "engine": "5.6L VK56VD V8, 7-speed automatic (9-speed from "
                  "2020)",
        "reliability": 6.6,
        "maintenance": 6.5,
        "annual_maintenance_usd": 720,
        "insurance_factor": 1.05,
        "tire_set_usd": 1100,
        "risk": None,
        "known_issues": [
            "90 of 172 complaints on the 2017 are ENGINE. The 2019 "
            "is quieter: 49 complaints, 17 ENGINE.",
            "Three to five recalls on every year pulled (2017, 2019, "
            "2021, 2022). Run the VIN.",
            "Discontinued after 2024. Parts are shared with the "
            "Armada, but resale and dealer interest are thin.",
            "The Titan XD with the Cummins diesel is a different "
            "truck with its own problems; this profile is the gas V8.",
        ],
        "note": "A strong V8 in a truck nobody bought. Priced well "
                "below rivals; prefer 2019 and later.",
    },
    {
        # 2015: 1 recall, 10 complaints.
        "make": "nissan", "model": "titan",
        "years": (2013, 2015),
        "generation": "A60 first gen",
        "engine": "5.6L VK56DE V8, 5-speed automatic",
        "reliability": 6.8,
        "maintenance": 7.0,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.03,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "One recall and 10 complaints on the 2015. Few were "
            "sold, so the small file proves little.",
            "Rear axle seals and exhaust manifolds are the usual "
            "repairs on this generation. Look and listen for both.",
            "Heavy on fuel even for a full-size truck.",
        ],
        "note": "The last years of a 2004 design. Simple and cheap, "
                "but old. Provisional.",
    },
    {
        # 2025: 2 recalls, 23 complaints.
        "make": "nissan", "model": "armada",
        "years": (2025, 2026),
        "generation": "Y63 third gen",
        "engine": "3.5L VR35DDTT twin-turbo V6, 9-speed automatic",
        "reliability": 6.4,
        "maintenance": 5.8,
        "annual_maintenance_usd": 800,
        "insurance_factor": 1.12,
        "tire_set_usd": 1300,
        "risk": None,
        "known_issues": [
            "Two recalls and 23 complaints on the 2025, electrical "
            "(7) leading. First year of a new design.",
            "A twin-turbo V6 replaces the old V8: more to go wrong "
            "and nothing yet known about how it ages.",
            "Air suspension on upper trims is a future expense.",
        ],
        "note": "Provisional. Too new to judge, and more complicated "
                "than the truck it replaces.",
    },
    {
        # 2018: 1 recall, 76 complaints, 41 ELECTRICAL SYSTEM.
        # 2022: 1 recall, 10 complaints.
        "make": "nissan", "model": "armada",
        "years": (2017, 2024),
        "generation": "Y62 second gen",
        "engine": "5.6L VK56VD V8, 7-speed automatic",
        "reliability": 7.4,
        "maintenance": 6.3,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.1,
        "tire_set_usd": 1200,
        "risk": None,
        "known_issues": [
            "41 of 76 complaints on the 2018 are ELECTRICAL SYSTEM: "
            "dead batteries from a parasitic drain and blank "
            "infotainment screens. Ask if either was fixed.",
            "One recall on each of the 2018 and 2022.",
            "Fuel use is poor, around 15 mpg in mixed driving. "
            "Price that into the running cost.",
        ],
        "note": "A Nissan Patrol underneath: heavy, thirsty and "
                "tough. The powertrain is the strong part.",
    },
    {
        # 2015: 3 recalls, 21 complaints, 8 AIR BAGS.
        "make": "nissan", "model": "armada",
        "years": (2013, 2015),
        "generation": "TA60 first gen",
        "engine": "5.6L VK56DE V8, 5-speed automatic",
        "reliability": 6.6,
        "maintenance": 6.8,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.05,
        "tire_set_usd": 1050,
        "risk": None,
        "known_issues": [
            "Three recalls on the 2015; 8 of its 21 complaints are "
            "AIR BAGS. Confirm the airbag recall work was done.",
            "Shares the first Titan's wear points: exhaust "
            "manifolds, rear axle seals, front brakes.",
        ],
        "note": "Titan-based and dated by 2015. Cheap to buy, costly "
                "to fuel. Provisional.",
    },
    {
        # 2026: 2 recalls; only 4 complaints under the battery-size
        # model names NHTSA uses for it.
        "make": "nissan", "model": "leaf",
        "years": (2026, 2026),
        "generation": "ZE2 third gen",
        "engine": "Single electric motor, 53 or 75 kWh liquid-cooled "
                  "battery",
        "reliability": 6.8,
        "maintenance": 7.5,
        "annual_maintenance_usd": 330,
        "insurance_factor": 1.08,
        "tire_set_usd": 800,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2026 already. Confirm both are "
            "closed.",
            "The battery is liquid-cooled at last and the fast-"
            "charge port is NACS, which fixes the old Leaf's two "
            "biggest drawbacks.",
            "No track record yet for the new pack or motor.",
        ],
        "note": "A clean break from the old Leaf. Provisional until "
                "there is a year or two of data.",
    },
    {
        # 2019: 5 recalls, 261 complaints, 179 ELECTRICAL SYSTEM.
        # 2021: 4 recalls, 59 complaints. 2022: 4 recalls.
        "make": "nissan", "model": "leaf",
        "years": (2018, 2025),
        "generation": "ZE1 second gen",
        "engine": "Single electric motor, 40 or 62 kWh air-cooled "
                  "battery",
        "reliability": 6.4,
        "maintenance": 7.5,
        "annual_maintenance_usd": 340,
        "insurance_factor": 1.05,
        "tire_set_usd": 720,
        "risk": "Air-cooled battery: capacity fades faster than in "
                "liquid-cooled EVs, a fast-charging fire recall "
                "covers these years, and a replacement pack costs "
                "more than many used Leafs",
        "known_issues": [
            "179 of 261 complaints on the 2019 are ELECTRICAL SYSTEM "
            "(69%), most about the drive battery or the fast-charge "
            "recall.",
            "Read the battery health bars on the dash and ask for a "
            "dealer battery report. Capacity, not mileage, sets the "
            "value.",
            "Fast charging uses the CHAdeMO plug, which public "
            "networks are removing. Plan on charging at home.",
            "Five recalls on the 2019, four on the 2021 and 2022.",
        ],
        "note": "Cheap electric commuting if you charge at home and "
                "the battery checks out. A poor road-trip car.",
    },
    {
        # 2015: 4 recalls, 111 complaints, 86 SERVICE BRAKES.
        "make": "nissan", "model": "leaf",
        "years": (2011, 2017),
        "generation": "ZE0 first gen",
        "engine": "Single electric motor, 24 or 30 kWh air-cooled "
                  "battery",
        "reliability": 5.8,
        "maintenance": 7.3,
        "annual_maintenance_usd": 360,
        "insurance_factor": 1.0,
        "tire_set_usd": 600,
        "risk": "Battery capacity loss: many of these now have well "
                "under 70 miles of real range, and a replacement "
                "pack costs more than the car",
        "known_issues": [
            "86 of 111 complaints on the 2015 are SERVICE BRAKES. "
            "Check that the brake recall work is recorded.",
            "Count the capacity bars on the dash (12 is new). "
            "Fewer than 9 means a short-range car.",
            "Hot-climate cars lose capacity fastest. Ask where it "
            "lived.",
            "CHAdeMO fast charging only, and only on some trims.",
        ],
        "note": "A city runabout at this age and nothing more. Buy "
                "on measured battery health alone.",
    },
    {
        # 2023: 4 recalls, 49 complaints, 28 ELECTRICAL SYSTEM.
        # 2024: 10 complaints; the recall endpoint returned nothing.
        "make": "nissan", "model": "ariya",
        "years": (2023, 2025),
        "generation": "FE0 first gen",
        "engine": "Single or dual electric motor, 63 or 87 kWh "
                  "liquid-cooled battery",
        "reliability": 6.4,
        "maintenance": 6.5,
        "annual_maintenance_usd": 380,
        "insurance_factor": 1.15,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "28 of 49 complaints on the 2023 are ELECTRICAL SYSTEM, "
            "many about the 12-volt battery failing. Ask if it has "
            "been replaced.",
            "Four recalls on the 2023. The 2024 file is smaller (10 "
            "complaints).",
            "DC fast charging tops out around 130 kW, slower than "
            "rivals, and uses CCS (NACS by adapter).",
            "Dropped from the US lineup after 2025, so resale is "
            "soft. That helps a used buyer.",
        ],
        "note": "A comfortable EV with a liquid-cooled battery, "
                "unlike the old Leaf. First-year cars are the ones "
                "with the electrical complaints.",
    },
    {
        # 2016: 8 recalls, 142 complaints. 2018: 2 recalls, 36.
        # 2021: 3 complaints; the recall endpoint returned nothing.
        "make": "nissan", "model": "maxima",
        "years": (2016, 2023),
        "generation": "A36 eighth gen",
        "engine": "3.5L VQ35DE V6, Xtronic CVT",
        "reliability": 6.8,
        "maintenance": 6.3,
        "annual_maintenance_usd": 640,
        "insurance_factor": 1.1,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "Eight recalls and 142 complaints on the 2016, the "
            "launch year, with POWER TRAIN (33) leading. Avoid that "
            "year.",
            "Much quieter after: 2 recalls and 36 complaints on the "
            "2018.",
            "The V6 is durable. The CVT needs fluid changes and "
            "does not like hard launches.",
        ],
        "note": "A quick, comfortable sedan with a good engine and a "
                "so-so transmission. 2018 and later.",
    },
    {
        # 2018: 2 recalls, 95 complaints. 2020: 1 recall, 59.
        "make": "nissan", "model": "rogue sport",
        "years": (2017, 2022),
        "generation": "J11 first gen (Qashqai)",
        "engine": "2.0L MR20DD I4, Xtronic CVT",
        "reliability": 6.3,
        "maintenance": 7.0,
        "annual_maintenance_usd": 560,
        "insurance_factor": 1.0,
        "tire_set_usd": 680,
        "risk": None,
        "known_issues": [
            "59 complaints on the 2020: ENGINE (22) and FORWARD "
            "COLLISION AVOIDANCE (14) lead. 95 on the 2018.",
            "Automatic braking can trigger falsely, as on the larger "
            "Rogue. Ask about the radar software update.",
            "Same CVT advice as every four-cylinder Nissan: proof "
            "of fluid changes, and no shudder on the drive.",
        ],
        "note": "A smaller, simpler Rogue with the older engine. "
                "Adequate, not special.",
    },
    {
        # 2023: 2 recalls, 2 complaints. 2024: 2 recalls, 2.
        "make": "nissan", "model": "z",
        "years": (2023, 2026),
        "generation": "RZ34 seventh gen",
        "engine": "3.0L VR30DDTT twin-turbo V6, 6-speed manual or "
                  "9-speed automatic",
        "reliability": 7.2,
        "maintenance": 5.8,
        "annual_maintenance_usd": 780,
        "insurance_factor": 1.28,
        "tire_set_usd": 1300,
        "risk": None,
        "known_issues": [
            "Two recalls on each of the 2023 and 2024. Only two "
            "complaints a year, but very few were sold.",
            "The same twin-turbo V6 had turbo failures in early "
            "Infiniti Q50s. Ask for oil change records.",
            "Check for signs of track use or a tune: tires, brakes, "
            "aftermarket parts.",
        ],
        "note": "A sports car on proven underpinnings. Insurance and "
                "tires cost more than the repairs will.",
    },
    {
        # 2016: 3 complaints. 2019: 1. The recall endpoint returned
        # nothing for either year.
        "make": "nissan", "model": "370z",
        "years": (2013, 2020),
        "generation": "Z34 sixth gen",
        "engine": "3.7L VQ37VHR V6, 6-speed manual or 7-speed "
                  "automatic",
        "reliability": 7.8,
        "maintenance": 6.5,
        "annual_maintenance_usd": 680,
        "insurance_factor": 1.25,
        "tire_set_usd": 1150,
        "risk": None,
        "known_issues": [
            "On manual cars the clutch slave cylinder sits inside "
            "the gearbox and fails. Ask if it was replaced.",
            "Three complaints on the 2016 and one on the 2019. Low "
            "sales, so that says little.",
            "Look for signs of track days and modifications.",
        ],
        "note": "An old-school V6 sports car with few weak points. "
                "Provisional: the NHTSA file is too thin to lean on.",
    },
]
