"""Reliability profiles: Subaru. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

Subaru complaint files are large for the sales volume, but much of
that is cracked windshields and drained batteries rather than engines
or gearboxes. The component split matters more than the total."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "subaru", "model": "legacy",
        "years": (2020, 2026),
        "generation": "BW seventh gen",
        "engine": "2.5L FB25 boxer (or 2.4L FA24 turbo on XT)",
        "reliability": 8.2,
        "maintenance": 7.5,
        "annual_maintenance_usd": 560,
        "insurance_factor": 1.0,
        "tire_set_usd": 750,
        "risk": None,
        "known_issues": [
            "CVT is durable in this generation but is a replace-not-rebuild "
            "part; confirm the fluid was serviced.",
            "Boxer layout makes some jobs (spark plugs, head gaskets) pricier "
            "in labor than an inline four.",
            "Starlink infotainment freezes were common early in the run.",
        ],
        "note": "AWD standard, built for snow, and common in snow-belt "
                "markets. FB25 engines are solid; upkeep slightly above "
                "Toyota.",
    },
    {
        "make": "subaru", "model": "legacy",
        "years": (2015, 2019),
        "generation": "BN sixth gen",
        "engine": "2.5L FB25 boxer",
        "reliability": 7.9,
        "maintenance": 7.5,
        "annual_maintenance_usd": 600,
        "insurance_factor": 1.0,
        "tire_set_usd": 720,
        "known_issues": [
            "Earlier CVTs in this generation are the weaker ones; service "
            "history matters more than mileage.",
            "Some oil consumption reports on higher-mileage FB25s.",
        ],
        "risk": "Earlier-generation CVT, weaker than the 2020+ unit; "
                "service history matters more than mileage here",
        "note": "Older sixth gen. Cheaper to buy, but check CVT service "
                "records carefully before committing.",
    },
    {
        "make": "subaru", "model": "impreza",
        "years": (2017, 2026),
        "generation": "GK/GT fifth gen (SGP)",
        "engine": "2.0L FB20 boxer",
        "reliability": 7.8,
        "maintenance": 7.8,
        "annual_maintenance_usd": 550,
        "insurance_factor": 0.92,
        "tire_set_usd": 650,
        "risk": None,
        "known_issues": [
            "Underpowered rather than unreliable: the drivetrain works hard.",
            "Same CVT service caveat as the Legacy.",
        ],
        "note": "AWD standard, budget-friendly, easy to find. A bit slow but "
                "dependable and cheap to run.",
    },
    {
        # 2015: 2 recalls, 79 complaints. 2016: 1 recall, 75.
        "make": "subaru", "model": "impreza",
        "years": (2012, 2016),
        "generation": "GJ/GP fourth gen",
        "engine": "2.0L FB20 boxer, CVT or 5-speed manual",
        "reliability": 7.4,
        "maintenance": 7.8,
        "annual_maintenance_usd": 580,
        "insurance_factor": 0.92,
        "tire_set_usd": 600,
        "risk": None,
        "known_issues": [
            "79 complaints on the 2015 and 75 on the 2016, spread "
            "across electrical, power train and engine with nothing "
            "dominant. Two recalls on the 2015, one on the 2016.",
            "Early FB20 engines can burn oil. Check the dipstick "
            "cold and ask how often it is topped up.",
            "First-generation Subaru CVT: ask for a fluid service "
            "record, or pick the manual.",
        ],
        "note": "Cheap AWD that mostly keeps going. Oil level and "
                "CVT history are the two things to check.",
    },
    {
        # 2024: 110 complaints, 2 recalls incl. a driveshaft campaign.
        # 2026: 8 complaints, 0 recalls, but far too new to read.
        "make": "subaru", "model": "crosstrek",
        "years": (2024, 2026),
        "generation": "third gen",
        "engine": "2.0L FB20 or 2.5L FB25 flat-four, CVT; symmetrical "
                  "AWD standard",
        "reliability": 7.7,
        "maintenance": 7.0,
        "annual_maintenance_usd": 540,
        "insurance_factor": 1.0,
        "tire_set_usd": 740,
        "risk": None,
        "known_issues": [
            "Standard AWD and real ground clearance: the strongest "
            "winter case among the small SUVs profiled here.",
            "Recall 23V754000 covers the driveshaft on early third-gen "
            "cars; 23V551000 covers instrument cluster software. Check "
            "both against the VIN.",
            "110 complaints on the 2024, spread thin: exterior "
            "lighting (13), wipers (12), collision avoidance (11). "
            "Annoyances rather than failures, but a lot of them.",
            "Subaru CVTs are acceptable but not Toyota-grade.",
            "Slow. The 2.0L in particular is genuinely underpowered.",
        ],
        "note": "Buy it for the AWD and the clearance. If those do not "
                "matter to you, the Mazdas are the better cars.",
    },
    {
        # 2018: 5 recalls, 195 complaints. 2019: 7 recalls, 288
        # complaints, 113 VISIBILITY/WIPER. 2021: 1 recall, 116.
        "make": "subaru", "model": "crosstrek",
        "years": (2018, 2023),
        "generation": "GT second gen (SGP)",
        "engine": "2.0L FB20 flat-four (2.5L FB25 on Sport and "
                  "Limited from 2021), CVT or 6-speed manual",
        "reliability": 7.5,
        "maintenance": 7.3,
        "annual_maintenance_usd": 550,
        "insurance_factor": 0.98,
        "tire_set_usd": 720,
        "risk": None,
        "known_issues": [
            "Seven recalls on the 2019 and five on the 2018; one on "
            "the 2021. Run the VIN on early cars.",
            "113 of 288 complaints on the 2019 are VISIBILITY/WIPER, "
            "mostly windshields that crack easily. Check the glass "
            "and your insurance glass cover.",
            "The 2.5L from 2021 is the one to have; the 2.0L is "
            "slow with a full load.",
        ],
        "note": "Mechanically sound. 2021 and later cars have fewer "
                "recalls and the better engine.",
    },
    {
        # 2016: 1 recall, 133 complaints. 2017: 1 recall, 99.
        "make": "subaru", "model": "crosstrek",
        "years": (2016, 2017),
        "generation": "GP first gen",
        "engine": "2.0L FB20 flat-four, CVT or 5-speed manual",
        "reliability": 7.3,
        "maintenance": 7.5,
        "annual_maintenance_usd": 580,
        "insurance_factor": 0.98,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "One recall on each of the 2016 and 2017. 133 complaints "
            "on the 2016 led by electrical (37), with no single "
            "failure standing out.",
            "Early FB20 engines can use oil between changes. Check "
            "the level before you buy and monthly after.",
            "Ask for a CVT fluid service record.",
        ],
        "note": "An Impreza on stilts. Slow and noisy, but a cheap "
                "way into a dependable AWD car.",
    },
    {
        # Same car as the 2016-2017 Crosstrek, under its earlier
        # name. 2015: 1 recall, 100 complaints, 25 POWER TRAIN.
        "make": "subaru", "model": "xv crosstrek",
        "years": (2013, 2015),
        "generation": "GP first gen",
        "engine": "2.0L FB20 flat-four, CVT or 5-speed manual",
        "reliability": 7.2,
        "maintenance": 7.5,
        "annual_maintenance_usd": 600,
        "insurance_factor": 0.98,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "One recall and 100 complaints on the 2015, with POWER "
            "TRAIN (25) the largest group.",
            "Oil consumption on early FB20 engines: check the level "
            "cold and ask how often it needs topping up.",
            "First-generation Subaru CVT. Service history matters "
            "more than mileage.",
        ],
        "note": "The Crosstrek before the name was shortened. Fine "
                "if the oil level and CVT records check out.",
    },
    {
        # 2026: 21 complaints; the recall endpoint returned nothing.
        "make": "subaru", "model": "outback",
        "years": (2026, 2026),
        "generation": "seventh gen",
        "engine": "2.5L FB25 flat-four (2.4L FA24 turbo on XT and "
                  "Wilderness), CVT",
        "reliability": 7.6,
        "maintenance": 7.2,
        "annual_maintenance_usd": 570,
        "insurance_factor": 1.0,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "21 complaints on the 2026 already, mostly electrical "
            "(6) and unclassified. The recall lookup returned "
            "nothing, which for a new model is not a clean record.",
            "New boxy body and new screens on carried-over engines "
            "and CVT.",
            "First year of a redesign. Subaru launch years have run "
            "to several recalls (six on the 2020 Outback).",
        ],
        "note": "Provisional. Known mechanicals, unknown "
                "electronics. Waiting a year costs nothing.",
    },
    {
        # 2020: 6 recalls, 906 complaints, 313 VISIBILITY/WIPER and
        # 259 ELECTRICAL SYSTEM. 2022: 4 recalls, 467 complaints.
        "make": "subaru", "model": "outback",
        "years": (2020, 2025),
        "generation": "BT sixth gen",
        "engine": "2.5L FB25 flat-four (2.4L FA24 turbo on XT and "
                  "Wilderness), CVT",
        "reliability": 7.6,
        "maintenance": 7.3,
        "annual_maintenance_usd": 570,
        "insurance_factor": 1.0,
        "tire_set_usd": 820,
        "risk": None,
        "known_issues": [
            "255 of 467 complaints on the 2022 are VISIBILITY/WIPER: "
            "windshields that crack from small chips. Budget for "
            "glass, and recalibrating EyeSight after it.",
            "259 ELECTRICAL SYSTEM complaints on the 2020: drained "
            "batteries and a frozen center screen. Check the battery "
            "date and that the screen software is current.",
            "Six recalls on the 2020, four on the 2022.",
            "Engine and CVT complaints are a small share of the "
            "file. The big numbers are glass and electrics.",
        ],
        "note": "Annoying more than unreliable. The drivetrain holds "
                "up; the windshield and the tablet screen do not "
                "always.",
    },
    {
        # 2017: 4 recalls, 921 complaints, 392 ELECTRICAL SYSTEM.
        # 2019: 3 recalls, 1036 complaints. 2015: 5 recalls, 509.
        "make": "subaru", "model": "outback",
        "years": (2015, 2019),
        "generation": "BS fifth gen",
        "engine": "2.5L FB25 flat-four (or 3.6L EZ36 flat-six), CVT",
        "reliability": 7.3,
        "maintenance": 7.3,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.0,
        "tire_set_usd": 780,
        "risk": "Earlier-generation CVT, weaker than the 2020+ unit; "
                "service history matters more than mileage here",
        "known_issues": [
            "392 of 921 complaints on the 2017 are ELECTRICAL "
            "SYSTEM, mostly batteries that drain while parked. Ask "
            "if the battery and software fix were done.",
            "205 VISIBILITY/WIPER complaints on the 2017 and 326 on "
            "the 2019: cracking windshields.",
            "Ask for a CVT fluid change in the records, and check "
            "the oil level on the 2.5L.",
            "Three to five recalls on each year pulled.",
        ],
        "note": "Roomy and good in snow. Expect a battery, maybe a "
                "windshield, and insist on CVT service history.",
    },
    {
        # 2025: 3 recalls, 102 complaints, no dominant component.
        "make": "subaru", "model": "forester",
        "years": (2025, 2026),
        "generation": "SL sixth gen",
        "engine": "2.5L FB25 flat-four, CVT (hybrid also offered)",
        "reliability": 7.7,
        "maintenance": 7.3,
        "annual_maintenance_usd": 550,
        "insurance_factor": 0.97,
        "tire_set_usd": 780,
        "risk": None,
        "known_issues": [
            "Three recalls on the 2025. Check them against the VIN.",
            "102 complaints on the 2025, spread thin: collision "
            "avoidance (13), fuel system (13), wipers (13).",
            "The hybrid is new to the Forester and has no record "
            "yet. The plain 2.5L is the known quantity.",
        ],
        "note": "A reskin of a sound car. Slightly provisional while "
                "the new electronics settle.",
    },
    {
        # 2019: 3 recalls, 834 complaints, 370 VISIBILITY/WIPER.
        # 2021: 215 complaints; the recall endpoint returned nothing.
        "make": "subaru", "model": "forester",
        "years": (2019, 2024),
        "generation": "SK fifth gen (SGP)",
        "engine": "2.5L FB25 flat-four, CVT",
        "reliability": 7.8,
        "maintenance": 7.5,
        "annual_maintenance_usd": 550,
        "insurance_factor": 0.97,
        "tire_set_usd": 760,
        "risk": None,
        "known_issues": [
            "370 of 834 complaints on the 2019 are VISIBILITY/WIPER "
            "(44%): windshields that crack. Inspect the glass and "
            "check your glass cover.",
            "The 2021 file is a quarter the size (215 complaints).",
            "Some cars need a thermostat or air-conditioning "
            "condenser early. Run the heat and the AC on the drive.",
            "No turbo and no hybrid in these years: one engine, one "
            "gearbox, both understood.",
        ],
        "note": "Plain, roomy and easy to see out of. The cracked "
                "glass is real but it is not a mechanical fault.",
    },
    {
        # 2015: 3 recalls, 617 complaints, 131 ENGINE. 2017: 1
        # recall, 593 complaints, 167 AIR BAGS.
        "make": "subaru", "model": "forester",
        "years": (2014, 2018),
        "generation": "SJ fourth gen",
        "engine": "2.5L FB25 flat-four (2.0L FA20 turbo on XT), CVT "
                  "or 6-speed manual",
        "reliability": 7.0,
        "maintenance": 7.3,
        "annual_maintenance_usd": 620,
        "insurance_factor": 0.97,
        "tire_set_usd": 720,
        "risk": "Oil consumption on 2014 and 2015 2.5L engines, bad "
                "enough in some cars to need a new short block, "
                "plus the earlier CVT",
        "known_issues": [
            "131 of 617 complaints on the 2015 are ENGINE, and oil "
            "use is the common story. Check the level cold and ask "
            "for oil consumption test results.",
            "167 AIR BAGS complaints on the 2017: the passenger seat "
            "sensor switches the airbag off. Watch the airbag light "
            "with someone in the seat.",
            "Ask for CVT fluid service on any car past 60k miles.",
        ],
        "note": "2017 and 2018 are the safer years. On a 2014 or "
                "2015, proof of low oil use decides it.",
    },
    {
        # 2021: 2 recalls, 106 complaints. 2023: 4 recalls, 47.
        "make": "subaru", "model": "ascent",
        "years": (2021, 2026),
        "generation": "WM first gen, later years",
        "engine": "2.4L FA24 turbo flat-four, CVT",
        "reliability": 7.0,
        "maintenance": 6.8,
        "annual_maintenance_usd": 640,
        "insurance_factor": 1.02,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "106 complaints on the 2021 against 444 on the 2019. "
            "The early faults were mostly fixed.",
            "Four recalls on the 2023, two on the 2021. Check the "
            "VIN.",
            "A turbo four and a CVT moving a three-row SUV work "
            "hard. Change the CVT fluid early if you tow.",
        ],
        "note": "The Ascent to buy if you want one. Still Subaru's "
                "most stressed drivetrain.",
    },
    {
        # 2019: 9 recalls, 444 complaints, 160 ELECTRICAL SYSTEM
        # and 90 POWER TRAIN.
        "make": "subaru", "model": "ascent",
        "years": (2019, 2020),
        "generation": "WM first gen, launch years",
        "engine": "2.4L FA24 turbo flat-four, CVT",
        "reliability": 6.0,
        "maintenance": 6.8,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.02,
        "tire_set_usd": 900,
        "risk": "CVT failures on launch-year cars: 90 POWER TRAIN "
                "complaints on the 2019, many describing a "
                "replacement transmission, and nine recalls",
        "known_issues": [
            "Nine recalls on the 2019. That is nine separate "
            "defects, not a sales-volume effect.",
            "90 POWER TRAIN complaints on the 2019: slipping, "
            "hesitation and replaced CVTs. Ask if the transmission "
            "is original.",
            "160 ELECTRICAL SYSTEM complaints on the 2019, with "
            "drained batteries common.",
        ],
        "note": "A launch year that went badly. Buy a 2021 or later "
                "one instead unless the price is very low.",
    },
    {
        # 2022: 1 recall, 25 complaints, 15 ENGINE. 2023: 1 recall,
        # 9 complaints.
        "make": "subaru", "model": "wrx",
        "years": (2022, 2026),
        "generation": "VB fifth gen",
        "engine": "2.4L FA24 turbo flat-four, 6-speed manual or CVT",
        "reliability": 7.2,
        "maintenance": 6.5,
        "annual_maintenance_usd": 680,
        "insurance_factor": 1.22,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "15 of 25 complaints on the 2022 are ENGINE. A small "
            "file, but ask for oil change records on a first-year "
            "car.",
            "One recall on each of the 2022 and 2023.",
            "Many are tuned or driven hard. A stock car with "
            "paperwork is worth paying extra for.",
        ],
        "note": "The 2.4L is less highly strung than the old 2.0L. "
                "Condition and previous owner matter most.",
    },
    {
        # 2015: 3 recalls, 52 complaints. 2018: 2 recalls, 43.
        "make": "subaru", "model": "wrx",
        "years": (2015, 2021),
        "generation": "VA fourth gen",
        "engine": "2.0L FA20 turbo flat-four, 6-speed manual or CVT "
                  "(the STI uses a different engine)",
        "reliability": 6.8,
        "maintenance": 6.5,
        "annual_maintenance_usd": 720,
        "insurance_factor": 1.25,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "ENGINE and POWER TRAIN lead the 2015 file (18 each of "
            "52 complaints).",
            "Check for an aftermarket tune, intake or blow-off "
            "valve. Modified cars are where the engine failures "
            "come from.",
            "Clutches wear quickly on hard-driven cars. Feel for "
            "slip in a high gear.",
        ],
        "note": "Sound when stock and serviced, a gamble when "
                "modified. The STI is a separate, riskier car.",
    },
    {
        # 2022: 1 recall, 10 complaints, 6 ENGINE. 2023: 1
        # complaint; the recall endpoint returned nothing.
        "make": "subaru", "model": "brz",
        "years": (2022, 2026),
        "generation": "ZD8 second gen",
        "engine": "2.4L FA24 flat-four, 6-speed manual or automatic",
        "reliability": 7.8,
        "maintenance": 7.0,
        "annual_maintenance_usd": 560,
        "insurance_factor": 1.2,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "6 of 10 complaints on the 2022 are ENGINE. Tiny "
            "numbers, but track-driven cars have had oil supply "
            "failures. Ask how the car was used.",
            "One recall on the 2022.",
            "Rear-wheel drive on summer tires: it needs a set of "
            "winters to be used year-round.",
        ],
        "note": "Simple, light and non-turbo. Provisional because "
                "the NHTSA file is so small.",
    },
    {
        # 2017: 7 complaints; the recall endpoint returned nothing.
        "make": "subaru", "model": "brz",
        "years": (2013, 2020),
        "generation": "ZC6 first gen",
        "engine": "2.0L FA20 flat-four, 6-speed manual or automatic",
        "reliability": 7.8,
        "maintenance": 7.2,
        "annual_maintenance_usd": 560,
        "insurance_factor": 1.18,
        "tire_set_usd": 750,
        "risk": None,
        "known_issues": [
            "2013 cars had a valve spring recall, and some engines "
            "failed after the dealer repair. On a 2013, ask who did "
            "the work and when.",
            "Only 7 complaints on the 2017 and no recalls returned. "
            "Few were sold, so that proves little.",
            "Check for track use and modifications.",
        ],
        "note": "A cheap, honest sports car. Provisional: scored on "
                "the generation's reputation more than on data.",
    },
    {
        # 2023: 4 recalls, 25 complaints. 2024: 2 recalls, 14.
        "make": "subaru", "model": "solterra",
        "years": (2023, 2026),
        "generation": "first gen (shared with the Toyota bZ4X)",
        "engine": "Dual electric motors, about 72 kWh battery; AWD "
                  "standard",
        "reliability": 7.0,
        "maintenance": 7.0,
        "annual_maintenance_usd": 360,
        "insurance_factor": 1.12,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2023, two on the 2024. Confirm "
            "every one is closed.",
            "Slow DC fast charging on 2023 and 2024 cars, and it "
            "gets slower in the cold. Fine for home charging, "
            "tiring on a road trip.",
            "Range is modest for the battery size. Check the "
            "figure for the exact trim and wheel.",
            "Complaints are few (25 on the 2023) and mostly driver "
            "aids, not the battery or motors.",
        ],
        "note": "Toyota hardware with Subaru AWD tuning. Dependable "
                "so far, but an average EV. Later years charge "
                "faster.",
    },
]
