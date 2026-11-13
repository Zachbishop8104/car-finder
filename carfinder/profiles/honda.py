"""Reliability profiles: Honda. The format and the caveats on reading
these numbers are in carfinder/reliability.py."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        # 107 complaints on the 2024 with STEERING at 51: nearly half
        # the file on one component, and there is a matching recall.
        "make": "honda", "model": "hr-v",
        "years": (2023, 2026),
        "generation": "third gen, Civic-based",
        "engine": "2.0L K20C I4, CVT; AWD available",
        "reliability": 6.8,
        "maintenance": 7.8,
        "annual_maintenance_usd": 500,
        "insurance_factor": 1.0,
        "tire_set_usd": 700,
        "risk": "Recall 24V744000 covers an electric power steering "
                "fault; steering is 51 of 107 complaints on the 2024, "
                "so verify the recall is closed before buying",
        "known_issues": [
            "Steering dominates the complaint file: 51 of 107 on the "
            "2024. A single component taking half the filings is the "
            "shape that survives the sales-volume caveat, and Honda "
            "issued recall 24V744000 against it.",
            "Two further recalls: 23V782000 (front seat belts) and "
            "24V859000 (seat fasteners).",
            "Underpowered for its weight; the CVT makes it feel worse "
            "than the numbers suggest.",
            "Interior quality and packaging are genuinely good. This "
            "is not a bad car, it is a car with one specific problem.",
        ],
        "note": "Only worth driving if the steering recall is confirmed "
                "closed on that exact VIN. The CR-V shares the fault.",
    },
    {
        # 244 complaints on the 2016 with POWER TRAIN at 77; the file
        # shrinks to 66 by the 2021.
        "make": "honda", "model": "hr-v",
        "years": (2016, 2022),
        "generation": "second gen, Fit-based (first sold in the US)",
        "engine": "1.8L R18 I4, CVT (6-speed manual through 2018); "
                  "AWD available",
        "reliability": 7.4,
        "maintenance": 8.2,
        "annual_maintenance_usd": 450,
        "insurance_factor": 0.98,
        "tire_set_usd": 640,
        "risk": None,
        "known_issues": [
            "Power train leads the 2016 file (77 of 244 complaints), "
            "which points at the early CVT. On a 2016-2018 car, ask "
            "for CVT fluid change records and drive it for shudder "
            "or hesitation from a stop.",
            "Recall count is low for the early years (2 on the 2016) "
            "but 7 on the 2019, including two fuel pump campaigns "
            "(20V314000, 21V215000) and two rearview camera display "
            "campaigns (23V046000, 24V384000).",
            "Complaints fall off late in the run: 243 on the 2019, 66 "
            "on the 2021.",
            "Slow, and loud on the highway. The folding rear seat is "
            "the reason to buy one.",
        ],
        "note": "A simple, old-fashioned engine in a practical body. "
                "Later years are the safer pick; on early ones the CVT "
                "is the thing to check.",
    },
    {
        # 374 complaints on the 2024, 119 of them STEERING: the same
        # 24V744000 campaign as the HR-V.
        "make": "honda", "model": "cr-v",
        "years": (2023, 2026),
        "generation": "sixth gen",
        "engine": "1.5L L15 turbo I4 or the 2.0L hybrid, CVT",
        "reliability": 6.9,
        "maintenance": 7.9,
        "annual_maintenance_usd": 510,
        "insurance_factor": 1.0,
        "tire_set_usd": 760,
        "risk": "Recall 24V744000 (electric power steering): steering "
                "is 119 of 374 complaints on the 2024; confirm closed",
        "known_issues": [
            "Steering is the top component by a wide margin (119 of "
            "374 on the 2024) and carries recall 24V744000, shared "
            "with the HR-V.",
            "Collision avoidance (47) and wipers (45) are the next "
            "clusters. Driver-assist complaints are common across "
            "this whole class, Honda included.",
            "The 1.5L turbo had oil-dilution trouble in colder "
            "climates on earlier generations. Largely addressed by "
            "this one, but a cold-climate buyer should still check that "
            "oil changes were done on schedule.",
            "A size class up from the subcompacts: bigger and roomier, so at "
            "the same money it will carry more miles.",
        ],
        "note": "A good car with a live steering campaign against it. "
                "Check the VIN first.",
    },
    {
        # 1,784 complaints on the 2017 and 2,169 on the 2018, against
        # 674 on the 2015 and 365 on the 2020. Same model, so the
        # jump is not a sales-volume effect.
        "make": "honda", "model": "cr-v",
        "years": (2017, 2022),
        "generation": "fifth gen",
        "engine": "1.5L L15 turbo I4 with CVT (2.4L on the LX through "
                  "2019); hybrid from 2020",
        "reliability": 6.6,
        "maintenance": 7.9,
        "annual_maintenance_usd": 500,
        "insurance_factor": 1.0,
        "tire_set_usd": 740,
        "risk": "On 2017-2018 cars the 1.5L turbo is known for fuel "
                "diluting the engine oil in cold climates; engine is "
                "the top complaint on both years (533 of 1,784 on the "
                "2017, 530 of 2,169 on the 2018)",
        "known_issues": [
            "Oil dilution on the 1.5L turbo, worst on 2017-2018 cars "
            "used for short trips in cold weather. Check the oil "
            "level and smell the dipstick for fuel, and ask whether "
            "the dealer software update was done.",
            "Steering is 335 complaints on the 2018 and 144 of 272 on "
            "the 2022. Recall 18V663000 covers a power steering "
            "torque sensor magnet on 2017-2018 cars.",
            "Forward collision avoidance is 283 complaints on the 2017 "
            "and 397 on the 2018: false braking alerts are the usual "
            "story.",
            "Recall count is moderate: 7 on the 2017, 5 on the 2018, "
            "7 on the 2020 (including 19V865000, rear subframe bolts), "
            "3 on the 2022.",
        ],
        "note": "The 2019-2022 cars are clearly better than the first "
                "two years. On a 2017 or 2018, the engine oil history "
                "decides it.",
    },
    {
        # 674 complaints on the 2015, 396 on the 2016. ENGINE (243) and
        # POWER TRAIN (150) lead the 2015.
        "make": "honda", "model": "cr-v",
        "years": (2015, 2016),
        "generation": "fourth gen, facelifted",
        "engine": "2.4L K24W direct-injected I4, CVT; AWD available",
        "reliability": 7.5,
        "maintenance": 8.2,
        "annual_maintenance_usd": 470,
        "insurance_factor": 0.98,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "The 2015 facelift brought a new engine and CVT, and with "
            "them a vibration at idle and low speed. Engine (243) and "
            "power train (150) lead the 674 complaints on the 2015. "
            "Drive it in gear at a stop and at 20 to 40 mph.",
            "Complaints drop to 396 on the 2016, so the second year "
            "is the better one.",
            "Only 3 recalls on each year. One, 17V305000, covers cars "
            "that got a replacement engine built with wrong pistons.",
            "At this age, budget for CVT fluid, engine mounts and an "
            "AC check.",
        ],
        "note": "A sound used buy if the vibration does not bother you "
                "on the test drive. Prefer the 2016.",
    },
    {
        "make": "honda", "model": "accord",
        "years": (2023, 2026),
        "generation": "eleventh gen",
        "engine": "1.5L L15 turbo I4 with CVT, or the 2.0L hybrid",
        "reliability": 7.8,
        "maintenance": 8.0,
        "annual_maintenance_usd": 470,
        "insurance_factor": 1.0,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "Complaint data is unavailable: NHTSA's complaints endpoint "
            "returned nothing for Honda sedans when this was written. "
            "That is an API gap, not a clean record, so this score is "
            "provisional and rests on recall history alone.",
            "The 2024 carries three recalls: 23V782000 (front seat "
            "belts), 24V763000 (fuel pump) and 24V859000 (seat "
            "critical fasteners). The 2026 currently shows none.",
            "Depreciated 17.3%/yr in one Michigan market (Aug 2026), the "
            "steepest of the sedans profiled here and out of step with the "
            "Accord's national reputation. Check the curve for your area "
            "before trusting either number.",
            "Genuinely one of the best-driving midsize sedans.",
        ],
        "note": "A better car than a weak local resale number would suggest. "
                "Worth it if your market's depreciation curve agrees, or if "
                "you find one well under MSRP.",
    },
    {
        # 1,902 complaints on the 2018 (first year) against 371 on
        # the 2020 and about 600 on the 2015 and 2016.
        "make": "honda", "model": "accord",
        "years": (2018, 2022),
        "generation": "tenth gen",
        "engine": "1.5L L15 turbo I4 with CVT, 2.0L turbo with "
                  "10-speed automatic, or the 2.0L hybrid",
        "reliability": 7.1,
        "maintenance": 7.9,
        "annual_maintenance_usd": 480,
        "insurance_factor": 1.02,
        "tire_set_usd": 720,
        "risk": None,
        "known_issues": [
            "The 2018 is the year to be careful with: 1,902 "
            "complaints, led by engine (561), forward collision "
            "avoidance (344) and fuel system (309). The 2020 has 371.",
            "The 1.5L turbo can dilute its oil with fuel on short "
            "cold trips, the same trait as the CR-V and Civic. Check "
            "the oil level and change history.",
            "False automatic-braking events are a common complaint "
            "(344 on the 2018, 104 on the 2020). Test the driver "
            "assists on the highway.",
            "Recall count is ordinary: 6 on the 2018, 5 on the 2020, "
            "including fuel pump campaigns 20V314000 and 21V215000.",
        ],
        "note": "Drives very well. Buy a 2020 or later if you can; the "
                "first model year carries most of the trouble.",
    },
    {
        # About 600 complaints on both the 2015 and the 2016, with
        # ELECTRICAL SYSTEM on top each time.
        "make": "honda", "model": "accord",
        "years": (2013, 2017),
        "generation": "ninth gen",
        "engine": "2.4L K24W direct-injected I4 with CVT, or 3.5L V6 "
                  "with 6-speed automatic",
        "reliability": 8.0,
        "maintenance": 8.3,
        "annual_maintenance_usd": 460,
        "insurance_factor": 0.98,
        "tire_set_usd": 680,
        "risk": None,
        "known_issues": [
            "Electrical is the top component: 237 of 602 complaints "
            "on the 2015 and 202 of 613 on the 2016. Starters and "
            "batteries are the usual culprits, and recall 17V418000 "
            "covers a battery sensor that can short. Listen to a cold "
            "start.",
            "Exterior lighting is 128 complaints on the 2016. Check "
            "that both LED daytime running light strips work; they "
            "are costly to replace.",
            "Recall count is low: 5 on the 2015, 4 on the 2016. "
            "20V769000 covers the driveshaft on 2013-2015 "
            "four-cylinder cars.",
            "The V6 has a timing belt due around 100,000 miles. Ask "
            "for proof it was done.",
        ],
        "note": "One of the safer ten-year-old sedans to buy. The "
                "faults it has are cheap ones.",
    },
    {
        "make": "honda", "model": "civic",
        "years": (2022, 2026),
        "generation": "eleventh gen",
        "engine": "2.0L naturally aspirated or 1.5L turbo I4, CVT; "
                  "hybrid from 2025",
        "reliability": 7.4,
        "maintenance": 8.2,
        "annual_maintenance_usd": 450,
        "insurance_factor": 1.0,
        "tire_set_usd": 660,
        "risk": "Two steering recalls on the 2024: 23V704000 (rack "
                "and pinion) and 24V744000 (electric power steering, "
                "the same campaign as the CR-V and HR-V); confirm both "
                "are closed on the VIN",
        "known_issues": [
            "The 2024 carries 23V704000 (steering rack and pinion) and "
            "24V744000 (electric power steering). Honda's steering "
            "campaign spans the Civic, CR-V and HR-V, and on the SUVs "
            "it came with a heavy complaint cluster.",
            "Also 24V859000, seat critical fasteners.",
            "Complaint data unavailable for Honda sedans (an NHTSA API "
            "gap, not a clean record). Provisional score.",
        ],
        "note": "Fine car carrying Honda's steering campaign. Check the "
                "VIN against both recalls before spending time on it.",
    },
    {
        # 1,083 complaints on the 2016 with STEERING at 446; 596 on
        # the 2018 with STEERING at 224; 239 on the 2020.
        "make": "honda", "model": "civic",
        "years": (2016, 2021),
        "generation": "tenth gen",
        "engine": "2.0L K20C2 I4 or 1.5L L15 turbo I4, CVT or 6-speed "
                  "manual",
        "reliability": 7.2,
        "maintenance": 8.2,
        "annual_maintenance_usd": 450,
        "insurance_factor": 1.03,
        "tire_set_usd": 640,
        "risk": "Steering is the top complaint by far on early cars "
                "(446 of 1,083 on the 2016, 224 of 596 on the 2018), "
                "and recall 18V663000 covers a power steering fault on "
                "2017-2018 cars",
        "known_issues": [
            "Steering takes about 40% of the complaint file on both "
            "the 2016 and the 2018. On the test drive, feel for a "
            "sticky or notchy wheel just off center at highway speed.",
            "The 2016 has 5 recalls, including 16V074000 (2.0L piston "
            "wrist pin clip, can seize the engine) and 16V725000 "
            "(parking brake). Confirm both are closed.",
            "The 1.5L turbo can dilute its oil with fuel in cold "
            "climates, mainly 2016-2018. Check the oil level and ask "
            "about the software update.",
            "Weak air conditioning is a familiar fault on this "
            "generation. Run the AC hard on the test drive.",
        ],
        "note": "The later years (2019-2021) have a much smaller "
                "complaint file. The 2.0L non-turbo is the low-risk "
                "engine.",
    },
    {
        # 381 complaints on the 2015 with POWER TRAIN at 177, and a
        # single recall that targets the CVT.
        "make": "honda", "model": "civic",
        "years": (2013, 2015),
        "generation": "ninth gen, facelifted",
        "engine": "1.8L R18 I4; 5-speed automatic on the 2013, CVT "
                  "from 2014",
        "reliability": 7.7,
        "maintenance": 8.5,
        "annual_maintenance_usd": 420,
        "insurance_factor": 1.0,
        "tire_set_usd": 600,
        "risk": None,
        "known_issues": [
            "Power train is 177 of 381 complaints on the 2015. Recall "
            "15V574000 is a CVT software fix on 2014-2015 cars that "
            "protects the drive pulley shaft from breaking. Confirm "
            "it was done.",
            "That is the only recall on the 2015, a very low count.",
            "Air bags are the next cluster (58 on the 2015). Run the "
            "VIN for open air bag campaigns.",
            "The 1.8L engine is simple and cheap to keep running; at "
            "this age look at engine mounts and the AC.",
        ],
        "note": "Cheap, simple transport. On a 2014 or 2015, the CVT "
                "recall and fluid history are what to check.",
    },
    {
        # 153 complaints and 6 recalls on the 2023; 217 and 5 on the
        # 2025; 31 and 1 on the 2026 so far.
        "make": "honda", "model": "pilot",
        "years": (2023, 2026),
        "generation": "fourth gen",
        "engine": "3.5L J35Y8 DOHC V6, 10-speed automatic; AWD "
                  "available",
        "reliability": 6.6,
        "maintenance": 7.3,
        "annual_maintenance_usd": 580,
        "insurance_factor": 1.03,
        "tire_set_usd": 900,
        "risk": "Three steering or stalling recalls reach this "
                "generation: 23V735000 (steering gearbox bearing, "
                "2023-2024), 26V721000 (loss of power steering assist) "
                "and 25V031000 (engine stall from fuel injection "
                "software)",
        "known_issues": [
            "Six recalls on the 2023 and five on the 2025. Besides "
            "the three above, the list includes 24V900000 (fuel filler "
            "pipe) and 25V391000 (brake pedal).",
            "Seat belts lead the 2023 complaint file (39 of 153). On "
            "the 2025 it is forward collision avoidance (57) and "
            "steering (44) out of 217.",
            "The 2026 already has recall 26V424000 for rear subframe "
            "bolts, and steering is 10 of its 31 complaints.",
            "The DOHC V6 is a new engine design with a short "
            "history, so there is no long-term record to lean on.",
        ],
        "note": "Roomy and pleasant, but the recall list is long for "
                "a new design. Run the VIN and make sure every "
                "campaign is closed.",
    },
    {
        # 1,731 complaints on the 2016 against 109 on the 2015 Pilot
        # before it: ENGINE 784, ELECTRICAL SYSTEM 584.
        "make": "honda", "model": "pilot",
        "years": (2016, 2022),
        "generation": "third gen",
        "engine": "3.5L J35Y6 direct-injected V6; 6-speed or ZF "
                  "9-speed automatic (9-speed on all from 2021)",
        "reliability": 5.8,
        "maintenance": 7.0,
        "annual_maintenance_usd": 640,
        "insurance_factor": 1.02,
        "tire_set_usd": 860,
        "risk": "Recall 23V751000 covers connecting rod bearings that "
                "can seize the engine on 2016 and 2018-2019 Pilots, "
                "and the recall count is high (13 on the 2019)",
        "known_issues": [
            "The 2016 has 1,731 complaints, led by engine (784) and "
            "electrical (584). Failed fuel injectors that light up "
            "the whole dashboard are the common story. Ask whether "
            "the injectors were replaced.",
            "Recalls: 8 on the 2016, 13 on the 2019, 10 on the 2021. "
            "Recall count does not scale with sales, so these are "
            "poor numbers.",
            "Recall 26V365000 covers rear subframe corrosion on "
            "2016-2022 Pilots sold in salt-belt states. Have the rear "
            "subframe inspected on a lift.",
            "The 9-speed automatic is known for rough, hesitant "
            "shifts. Drive it in stop-and-go traffic before deciding.",
        ],
        "note": "The weakest Pilot generation. If you want one, pick "
                "a 2020-2022 with every recall closed and service "
                "records in hand.",
    },
    {
        # Only the 2015 was pulled: 109 complaints, 4 recalls.
        "make": "honda", "model": "pilot",
        "years": (2012, 2015),
        "generation": "second gen, facelifted",
        "engine": "3.5L J35Z4 V6 with cylinder deactivation, 5-speed "
                  "automatic",
        "reliability": 7.6,
        "maintenance": 7.6,
        "annual_maintenance_usd": 580,
        "insurance_factor": 0.98,
        "tire_set_usd": 820,
        "risk": None,
        "known_issues": [
            "A small complaint file: 109 on the 2015, with engine the "
            "top component at 22.",
            "Three of the four recalls on the 2015 are passenger air "
            "bag inflator campaigns (18V661000, 19V378000, "
            "19V502000). Do not buy one with an open inflator recall.",
            "The cylinder deactivation system on this V6 is linked to "
            "oil burning and fouled spark plugs. Check the oil level "
            "and look for blue smoke on a cold start.",
            "Timing belt and water pump are due around 100,000 "
            "miles, a four-figure job. Ask for the receipt.",
        ],
        "note": "Old and thirsty but far less troubled than the "
                "generation that replaced it. Condition and the timing "
                "belt matter more than the badge year.",
    },
    {
        # 144 complaints on the 2022, 132 on the 2024, then 464 on
        # the 2025: a jump inside one model, not a volume effect.
        "make": "honda", "model": "odyssey",
        "years": (2021, 2026),
        "generation": "fifth gen, facelifted",
        "engine": "3.5L J35Y6 V6, 10-speed automatic",
        "reliability": 6.7,
        "maintenance": 7.2,
        "annual_maintenance_usd": 600,
        "insurance_factor": 0.97,
        "tire_set_usd": 820,
        "risk": None,
        "known_issues": [
            "Recall count comes down after the facelift: 9 on the "
            "2022 (one of them for wheelchair conversions only), 3 "
            "on the 2024, 2 on the 2025.",
            "The 2025 has 464 complaints against 132 on the 2024, "
            "most of them tagged engine, electrical or both. Until "
            "that is explained, check a 2025 for warning lights and "
            "open campaigns with extra care.",
            "Recall 24V114000 covers a steering gearbox that can let "
            "water in on 2023-2024 vans. Confirm it is closed.",
            "Power sliding doors and the rear entertainment system "
            "are the usual wear items. Operate every door several "
            "times.",
        ],
        "note": "Much better sorted than the 2018-2020 vans. A 2022 "
                "to 2024 is the comfortable choice.",
    },
    {
        # 16 recalls on the 2018 and 20 on the 2019, each with about
        # 1,000 complaints. The 2016 before it has 6 and 272.
        "make": "honda", "model": "odyssey",
        "years": (2018, 2020),
        "generation": "fifth gen",
        "engine": "3.5L J35Y6 V6; ZF 9-speed automatic, or 10-speed "
                  "on upper trims (all trims for 2020)",
        "reliability": 5.5,
        "maintenance": 7.0,
        "annual_maintenance_usd": 650,
        "insurance_factor": 0.98,
        "tire_set_usd": 800,
        "risk": "Twenty recalls on the 2019 and sixteen on the 2018, "
                "including 23V751000 (connecting rod bearings that "
                "can seize the engine) and 19V299000 (transmission "
                "can shift itself to Park)",
        "known_issues": [
            "The recall list is the problem. Among them: sliding door "
            "latches (18V795000, 20V437000), third-row wiring "
            "(20V066000) and rearview cameras (20V439000). Two on "
            "each year apply only to wheelchair conversions.",
            "About 1,000 complaints on each of the 2018 and 2019, "
            "spread across electrical (266 on the 2018), forward "
            "collision avoidance (211) and engine (193).",
            "The 9-speed automatic on lower trims shifts roughly. "
            "The 10-speed is the one to have.",
            "Infotainment screens that freeze or go black are a "
            "common complaint. Use the screen for the whole test "
            "drive.",
        ],
        "note": "A great van to ride in and a poor one to own from "
                "these years. Buy 2021 or later unless the price is "
                "very low and every recall is closed.",
    },
    {
        # 209 complaints on the 2015, 272 on the 2016; 6 recalls each.
        "make": "honda", "model": "odyssey",
        "years": (2014, 2017),
        "generation": "fourth gen, facelifted",
        "engine": "3.5L J35Z8 V6 with cylinder deactivation, 6-speed "
                  "automatic",
        "reliability": 7.2,
        "maintenance": 7.5,
        "annual_maintenance_usd": 590,
        "insurance_factor": 0.95,
        "tire_set_usd": 760,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2016, four of them for the second-row "
            "seats (16V932000, 16V933000, 17V725000, 18V170000). "
            "Check that the middle-row seats latch firmly.",
            "Engine is the top complaint (93 of 272 on the 2016). "
            "The cylinder deactivation system on this V6 is linked to "
            "oil burning and fouled plugs; check the oil level.",
            "Timing belt and water pump are due around 100,000 "
            "miles. Ask for the receipt.",
            "Power sliding door motors and cables wear out. Run both "
            "doors several times.",
        ],
        "note": "An honest older van. Fewer gadgets to fail than the "
                "generation after it, and a far shorter recall list.",
    },
    {
        # First year of a new design: 1 recall and 79 complaints on
        # the 2026 when this was written.
        "make": "honda", "model": "passport",
        "years": (2026, 2026),
        "generation": "fourth gen",
        "engine": "3.5L J35Y8 DOHC V6, 10-speed automatic; AWD "
                  "standard",
        "reliability": 6.7,
        "maintenance": 7.2,
        "annual_maintenance_usd": 590,
        "insurance_factor": 1.03,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "Recall 26V424000 covers rear subframe bolts that may "
            "not have been tightened properly. Confirm it is closed.",
            "79 complaints on the 2026 so far, led by electrical "
            "(17), steering (12) and seats (11). That is a lot for a "
            "new model this early.",
            "Shares its engine and transmission with the 2023 and "
            "later Pilot, which has steering and engine software "
            "recalls of its own.",
        ],
        "note": "Provisional: one model year of data. Sensible "
                "hardware, but let the first-year faults surface "
                "before paying full price.",
    },
    {
        # 286 complaints and 10 recalls on the 2019, falling to 40
        # and 5 on the 2023.
        "make": "honda", "model": "passport",
        "years": (2019, 2025),
        "generation": "third gen, Pilot-based",
        "engine": "3.5L J35Y6 V6, ZF 9-speed automatic; AWD available",
        "reliability": 6.6,
        "maintenance": 7.2,
        "annual_maintenance_usd": 600,
        "insurance_factor": 1.02,
        "tire_set_usd": 880,
        "risk": "Recall 26V365000 covers rear subframe corrosion on "
                "2019-2023 Passports sold in salt-belt states, which "
                "can lead to rear suspension failure",
        "known_issues": [
            "Recall count falls with age of design: 10 on the 2019, "
            "7 on the 2021, 5 on the 2023. The recalls endpoint "
            "returned none for the 2025.",
            "Complaints fall the same way: 286 on the 2019 (led by "
            "electrical at 86), 147 on the 2021, 40 on the 2023.",
            "Forward collision avoidance is the top complaint on the "
            "2021 (53 of 147). Test the automatic braking on an open "
            "road.",
            "The 9-speed automatic can shift roughly at low speed. "
            "Drive it in traffic.",
        ],
        "note": "A shortened Pilot with the same faults in smaller "
                "numbers. The 2022-2025 cars are the ones to look at.",
    },
    {
        # 104 complaints and 7 recalls on the 2021; 78 and 1 on the
        # 2024; 107 and 2 on the 2025.
        "make": "honda", "model": "ridgeline",
        "years": (2020, 2026),
        "generation": "second gen, 9-speed",
        "engine": "3.5L J35Y6 V6, ZF 9-speed automatic; AWD standard "
                  "from 2021",
        "reliability": 7.0,
        "maintenance": 7.3,
        "annual_maintenance_usd": 590,
        "insurance_factor": 1.0,
        "tire_set_usd": 880,
        "risk": None,
        "known_issues": [
            "Recall count is low on recent trucks: 1 on the 2024, 2 "
            "on the 2025. The 2021 has 7.",
            "Recall 24V321000 covers the tailgate rearview camera on "
            "2020-2024 trucks, and 23V458000 a brake master cylinder "
            "on 2020-2023. Confirm both.",
            "Recall 26V365000 covers rear subframe corrosion on "
            "trucks through 2023 sold in salt-belt states. Inspect "
            "the subframe on a lift.",
            "Exterior lighting is an odd cluster: 14 complaints on "
            "the 2021 and 20 of 107 on the 2025. Check every lamp.",
        ],
        "note": "The most dependable of Honda's V6 trucks and SUVs "
                "from these years. A good pick if a unibody truck "
                "suits your use.",
    },
    {
        # 348 complaints, 9 recalls and 6 fire reports on the 2017.
        "make": "honda", "model": "ridgeline",
        "years": (2017, 2019),
        "generation": "second gen, 6-speed",
        "engine": "3.5L J35Y6 direct-injected V6, 6-speed automatic",
        "reliability": 6.2,
        "maintenance": 7.3,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.0,
        "tire_set_usd": 860,
        "risk": "Recall 23V751000 covers connecting rod bearings that "
                "can seize the engine on 2017 and 2019 Ridgelines, "
                "and 19V053000 a fuel pump port that can crack and "
                "leak fuel",
        "known_issues": [
            "Nine recalls on the 2017 and twelve on the 2019. Run "
            "the VIN and insist every one is closed.",
            "348 complaints on the 2017, led by electrical (93) and "
            "engine (89), with six fire reports. Failed fuel "
            "injectors are the common engine story on this V6.",
            "Recall 22V867000 covers the rearview camera wiring in "
            "the tailgate. Check the camera with the tailgate opened "
            "both ways.",
            "Recall 26V365000 covers rear subframe corrosion in "
            "salt-belt states. Inspect it on a lift.",
        ],
        "note": "The 6-speed gearbox is smoother than the later "
                "9-speed, but the engine recalls make a 2020 or later "
                "truck the safer buy.",
    },
    {
        # The complaints endpoint returned nothing for the Prologue.
        # Recalls: 3 on the 2024, 1 on the 2025.
        "make": "honda", "model": "prologue",
        "years": (2024, 2026),
        "generation": "first gen, built by GM on the Ultium platform",
        "engine": "Battery electric, 85 kWh; single motor FWD or dual "
                  "motor AWD",
        "reliability": 6.3,
        "maintenance": 6.3,
        "annual_maintenance_usd": 330,
        "insurance_factor": 1.12,
        "tire_set_usd": 1050,
        "risk": None,
        "known_issues": [
            "Three recalls on the 2024: 24V540000 (front lower "
            "control arm) and two rearview camera campaigns "
            "(26V112000, 26V306000). The 2025 has one.",
            "NHTSA's complaints endpoint returned nothing for this "
            "model. That is a data gap, not a clean record.",
            "It is a GM electric car under the skin, so battery, "
            "charging and software repairs depend on parts and "
            "know-how a Honda dealer did not design. Ask the dealer "
            "how many they have serviced.",
            "Running costs are low (no oil, few brake jobs), but it "
            "is heavy and wears tires quickly. Check the battery "
            "warranty dates and charge it once on a fast charger "
            "before buying.",
        ],
        "note": "Provisional: no complaint data and a short history. "
                "Pleasant to drive; treat it as a GM EV when judging "
                "long-term repair risk.",
    },
    {
        # 284 complaints on the 2015 (first year), 117 on the 2018,
        # 38 on the 2020. Four recalls on each.
        "make": "honda", "model": "fit",
        "years": (2015, 2020),
        "generation": "third gen",
        "engine": "1.5L L15B direct-injected I4, CVT or 6-speed manual",
        "reliability": 7.9,
        "maintenance": 8.6,
        "annual_maintenance_usd": 400,
        "insurance_factor": 0.97,
        "tire_set_usd": 520,
        "risk": None,
        "known_issues": [
            "The 2015 is the weak year: 284 complaints with "
            "electrical at 117, against 117 total on the 2018 and 38 "
            "on the 2020. A hard or slow start is the thing to "
            "listen for.",
            "Recall 15V574000 is a CVT software fix on the 2015 that "
            "protects the drive pulley shaft. Confirm it was done.",
            "Four recalls on each year pulled. On the 2018 and 2020 "
            "they are mostly rearview camera display (23V046000, "
            "24V384000) and air bag sensor campaigns.",
            "Thin paint, road noise and a firm ride are the "
            "everyday complaints, not breakdowns.",
        ],
        "note": "One of the cheapest cars here to keep running. Skip "
                "the 2015 if a 2017 or later is within reach.",
    },
    {
        # 101 complaints and 8 recalls on the 2019 (first year); 25
        # and 3 on the 2021.
        "make": "honda", "model": "insight",
        "years": (2019, 2022),
        "generation": "third gen, Civic-based",
        "engine": "1.5L I4 two-motor hybrid, no conventional gearbox",
        "reliability": 8.0,
        "maintenance": 7.8,
        "annual_maintenance_usd": 430,
        "insurance_factor": 1.0,
        "tire_set_usd": 640,
        "risk": None,
        "known_issues": [
            "The first year has the recalls: 8 on the 2019, "
            "including two fuel pump campaigns (20V314000, "
            "21V215000) and a body control module software fix "
            "(20V771000). The 2021 has 3.",
            "Recall 20V798000 covers the hybrid system's DC/DC "
            "converter on 2020-2021 cars. Confirm it is closed.",
            "Complaints are few: 101 on the 2019, 25 on the 2021, "
            "with forward collision avoidance on top both times.",
            "The engine drones loudly on long climbs. Normal for "
            "this hybrid system, but drive one up a hill first.",
        ],
        "note": "A Civic that uses very little fuel, with a short "
                "complaint file. Prefer 2020 or later.",
    },
]
