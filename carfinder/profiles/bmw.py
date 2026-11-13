"""Reliability profiles: BMW. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

NHTSA splits BMW sedans by trim: recalls are filed under names like 330I
or 528I while complaints sit under 3 SERIES or 5 SERIES. Counts quoted
here say which names they cover. Dealer feeds use the series name, so
that is the model key.
"""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "bmw", "model": "3 series",
        "years": (2019, 2026),
        "generation": "G20",
        "engine": "2.0L turbo I4 (330i) or 3.0L turbo I6 (M340i), 8-speed "
                  "automatic; 330e plug-in hybrid",
        "reliability": 7.0,
        "maintenance": 4.8,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.2,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "NHTSA files recalls under 330i and M340i: 15 campaigns across "
            "the two on the 2020, nine on the 2019, and two or three on the "
            "2023 and 2024.",
            "110 complaints on the 2020 across the 3 Series and M340i files, "
            "led by engine (61). The complaints endpoint returned nothing "
            "for 2023 and 2024.",
            "Both engines have a good record so far. The usual BMW leaks "
            "(coolant, oil filter housing) are what to look for on older "
            "cars.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "The dependable modern BMW, by the brand's standards. Early "
                "years carry the campaigns; a 2022 or later is the easier "
                "buy.",
    },
    {
        "make": "bmw", "model": "3 series",
        "years": (2017, 2018),
        "generation": "F30, later engines",
        "engine": "2.0L turbo I4 (330i) or 3.0L turbo I6 (340i), 8-speed "
                  "automatic",
        "reliability": 6.8,
        "maintenance": 4.8,
        "annual_maintenance_usd": 1000,
        "insurance_factor": 1.15,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "One recall on the 2018 330i and 61 complaints across the 3 "
            "Series file, led by engine (20) and electrical (16).",
            "These years have the newer engine family, which avoided the "
            "timing chain trouble of the 2015 to 2016 328i.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "The pick of the old-shape 3 Series: the later engines in a "
                "well-sorted body.",
    },
    {
        "make": "bmw", "model": "3 series",
        "years": (2015, 2016),
        "generation": "F30",
        "engine": "2.0L turbo I4 (320i, 328i) or 3.0L turbo I6 (335i, 340i), "
                  "8-speed automatic",
        "reliability": 6.0,
        "maintenance": 4.8,
        "annual_maintenance_usd": 1050,
        "insurance_factor": 1.15,
        "tire_set_usd": 950,
        "risk": "The N20 four-cylinder (the 28i engine) has a known timing "
                "chain guide failure that can destroy the engine; later "
                "builds have revised parts, so ask for proof of which a car "
                "has",
        "known_issues": [
            "Five recalls on the 2015 328i and 160 complaints across the "
            "320i and 328i, led by electrical (61) and engine cooling (42), "
            "with nine fires reported.",
            "Ask for evidence of timing chain work on any four-cylinder, and "
            "listen for a whine from the front of the engine.",
            "Oil leaks from the valve cover and oil filter housing gaskets "
            "are routine at this age. Look under the car.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "A good car to drive with one expensive weakness. A "
                "six-cylinder, or a 2017 or later four, is the safer choice.",
    },
    {
        "make": "bmw", "model": "5 series",
        "years": (2024, 2026),
        "generation": "G60",
        "engine": "2.0L turbo I4 (530i) or 3.0L turbo I6 (540i), mild "
                  "hybrid, 8-speed automatic",
        "reliability": 6.6,
        "maintenance": 4.4,
        "annual_maintenance_usd": 1050,
        "insurance_factor": 1.25,
        "tire_set_usd": 1150,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2024 530i, the first year of this "
            "generation.",
            "Service brakes lead the small 2024 file (13 of 18 complaints "
            "across 530i and 540i), which matches BMW's recall of the brake "
            "control unit. Confirm that recall is closed.",
            "Most functions run through the touchscreen. Check that the "
            "software is current and every menu responds.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "Too new for a firm number. The engines are carried over and "
                "proven; the electronics are not yet.",
    },
    {
        "make": "bmw", "model": "5 series",
        "years": (2017, 2023),
        "generation": "G30",
        "engine": "2.0L turbo I4 (530i) or 3.0L turbo I6 (540i), 8-speed "
                  "automatic; 530e plug-in hybrid",
        "reliability": 6.9,
        "maintenance": 4.6,
        "annual_maintenance_usd": 1100,
        "insurance_factor": 1.2,
        "tire_set_usd": 1100,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2018 (530i, 540i), six on the 2020 and four "
            "on the 2022.",
            "81 complaints on the 2018, led by air bags (35) and seat belts "
            "(24); only 16 on the 2020 and 18 on the 2022.",
            "The plug-in 530e has had battery recalls of its own. Check any "
            "530e VIN separately.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "One of the better records among German luxury sedans. "
                "Costly to maintain, but not known for big failures.",
    },
    {
        "make": "bmw", "model": "5 series",
        "years": (2015, 2016),
        "generation": "F10",
        "engine": "2.0L turbo I4 (528i) or 3.0L turbo I6 (535i), 8-speed "
                  "automatic",
        "reliability": 5.8,
        "maintenance": 4.4,
        "annual_maintenance_usd": 1150,
        "insurance_factor": 1.2,
        "tire_set_usd": 1050,
        "risk": "The N20 four-cylinder (the 28i engine) has a known timing "
                "chain guide failure that can destroy the engine; later "
                "builds have revised parts, so ask for proof of which a car "
                "has",
        "known_issues": [
            "Two recalls on the 2015 528i and 88 complaints across the 528i "
            "and 535i, led by electrical (43) and engine cooling (37), with "
            "five fires reported.",
            "Ask for evidence of timing chain work on a 528i. The 535i "
            "avoids that fault but leaks oil from the usual gaskets.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "Comfortable and cheap to buy now, and expensive to keep. "
                "Prefer the six-cylinder.",
    },
    {
        "make": "bmw", "model": "x1",
        "years": (2023, 2026),
        "generation": "U11",
        "engine": "2.0L turbo I4, 7-speed dual-clutch automatic, AWD",
        "reliability": 6.3,
        "maintenance": 5.0,
        "annual_maintenance_usd": 900,
        "insurance_factor": 1.12,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2023, the first year, and three on the 2024.",
            "Service brakes are a lopsided share of complaints on the 2023 "
            "(53 of 71) and the 2024 (19 of 30), which matches BMW's recall "
            "of the brake control unit. Confirm that recall is closed.",
            "The dual-clutch gearbox can feel hesitant pulling away. Drive "
            "it in slow traffic before deciding.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "A roomy small SUV whose file is dominated by one recalled "
                "brake fault. With that closed, the rest is quiet so far.",
    },
    {
        "make": "bmw", "model": "x1",
        "years": (2016, 2022),
        "generation": "F48",
        "engine": "2.0L turbo I4, 8-speed automatic, FWD or AWD",
        "reliability": 6.8,
        "maintenance": 5.2,
        "annual_maintenance_usd": 900,
        "insurance_factor": 1.1,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2017 and one on the 2020.",
            "156 complaints on the 2017, led by power train (57); only 13 on "
            "the 2020.",
            "Front-drive based and simpler than the bigger BMWs. Engine "
            "mounts and front control arm bushings are the usual wear items.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "One of the cheaper BMWs to own. The later years have much "
                "the shorter file.",
    },
    {
        "make": "bmw", "model": "x1",
        "years": (2015, 2015),
        "generation": "E84",
        "engine": "2.0L turbo I4 (28i) or 3.0L turbo I6 (35i), 8-speed or "
                  "6-speed automatic",
        "reliability": 5.8,
        "maintenance": 4.8,
        "annual_maintenance_usd": 1000,
        "insurance_factor": 1.1,
        "tire_set_usd": 900,
        "risk": "The N20 four-cylinder (the 28i engine) has a known timing "
                "chain guide failure that can destroy the engine; later "
                "builds have revised parts, so ask for proof of which a car "
                "has",
        "known_issues": [
            "Three recalls on the 2015. NHTSA's complaints endpoint returned "
            "nothing for this year, which is a gap, not a clean record.",
            "Ask for evidence of timing chain work on a 28i, and look for "
            "oil leaks at the valve cover and oil filter housing.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "Provisional. The last year of the old rear-drive X1: fun to "
                "drive, dated inside, and now old enough to need steady "
                "spending.",
    },
    {
        "make": "bmw", "model": "x3",
        "years": (2025, 2026),
        "generation": "G45",
        "engine": "2.0L turbo I4 (30) or 3.0L turbo I6 (M50), mild hybrid, "
                  "8-speed automatic",
        "reliability": 6.2,
        "maintenance": 4.6,
        "annual_maintenance_usd": 980,
        "insurance_factor": 1.18,
        "tire_set_usd": 1100,
        "risk": None,
        "known_issues": [
            "Nine recalls on the 2025, the first year of this generation, "
            "including two each for steering, brakes, air bags and "
            "electrical.",
            "38 complaints on the 2025, led by electrical (15), steering (8) "
            "and forward collision avoidance (8).",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "Too new for a firm number, and nine campaigns in the first "
                "year is a rough start. The outgoing 2022 to 2024 X3 is the "
                "safer buy.",
    },
    {
        "make": "bmw", "model": "x3",
        "years": (2018, 2024),
        "generation": "G01",
        "engine": "2.0L turbo I4 (30i) or 3.0L turbo I6 (M40i), 8-speed "
                  "automatic; 30e plug-in hybrid",
        "reliability": 7.0,
        "maintenance": 4.8,
        "annual_maintenance_usd": 980,
        "insurance_factor": 1.15,
        "tire_set_usd": 1050,
        "risk": None,
        "known_issues": [
            "10 recalls on the 2019 and on the 2021; four on the 2023.",
            "171 complaints on the 2019 and 117 on the 2021, led by "
            "electrical (47 and 35); just 17 on the 2023.",
            "Both gas engines have a good record. Check the plug-in 30e VIN "
            "separately for battery recalls.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "A sound choice among luxury compact SUVs, and the 2022 to "
                "2024 cars have the shortest file.",
    },
    {
        "make": "bmw", "model": "x3",
        "years": (2015, 2017),
        "generation": "F25",
        "engine": "2.0L turbo I4 (28i), 3.0L turbo I6 (35i) or 2.0L diesel "
                  "(28d), 8-speed automatic",
        "reliability": 6.0,
        "maintenance": 4.6,
        "annual_maintenance_usd": 1050,
        "insurance_factor": 1.12,
        "tire_set_usd": 1000,
        "risk": "The N20 four-cylinder (the 28i engine) has a known timing "
                "chain guide failure that can destroy the engine; later "
                "builds have revised parts, so ask for proof of which a car "
                "has",
        "known_issues": [
            "Eight recalls on the 2015 and seven on the 2017.",
            "92 complaints on the 2017, led by electrical (30) and engine "
            "cooling (22). The complaints endpoint returned nothing for the "
            "2015.",
            "Ask for evidence of timing chain work on a 28i. Oil leaks and "
            "transfer case wear are the other things to check.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "Practical and cheap to buy now. The 35i six is the engine "
                "to have.",
    },
    {
        "make": "bmw", "model": "x5",
        "years": (2024, 2026),
        "generation": "G05 facelift",
        "engine": "3.0L turbo I6 (40i), 4.4L turbo V8 (M60i) or plug-in "
                  "hybrid (50e); 8-speed automatic",
        "reliability": 6.0,
        "maintenance": 4.2,
        "annual_maintenance_usd": 1250,
        "insurance_factor": 1.28,
        "tire_set_usd": 1400,
        "risk": None,
        "known_issues": [
            "Eight recalls on the 2024.",
            "Service brakes are a lopsided share of the 2024 complaints (90 "
            "of 145), which matches BMW's recall of the brake control unit. "
            "Confirm that recall is closed.",
            "The six-cylinder 40i is the dependable choice. The V8 costs far "
            "more to maintain and has a poorer history.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "A good SUV with one recalled brake fault dominating the "
                "file. Make sure that work is done.",
    },
    {
        "make": "bmw", "model": "x5",
        "years": (2019, 2023),
        "generation": "G05",
        "engine": "3.0L turbo I6 (40i), 4.4L turbo V8 (50i, M50i) or plug-in "
                  "hybrid (45e); 8-speed automatic",
        "reliability": 6.3,
        "maintenance": 4.2,
        "annual_maintenance_usd": 1250,
        "insurance_factor": 1.25,
        "tire_set_usd": 1350,
        "risk": None,
        "known_issues": [
            "13 recalls on the 2019, 12 on the 2021 and four on the 2023.",
            "195 complaints on the 2019, led by electrical (72) and engine "
            "(52); 114 on the 2021 and 34 on the 2023.",
            "Air suspension, where fitted, is the big-ticket item as these "
            "age. Check the car sits level after standing overnight.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "The 40i is one of the better large luxury SUVs to own. The "
                "2019 launch year has the longest file; later is better.",
    },
    {
        "make": "bmw", "model": "x5",
        "years": (2015, 2018),
        "generation": "F15",
        "engine": "3.0L turbo I6 (35i), 4.4L turbo V8 (50i), 3.0L diesel "
                  "(35d) or plug-in hybrid (40e); 8-speed automatic",
        "reliability": 5.6,
        "maintenance": 4.2,
        "annual_maintenance_usd": 1300,
        "insurance_factor": 1.25,
        "tire_set_usd": 1300,
        "risk": "The V8 (xDrive50i) is known for heavy oil consumption, "
                "valve stem seal wear and turbo coolant line leaks; the "
                "six-cylinder 35i is the one to buy",
        "known_issues": [
            "Six recalls on the 2015 and seven on the 2017.",
            "76 complaints on the 2017, led by electrical (17) and fuel "
            "system (15). The complaints endpoint returned nothing for the "
            "2015.",
            "Rear air suspension bags and the transfer case are common "
            "repairs past 80,000 miles.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "Cheap to buy and costly to keep. Stick to the 35i, and "
                "budget for suspension work.",
    },
    {
        "make": "bmw", "model": "x7",
        "years": (2019, 2026),
        "generation": "G07",
        "engine": "3.0L turbo I6 (40i) or 4.4L turbo V8; 8-speed automatic, "
                  "air suspension standard",
        "reliability": 5.9,
        "maintenance": 4.0,
        "annual_maintenance_usd": 1400,
        "insurance_factor": 1.3,
        "tire_set_usd": 1500,
        "risk": None,
        "known_issues": [
            "11 recalls on the 2019, 12 on the 2020 and eight on the 2023.",
            "48 complaints on the 2019 and 56 on the 2020, led by electrical "
            "and power train. On the 2023, service brakes lead (26 of 44), "
            "which matches BMW's recall of the brake control unit. Confirm "
            "that recall is closed.",
            "Every X7 has air suspension, which is a certain cost as the car "
            "ages. Check it holds height overnight.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "A fine big SUV with a long recall list and high running "
                "costs. Best owned under warranty.",
    },
    {
        "make": "bmw", "model": "4 series",
        "years": (2021, 2026),
        "generation": "G22",
        "engine": "2.0L turbo I4 (430i) or 3.0L turbo I6 (M440i), 8-speed "
                  "automatic",
        "reliability": 7.0,
        "maintenance": 4.8,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.25,
        "tire_set_usd": 1050,
        "risk": None,
        "known_issues": [
            "Seven recalls across the 2021 430i and M440i; three on the "
            "2023.",
            "21 complaints on the 2021, led by electrical (7). The "
            "complaints endpoint returned nothing for the 2023.",
            "Mechanically a 3 Series, so the same engines and the same good "
            "record apply.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "As dependable as the 3 Series it is based on. Insurance "
                "runs a little higher for the coupe and convertible.",
    },
    {
        "make": "bmw", "model": "4 series",
        "years": (2017, 2020),
        "generation": "F32, later engines",
        "engine": "2.0L turbo I4 (430i) or 3.0L turbo I6 (440i), 8-speed "
                  "automatic",
        "reliability": 6.8,
        "maintenance": 4.8,
        "annual_maintenance_usd": 1000,
        "insurance_factor": 1.2,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "One recall on the 2018 430i and 34 complaints across the 4 "
            "Series file, led by engine (10).",
            "These years have the newer engine family, which avoided the "
            "timing chain trouble of the 2015 to 2016 428i.",
            "On convertibles, run the folding hard top through a full cycle "
            "and check the trunk for water.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "The better years of the first 4 Series.",
    },
    {
        "make": "bmw", "model": "4 series",
        "years": (2015, 2016),
        "generation": "F32",
        "engine": "2.0L turbo I4 (428i) or 3.0L turbo I6 (435i), 8-speed "
                  "automatic",
        "reliability": 6.0,
        "maintenance": 4.8,
        "annual_maintenance_usd": 1050,
        "insurance_factor": 1.2,
        "tire_set_usd": 1000,
        "risk": "The N20 four-cylinder (the 28i engine) has a known timing "
                "chain guide failure that can destroy the engine; later "
                "builds have revised parts, so ask for proof of which a car "
                "has",
        "known_issues": [
            "Six recalls on the 2015 428i and 94 complaints across the 428i "
            "and 435i, led by electrical (37) and engine cooling (26), with "
            "four fires reported.",
            "Ask for evidence of timing chain work on a 428i, and look for "
            "oil leaks at the valve cover and oil filter housing.",
            "Out of warranty, expect luxury-brand parts prices: plastic "
            "cooling parts, oil leaks at gaskets and run-flat tires are the "
            "routine costs. An independent BMW specialist cuts the bills a "
            "lot.",
        ],
        "note": "Good looking and good to drive, with the 328i's engine "
                "risk. Prefer the 435i or a 2017 or later car.",
    },
    {
        "make": "bmw", "model": "i4",
        "years": (2022, 2026),
        "generation": "G26",
        "engine": "single-motor RWD (eDrive35, eDrive40) or dual-motor AWD "
                  "(xDrive40, M50); roughly 67 or 81 kWh battery",
        "reliability": 6.8,
        "maintenance": 4.8,
        "annual_maintenance_usd": 450,
        "insurance_factor": 1.25,
        "tire_set_usd": 1200,
        "risk": None,
        "known_issues": [
            "Eight recalls on the 2022, seven on the 2023 and three on the "
            "2024. On the 2022 and 2023 nearly all sit under electrical "
            "system, which on an EV includes the high-voltage battery and "
            "its software.",
            "Only 10 complaints on the 2022. The complaints endpoint "
            "returned nothing for 2023 and 2024, which is a gap, not a clean "
            "record.",
            "Check that every battery-related recall is closed, and ask for "
            "a battery health report. Battery warranty is 8 years or 100,000 "
            "miles.",
            "Servicing is cheap for a BMW (no oil changes), but tires wear "
            "quickly on the M50 and crash repair is priced like any BMW.",
        ],
        "note": "A well-built EV on a proven 4 Series body. The recall list "
                "is almost all battery and software work, so make sure it is "
                "done.",
    },
    {
        "make": "bmw", "model": "ix",
        "years": (2022, 2026),
        "generation": "I20",
        "engine": "dual-motor AWD; roughly 95 to 110 kWh battery",
        "reliability": 6.4,
        "maintenance": 4.2,
        "annual_maintenance_usd": 550,
        "insurance_factor": 1.3,
        "tire_set_usd": 1500,
        "risk": None,
        "known_issues": [
            "11 recalls on the 2022, 12 on the 2023 and four on the 2024. "
            "Most are filed under electrical system, which on an EV includes "
            "the high-voltage battery and its software.",
            "32 complaints on the 2022, 38 on the 2023 and 34 on the 2024. "
            "Electrical leads the 2022 and 2024, air bags the 2023.",
            "The body uses carbon fibre and aluminium, so crash repair needs "
            "a certified shop and insurers price that in.",
            "Servicing is light (no oil changes). Battery warranty is 8 "
            "years or 100,000 miles; check that every battery recall is "
            "closed.",
        ],
        "note": "Comfortable, fast and efficient, with a long list of "
                "battery and software campaigns in its first two years. A "
                "2024 or later is the calmer buy.",
    },
]
