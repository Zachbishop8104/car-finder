"""Reliability profiles: Gmc. The format and the caveats on reading
these numbers are in carfinder/reliability.py."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "gmc", "model": "terrain",
        "years": (2022, 2024),
        "generation": "second gen, facelifted",
        "engine": "1.5L LYX turbo I4, 9-speed automatic; AWD available",
        "reliability": 6.7,
        "maintenance": 7.6,
        "annual_maintenance_usd": 540,
        "insurance_factor": 0.98,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "Power train is the top complaint component on the 2024: "
            "20 of 48 filings, and engine and fuel add 21 more. Roughly "
            "two-thirds of the file is powertrain-adjacent.",
            "The 2023 shows the same shape: engine 14 and fuel 14 out "
            "of 37.",
            "Recalls are light: 23V869000 (door) on the 2024, and on "
            "the 2023 an airbag occupant sensor plus a child-seat "
            "anchor campaign.",
            "The 1.5L turbo four is adequate rather than strong, and "
            "the 9-speed hunts.",
            "Depreciated 20.2%/yr in one Michigan market (Aug 2026), among "
            "the steepest measured for these profiles. If your local curve "
            "looks similar, that costs more than any repair.",
        ],
        "note": "Nicely finished and easy to live with. Check the local "
                "depreciation curve, and price it against a Trailblazer or "
                "Trax before committing.",
    },
    {
        "make": "gmc", "model": "acadia",
        "years": (2020, 2023),
        "generation": "second gen, facelifted",
        "engine": "2.0L LSY turbo I4 or 3.6L LGX V6, 9-speed automatic",
        "reliability": 6.3,
        "maintenance": 7.0,
        "annual_maintenance_usd": 640,
        "insurance_factor": 1.0,
        "tire_set_usd": 780,
        "risk": "Four recalls on the 2023 including 23V172000 "
                "(automatic transmission) and 23V043000 (driveshaft)",
        "known_issues": [
            "Four recalls on the 2023, and two of them are driveline: "
            "23V172000 covers the automatic transmission and 23V043000 "
            "the driveshaft. Those are not software flashes.",
            "Power train (12) and engine (11) lead the 41 complaints, "
            "the same powertrain-heavy shape as the Terrain.",
            "Depreciated 20.3%/yr in one Michigan market (Aug 2026), "
            "effectively tied with the Terrain.",
            "Third row is small and only usable with the second row "
            "slid forward.",
        ],
        "note": "Two driveline recalls and weak resale where it was "
                "measured. Hard to make a numbers case for it.",
    },
    # Added profiles: other generations and models. Counts are
    # from NHTSA for the model year named in each line.
    {
        "make": "gmc", "model": "sierra 1500",
        "years": (2014, 2018),
        "generation": "third gen (K2XX)",
        "engine": "4.3L V6, 5.3L V8 or 6.2L V8; 6-speed automatic, with an "
                  "8-speed on 6.2L and some 5.3L trucks from 2015",
        "reliability": 6.4,
        "maintenance": 7.8,
        "annual_maintenance_usd": 730,
        "insurance_factor": 1.07,
        "tire_set_usd": 1000,
        "risk": "The 8-speed automatic on 2015-2018 trucks is known for "
                "shudder and harsh shifts, and 5.3L and 6.2L "
                "cylinder-deactivation lifters can fail",
        "known_issues": [
            "8 recalls on the 2016 and 7 on the 2018, several of them brake "
            "campaigns including 19V645000 (brake vacuum pump). Run the VIN.",
            "Power train is 131 of 306 complaints on the 2018, which fits "
            "the known 8-speed shudder.",
            "On an 8-speed truck, hold a steady 40 to 60 mph on light "
            "throttle. A vibration like rumble strips is torque converter "
            "shudder; ask whether the fluid was changed to the updated type.",
            "A ticking 5.3L or 6.2L with a misfire code points to a "
            "collapsed cylinder-deactivation lifter. Walk away or price in "
            "the repair.",
        ],
        "note": "The Silverado's twin, with the same two weak spots. The "
                "6-speed trucks are the safer buy.",
    },
    {
        "make": "gmc", "model": "sierra 1500",
        "years": (2019, 2021),
        "generation": "fourth gen (T1), before the 2022 refresh",
        "engine": "2.7L turbo I4, 4.3L V6, 5.3L V8, 6.2L V8 or 3.0L Duramax "
                  "diesel; 6-, 8- or 10-speed automatic",
        "reliability": 5.5,
        "maintenance": 7.4,
        "annual_maintenance_usd": 770,
        "insurance_factor": 1.1,
        "tire_set_usd": 1050,
        "risk": "Engine is more than half the complaint file on the 2021 "
                "(328 of 606), and valve lifter failures on the 5.3L and "
                "6.2L V8 are the well documented cause",
        "known_issues": [
            "Engine is 245 of 486 complaints on the 2020 and 328 of 606 on "
            "the 2021. A share that size is not a sales-volume effect.",
            "12 recalls on the 2020 and 7 on the 2021, including 24V797000 "
            "(transmission control valve) on both.",
            "Ask for service records showing lifter or camshaft work. A "
            "truck that already had the repair is a better bet than one that "
            "has not.",
            "Denali trims add adaptive dampers and more electronics to "
            "maintain. The engine risk is the same on every trim.",
        ],
        "note": "The weakest stretch of the modern Sierra. Buy only with "
                "records and a price that reflects the engine risk.",
    },
    {
        "make": "gmc", "model": "sierra 1500",
        "years": (2022, 2026),
        "generation": "fourth gen (T1), refreshed interior",
        "engine": "2.7L turbo I4, 5.3L V8, 6.2L V8 or 3.0L Duramax diesel; "
                  "8- or 10-speed automatic",
        "reliability": 6.0,
        "maintenance": 7.4,
        "annual_maintenance_usd": 750,
        "insurance_factor": 1.12,
        "tire_set_usd": 1100,
        "risk": "Recall 25V274000 covers 6.2L V8 engines on 2021-2024 trucks "
                "for internal damage that can end in engine failure",
        "known_issues": [
            "Engine is 219 of 520 complaints on the 2023 and 192 of 386 on "
            "the 2024, about half the file on the later year.",
            "Structure is 97 of the 2023 filings: owners describe the upper "
            "grille deflector breaking off at highway speed. Check that it "
            "is secure.",
            "3 recalls on the 2023 and 1 on the 2024. On a 6.2L, confirm "
            "25V274000 was done and ask what the dealer found.",
            "The 2.7L turbo four and the 3.0L diesel avoid the V8 lifter "
            "question entirely and are worth a look.",
        ],
        "note": "Fewer recalls than the 2019-2021 trucks, but the engine "
                "complaints have not gone away. Engine choice matters more "
                "than trim.",
    },
    {
        "make": "gmc", "model": "sierra 2500hd",
        "years": (2015, 2019),
        "generation": "third gen HD (K2XX)",
        "engine": "6.0L gas V8 with a 6-speed automatic, or 6.6L Duramax "
                  "diesel with an Allison 6-speed",
        "reliability": 7.2,
        "maintenance": 6.6,
        "annual_maintenance_usd": 910,
        "insurance_factor": 1.1,
        "tire_set_usd": 1300,
        "risk": "The 2015-2016 Duramax (LML) uses a CP4 fuel pump that can "
                "fail and send metal through the whole fuel system, a repair "
                "that runs to several thousand dollars",
        "known_issues": [
            "6 recalls and 98 complaints on the 2017, with power train (29) "
            "and service brakes (28) leading and no lopsided cluster.",
            "Check the VIN for 19V328000 (filed under engine) and, on "
            "diesels with two tanks, 23V047000 (fuel tank).",
            "The 6.0L gas V8 is thirsty but simple and long lived. For a "
            "truck that tows now and then it is the cheaper one to own.",
            "Diesel emissions parts (DEF system, particulate filter) are "
            "costly out of warranty. Ask for records.",
        ],
        "note": "A sturdy work truck. The gas engine is the low-risk choice; "
                "the 2017-on diesel is the one to want if you tow heavy.",
    },
    {
        "make": "gmc", "model": "sierra 2500hd",
        "years": (2020, 2023),
        "generation": "fourth gen HD (T1)",
        "engine": "6.6L gas V8 with a 6-speed automatic, or 6.6L Duramax "
                  "diesel with an Allison 10-speed",
        "reliability": 7.3,
        "maintenance": 6.4,
        "annual_maintenance_usd": 930,
        "insurance_factor": 1.12,
        "tire_set_usd": 1350,
        "risk": None,
        "known_issues": [
            "6 recalls on the 2021, including 24V797000 (transmission "
            "control valve) and 21V758000 (electronic brake assist). Confirm "
            "both.",
            "53 complaints on the 2021, led by power train (13). A small "
            "file.",
            "Diesel emissions parts (DEF system, particulate filter) are "
            "costly out of warranty. Ask for records.",
            "Heavy truck tires and brakes cost real money. Check both before "
            "you agree a price.",
        ],
        "note": "Quieter in the data than the half-ton trucks of the same "
                "years. Running costs are high because everything on it is "
                "big.",
    },
    {
        "make": "gmc", "model": "sierra 2500hd",
        "years": (2024, 2026),
        "generation": "fourth gen HD (T1), refreshed",
        "engine": "6.6L gas V8 or 6.6L Duramax diesel, both with an Allison "
                  "10-speed automatic",
        "reliability": 7.0,
        "maintenance": 6.3,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.14,
        "tire_set_usd": 1400,
        "risk": None,
        "known_issues": [
            "4 recalls on the 2024, including 23V549000 (steering gear "
            "shaft). Confirm it was done.",
            "108 complaints on the 2024, led by electrical (33) and power "
            "train (27). Check every screen, camera and trailer function on "
            "the test drive.",
            "Diesel emissions parts (DEF system, particulate filter) are "
            "costly out of warranty. Ask for records.",
            "Too new for a long-term read. Treat the score as provisional.",
        ],
        "note": "The same strong frame and engines with a new cabin. The "
                "electronics are where the early complaints are.",
    },
    {
        "make": "gmc", "model": "canyon",
        "years": (2015, 2022),
        "generation": "second gen",
        "engine": "2.5L I4, 3.6L V6 or 2.8L Duramax diesel; 6-speed "
                  "automatic, with an 8-speed on the V6 from 2017",
        "reliability": 6.6,
        "maintenance": 7.6,
        "annual_maintenance_usd": 610,
        "insurance_factor": 1.02,
        "tire_set_usd": 850,
        "risk": "Loss of power steering on 2015-2016 trucks (steering is 182 "
                "of 273 complaints on the 2016) and 8-speed torque converter "
                "shudder on 2017-2019 V6 trucks",
        "known_issues": [
            "Steering is two-thirds of the 2016 complaint file, 182 of 273. "
            "On a 2015 or 2016, ask whether the steering gear was replaced.",
            "4 recalls on the 2016, including 18V358000 (fuel pump). The API "
            "returned none for the 2019, and only 17 complaints.",
            "On a 2017-2019 V6, drive at steady light throttle and feel for "
            "a vibration from the 8-speed.",
            "2020-2022 trucks are the settled years of this generation.",
        ],
        "note": "A Colorado with a nicer cabin. Pick the year with care; "
                "later is better.",
    },
    {
        "make": "gmc", "model": "canyon",
        "years": (2023, 2026),
        "generation": "third gen",
        "engine": "2.7L turbo I4, 8-speed automatic",
        "reliability": 6.4,
        "maintenance": 7.3,
        "annual_maintenance_usd": 630,
        "insurance_factor": 1.04,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "Exterior lighting is 159 of 208 complaints on the 2024. Owners "
            "describe the turn signal flashing the wrong side after it "
            "cancels, and headlights that flicker. Test both at night.",
            "3 recalls on the 2023, including 24V133000 (front camera "
            "module), and 3 on the 2024, including 24V491000 (fuel pump lock "
            "ring).",
            "Early trucks drew software complaints. Confirm that module "
            "updates are done.",
            "One engine for every trim, shared with the Silverado, so parts "
            "and know-how are easy to find.",
        ],
        "note": "A much nicer truck than the one it replaced, still working "
                "through first-generation electronics. Provisional score.",
    },
    {
        "make": "gmc", "model": "yukon",
        "years": (2015, 2020),
        "generation": "fourth gen (K2XX)",
        "engine": "5.3L V8 with a 6-speed automatic; Denali has a 6.2L V8 "
                  "with an 8- or 10-speed",
        "reliability": 6.9,
        "maintenance": 7.3,
        "annual_maintenance_usd": 800,
        "insurance_factor": 1.08,
        "tire_set_usd": 1100,
        "risk": None,
        "known_issues": [
            "Exterior lighting is 104 of 271 complaints on the 2016: the LED "
            "tail lights fail. Check both, and price in a replacement if one "
            "is out.",
            "Service brakes are 55 of the 2016 filings. Recall 19V645000 "
            "(brake vacuum pump) covers 2016 and 2018 trucks; confirm it.",
            "The 2018 file is smaller: 3 recalls and 71 complaints, engine "
            "leading with 28.",
            "The V8s can collapse a cylinder-deactivation lifter, and the "
            "Denali's 8-speed can shudder. Test drive it cold.",
        ],
        "note": "A Tahoe in better clothes. The 5.3L and 6-speed is the "
                "low-risk pairing; the Denali costs more to keep.",
    },
    {
        "make": "gmc", "model": "yukon",
        "years": (2021, 2026),
        "generation": "fifth gen (T1)",
        "engine": "5.3L V8, 6.2L V8 or 3.0L Duramax diesel, 10-speed "
                  "automatic",
        "reliability": 5.4,
        "maintenance": 6.9,
        "annual_maintenance_usd": 880,
        "insurance_factor": 1.12,
        "tire_set_usd": 1200,
        "risk": "13 recalls on the 2021 and engine at more than half of all "
                "complaints, with V8 lifter failures and the 6.2L recall "
                "25V274000 behind it",
        "known_issues": [
            "13 recalls on the 2021 and 4 on the 2023. Recall count does not "
            "scale with sales, so 13 is a bad number on its own.",
            "Engine is 191 of 350 complaints on the 2021 and 162 of 249 on "
            "the 2023. That is 55% and 65% of the file.",
            "On a 6.2L, confirm 25V274000 was completed. On any V8, ask for "
            "records of lifter or camshaft repairs.",
            "The 3.0L diesel sidesteps the lifter problem and uses far less "
            "fuel.",
        ],
        "note": "Comfortable and capable, with the most engine-heavy "
                "complaint file of the GM full-size trio. Favor the diesel.",
    },
    {
        "make": "gmc", "model": "yukon xl",
        "years": (2015, 2020),
        "generation": "fourth gen (K2XX)",
        "engine": "5.3L V8 with a 6-speed automatic; Denali has a 6.2L V8 "
                  "with an 8- or 10-speed",
        "reliability": 6.9,
        "maintenance": 7.3,
        "annual_maintenance_usd": 820,
        "insurance_factor": 1.08,
        "tire_set_usd": 1100,
        "risk": None,
        "known_issues": [
            "NHTSA's complaints endpoint returned nothing for the 2016 and "
            "2018 Yukon XL while returning full files for the Yukon. That is "
            "a gap in the data, not a clean record.",
            "3 recalls came back for the 2016: two air bag campaigns and "
            "16V256000 (front control arm).",
            "Read the Yukon's file: failed LED tail lights and brake vacuum "
            "pump complaints apply here too.",
            "The V8s can collapse a cylinder-deactivation lifter, and the "
            "Denali's 8-speed can shudder. Test drive it cold.",
        ],
        "note": "Mechanically a longer Yukon. The score is provisional "
                "because the complaint data is missing.",
    },
    {
        "make": "gmc", "model": "yukon xl",
        "years": (2021, 2026),
        "generation": "fifth gen (T1)",
        "engine": "5.3L V8, 6.2L V8 or 3.0L Duramax diesel, 10-speed "
                  "automatic",
        "reliability": 5.4,
        "maintenance": 6.9,
        "annual_maintenance_usd": 900,
        "insurance_factor": 1.12,
        "tire_set_usd": 1200,
        "risk": "12 recalls on the 2021 and engine at about two-thirds of "
                "all complaints, with V8 lifter failures and the 6.2L recall "
                "25V274000 behind it",
        "known_issues": [
            "12 recalls on the 2021 and 4 on the 2023.",
            "Engine is 148 of 237 complaints on the 2021 and 155 of 230 on "
            "the 2023, about two-thirds of the file on the later year.",
            "On a 6.2L, confirm 25V274000 was completed. On any V8, ask for "
            "records of lifter or camshaft repairs.",
            "The 3.0L diesel sidesteps the lifter problem and uses far less "
            "fuel.",
        ],
        "note": "Same story as the Yukon: a fine long-haul family truck with "
                "a real engine risk. Favor the diesel.",
    },
    {
        "make": "gmc", "model": "terrain",
        "years": (2015, 2017),
        "generation": "first gen, late years",
        "engine": "2.4L I4 or 3.6L V6, 6-speed automatic",
        "reliability": 5.9,
        "maintenance": 7.6,
        "annual_maintenance_usd": 600,
        "insurance_factor": 0.97,
        "tire_set_usd": 680,
        "risk": "The 2.4L four is known for burning oil, and engine ties for "
                "the top complaint on the 2016 (46 of 153)",
        "known_issues": [
            "Engine and visibility/wiper lead the 2016 file with 46 each out "
            "of 153.",
            "Check the dipstick yourself. A 2.4L that is low between changes "
            "is burning oil, and running it low wrecks the timing chain.",
            "Run the wipers on the test drive. 2 recalls on the 2016, one of "
            "them 22V137000 (headlights).",
            "The 3.6L V6 is the better engine if you can find one.",
        ],
        "note": "Cheap and roomy, but the 2.4L is a known oil burner. Buy on "
                "proof of oil level and service history, or not at all.",
    },
    {
        "make": "gmc", "model": "terrain",
        "years": (2018, 2021),
        "generation": "second gen",
        "engine": "1.5L turbo I4 with a 9-speed automatic; 2.0L turbo I4 "
                  "through 2020; 1.6L diesel in 2018-2019",
        "reliability": 6.5,
        "maintenance": 7.6,
        "annual_maintenance_usd": 550,
        "insurance_factor": 0.98,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "Service brakes lead both years pulled: 84 of 227 on the 2018 "
            "and 73 of 198 on the 2020. It is the same brake vacuum pump "
            "complaint as on the Equinox of these years.",
            "Ask whether the vacuum pump has been replaced, and watch for a "
            "'Service Brake Assist' message.",
            "5 recalls on the 2018, including 20V668000 (automatic "
            "transmission) and 17V516000 (front driveshaft). 2 on the 2020.",
            "The push-button gear selector is odd. Make sure you can live "
            "with it.",
        ],
        "note": "A fair small SUV with one specific thing to check: the "
                "brake vacuum pump.",
    },
    {
        "make": "gmc", "model": "terrain",
        "years": (2025, 2026),
        "generation": "third gen",
        "engine": "1.5L turbo I4; CVT on FWD, 8-speed automatic on AWD",
        "reliability": 6.7,
        "maintenance": 7.6,
        "annual_maintenance_usd": 540,
        "insurance_factor": 0.98,
        "tire_set_usd": 720,
        "risk": None,
        "known_issues": [
            "Only 14 complaints on the 2025 so far, and the API returned no "
            "recalls. Too little to read either way.",
            "The related 2025 Chevrolet Equinox drew 244 complaints led by "
            "electrical (82), so check every screen and driver-assist "
            "function.",
            "New body on a carried-over engine. Provisional score.",
        ],
        "note": "Too new to judge. It shares its parts with the new Equinox, "
                "so watch that car's record.",
    },
    {
        "make": "gmc", "model": "acadia",
        "years": (2015, 2016),
        "generation": "first gen, final years",
        "engine": "3.6L V6, 6-speed automatic",
        "reliability": 6.3,
        "maintenance": 6.8,
        "annual_maintenance_usd": 690,
        "insurance_factor": 1.0,
        "tire_set_usd": 800,
        "risk": None,
        "known_issues": [
            "Air bags are 108 of 261 complaints on the 2015, and three of "
            "its 4 recalls are air bag campaigns. Run the VIN and confirm "
            "they are closed.",
            "Steering (33) and electrical (32) follow. Check for power "
            "steering leaks or noise.",
            "The 3.6L wants clean oil. Stretched timing chains show up on "
            "engines with long oil change intervals, and the job is "
            "expensive.",
            "A 2017 'Acadia Limited' is this same older truck.",
        ],
        "note": "The big original Acadia at the end of its run. Roomy and "
                "cheap to buy, costly when something large fails.",
    },
    {
        "make": "gmc", "model": "acadia",
        "years": (2017, 2019),
        "generation": "second gen",
        "engine": "2.5L I4 or 3.6L V6, 6-speed automatic",
        "reliability": 6.1,
        "maintenance": 7.2,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.0,
        "tire_set_usd": 780,
        "risk": None,
        "known_issues": [
            "707 complaints on the 2017 and 399 on the 2018, with power "
            "train (236 and 164) and electrical (193 and 110) leading. Large "
            "numbers for a mid-volume model.",
            "Most trace to the 'Shift to Park' fault: the truck will not "
            "accept that it is in park and will not shut off. Ask whether "
            "the shifter was repaired.",
            "4 recalls on the 2017, including 17V516000 (front driveshaft) "
            "and 18V358000 (fuel pump).",
            "The 2020 facelift brought a 9-speed and a calmer file.",
        ],
        "note": "Smaller and lighter than the first Acadia, with one very "
                "common and annoying fault. Fixed examples are fine.",
    },
    {
        "make": "gmc", "model": "acadia",
        "years": (2024, 2026),
        "generation": "third gen",
        "engine": "2.5L turbo I4, 8-speed automatic",
        "reliability": 6.3,
        "maintenance": 7.0,
        "annual_maintenance_usd": 650,
        "insurance_factor": 1.03,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "Service brakes are the top complaint on both years: 26 of 63 on "
            "the 2024 and 41 of 69 on the 2025. Filings describe ABS and "
            "stability warnings and, in some, replaced brake hardware.",
            "The API returned no recalls for either year. Ask the dealer "
            "whether a brake bulletin applies to the VIN.",
            "A new engine and transmission for this generation, with no "
            "long-term record yet. Provisional score.",
        ],
        "note": "Back to full size and much nicer inside. The brake "
                "complaints on the first two years are worth a direct "
                "question.",
    },
]
