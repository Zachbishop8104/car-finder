"""Reliability profiles: Chevrolet. The format and the caveats on reading
these numbers are in carfinder/reliability.py."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        # Same GM platform, engine and VCU recall as the Envista. 165
        # complaints on the 2024 vs the Envista's 49, but the Trax
        # sells in far higher volume, so read the SHAPE not the total.
        "make": "chevrolet", "model": "trax",
        "years": (2024, 2026),
        "generation": "second gen",
        "engine": "1.2L turbo I3, 6-speed automatic, the same "
                  "powertrain as the Buick Envista and Encore GX",
        "reliability": 7.0,
        "maintenance": 8.5,
        "annual_maintenance_usd": 430,
        "insurance_factor": 0.92,
        "tire_set_usd": 650,
        "risk": None,
        "known_issues": [
            "Mechanically the same car as the Buick Envista underneath, for "
            "roughly $2-3k less. The Buick adds sound insulation, "
            "nicer materials and a longer standard equipment list.",
            "Recall 23V744000 (VCU/instrument cluster blanking) hits "
            "the 2024 exactly as it does the Envista. Free software "
            "fix, confirm it was done.",
            "Electrical and engine dominate the 2024 complaints (62 "
            "and 46 of 165). That lopsided shape is meaningful even "
            "after allowing for sales volume: the Envista's own file "
            "leans electrical the same way.",
            "Seven fire-related filings on the 2024. Small against the "
            "sales base, but higher than any other small SUV profiled here.",
        ],
        "note": "The value play if you don't need the Buick Envista's nicer "
                "interior. Same drive, same 30 mpg, plainer "
                "cabin.",
    },
    {
        "make": "chevrolet", "model": "trailblazer",
        "years": (2021, 2026),
        "generation": "first gen",
        "engine": "1.2L or 1.3L turbo I3, CVT on FWD and a 9-speed on "
                  "AWD; shares its family with the Trax and Envista",
        "reliability": 7.6,
        "maintenance": 8.4,
        "annual_maintenance_usd": 450,
        "insurance_factor": 0.94,
        "tire_set_usd": 660,
        "risk": None,
        "known_issues": [
            "Zero recalls on the 2024 and 32 complaints with no "
            "dominant cluster, the cleanest NHTSA file of any GM vehicle "
            "profiled here.",
            "Depreciated 12.7%/yr in one Michigan market (Aug 2026), far "
            "better than the Terrain's 20.2% in the same sample.",
            "Turbo three-cylinder, so oil service history matters.",
            "AWD is available, and AWD cars get the 9-speed automatic instead of the CVT, "
            "which is the better combination.",
            "Marketcheck files this model under two spellings, "
            "'Trailblazer' and 'TrailBlazer', split across model "
            "years. Search both or you will miss half the inventory.",
        ],
        "note": "The quiet winner among domestic small SUVs: cleanest "
                "recall record, mid-pack depreciation, AWD available, "
                "and cheaper than the GMC badge.",
    },
    {
        "make": "chevrolet", "model": "equinox",
        "years": (2022, 2024),
        "generation": "third gen, facelifted",
        "engine": "1.5L LYX turbo I4, CVT or 6-speed automatic",
        "reliability": 6.5,
        "maintenance": 7.8,
        "annual_maintenance_usd": 530,
        "insurance_factor": 0.95,
        "tire_set_usd": 680,
        "risk": "Fuel/propulsion is 42 of 92 complaints on the 2023, "
                "46% of the file on one system",
        "known_issues": [
            "Fuel and propulsion is 46% of the 2023 complaint file (42 "
            "of 92) and still the top cluster on the 2024 (20 of 71). "
            "A share that lopsided survives the sales-volume caveat.",
            "Three recalls on the 2023 covering seats, an airbag "
            "occupant sensor and child-seat anchors.",
            "Depreciated 10.8%/yr in one Michigan market (Aug 2026), one of "
            "the better domestic numbers. The Equinox's problem is the complaint "
            "file, not the resale.",
            "Roomy, cheap, and everywhere. Any shop can work on it.",
        ],
        "note": "Good value and good resale for a domestic, undercut by "
                "a persistent fuel-system complaint cluster. Worth a "
                "drive if the price is right, with the fuel history "
                "checked.",
    },
    {
        "make": "chevrolet", "model": "blazer",
        "years": (2023, 2026),
        "generation": "first gen, facelifted",
        "engine": "2.0L turbo I4 or 3.6L V6, 9-speed automatic",
        "reliability": 6.9,
        "maintenance": 7.5,
        "annual_maintenance_usd": 570,
        "insurance_factor": 1.0,
        "tire_set_usd": 760,
        "risk": None,
        "known_issues": [
            "42 complaints on the 2024, led by forward collision "
            "avoidance (10): driver-assist gripes rather than "
            "mechanical failure.",
            "One recall, 23V869000, the same door campaign as the "
            "Terrain and Equinox.",
            "The one depreciation sample behind this profile read 5.6%/yr, "
            "which is implausibly good and rested on only six points spanning "
            "two body styles and a V6/turbo-four split. Expect thin, mixed "
            "comps for this model and treat a flattering curve with "
            "suspicion.",
            "Thirsty with the V6.",
        ],
        "note": "Middling on the complaint data. If its depreciation curve "
                "looks flattering, check the sample size before leaning on "
                "it.",
    },
    # Added profiles: other generations and models. Counts are
    # from NHTSA for the model year named in each line.
    {
        "make": "chevrolet", "model": "silverado 1500",
        "years": (2014, 2018),
        "generation": "third gen (K2XX)",
        "engine": "4.3L V6, 5.3L V8 or 6.2L V8; 6-speed automatic, with an "
                  "8-speed on 6.2L and some 5.3L trucks from 2015",
        "reliability": 6.4,
        "maintenance": 7.8,
        "annual_maintenance_usd": 720,
        "insurance_factor": 1.05,
        "tire_set_usd": 1000,
        "risk": "The 8-speed automatic on 2015-2018 trucks is known for "
                "shudder and harsh shifts, and 5.3L and 6.2L "
                "cylinder-deactivation lifters can fail",
        "known_issues": [
            "12 recalls on the 2016 and 7 on the 2018. Several are brake "
            "campaigns, including 19V645000 (brake vacuum pump, loss of "
            "power assist). Run the VIN and confirm each one is closed.",
            "Service brakes lead the 2016 complaint file (266 of 801) and "
            "power train leads the 2018 (170 of 524).",
            "On an 8-speed truck, hold a steady 40 to 60 mph on light "
            "throttle. A vibration like rumble strips is torque converter "
            "shudder; ask whether the fluid was changed to the updated type.",
            "A ticking 5.3L or 6.2L with a misfire code points to a "
            "collapsed cylinder-deactivation lifter. Walk away or price in "
            "the repair.",
        ],
        "note": "A simple, easily repaired truck with two well known weak "
                "spots. The 6-speed trucks are the safer buy.",
    },
    {
        "make": "chevrolet", "model": "silverado 1500",
        "years": (2019, 2021),
        "generation": "fourth gen (T1), before the 2022 refresh",
        "engine": "2.7L turbo I4, 4.3L V6, 5.3L V8, 6.2L V8 or 3.0L Duramax "
                  "diesel; 6-, 8- or 10-speed automatic",
        "reliability": 5.6,
        "maintenance": 7.4,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.08,
        "tire_set_usd": 1050,
        "risk": "Engine is 401 of 863 complaints on the 2021, and valve "
                "lifter failures on the 5.3L and 6.2L V8 are the well "
                "documented cause",
        "known_issues": [
            "Engine is the top complaint component on both years pulled: 252 "
            "of 755 on the 2020 and 401 of 863 on the 2021. A share near "
            "half the file is not a sales-volume effect.",
            "12 recalls on the 2020 and 8 on the 2021, including 24V797000 "
            "(transmission control valve) on both and 25V274000 (6.2L "
            "engine) on the 2021.",
            "Ask for service records showing lifter or camshaft work. A "
            "truck that already had the repair is a better bet than one that "
            "has not.",
            "Power train is the second cluster (240 on the 2020). Test for "
            "harsh or delayed shifts when cold.",
        ],
        "note": "The weakest stretch of the modern Silverado. Buy only with "
                "records and a price that reflects the engine risk.",
    },
    {
        "make": "chevrolet", "model": "silverado 1500",
        "years": (2022, 2026),
        "generation": "fourth gen (T1), refreshed interior",
        "engine": "2.7L turbo I4, 5.3L V8, 6.2L V8 or 3.0L Duramax diesel; "
                  "8- or 10-speed automatic",
        "reliability": 6.2,
        "maintenance": 7.4,
        "annual_maintenance_usd": 740,
        "insurance_factor": 1.1,
        "tire_set_usd": 1100,
        "risk": "Recall 25V274000 covers 6.2L V8 engines on 2021-2024 trucks "
                "for internal damage that can end in engine failure",
        "known_issues": [
            "Engine is still close to half the file: 157 of 400 complaints "
            "on the 2023 and 154 of 325 on the 2024.",
            "Recall count is lower than on the 2019-2021 trucks: 3 on the "
            "2023 and 2 on the 2024.",
            "On a 6.2L, confirm recall 25V274000 was done and ask what the "
            "dealer found and what was replaced.",
            "The 2.7L turbo four and the 3.0L diesel avoid the V8 lifter "
            "question entirely and are worth a look.",
        ],
        "note": "Better than the 2019-2021 trucks on recalls, but the engine "
                "complaints have not gone away. Engine choice matters more "
                "than trim.",
    },
    {
        "make": "chevrolet", "model": "silverado 2500hd",
        "years": (2015, 2019),
        "generation": "third gen HD (K2XX)",
        "engine": "6.0L gas V8 with a 6-speed automatic, or 6.6L Duramax "
                  "diesel with an Allison 6-speed",
        "reliability": 7.2,
        "maintenance": 6.6,
        "annual_maintenance_usd": 900,
        "insurance_factor": 1.08,
        "tire_set_usd": 1300,
        "risk": "The 2015-2016 Duramax (LML) uses a CP4 fuel pump that can "
                "fail and send metal through the whole fuel system, a repair "
                "that runs to several thousand dollars",
        "known_issues": [
            "5 recalls and 178 complaints on the 2017, with power train (42) "
            "and service brakes (37) leading and no single lopsided cluster.",
            "Eight fire-related filings on the 2017. Check the VIN for "
            "19V328000 (filed under engine) and, on diesels with two tanks, "
            "23V047000 (fuel tank).",
            "The 6.0L gas V8 is thirsty but simple and long lived. For a "
            "truck that tows now and then it is the cheaper one to own.",
            "Diesel emissions parts (DEF system, particulate filter) are "
            "costly out of warranty. Ask for records.",
        ],
        "note": "A sturdy work truck. The gas engine is the low-risk choice; "
                "the 2017-on diesel is the one to want if you tow heavy.",
    },
    {
        "make": "chevrolet", "model": "silverado 2500hd",
        "years": (2020, 2023),
        "generation": "fourth gen HD (T1)",
        "engine": "6.6L gas V8 with a 6-speed automatic, or 6.6L Duramax "
                  "diesel with an Allison 10-speed",
        "reliability": 7.3,
        "maintenance": 6.4,
        "annual_maintenance_usd": 920,
        "insurance_factor": 1.1,
        "tire_set_usd": 1350,
        "risk": None,
        "known_issues": [
            "6 recalls on the 2021, including 24V797000 (transmission "
            "control valve) and 21V758000 (electronic brake assist). Confirm "
            "both.",
            "89 complaints on the 2021, led by power train (30). A modest "
            "file for a truck that sells in volume.",
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
        "make": "chevrolet", "model": "silverado 2500hd",
        "years": (2024, 2026),
        "generation": "fourth gen HD (T1), refreshed",
        "engine": "6.6L gas V8 or 6.6L Duramax diesel, both with an Allison "
                  "10-speed automatic",
        "reliability": 7.0,
        "maintenance": 6.3,
        "annual_maintenance_usd": 940,
        "insurance_factor": 1.12,
        "tire_set_usd": 1400,
        "risk": None,
        "known_issues": [
            "4 recalls on the 2024, including 23V549000 (steering gear "
            "shaft). Confirm it was done.",
            "145 complaints on the 2024, led by electrical (56) and service "
            "brakes (39). Check every screen, camera and trailer function on "
            "the test drive.",
            "Diesel emissions parts (DEF system, particulate filter) are "
            "costly out of warranty. Ask for records.",
            "Too new for a long-term read. Treat the score as provisional.",
        ],
        "note": "The same strong frame and engines with a new cabin. The "
                "electronics are where the early complaints are.",
    },
    {
        "make": "chevrolet", "model": "colorado",
        "years": (2015, 2022),
        "generation": "second gen",
        "engine": "2.5L I4, 3.6L V6 or 2.8L Duramax diesel; 6-speed "
                  "automatic, with an 8-speed on the V6 from 2017",
        "reliability": 6.6,
        "maintenance": 7.6,
        "annual_maintenance_usd": 600,
        "insurance_factor": 1.0,
        "tire_set_usd": 850,
        "risk": "Loss of power steering on 2015-2016 trucks (steering is 465 "
                "of 716 complaints on the 2016) and 8-speed torque converter "
                "shudder on 2017-2019 V6 trucks",
        "known_issues": [
            "Steering is about 65% of the 2016 complaint file, 465 of 716. "
            "Owners describe power steering cutting out while driving. On a "
            "2015 or 2016, ask whether the steering gear was replaced.",
            "Power train leads the 2019 file (66 of 151), which fits the "
            "known 8-speed shudder. Drive at steady light throttle and feel "
            "for a vibration.",
            "4 recalls on the 2016, including 18V358000 (fuel pump). The API "
            "returned none for the 2019.",
            "2020-2022 trucks are the settled years of this generation.",
        ],
        "note": "A handy size and cheap to keep, but pick the year with "
                "care. Later is better.",
    },
    {
        "make": "chevrolet", "model": "colorado",
        "years": (2023, 2026),
        "generation": "third gen",
        "engine": "2.7L turbo I4, 8-speed automatic",
        "reliability": 6.5,
        "maintenance": 7.3,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.02,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "3 recalls on the 2023, including 24V133000 (front camera "
            "module), and 3 on the 2024, including 24V491000 (fuel pump lock "
            "ring).",
            "Complaints are electronics more than mechanics: forward "
            "collision avoidance (46) and electrical (45) lead the 142 "
            "filings on the 2023.",
            "Early trucks drew software and battery drain complaints. Check "
            "that module updates are done and that it starts after sitting a "
            "few days.",
            "One engine for every trim, shared with the Silverado, so parts "
            "and know-how are easy to find.",
        ],
        "note": "A much nicer truck than the one it replaced, still working "
                "through first-generation electronics. Provisional score.",
    },
    {
        "make": "chevrolet", "model": "tahoe",
        "years": (2015, 2020),
        "generation": "fourth gen (K2XX)",
        "engine": "5.3L V8 with a 6-speed automatic; 6.2L V8 with a 10-speed "
                  "on some 2018-2020 trucks",
        "reliability": 6.9,
        "maintenance": 7.4,
        "annual_maintenance_usd": 780,
        "insurance_factor": 1.05,
        "tire_set_usd": 1050,
        "risk": None,
        "known_issues": [
            "Service brakes are 93 of 257 complaints on the 2016. Most "
            "describe a hard or soft pedal from a failing brake vacuum pump, "
            "the subject of recall 19V645000. Confirm it was done.",
            "The 2018 file is much smaller: 3 recalls and 106 complaints "
            "with no dominant cluster.",
            "The 5.3L can collapse a cylinder-deactivation lifter. Listen "
            "for a tick at cold start and check for misfire codes.",
            "A/C condensers are a common leak point. Make sure the air blows "
            "cold.",
        ],
        "note": "The 5.3L and 6-speed pairing is old but proven. Later years "
                "of this generation are the pick.",
    },
    {
        "make": "chevrolet", "model": "tahoe",
        "years": (2021, 2026),
        "generation": "fifth gen (T1)",
        "engine": "5.3L V8, 6.2L V8 or 3.0L Duramax diesel, 10-speed "
                  "automatic",
        "reliability": 5.5,
        "maintenance": 7.0,
        "annual_maintenance_usd": 850,
        "insurance_factor": 1.1,
        "tire_set_usd": 1150,
        "risk": "16 recalls on the 2021 and engine as the top complaint on "
                "both years pulled, with V8 lifter failures and the 6.2L "
                "recall 25V274000 behind it",
        "known_issues": [
            "16 recalls on the 2021. Recall count does not scale with sales, "
            "so that is a bad number on its own. The 2023 has 5.",
            "Engine is 173 of 468 complaints on the 2021 and 129 of 236 on "
            "the 2023, more than half the later file.",
            "On a 6.2L, confirm 25V274000 was completed. On any V8, ask for "
            "records of lifter or camshaft repairs.",
            "The 3.0L diesel sidesteps the lifter problem and uses far less "
            "fuel.",
        ],
        "note": "Roomy and pleasant, with an engine record that is hard to "
                "ignore. Favor 2023 and later, and think hard about the "
                "diesel.",
    },
    {
        "make": "chevrolet", "model": "suburban",
        "years": (2015, 2020),
        "generation": "eleventh gen (K2XX)",
        "engine": "5.3L V8 with a 6-speed automatic; 6.2L V8 with a 10-speed "
                  "on some 2019-2020 trucks",
        "reliability": 6.9,
        "maintenance": 7.4,
        "annual_maintenance_usd": 800,
        "insurance_factor": 1.05,
        "tire_set_usd": 1050,
        "risk": None,
        "known_issues": [
            "NHTSA's complaints endpoint returned nothing for the 2016 and "
            "2018 Suburban while returning full files for the Tahoe. That is "
            "a gap in the data, not a clean record.",
            "Recalls did come back: 6 on the 2016, including 19V645000 "
            "(brake vacuum pump). Confirm it was done.",
            "The 5.3L can collapse a cylinder-deactivation lifter. Listen "
            "for a tick at cold start and check for misfire codes.",
            "A/C condensers are a common leak point. Make sure the air blows "
            "cold.",
        ],
        "note": "Mechanically a longer Tahoe, so read the Tahoe's file. The "
                "score is provisional because the complaint data is missing.",
    },
    {
        "make": "chevrolet", "model": "suburban",
        "years": (2021, 2026),
        "generation": "twelfth gen (T1)",
        "engine": "5.3L V8, 6.2L V8 or 3.0L Duramax diesel, 10-speed "
                  "automatic",
        "reliability": 5.6,
        "maintenance": 7.0,
        "annual_maintenance_usd": 870,
        "insurance_factor": 1.1,
        "tire_set_usd": 1150,
        "risk": "12 recalls on the 2021 and engine as the top complaint on "
                "both years pulled, with V8 lifter failures and the 6.2L "
                "recall 25V274000 behind it",
        "known_issues": [
            "12 recalls on the 2021 and 3 on the 2023.",
            "Engine is 93 of 208 complaints on the 2021 and 69 of 134 on the "
            "2023, about half the file each time.",
            "On a 6.2L, confirm 25V274000 was completed. On any V8, ask for "
            "records of lifter or camshaft repairs.",
            "The 3.0L diesel sidesteps the lifter problem and uses far less "
            "fuel.",
        ],
        "note": "Same story as the Tahoe of these years: a fine family "
                "hauler with a real engine risk. Favor 2023 and later.",
    },
    {
        "make": "chevrolet", "model": "traverse",
        "years": (2015, 2017),
        "generation": "first gen, late years",
        "engine": "3.6L V6, 6-speed automatic",
        "reliability": 6.3,
        "maintenance": 6.8,
        "annual_maintenance_usd": 680,
        "insurance_factor": 0.98,
        "tire_set_usd": 800,
        "risk": None,
        "known_issues": [
            "Air bags are 163 of 292 complaints on the 2016. Most are owners "
            "waiting on parts for an air bag inflator recall, so check the "
            "VIN for an open air bag campaign.",
            "5 recalls on the 2016.",
            "The 3.6L wants clean oil. Stretched timing chains show up on "
            "engines with long oil change intervals, and the job is "
            "expensive because of how the engine is packaged.",
            "Power steering and A/C leaks are common at this age. Look under "
            "it.",
        ],
        "note": "An old design by these years, with most early faults worked "
                "out. Cheap to buy, not cheap to fix when something big "
                "goes.",
    },
    {
        "make": "chevrolet", "model": "traverse",
        "years": (2018, 2023),
        "generation": "second gen",
        "engine": "3.6L V6, 9-speed automatic (a 2.0L turbo I4 was offered "
                  "briefly on the RS)",
        "reliability": 6.6,
        "maintenance": 7.0,
        "annual_maintenance_usd": 640,
        "insurance_factor": 1.0,
        "tire_set_usd": 820,
        "risk": None,
        "known_issues": [
            "The first year is the one to avoid: 466 complaints on the 2018 "
            "with power train at 196, against 95 on the 2021 with no "
            "dominant cluster.",
            "2 recalls on the 2018, one of them 20V668000 (automatic "
            "transmission), and 3 on the 2021.",
            "A 'Shift to Park' message that will not clear is a known fault. "
            "Park it, shut it off and see whether it lets you lock the car.",
            "2020 and later are the calmer years.",
        ],
        "note": "A big, comfortable three-row that got better as it aged. "
                "Skip the 2018.",
    },
    {
        "make": "chevrolet", "model": "traverse",
        "years": (2024, 2026),
        "generation": "third gen",
        "engine": "2.5L turbo I4, 8-speed automatic",
        "reliability": 6.3,
        "maintenance": 7.0,
        "annual_maintenance_usd": 640,
        "insurance_factor": 1.02,
        "tire_set_usd": 880,
        "risk": None,
        "known_issues": [
            "Service brakes are 65 of 148 complaints on the 2024. Filings "
            "describe brake system warnings and, in some, a replaced master "
            "cylinder. Ask the dealer whether a brake bulletin applies to "
            "the VIN.",
            "The API returned no recalls for the 2024.",
            "A new engine and transmission for this generation, with no "
            "long-term record yet. Provisional score.",
        ],
        "note": "Too new to call. The brake complaints on the first year are "
                "worth a direct question at the dealer.",
    },
    {
        "make": "chevrolet", "model": "malibu",
        "years": (2015, 2015),
        "generation": "eighth gen, final year",
        "engine": "2.5L I4 or 2.0L turbo I4, 6-speed automatic",
        "reliability": 6.6,
        "maintenance": 8.0,
        "annual_maintenance_usd": 520,
        "insurance_factor": 1.0,
        "tire_set_usd": 620,
        "risk": None,
        "known_issues": [
            "270 complaints and 3 recalls on the 2015, with engine (70) and "
            "electrical (68) leading and nine fire-related filings.",
            "The 2.5L has engine stop-start. A weak battery makes it "
            "misbehave, so check battery age.",
            "Air bags are 49 of the filings. Make sure the air bag light "
            "comes on at start and then goes out.",
        ],
        "note": "Ordinary and cheap to keep. Nothing here is alarming, "
                "nothing is special.",
    },
    {
        "make": "chevrolet", "model": "malibu",
        "years": (2016, 2018),
        "generation": "ninth gen, early years",
        "engine": "1.5L turbo I4 with a 6-speed automatic, 2.0L turbo I4 "
                  "with an 8- or 9-speed, or 1.8L hybrid",
        "reliability": 5.9,
        "maintenance": 7.8,
        "annual_maintenance_usd": 560,
        "insurance_factor": 1.02,
        "tire_set_usd": 640,
        "risk": "Engine is 256 of 727 complaints on the 2017, and cracked "
                "pistons on the 1.5L turbo are the well documented cause",
        "known_issues": [
            "727 complaints on the 2017 against 203 on the 2020. Within one "
            "model, that drop is the signal.",
            "Owners report an 'Engine Power is Reduced' message and sudden "
            "limp mode; vehicle speed control is 136 of the 2017 filings.",
            "A rough idle or misfire on a 1.5L can mean a cracked piston. "
            "Have a shop pull codes and run a compression test before "
            "buying.",
            "4 recalls on the 2017, including 18V358000 (fuel pump).",
        ],
        "note": "The early years of this body are the ones the complaints "
                "are about. Buy a 2019 or later instead if the budget "
                "allows.",
    },
    {
        "make": "chevrolet", "model": "malibu",
        "years": (2019, 2025),
        "generation": "ninth gen, facelifted",
        "engine": "1.5L turbo I4 with a CVT; 2.0L turbo I4 with a 9-speed "
                  "through 2022",
        "reliability": 6.8,
        "maintenance": 7.8,
        "annual_maintenance_usd": 540,
        "insurance_factor": 1.02,
        "tire_set_usd": 640,
        "risk": None,
        "known_issues": [
            "203 complaints and 1 recall on the 2020; 73 complaints and 2 "
            "recalls on the 2023. A much quieter file than the 2016-2018 "
            "cars.",
            "Engine (61), power train (60) and electrical (58) are level on "
            "the 2020, with no single cluster.",
            "The CVT wants its fluid changed on schedule. Ask for the "
            "record.",
            "Many were rental cars. Check the history report and the "
            "interior wear.",
        ],
        "note": "A plain, roomy sedan that settled down after its early "
                "years. Good value used because nobody is chasing them.",
    },
    {
        "make": "chevrolet", "model": "bolt ev",
        "years": (2017, 2019),
        "generation": "first gen",
        "engine": "single electric motor, front-wheel drive, 60 kWh battery",
        "reliability": 6.4,
        "maintenance": 7.0,
        "annual_maintenance_usd": 320,
        "insurance_factor": 1.05,
        "tire_set_usd": 700,
        "risk": "Battery fire recalls 20V701000 and 21V560000 cover these "
                "years, so confirm from the VIN that the battery was "
                "replaced or the final remedy applied",
        "known_issues": [
            "6 recalls on the 2019. The battery campaigns are the ones that "
            "matter: a car with a replaced pack has a newer battery than its "
            "age suggests, so ask for the paperwork.",
            "Electrical is 85 of 179 complaints on the 2019, with ten "
            "fire-related filings.",
            "Steering is 43 of 47 complaints on the 2017. Owners describe a "
            "rack that binds and does not return to center. Turn lock to "
            "lock on the test drive.",
            "EV running costs are low: no oil changes and few brake jobs. DC "
            "fast charging tops out near 50 kW, which is slow on a road "
            "trip.",
        ],
        "note": "A good cheap EV if, and only if, the battery recall is "
                "documented as done.",
    },
    {
        "make": "chevrolet", "model": "bolt ev",
        "years": (2020, 2023),
        "generation": "first gen, restyled for 2022",
        "engine": "single electric motor, front-wheel drive, about 65 kWh "
                  "battery",
        "reliability": 7.2,
        "maintenance": 7.2,
        "annual_maintenance_usd": 300,
        "insurance_factor": 1.05,
        "tire_set_usd": 700,
        "risk": "Battery fire recall 21V650000 covers 2020-2022 cars, so "
                "confirm from the VIN that the remedy was completed",
        "known_issues": [
            "7 recalls on the 2022, three of them battery campaigns "
            "(21V650000, 24V481000, 24V812000). 3 on the 2023, none for the "
            "battery.",
            "59 complaints on the 2022 and 63 on the 2023, electrical "
            "leading both.",
            "Steering is 17 of 63 on the 2023. Check that the wheel returns "
            "to center on its own after a turn.",
            "EV running costs are low: no oil changes and few brake jobs. DC "
            "fast charging tops out near 50 kW, which is slow on a road "
            "trip.",
        ],
        "note": "One of the cheapest sound used EVs once the battery recall "
                "is confirmed. The 2023 has the cleanest recall list.",
    },
    {
        "make": "chevrolet", "model": "bolt euv",
        "years": (2022, 2023),
        "generation": "first gen",
        "engine": "single electric motor, front-wheel drive, about 65 kWh "
                  "battery",
        "reliability": 7.2,
        "maintenance": 7.2,
        "annual_maintenance_usd": 300,
        "insurance_factor": 1.05,
        "tire_set_usd": 720,
        "risk": "Battery fire recall 21V650000 covers the 2022, so confirm "
                "from the VIN that the remedy was completed",
        "known_issues": [
            "4 recalls on the 2022, three of them battery campaigns. The API "
            "returned no recalls for the 2023.",
            "119 complaints on the 2023 against 26 on the 2022, led by "
            "forward collision avoidance (31), electrical (26) and steering "
            "(25).",
            "Check that the steering wheel returns to center on its own "
            "after a turn, and that the driver-assist features work without "
            "false alarms.",
            "EV running costs are low: no oil changes and few brake jobs. DC "
            "fast charging tops out near 50 kW, which is slow on a road "
            "trip.",
        ],
        "note": "A slightly longer Bolt with more rear leg room. Same "
                "strengths, same slow fast charging.",
    },
    {
        "make": "chevrolet", "model": "equinox ev",
        "years": (2024, 2026),
        "generation": "first gen",
        "engine": "single motor front-wheel drive or dual motor all-wheel "
                  "drive, 85 kWh battery",
        "reliability": 6.6,
        "maintenance": 6.8,
        "annual_maintenance_usd": 330,
        "insurance_factor": 1.1,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "Visibility is the top complaint on both years: 58 of 108 on the "
            "2024 and 80 of 166 on the 2025. Owners describe the dashboard "
            "reflecting in the windshield in sunlight. Test drive it on a "
            "bright day.",
            "1 recall on the 2024 and 6 on the 2025, among them 24V737000 "
            "(door latch) and 25V012000 (adaptive cruise braking on AWD "
            "cars).",
            "Electrical is only 8 of 108 on the 2024, so no battery or "
            "charging pattern has shown up in the complaints yet.",
            "EV running costs are low, but the car is new. Provisional "
            "score.",
        ],
        "note": "Good range for the money and no battery pattern so far. "
                "Check the windshield glare for yourself before buying.",
    },
    {
        "make": "chevrolet", "model": "blazer ev",
        "years": (2024, 2026),
        "generation": "first gen",
        "engine": "single or dual motor; front-, rear- or all-wheel drive; "
                  "85 or 102 kWh battery",
        "reliability": 5.9,
        "maintenance": 6.5,
        "annual_maintenance_usd": 350,
        "insurance_factor": 1.15,
        "tire_set_usd": 950,
        "risk": "6 recalls on the 2024 and 4 already on the 2025, after a "
                "launch that was halted for software faults",
        "known_issues": [
            "6 recalls on the 2024, including 24V487000 (front lower control "
            "arm) and 24V320000 (wiring). 4 on the 2025.",
            "Recall 26V717000 (anti-lock brakes) covers both years. Confirm "
            "it.",
            "78 complaints on the 2024, led by forward collision avoidance "
            "(24) and electrical (21).",
            "Check the software level, and that the car charges at both a "
            "home unit and a DC fast charger, before you sign.",
        ],
        "note": "A rough start. Later builds are better sorted, but the "
                "recall list is long for a car this new.",
    },
    {
        "make": "chevrolet", "model": "corvette",
        "years": (2014, 2019),
        "generation": "C7",
        "engine": "6.2L V8 (supercharged in the Z06 and ZR1); 7-speed manual "
                  "or 8-speed automatic",
        "reliability": 7.3,
        "maintenance": 5.6,
        "annual_maintenance_usd": 900,
        "insurance_factor": 1.35,
        "tire_set_usd": 1700,
        "risk": "Cracked and bent wheels: wheels are 124 of 148 complaints "
                "on the 2019 and 59 of 105 on the 2016",
        "known_issues": [
            "Inspect every wheel inside and out for cracks or weld repairs, "
            "most of all on wide-body Grand Sport and Z06 cars. Budget for "
            "forged replacements if they are original.",
            "The 8-speed automatic can shudder at steady speed. The manual "
            "avoids it.",
            "Recalls are few: 2 on the 2016 and 1 on the 2019.",
            "The engine is quiet in the data: 4 engine filings on the 2019.",
        ],
        "note": "A strong drivetrain in a car with one odd, expensive "
                "weakness. Wheels and tires are the budget items.",
    },
    {
        "make": "chevrolet", "model": "corvette",
        "years": (2020, 2026),
        "generation": "C8, mid-engine",
        "engine": "6.2L V8 with an 8-speed dual-clutch automatic; Z06, E-Ray "
                  "and ZR1 use different drivetrains",
        "reliability": 7.2,
        "maintenance": 4.8,
        "annual_maintenance_usd": 1050,
        "insurance_factor": 1.4,
        "tire_set_usd": 1900,
        "risk": None,
        "known_issues": [
            "4 recalls on the 2020, including 20V489000 (the car can be "
            "driven with the front trunk lid open). 1 on the 2023: 25V536000 "
            "(fuel system, cars with a left-side radiator fan).",
            "Small complaint files: 34 on the 2020 and 27 on the 2023, "
            "though three of the 2023 filings involve fire.",
            "Dual-clutch transmission work is dealer-only and expensive. "
            "Check for leaks and fault codes and ask for the service "
            "history.",
            "Tires and brakes are priced like the performance they deliver.",
        ],
        "note": "Dependable for what it is. The costs are in tires, "
                "insurance and any transmission work, not in the engine.",
    },
    {
        "make": "chevrolet", "model": "camaro",
        "years": (2015, 2015),
        "generation": "fifth gen, final year",
        "engine": "3.6L V6 or 6.2L V8; 6-speed manual or automatic",
        "reliability": 7.0,
        "maintenance": 6.8,
        "annual_maintenance_usd": 650,
        "insurance_factor": 1.3,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "Electrical is 112 of 208 complaints on the 2015, many about the "
            "ignition: the key sticks in the cylinder or the switch runs "
            "hot. Cycle the key several times.",
            "2 recalls on the 2015, one of them 19E064000 (replacement flip "
            "keys).",
            "Many have been driven hard or modified. Look for uneven tire "
            "wear and signs of an aftermarket tune.",
        ],
        "note": "Sound engines in an aging body. Condition and history "
                "matter more than the model's record.",
    },
    {
        "make": "chevrolet", "model": "camaro",
        "years": (2016, 2024),
        "generation": "sixth gen",
        "engine": "2.0L turbo I4, 3.6L V6 or 6.2L V8; 6-speed manual, 8- or "
                  "10-speed automatic",
        "reliability": 7.0,
        "maintenance": 6.6,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.3,
        "tire_set_usd": 1100,
        "risk": None,
        "known_issues": [
            "Steering (58) and power train (54) lead the 191 complaints on "
            "the 2017. Recalls 19V086000 and 25V175000 both cover the "
            "electric power steering on 2017 cars.",
            "The 8-speed automatic can shudder at light throttle. 10-speed "
            "cars from 2020-2022 are covered by 25V148000 (transmission).",
            "The file shrinks with age: 33 complaints on the 2020.",
            "Many have been driven hard or modified. Look for uneven tire "
            "wear and signs of an aftermarket tune.",
        ],
        "note": "Mechanically sturdy, costly to insure, hard to see out of. "
                "A manual V8 is the one that holds its appeal.",
    },
    {
        "make": "chevrolet", "model": "cruze",
        "years": (2015, 2015),
        "generation": "first gen, final year",
        "engine": "1.8L I4 or 1.4L turbo I4; 6-speed manual or automatic",
        "reliability": 5.8,
        "maintenance": 7.6,
        "annual_maintenance_usd": 580,
        "insurance_factor": 1.0,
        "tire_set_usd": 560,
        "risk": "Coolant leaks, failed water pumps and PCV faults on the "
                "1.4L turbo are common and lead to overheating if ignored",
        "known_issues": [
            "Engine is 99 of 254 complaints on the 2015.",
            "4 recalls on the 2015, including 15V442000 (steering).",
            "Smell for coolant, look for dried residue around the water "
            "outlet and thermostat housing, and check the level with the "
            "engine cold.",
            "A hiss or whistle at idle means the PCV diaphragm in the valve "
            "cover has failed. It is a cheap part that sets off other "
            "faults.",
        ],
        "note": "Cheap for a reason. Fine if someone has already replaced "
                "the cooling system parts and can prove it.",
    },
    {
        "make": "chevrolet", "model": "cruze",
        "years": (2016, 2019),
        "generation": "second gen",
        "engine": "1.4L turbo I4 or 1.6L diesel; 6-speed manual or "
                  "automatic, 9-speed automatic on the diesel",
        "reliability": 6.3,
        "maintenance": 7.8,
        "annual_maintenance_usd": 540,
        "insurance_factor": 1.0,
        "tire_set_usd": 580,
        "risk": "Cracked pistons on 2016-2017 1.4L turbo engines are well "
                "documented, and engine is 73 of 203 complaints on the 2017",
        "known_issues": [
            "Engine leads both years pulled: 73 of 203 on the 2017 and 27 of "
            "109 on the 2018.",
            "Six fire-related filings on the 2017. Recall 18V304000 (fuel "
            "system, LS cars with a tire inflator kit) covers 2016-2018.",
            "A misfire or rough idle on a 2016 or 2017 needs a compression "
            "test before you buy.",
            "2018 and 2019 are the better years.",
        ],
        "note": "Lighter and more efficient than the first Cruze, with its "
                "own early engine fault. Buy late.",
    },
    {
        "make": "chevrolet", "model": "spark",
        "years": (2015, 2015),
        "generation": "third gen (M300), final year",
        "engine": "1.2L I4, 5-speed manual or CVT",
        "reliability": 6.0,
        "maintenance": 8.0,
        "annual_maintenance_usd": 480,
        "insurance_factor": 1.0,
        "tire_set_usd": 460,
        "risk": "The CVT on 2014-2015 cars has a poor record, and power "
                "train is 27 of 84 complaints on the 2015",
        "known_issues": [
            "5 recalls on the 2015, a lot for a car this simple.",
            "Prefer the 5-speed manual. On a CVT car, any whine, slip or "
            "judder is a reason to pass.",
            "Cheap tires and brakes, 84 hp. Fine in town, tiring on the "
            "highway.",
        ],
        "note": "Basic transport. The manual is fine; the CVT is the gamble.",
    },
    {
        "make": "chevrolet", "model": "spark",
        "years": (2016, 2022),
        "generation": "fourth gen (M400)",
        "engine": "1.4L I4, 5-speed manual or CVT",
        "reliability": 7.2,
        "maintenance": 8.4,
        "annual_maintenance_usd": 430,
        "insurance_factor": 0.98,
        "tire_set_usd": 480,
        "risk": None,
        "known_issues": [
            "Small files: 29 complaints and 1 recall on the 2017, 20 "
            "complaints and no recalls returned for the 2020.",
            "No dominant complaint cluster on either year.",
            "The CVT needs its fluid changed on schedule; the manual is the "
            "simple choice.",
            "Two fire-related filings on the 2020. Small numbers, but run "
            "the VIN for open campaigns.",
        ],
        "note": "About as cheap to run as a car gets, and quiet in the data. "
                "Slow and small, which you already know.",
    },
    {
        "make": "chevrolet", "model": "trax",
        "years": (2015, 2022),
        "generation": "first gen",
        "engine": "1.4L turbo I4, 6-speed automatic; AWD available",
        "reliability": 6.4,
        "maintenance": 7.8,
        "annual_maintenance_usd": 540,
        "insurance_factor": 0.95,
        "tire_set_usd": 620,
        "risk": None,
        "known_issues": [
            "Engine leads the file on older cars: 46 of 120 complaints on "
            "the 2016 and 37 of 136 on the 2019. Turbo, coolant leak and PCV "
            "faults are the usual stories.",
            "Recalls 19V652000 (2015-2018) and 19V312000 (2017-2019) cover a "
            "front lower control arm joint. Confirm from the VIN.",
            "The 2021 is far quieter: 26 complaints and no recalls returned.",
            "Check the coolant level cold and look for oil around the turbo.",
        ],
        "note": "An older, simpler car than the 2024 Trax that replaced it "
                "(there was no 2023 model). Late years are fine cheap "
                "transport.",
    },
    {
        "make": "chevrolet", "model": "equinox",
        "years": (2015, 2017),
        "generation": "second gen, late years",
        "engine": "2.4L I4 or 3.6L V6, 6-speed automatic",
        "reliability": 5.8,
        "maintenance": 7.6,
        "annual_maintenance_usd": 600,
        "insurance_factor": 0.95,
        "tire_set_usd": 660,
        "risk": "The 2.4L four is known for burning oil, and engine is 203 "
                "of 400 complaints on the 2016",
        "known_issues": [
            "Engine is half the 2016 file, 203 of 400.",
            "Check the dipstick yourself. A 2.4L that is low between changes "
            "is burning oil, and running it low wrecks the timing chain.",
            "Visibility/wiper is 114 of the 2016 filings: owners describe "
            "the wipers stopping in the rain. Run them on the test drive.",
            "The 3.6L V6 is the better engine if you can find one.",
        ],
        "note": "Cheap and roomy, but the 2.4L is a known oil burner. Buy on "
                "proof of oil level and service history, or not at all.",
    },
    {
        "make": "chevrolet", "model": "equinox",
        "years": (2018, 2021),
        "generation": "third gen",
        "engine": "1.5L turbo I4 with a 6-speed automatic; 2.0L turbo I4 "
                  "with a 9-speed through 2020; 1.6L diesel in 2018-2019",
        "reliability": 6.4,
        "maintenance": 7.7,
        "annual_maintenance_usd": 550,
        "insurance_factor": 0.95,
        "tire_set_usd": 680,
        "risk": None,
        "known_issues": [
            "Service brakes lead both years pulled: 132 of 410 on the 2018 "
            "and 117 of 321 on the 2020. Owners describe a rock-hard pedal "
            "when the brake vacuum pump fails.",
            "Ask whether the vacuum pump has been replaced, and watch for a "
            "'Service Brake Assist' message.",
            "5 recalls on the 2018 and 4 on the 2020, including 20V668000 "
            "(automatic transmission) on both.",
            "Seven fire-related filings on the 2020.",
        ],
        "note": "A fair commuter with one specific thing to check: the brake "
                "vacuum pump.",
    },
    {
        "make": "chevrolet", "model": "equinox",
        "years": (2025, 2026),
        "generation": "fourth gen",
        "engine": "1.5L turbo I4; CVT on FWD, 8-speed automatic on AWD",
        "reliability": 6.5,
        "maintenance": 7.6,
        "annual_maintenance_usd": 540,
        "insurance_factor": 0.97,
        "tire_set_usd": 720,
        "risk": None,
        "known_issues": [
            "244 complaints on the 2025 already, led by electrical (82). "
            "That is a lot for a first year, even for a high-volume car.",
            "The API returned no recalls for the 2025.",
            "Check every screen and driver-assist function, and confirm the "
            "software updates are current.",
            "New body on a carried-over engine. Provisional score.",
        ],
        "note": "Looks far better than the old one and drives much the same. "
                "The first-year electrical complaints are the thing to "
                "watch.",
    },
    {
        "make": "chevrolet", "model": "blazer",
        "years": (2019, 2022),
        "generation": "first gen",
        "engine": "2.5L I4, 2.0L turbo I4 or 3.6L V6, 9-speed automatic",
        "reliability": 6.6,
        "maintenance": 7.4,
        "annual_maintenance_usd": 580,
        "insurance_factor": 1.0,
        "tire_set_usd": 760,
        "risk": None,
        "known_issues": [
            "191 complaints on the 2019, led by power train (64) and "
            "electrical (62). 142 on the 2021, led by engine (43).",
            "2 recalls on the 2019, including 20V668000 (automatic "
            "transmission), and 1 on the 2021.",
            "A 'Shift to Park' message that will not clear is a known fault "
            "on early cars. Park it, shut it off and see whether it lets you "
            "lock up.",
            "The V6 is the engine to have; the base 2.5L is slow for the "
            "weight.",
        ],
        "note": "Sharp looking and average underneath. Later years of this "
                "run are the safer pick.",
    },
]
