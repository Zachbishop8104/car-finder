"""Reliability profiles: Volkswagen. The format and the caveats on reading
these numbers are in carfinder/reliability.py."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "volkswagen", "model": "jetta",
        "years": (2022, 2026),
        "generation": "A7 facelift",
        "engine": "1.5L TSI turbo I4, 8-speed automatic",
        "reliability": 6.9,
        "maintenance": 6.4,
        "annual_maintenance_usd": 640,
        "insurance_factor": 1.0,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "Recall 26V138000 (electrical wiring) hits both 2025 and 2026; "
            "the 2025 adds 26V185000, instrument cluster.",
            "Power train is the top complaint component on the 2025 (6 of "
            "22): a small file, but the cluster is in the expensive place.",
            "Volkswagen parts and labour run above the Japanese and Korean "
            "sedans, and independent shops willing to work on them are "
            "thinner on the ground outside big cities.",
            "34 mpg and a genuinely good highway ride. It is the "
            "nicest-driving cheap sedan profiled here.",
        ],
        "note": "Usually the cheapest way into a new sedan, though the "
                "running costs claw a lot of that back.",
    },
    {
        "make": "volkswagen", "model": "jetta",
        "years": (2019, 2021),
        "generation": "A7",
        "engine": "1.4L TSI turbo I4, 8-speed automatic or 6-speed manual",
        "reliability": 5.8,
        "maintenance": 6.4,
        "annual_maintenance_usd": 660,
        "insurance_factor": 1.0,
        "tire_set_usd": 680,
        "risk": "The 2019 launch year carries 11 recalls and 553 complaints, "
                "against 4 and 71 for the 2021",
        "known_issues": [
            "11 recalls on the 2019, the first year of this generation, and "
            "four on the 2021.",
            "553 complaints on the 2019, led by power train (163), "
            "electrical (154) and engine (148). The 2021 has 71, led by "
            "service brakes (26).",
            "If you want this generation, a 2021 has a much shorter file "
            "than a 2019. On any of them, check for harsh or delayed shifts "
            "when cold.",
            "Volkswagen parts and labour run above the Japanese and Korean "
            "brands, and independent shops willing to work on them are "
            "thinner on the ground outside big cities.",
        ],
        "note": "Avoid the 2019 unless every recall is closed and the price "
                "reflects it. The 2021 is a reasonable cheap sedan.",
    },
    {
        "make": "volkswagen", "model": "jetta",
        "years": (2015, 2018),
        "generation": "A6",
        "engine": "1.4L or 1.8L TSI turbo I4 (2.0L base and TDI diesel in "
                  "2015)",
        "reliability": 6.4,
        "maintenance": 6.6,
        "annual_maintenance_usd": 620,
        "insurance_factor": 0.98,
        "tire_set_usd": 660,
        "risk": None,
        "known_issues": [
            "Five recalls and 162 complaints on the 2016, led by engine (44) "
            "and electrical (36), with five fires reported.",
            "2015 TDI diesels were part of the emissions settlement. Confirm "
            "the emissions fix was done and what extended warranty remains.",
            "Water pump and thermostat housing leaks are common on the turbo "
            "engines. Look for dried coolant on the passenger side of the "
            "engine.",
            "Volkswagen parts and labour run above the Japanese and Korean "
            "brands, and independent shops willing to work on them are "
            "thinner on the ground outside big cities.",
        ],
        "note": "A simple, roomy old sedan with an average record. Buy on "
                "service history; a neglected one gets expensive.",
    },
    {
        "make": "volkswagen", "model": "tiguan",
        "years": (2025, 2026),
        "generation": "third gen",
        "engine": "2.0L TSI turbo I4, 8-speed automatic",
        "reliability": 6.4,
        "maintenance": 6.2,
        "annual_maintenance_usd": 690,
        "insurance_factor": 1.0,
        "tire_set_usd": 800,
        "risk": None,
        "known_issues": [
            "Three recalls on the 2025, the first year of the redesign.",
            "58 complaints on the 2025, led by electrical (18), forward "
            "collision avoidance (14) and engine (13).",
            "The third row is gone and most controls moved to the "
            "touchscreen. Try the climate and volume controls on a test "
            "drive.",
            "Volkswagen parts and labour run above the Japanese and Korean "
            "brands, and independent shops willing to work on them are "
            "thinner on the ground outside big cities.",
        ],
        "note": "Too new for a firm number. A calmer start than the 2018 "
                "launch of the previous generation, which had 14 recalls.",
    },
    {
        "make": "volkswagen", "model": "tiguan",
        "years": (2018, 2024),
        "generation": "second gen (long wheelbase)",
        "engine": "2.0L TSI turbo I4, 8-speed automatic",
        "reliability": 6.0,
        "maintenance": 6.2,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.0,
        "tire_set_usd": 780,
        "risk": "Fourteen recalls on the 2018 launch year, and engine is the "
                "top complaint component on both the 2018 and the 2022",
        "known_issues": [
            "14 recalls on the 2018; five each on the 2019 and 2022.",
            "Engine leads the complaints on the 2018 (82 of 289) and is a "
            "lopsided share on the 2022 (114 of 283).",
            "The panoramic sunroof is a known leak point. Check the "
            "headliner and the front footwells for water stains.",
            "Volkswagen parts and labour run above the Japanese and Korean "
            "brands, and independent shops willing to work on them are "
            "thinner on the ground outside big cities.",
        ],
        "note": "Roomy and pleasant to drive, with a below-average record. "
                "Later years have fewer campaigns than the 2018, but the "
                "engine complaints did not go away.",
    },
    {
        "make": "volkswagen", "model": "tiguan",
        "years": (2015, 2017),
        "generation": "first gen",
        "engine": "2.0L TSI turbo I4, 6-speed automatic",
        "reliability": 6.2,
        "maintenance": 6.0,
        "annual_maintenance_usd": 720,
        "insurance_factor": 1.0,
        "tire_set_usd": 760,
        "risk": None,
        "known_issues": [
            "Two recalls and 97 complaints on the 2016, with air bags the "
            "largest group (37).",
            "The 2.0T of this era leaks coolant from its plastic water pump "
            "housing and builds carbon on the intake valves. Ask whether "
            "either has been dealt with.",
            "It asks for premium fuel and returns poor economy for its size.",
            "Volkswagen parts and labour run above the Japanese and Korean "
            "brands, and independent shops willing to work on them are "
            "thinner on the ground outside big cities.",
        ],
        "note": "Small, thirsty and dated, but a short recall list. Only "
                "worth it with a full service history.",
    },
    {
        "make": "volkswagen", "model": "atlas",
        "years": (2024, 2026),
        "generation": "first gen, second facelift",
        "engine": "2.0L TSI turbo I4 (269 hp), 8-speed automatic",
        "reliability": 5.9,
        "maintenance": 5.8,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.05,
        "tire_set_usd": 920,
        "risk": None,
        "known_issues": [
            "Eight recalls on the 2024 (three for the rear camera) and five "
            "on the 2025.",
            "179 complaints on the 2024, led by electrical (46) and service "
            "brakes (38); 51 on the 2025.",
            "The V6 was dropped for 2024. Every car now has the turbo four, "
            "which tows 5,000 lb but works hard doing it.",
            "Volkswagen parts and labour run above the Japanese and Korean "
            "brands, and independent shops willing to work on them are "
            "thinner on the ground outside big cities.",
        ],
        "note": "Fewer campaigns than the earlier Atlas, still more than a "
                "Highlander or Pilot. Space is the reason to buy one.",
    },
    {
        "make": "volkswagen", "model": "atlas",
        "years": (2021, 2023),
        "generation": "first gen, first facelift",
        "engine": "2.0L TSI turbo I4 or 3.6L VR6, 8-speed automatic",
        "reliability": 5.2,
        "maintenance": 5.8,
        "annual_maintenance_usd": 780,
        "insurance_factor": 1.05,
        "tire_set_usd": 900,
        "risk": "Seventeen recalls on the 2021, a very high campaign count "
                "for a single model year",
        "known_issues": [
            "17 recalls on the 2021 and seven on the 2022.",
            "481 complaints on the 2021, led by electrical (149), service "
            "brakes (95) and engine (87).",
            "Faults in the door wiring harness set off air bag warnings, "
            "window faults and parking brake warnings. VW recalled it; "
            "confirm the work is done.",
            "Volkswagen parts and labour run above the Japanese and Korean "
            "brands, and independent shops willing to work on them are "
            "thinner on the ground outside big cities.",
        ],
        "note": "A huge cabin and a poor record. Check every recall against "
                "the VIN before you go to see one.",
    },
    {
        "make": "volkswagen", "model": "atlas",
        "years": (2018, 2020),
        "generation": "first gen",
        "engine": "2.0L TSI turbo I4 or 3.6L VR6, 8-speed automatic",
        "reliability": 5.0,
        "maintenance": 5.8,
        "annual_maintenance_usd": 780,
        "insurance_factor": 1.05,
        "tire_set_usd": 900,
        "risk": "Seventeen recalls on the 2018 and twelve on the 2019, with "
                "air bags the largest recall group on both",
        "known_issues": [
            "17 recalls on the 2018 and 12 on the 2019. Four on each are air "
            "bag campaigns, and the 2018 has two for the fuel system.",
            "Air bags lead the 2019 complaints (142 of 487); electrical "
            "(110) and engine (101) lead the 2018.",
            "Faults in the door wiring harness set off air bag and parking "
            "brake warnings. Confirm that recall is closed on the car you "
            "are looking at.",
            "Volkswagen parts and labour run above the Japanese and Korean "
            "brands, and independent shops willing to work on them are "
            "thinner on the ground outside big cities.",
        ],
        "note": "The launch years of a new design, and the file shows it. A "
                "later Atlas or a rival three-row is the safer buy.",
    },
    {
        "make": "volkswagen", "model": "atlas cross sport",
        "years": (2024, 2026),
        "generation": "first gen, facelift",
        "engine": "2.0L TSI turbo I4 (269 hp), 8-speed automatic",
        "reliability": 5.9,
        "maintenance": 5.8,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.05,
        "tire_set_usd": 920,
        "risk": None,
        "known_issues": [
            "Eight recalls on the 2024, three of them for the rear camera.",
            "102 complaints on the 2024, led by electrical (35) and forward "
            "collision avoidance (19).",
            "Volkswagen parts and labour run above the Japanese and Korean "
            "brands, and independent shops willing to work on them are "
            "thinner on the ground outside big cities.",
        ],
        "note": "A two-row Atlas with the same parts and much the same "
                "record. Better than the early cars, still below the class "
                "average.",
    },
    {
        "make": "volkswagen", "model": "atlas cross sport",
        "years": (2020, 2023),
        "generation": "first gen",
        "engine": "2.0L TSI turbo I4 or 3.6L VR6, 8-speed automatic",
        "reliability": 5.3,
        "maintenance": 5.8,
        "annual_maintenance_usd": 780,
        "insurance_factor": 1.05,
        "tire_set_usd": 900,
        "risk": "Eleven recalls on the 2020 and fourteen on the 2021, a very "
                "high campaign count",
        "known_issues": [
            "11 recalls on the 2020, 14 on the 2021 and seven on the 2022.",
            "165 complaints on the 2021, led by electrical (54), air bags "
            "(37) and service brakes (36).",
            "It shares the Atlas door wiring harness fault, which sets off "
            "air bag and parking brake warnings. Confirm the recall is "
            "closed.",
            "Volkswagen parts and labour run above the Japanese and Korean "
            "brands, and independent shops willing to work on them are "
            "thinner on the ground outside big cities.",
        ],
        "note": "Roomy for a two-row, with the Atlas's heavy recall list. "
                "Check every campaign against the VIN.",
    },
    {
        "make": "volkswagen", "model": "taos",
        "years": (2025, 2026),
        "generation": "first gen, facelift",
        "engine": "1.5L TSI turbo I4, 8-speed automatic",
        "reliability": 6.3,
        "maintenance": 6.3,
        "annual_maintenance_usd": 650,
        "insurance_factor": 1.0,
        "tire_set_usd": 720,
        "risk": None,
        "known_issues": [
            "Two recalls and 14 complaints on the 2025: a short file so far.",
            "The facelift replaced the dual-clutch gearbox on AWD cars with "
            "a conventional 8-speed automatic, which removes a common "
            "complaint.",
            "Volkswagen parts and labour run above the Japanese and Korean "
            "brands, and independent shops willing to work on them are "
            "thinner on the ground outside big cities.",
        ],
        "note": "The facelift fixed the gearbox that hurt the early AWD "
                "cars. Still new, so treat the score as provisional.",
    },
    {
        "make": "volkswagen", "model": "taos",
        "years": (2022, 2024),
        "generation": "first gen",
        "engine": "1.5L TSI turbo I4; 8-speed automatic (FWD) or 7-speed "
                  "dual-clutch (AWD)",
        "reliability": 5.6,
        "maintenance": 6.3,
        "annual_maintenance_usd": 660,
        "insurance_factor": 1.0,
        "tire_set_usd": 720,
        "risk": "Engine is a lopsided share of complaints on the 2022 (147 "
                "of 327), with stalling and coolant-loss reports on early "
                "cars",
        "known_issues": [
            "Six recalls and 327 complaints on the 2022, its first year. "
            "Engine (147) is nearly half the file.",
            "The 2023 has no recalls on file and 110 complaints, but engine "
            "(43) and service brakes (34) still lead.",
            "AWD cars use a dual-clutch gearbox that hesitates and shudders "
            "at low speed. Drive one in stop-and-go traffic before buying.",
            "Volkswagen parts and labour run above the Japanese and Korean "
            "brands, and independent shops willing to work on them are "
            "thinner on the ground outside big cities.",
        ],
        "note": "Roomy and efficient, with a troubled first year. Prefer a "
                "2023 or 2024 with front-wheel drive, and check the coolant "
                "level.",
    },
    {
        "make": "volkswagen", "model": "id.4",
        "years": (2024, 2026),
        "generation": "first gen, updated motor and infotainment",
        "engine": "single-motor RWD or dual-motor AWD; 62 or 82 kWh battery",
        "reliability": 6.0,
        "maintenance": 5.6,
        "annual_maintenance_usd": 380,
        "insurance_factor": 1.1,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "Nine recalls on the 2024 (five electrical) and two on the 2025.",
            "54 complaints on the 2024 and 31 on the 2025, with electrical "
            "the largest group on both (30 and 17).",
            "The 2024 update brought a stronger rear motor and a faster, "
            "larger screen, which answers the main gripe about the early "
            "cars.",
            "Servicing is cheap for a Volkswagen: no oil changes, long brake "
            "life. Battery warranty is 8 years or 100,000 miles.",
        ],
        "note": "The ID.4 to buy. Running costs are low, but the electrical "
                "file has shrunk, not cleared.",
    },
    {
        "make": "volkswagen", "model": "id.4",
        "years": (2021, 2023),
        "generation": "first gen",
        "engine": "single-motor RWD or dual-motor AWD; 62 or 82 kWh battery",
        "reliability": 5.4,
        "maintenance": 5.6,
        "annual_maintenance_usd": 400,
        "insurance_factor": 1.1,
        "tire_set_usd": 950,
        "risk": "Electrical system is about half of all complaints on both "
                "the 2021 (184 of 342) and the 2023 (234 of 470)",
        "known_issues": [
            "11 recalls on the 2021 and 14 on the 2023, six of the 2023's "
            "for the electrical system.",
            "470 complaints on the 2023, with electrical at 234 and nine "
            "fires reported.",
            "Slow, buggy infotainment and 12-volt battery failures that "
            "leave the car unable to start are the everyday complaints. "
            "Check the software version and the 12-volt battery date.",
            "Servicing is cheap (no oil changes), and the battery carries an "
            "8-year or 100,000-mile warranty. Confirm the door handle recall "
            "is closed.",
        ],
        "note": "Cheap used and cheap to run, with a long electrical file. "
                "Buy one only with every recall and software update done.",
    },
    {
        "make": "volkswagen", "model": "golf",
        "years": (2015, 2021),
        "generation": "Mk7",
        "engine": "1.8L TSI turbo I4 (1.4L from 2019); manual or automatic",
        "reliability": 6.6,
        "maintenance": 6.6,
        "annual_maintenance_usd": 620,
        "insurance_factor": 0.98,
        "tire_set_usd": 640,
        "risk": None,
        "known_issues": [
            "12 recalls on the 2015 (four for the fuel system), nine on the "
            "2016 and six on the 2019.",
            "131 complaints on the 2015 and 82 on the 2019, with engine the "
            "largest group on the 2019 (37).",
            "Water pump and thermostat housing leaks are the common repair. "
            "Look for dried coolant on the engine and ask if it has been "
            "replaced.",
            "2015 TDI diesels were part of the emissions settlement. Confirm "
            "the fix and what extended warranty remains.",
        ],
        "note": "A well-made small hatchback with average dependability. The "
                "early years carry the most campaigns; a 2018 or later is "
                "the easier buy.",
    },
    {
        "make": "volkswagen", "model": "golf gti",
        "years": (2022, 2026),
        "generation": "Mk8",
        "engine": "2.0L TSI turbo I4; 7-speed dual-clutch (6-speed manual to "
                  "2024)",
        "reliability": 6.5,
        "maintenance": 6.2,
        "annual_maintenance_usd": 720,
        "insurance_factor": 1.1,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2022 and two on the 2024.",
            "110 complaints on the 2022, led by forward collision avoidance "
            "(32) and power train (25).",
            "2022 to 2024 cars use touch sliders and touch-sensitive wheel "
            "buttons that owners dislike. The 2025 facelift brought back "
            "real buttons on the wheel.",
            "Many are modified. Ask about engine tunes, which can void the "
            "powertrain warranty and shorten clutch life.",
        ],
        "note": "Mechanically sound and quick. The complaints are mostly "
                "about driver-assist behaviour and the controls, not the "
                "engine.",
    },
    {
        "make": "volkswagen", "model": "golf gti",
        "years": (2015, 2021),
        "generation": "Mk7",
        "engine": "2.0L TSI turbo I4; 6-speed manual or dual-clutch "
                  "automatic",
        "reliability": 6.6,
        "maintenance": 6.2,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.1,
        "tire_set_usd": 800,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2015 and three on the 2018.",
            "219 complaints on the 2015, led by engine (65); only 50 on the "
            "2018.",
            "Water pump and thermostat housing leaks are the common repair, "
            "and manual cars with a tune wear out the clutch early.",
            "Many are modified. Look for aftermarket intakes and ask for the "
            "service history; an unmodified car is worth paying more for.",
        ],
        "note": "A durable engine in a well-made car. Later years have the "
                "shorter file, and condition matters more than mileage.",
    },
    {
        "make": "volkswagen", "model": "passat",
        "years": (2020, 2022),
        "generation": "NMS, final facelift",
        "engine": "2.0L TSI turbo I4, 6-speed automatic",
        "reliability": 7.0,
        "maintenance": 6.6,
        "annual_maintenance_usd": 620,
        "insurance_factor": 0.98,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "Three recalls and 18 complaints on the 2020; one recall and two "
            "complaints on the 2021. It sold in small numbers, so the files "
            "are small.",
            "An old design by 2020: a simple 6-speed automatic and a proven "
            "engine, with no dual-clutch gearbox to worry about.",
            "Volkswagen parts and labour run above the Japanese and Korean "
            "brands, and independent shops willing to work on them are "
            "thinner on the ground outside big cities.",
        ],
        "note": "A big, simple sedan with a short file. Discontinued after "
                "2022, so check that trim parts are still easy to get.",
    },
    {
        "make": "volkswagen", "model": "passat",
        "years": (2015, 2019),
        "generation": "NMS",
        "engine": "1.8L TSI turbo I4 (2.0L from 2018); V6 to 2018, TDI "
                  "diesel in 2015",
        "reliability": 6.5,
        "maintenance": 6.6,
        "annual_maintenance_usd": 630,
        "insurance_factor": 0.98,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "Seven recalls on the 2015, five on the 2016 and four on the "
            "2018.",
            "243 complaints on the 2015, with air bags the largest group "
            "(88); 47 on the 2018.",
            "An air bag warning light on these years is often the clock "
            "spring in the steering wheel. Have the light diagnosed before "
            "you buy.",
            "2015 TDI diesels were part of the emissions settlement. Confirm "
            "the fix and what extended warranty remains.",
        ],
        "note": "Roomy and cheap used. The record improves year by year, so "
                "a 2018 or 2019 is the one to look for.",
    },
]
