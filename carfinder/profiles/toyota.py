"""Reliability profiles: Toyota. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

Recall counts quoted here are everything NHTSA lists for that model
year, which for Toyota includes small label and accessory campaigns
run by regional distributors (Gulf States, Southeast Toyota). Where
those pad the count, the profile says so.

Dealer feeds often list hybrids as their own model ("RAV4 Hybrid").
These profiles are keyed on the base model name; the hybrid is
described inside the same profile."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    # ---- Camry -------------------------------------------------------
    {
        # Written 2026-08-14 from a research pull on a 2025 example.
        # The 2025 redesign is hybrid-only and a different car from the
        # XV70 below. Do not let the older profile's numbers apply to it.
        "make": "toyota", "model": "camry",
        "years": (2025, 2026),
        "generation": "XV80, ninth gen, hybrid only",
        "engine": "2.5L + hybrid system, 184 hp combined; AWD via a rear "
                  "electric motor rather than a driveshaft",
        "reliability": 8.5,
        "maintenance": 9.0,
        "annual_maintenance_usd": 380,
        "insurance_factor": 1.0,
        "tire_set_usd": 720,
        "risk": None,
        "known_issues": [
            "First model year of a full redesign. 144 NHTSA complaints vs "
            "46 for the 2024, but the shape is reassuring: electrical, "
            "seats, wipers and driver-assist, with only 8 engine and 8 "
            "powertrain filings. The hybrid drivetrain itself is quiet in "
            "the data.",
            "Widely reported low-oil-level warning that appears with "
            "correct oil; dealers call it a software fault and owners "
            "report no fix available.",
            "Lane-departure and collision-avoidance systems are "
            "intrusive, with multiple reports of the wheel fighting the "
            "driver. Try them on the test drive.",
            "Real-world mpg falls well short of the 50 EPA combined in "
            "cold weather; one owner reported 34. Budget closer to 40-45 "
            "for a cold-climate year.",
        ],
        "note": "Hybrid-only redesign. Roughly 70% better fuel economy "
                "than the outgoing gas AWD car, and Toyota's hybrid system "
                "is long-proven even if this body is not.",
    },
    {
        "make": "toyota", "model": "camry",
        "years": (2020, 2024),
        "generation": "XV70 (2020+ AWD)",
        "engine": "2.5L A25A-FKS I4",
        "reliability": 9.3,
        "maintenance": 9.5,
        "annual_maintenance_usd": 400,
        "insurance_factor": 0.95,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "Very few systemic faults; the AWD hardware is shared with the "
            "RAV4 and is well proven.",
            "Some 2020-21 cars had infotainment software gripes: a dealer "
            "update, not a mechanical problem.",
        ],
        "note": "AWD offered 2020+. Bulletproof powertrain, cheapest and "
                "easiest to fix, parts available at any shop.",
    },
    {
        # 2018: 8 recalls, 757 complaints. 2019: 6 recalls, 405.
        "make": "toyota", "model": "camry",
        "years": (2018, 2019),
        "generation": "XV70, eighth gen, first two years",
        "engine": "2.5L A25A-FKS I4 with 8-speed automatic; 3.5L V6 or "
                  "2.5L hybrid optional",
        "reliability": 8.2,
        "maintenance": 9.3,
        "annual_maintenance_usd": 410,
        "insurance_factor": 0.95,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "The launch years are the weak ones. The 2018 has 8 recalls "
            "and 757 complaints, with power train the top component "
            "(202); the 2019 has 6 recalls and 405 complaints.",
            "Owners widely report the new 8-speed automatic hesitating "
            "or shifting roughly at low speed. Drive it in stop-and-go "
            "traffic before buying.",
            "Confirm the fuel pump recalls (20V012000, 20V682000) and "
            "the brake vacuum pump recall (21V890000) are done.",
        ],
        "note": "Still a Camry and cheap to run, but a 2020 or later car "
                "of the same generation has a much quieter record.",
    },
    {
        # 2015: 1 recall, 271 complaints. 2016: 2 recalls, 189.
        "make": "toyota", "model": "camry",
        "years": (2015, 2017),
        "generation": "XV50, seventh gen facelift",
        "engine": "2.5L 2AR-FE I4 with 6-speed automatic; 3.5L V6 or "
                  "2.5L hybrid optional",
        "reliability": 9.1,
        "maintenance": 9.5,
        "annual_maintenance_usd": 390,
        "insurance_factor": 0.95,
        "tire_set_usd": 680,
        "risk": None,
        "known_issues": [
            "One recall on the 2015 (15V144000, electric power steering) "
            "and steering is the top complaint component that year (105 "
            "of 271). Confirm the recall was completed.",
            "The 2016 file is quieter: 2 recalls and 189 complaints with "
            "no dominant component.",
            "Port-injected four and a conventional 6-speed automatic. "
            "There is very little here to go wrong; at this age buy on "
            "service history and rust.",
        ],
        "note": "One of the safest used sedans to own. Old enough now "
                "that condition matters more than the nameplate.",
    },
    # ---- Corolla Cross -----------------------------------------------
    {
        # 2022: 2 recalls and 44 complaints with ENGINE the top
        # component at 14. The early cars are the weaker buy.
        "make": "toyota", "model": "corolla cross",
        "years": (2022, 2023),
        "generation": "first gen, early build",
        "engine": "2.0L M20A-FKS I4 with CVT, or the 2.0L hybrid "
                  "(hybrid adds a rear motor for AWD)",
        "reliability": 7.6,
        "maintenance": 8.8,
        "annual_maintenance_usd": 410,
        "insurance_factor": 0.98,
        "tire_set_usd": 680,
        "risk": None,
        "known_issues": [
            "Engine is the top complaint component on the 2022 (14 of "
            "44). The later cars clean this up considerably.",
            "Two recalls: 23V384000 (instrument panel perforation "
            "affecting passenger airbag deployment) and 23V864000 "
            "(frontal airbags). Both need confirming as completed.",
            "The non-hybrid uses a CVT. Toyota's is far better proven "
            "than Nissan's Xtronic, but it is still a CVT.",
            "Noisy at highway speed.",
        ],
        "note": "Toyota running costs and resale in a subcompact SUV "
                "package. Prefer a later car if the price gap allows.",
    },
    {
        # 2026: 0 recalls, 21 complaints, no cluster.
        "make": "toyota", "model": "corolla cross",
        "years": (2024, 2026),
        "generation": "first gen, updated",
        "engine": "2.0L M20A-FKS I4 with CVT, or the 2.0L hybrid "
                  "(hybrid adds a rear motor for AWD)",
        "reliability": 8.5,
        "maintenance": 8.8,
        "annual_maintenance_usd": 400,
        "insurance_factor": 0.98,
        "tire_set_usd": 680,
        "risk": None,
        "known_issues": [
            "2026: zero recalls and 21 complaints, none of them a "
            "cluster. One of the cleanest records of the small SUVs profiled "
            "here.",
            "Hybrid propulsion is the top component (5 of 21) but at "
            "that volume it is noise, not a pattern.",
            "Still a CVT on the non-hybrid, and still loud on the highway.",
            "Holds value well, which raises the purchase price. The "
            "long-run cost math is better than the sticker suggests.",
        ],
        "note": "One of the safest small-SUV picks on the data. Costs more up "
                "front than its rivals and gives most of it back in resale.",
    },
    # ---- RAV4 --------------------------------------------------------
    {
        # NHTSA returned nothing for the 2026 at the time of writing.
        "make": "toyota", "model": "rav4",
        "years": (2026, 2026),
        "generation": "XA60 sixth gen, hybrid and plug-in hybrid only",
        "engine": "2.5L hybrid, or the same engine as a plug-in hybrid; "
                  "AWD via a rear electric motor",
        "reliability": 8.0,
        "maintenance": 8.6,
        "annual_maintenance_usd": 420,
        "insurance_factor": 1.0,
        "tire_set_usd": 800,
        "risk": None,
        "known_issues": [
            "First model year of a full redesign. NHTSA had no recalls "
            "or complaints on file for the 2026 when this was written, "
            "which means too new to judge, not clean.",
            "No gas-only version any more. The hybrid system is a "
            "development of the one Toyota has sold for years; the new "
            "cabin software is the unproven part.",
            "The plug-in costs several thousand more. It only pays back "
            "if you can charge at home most nights.",
        ],
        "note": "Provisional score. The drivetrain has a long record, the "
                "body and electronics do not yet. A late XA50 is the "
                "known quantity.",
    },
    {
        "make": "toyota", "model": "rav4",
        "years": (2019, 2025),
        "generation": "XA50 fifth gen",
        "engine": "2.5L A25A-FKS I4, 8-speed automatic; hybrid adds a "
                  "rear motor for AWD",
        "reliability": 8.2,
        "maintenance": 8.6,
        "annual_maintenance_usd": 430,
        "insurance_factor": 1.0,
        "tire_set_usd": 780,
        "risk": None,
        "known_issues": [
            "167 complaints on the 2024 against a very large sales "
            "base, spread across engine (37), electrical (32) and "
            "steering (25) with no single dominant cluster.",
            "Three recalls on the 2024, including 24V911000 (brake "
            "calipers). Check the VIN.",
            "Strong resale means the affordable ones are high-mileage; budget "
            "accordingly.",
            "A conventional 8-speed automatic, no CVT and no turbo.",
        ],
        "note": "The default answer to 'reliable compact SUV', and "
                "priced accordingly. At the price of a newer subcompact you "
                "trade low miles for Toyota's record.",
    },
    {
        # 2016: 3 recalls, 239 complaints. 2018: 3 recalls, 333
        # complaints, 33 of them reporting a fire.
        "make": "toyota", "model": "rav4",
        "years": (2015, 2018),
        "generation": "XA40 fourth gen",
        "engine": "2.5L 2AR-FE I4 with 6-speed automatic; hybrid from "
                  "2016",
        "reliability": 8.6,
        "maintenance": 8.8,
        "annual_maintenance_usd": 420,
        "insurance_factor": 0.98,
        "tire_set_usd": 720,
        "risk": None,
        "known_issues": [
            "Recall 23V734000 covers 2013-2018 cars: some replacement "
            "12V batteries can shift and short against the hold-down "
            "clamp. The 2018 file has 33 complaints reporting a fire "
            "and electrical is its top component (130 of 333). Confirm "
            "the recall is done.",
            "Outside that, three recalls each on the 2016 and 2018 and "
            "no engine or transmission cluster.",
            "Some owners report a shudder from the 6-speed automatic's "
            "torque converter at light throttle around 25-45 mph. Feel "
            "for it on the test drive.",
        ],
        "note": "Simple, proven and cheap to keep. Do the battery recall "
                "and it is one of the lowest-risk used SUVs on sale.",
    },
    # ---- Corolla -----------------------------------------------------
    {
        "make": "toyota", "model": "corolla",
        "years": (2023, 2026),
        "generation": "E210, twelfth gen facelift",
        "engine": "2.0L M20A-FKS I4 with CVT; the hybrid pairs a 1.8L "
                  "with Toyota's proven hybrid system",
        "reliability": 8.7,
        "maintenance": 9.0,
        "annual_maintenance_usd": 360,
        "insurance_factor": 0.95,
        "tire_set_usd": 620,
        "risk": None,
        "known_issues": [
            "15 complaints on the 2026 with no cluster, and one recall "
            "(26V110000, headlights). About as quiet as a file gets.",
            "The safest mechanical package among the sedans profiled "
            "here: Toyota's CVT and a naturally aspirated four, both "
            "long-proven.",
            "Depreciated 11.4%/yr in one Michigan market (Aug 2026) against "
            "the Camry's 9.9%. The cheaper car is not automatically the "
            "cheaper car to own, so check your local curve.",
            "Noticeably smaller inside than a Camry or Accord, and "
            "slower. It is a commuter, not a highway cruiser.",
        ],
        "note": "Excellent car. Compare it against a Camry hybrid on total "
                "cost before assuming the smaller car is cheaper to own.",
    },
    {
        # 2020: 3 recalls, 316 complaints (engine 111).
        # 2021: 1 recall, 188 complaints.
        "make": "toyota", "model": "corolla",
        "years": (2020, 2022),
        "generation": "E210, twelfth gen, before the facelift",
        "engine": "1.8L 2ZR-FAE or 2.0L M20A-FKS I4 with CVT; hybrid "
                  "uses a 1.8L",
        "reliability": 8.3,
        "maintenance": 9.0,
        "annual_maintenance_usd": 365,
        "insurance_factor": 0.95,
        "tire_set_usd": 620,
        "risk": None,
        "known_issues": [
            "The 2020 launch year is the noisy one: 316 complaints with "
            "engine the top component (111). By 2021 the file drops to "
            "188 with air bags leading (53).",
            "Recall 23V865000 (front passenger occupant sensor, which "
            "can stop the airbag deploying) covers 2020-2021 cars. "
            "Confirm it is done.",
            "The 2.0L is the better engine to live with; the 1.8L is "
            "slow but very simple.",
        ],
        "note": "A sound cheap commuter. Prefer a 2021 or 2022 over the "
                "2020 if the price is close.",
    },
    {
        # 2016: 1 recall, 216 complaints. 2019: 5 recalls, 207.
        "make": "toyota", "model": "corolla",
        "years": (2015, 2019),
        "generation": "E170, eleventh gen sedan (the 2019 hatchback is "
                      "the newer E210)",
        "engine": "1.8L 2ZR-FE I4 with CVT or 6-speed manual",
        "reliability": 8.9,
        "maintenance": 9.3,
        "annual_maintenance_usd": 350,
        "insurance_factor": 0.95,
        "tire_set_usd": 580,
        "risk": None,
        "known_issues": [
            "One recall on the 2016 (20V024000, airbag control module) "
            "and air bags are the top complaint component (65 of 216). "
            "Confirm the recall was completed.",
            "The 2019 lists 5 recalls, but one is for the hatchback's "
            "CVT torque converter (18V901000) and two are distributor "
            "label campaigns.",
            "A port-injected 1.8L that has been in production for many "
            "years. Slow, noisy, and very hard to kill.",
        ],
        "note": "About as cheap to keep running as a car gets. Dull to "
                "drive, and that is the whole complaint.",
    },
    # ---- Prius -------------------------------------------------------
    {
        # 2023: 4 recalls, 21 complaints. 2024: 4 recalls, 27.
        "make": "toyota", "model": "prius",
        "years": (2023, 2026),
        "generation": "XW60 fifth gen",
        "engine": "2.0L hybrid, 194 hp (196 with AWD); AWD adds a rear "
                  "electric motor",
        "reliability": 8.3,
        "maintenance": 8.6,
        "annual_maintenance_usd": 400,
        "insurance_factor": 0.98,
        "tire_set_usd": 720,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2023-2024 cars for the rear door "
            "switches (24V274000 and 26V049000): water can get in and a "
            "rear door can open while driving. Confirm both are done.",
            "Complaint volume is low (21 on the 2023, 27 on the 2024) "
            "with no component standing out.",
            "Low roofline and small rear door openings. Sit in the back "
            "before buying it as a family car.",
        ],
        "note": "The first Prius people buy for its looks. The hybrid "
                "system is proven; get the door recalls confirmed.",
    },
    {
        # 2016: 5 recalls, 181 complaints. 2017: 3 recalls, 91.
        # 2020: 0 recalls, 14 complaints.
        "make": "toyota", "model": "prius",
        "years": (2016, 2022),
        "generation": "XW50 fourth gen",
        "engine": "1.8L 2ZR-FXE hybrid; AWD-e with a small rear motor "
                  "from 2019",
        "reliability": 9.0,
        "maintenance": 8.8,
        "annual_maintenance_usd": 400,
        "insurance_factor": 0.95,
        "tire_set_usd": 620,
        "risk": None,
        "known_issues": [
            "The record improves steadily: 5 recalls and 181 complaints "
            "on the 2016, 3 and 91 on the 2017, none and 14 on the 2020.",
            "On 2016-2018 cars confirm recall 18V579000 (engine wire "
            "harness that can chafe and short).",
            "Visibility and wipers lead the 2016 complaints (42 of "
            "181), mostly windshields that crack easily. Check the "
            "glass and your insurance glass cover.",
            "The hybrid battery is the long-run cost. On a car past "
            "150k miles, price in a replacement pack.",
        ],
        "note": "The taxi driver's choice for a reason. A 2019 or later "
                "car is the one to have.",
    },
    {
        # 2015: 1 recall, 168 complaints, 95 of them service brakes.
        "make": "toyota", "model": "prius",
        "years": (2015, 2015),
        "generation": "XW30 third gen, final year",
        "engine": "1.8L 2ZR-FXE hybrid",
        "reliability": 7.7,
        "maintenance": 8.4,
        "annual_maintenance_usd": 450,
        "insurance_factor": 0.95,
        "tire_set_usd": 600,
        "risk": "Brake booster and actuator failures (service brakes "
                "are 95 of 168 complaints on the 2015), and at high "
                "mileage a clogged EGR circuit that leads to head "
                "gasket failure",
        "known_issues": [
            "Service brakes are 95 of the 168 complaints on the 2015, "
            "a lopsided share. Ask whether the brake booster and "
            "actuator have been replaced; out of warranty it is a "
            "four-figure repair.",
            "This generation is known for EGR cooler clogging that ends "
            "in a head gasket failure, usually past 120k miles. A cold "
            "start that shakes or knocks is the warning.",
            "Confirm recall 20V369000 (hybrid inverter) is done.",
            "The original hybrid battery is now more than ten years "
            "old.",
        ],
        "note": "Cheap to buy and cheap on fuel, but this is the Prius "
                "generation with real age-related bills. The 2016 "
                "redesign is a much safer used buy.",
    },
    # ---- Highlander --------------------------------------------------
    {
        # 2020: 4 recalls, 323 complaints. 2021: 4 recalls, 543.
        # 2024: 7 recalls, 43 complaints.
        "make": "toyota", "model": "highlander",
        "years": (2020, 2026),
        "generation": "XU70 fourth gen",
        "engine": "3.5L V6 with 8-speed automatic through 2022, 2.4L "
                  "turbo I4 from 2023; 2.5L hybrid optional",
        "reliability": 7.8,
        "maintenance": 8.2,
        "annual_maintenance_usd": 480,
        "insurance_factor": 1.0,
        "tire_set_usd": 880,
        "risk": None,
        "known_issues": [
            "Power train is a lopsided share of the early files: 127 of "
            "323 complaints on the 2020 and 237 of 543 on the 2021. "
            "Test the transmission carefully on a 2020-2022 car.",
            "Seven recalls on the 2024, though two are tire campaigns "
            "run by regional distributors. The ones that matter cover "
            "the second-row seat recliner (26V128000) and rear seat "
            "belt anchors (25V872000).",
            "Recall 23V720000 (2020-2023): the front bumper cover can "
            "detach. Confirm it is done.",
            "The 2.4L turbo from 2023 has less of a track record than "
            "the V6 it replaced. The hybrid is the proven choice.",
        ],
        "note": "A good family SUV with a noisier record than its "
                "reputation suggests. The hybrid, or a 2023 or later "
                "car, is the better bet.",
    },
    {
        # 2017: 4 recalls, 272 complaints (power train 78).
        "make": "toyota", "model": "highlander",
        "years": (2015, 2019),
        "generation": "XU50 third gen",
        "engine": "3.5L V6, 6-speed automatic through 2016 and 8-speed "
                  "from 2017; 2.7L I4 on base cars, hybrid optional",
        "reliability": 8.4,
        "maintenance": 8.4,
        "annual_maintenance_usd": 480,
        "insurance_factor": 1.0,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "Power train leads the 2017 complaints (78 of 272), the "
            "year the 8-speed automatic arrived. Owners describe "
            "hesitation and harsh low-speed shifts.",
            "The 2015-2016 cars keep the older 6-speed, which is the "
            "smoother and better-proven gearbox.",
            "Four recalls on the 2017, half of them distributor "
            "accessory campaigns. On 2018-2019 cars confirm the fuel "
            "pump recall (20V012000).",
        ],
        "note": "A dependable three-row. For the least trouble pick a "
                "2015-2016 V6 with the 6-speed.",
    },
    # ---- Grand Highlander --------------------------------------------
    {
        # 2024: 4 recalls, 242 complaints. 2025: 3 recalls, 81.
        "make": "toyota", "model": "grand highlander",
        "years": (2024, 2026),
        "generation": "first gen",
        "engine": "2.4L turbo I4 with 8-speed automatic, 2.5L hybrid, "
                  "or the 2.4L turbo Hybrid Max",
        "reliability": 7.2,
        "maintenance": 8.0,
        "annual_maintenance_usd": 500,
        "insurance_factor": 1.02,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "A rough first year: 242 complaints on the 2024 against 81 "
            "on the 2025, led by power train (53), engine (38) and "
            "fuel system (35).",
            "Recall 24V461000: the driver side curtain airbag may not "
            "deploy properly with the window open. Sales were stopped "
            "for months over it. Confirm it is done.",
            "The 2.5L hybrid is the proven drivetrain. The turbo four "
            "and the Hybrid Max are newer and more complex.",
        ],
        "note": "The most useful three-row Toyota sells, still settling "
                "down. A 2025 or later hybrid is the pick.",
    },
    # ---- Tacoma ------------------------------------------------------
    {
        # 2024: 5 recalls, 156 complaints. 2025: 5 recalls, 118.
        "make": "toyota", "model": "tacoma",
        "years": (2024, 2026),
        "generation": "N400 fourth gen",
        "engine": "2.4L turbo I4 with 8-speed automatic or 6-speed "
                  "manual; i-Force Max adds a hybrid motor",
        "reliability": 6.8,
        "maintenance": 7.6,
        "annual_maintenance_usd": 560,
        "insurance_factor": 1.02,
        "tire_set_usd": 950,
        "risk": "Five recalls each on the 2024 and 2025, and power "
                "train is the top complaint component on the 2024 (55 "
                "of 156), matching reports of early 8-speed automatic "
                "failures",
        "known_issues": [
            "Five recalls on the 2024 and five on the 2025, including "
            "the brakes (25V058000), rear shock absorbers (26V514000) "
            "and, on the 2025, the driveshaft (25V656000).",
            "Power train leads the 2024 complaints (55 of 156). Early "
            "trucks had 8-speed automatics replaced under warranty; "
            "ask for the service history.",
            "Structure is the top component on the 2025 (44 of 118). "
            "Read the open recalls for the VIN before you sign.",
            "A turbo four replaces the old V6. Stronger and more "
            "efficient, with far less history behind it.",
        ],
        "note": "A much better truck to drive than the one it replaced "
                "and, so far, a less dependable one. Buy with warranty "
                "left.",
    },
    {
        # 2017: 5 recalls, 246 complaints. 2020: 1 recall, 90.
        "make": "toyota", "model": "tacoma",
        "years": (2016, 2023),
        "generation": "N300 third gen",
        "engine": "3.5L 2GR-FKS V6 with 6-speed automatic or manual; "
                  "2.7L I4 on base trucks",
        "reliability": 8.3,
        "maintenance": 8.6,
        "annual_maintenance_usd": 480,
        "insurance_factor": 1.0,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "The 2016-2017 trucks are the weak years: 5 recalls and 246 "
            "complaints on the 2017, including the crank position "
            "sensor (17V356000) and a rear differential leak "
            "(17V285000). By 2020 it is 1 recall and 90 complaints.",
            "Power train leads the 2017 file (68). The automatic hunts "
            "between gears and feels short of low-end pull; a dealer "
            "reflash helps. Drive it on a hill.",
            "Check the frame and rear leaf springs for rust on any "
            "truck from a salt state.",
        ],
        "note": "Holds its value better than almost anything on the "
                "road. A 2018 or later truck is the one to buy.",
    },
    {
        # 2015: 4 recalls, 102 complaints.
        "make": "toyota", "model": "tacoma",
        "years": (2015, 2015),
        "generation": "N200 second gen, final year",
        "engine": "4.0L 1GR-FE V6 or 2.7L 2TR-FE I4, 5-speed automatic "
                  "or manual",
        "reliability": 8.7,
        "maintenance": 8.8,
        "annual_maintenance_usd": 460,
        "insurance_factor": 1.0,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "Frame rust is the thing that ends these trucks. Get under "
            "it with a light and a screwdriver before anything else.",
            "Four recalls on the 2015, mostly tire, label and accessory "
            "campaigns, and 102 complaints with no dominant component.",
            "The 4.0L V6 and 5-speed automatic are old designs with a "
            "very long record. Thirsty, but simple.",
        ],
        "note": "Mechanically one of the toughest trucks sold. Buy the "
                "frame, not the odometer.",
    },
    # ---- Tundra ------------------------------------------------------
    {
        # 2022: 13 recalls, 434 complaints (engine 166).
        # 2024: 10 recalls, 358 (engine 157). 2025: 5 recalls, 144.
        "make": "toyota", "model": "tundra",
        "years": (2022, 2026),
        "generation": "XK70 third gen",
        "engine": "3.4L twin-turbo V6 (V35A-FTS) with 10-speed "
                  "automatic; i-Force Max adds a hybrid motor",
        "reliability": 5.4,
        "maintenance": 6.6,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.08,
        "tire_set_usd": 1050,
        "risk": "Engine main bearing failures from machining debris "
                "left in the block: two engine recalls so far "
                "(24V381000 and 25V767000), with engine the top "
                "complaint component on the 2022 and 2024",
        "known_issues": [
            "Thirteen recalls on the 2022 and ten on the 2024. Recall "
            "count does not scale with sales, so these are bad numbers "
            "for any truck and startling for a Toyota.",
            "Engine is the top complaint component on the 2022 (166 of "
            "434) and the 2024 (157 of 358). Toyota is replacing "
            "engines under recall; ask whether this truck has had its "
            "engine replaced and get the paperwork.",
            "Also confirm 24V125000 (automatic transmission) and "
            "22V445000 (rear axle shaft, 2022 trucks).",
            "The 2025 file is calmer (5 recalls, 144 complaints) but "
            "engine still leads it (48).",
        ],
        "note": "The least dependable Toyota profiled here. Do not buy "
                "one without a recall printout for the VIN and factory "
                "powertrain warranty remaining.",
    },
    {
        # 2018: 9 recalls, 100 complaints.
        "make": "toyota", "model": "tundra",
        "years": (2015, 2021),
        "generation": "XK50 second gen facelift",
        "engine": "5.7L 3UR-FE V8 with 6-speed automatic (a 4.6L V8 "
                  "was offered through 2019)",
        "reliability": 8.6,
        "maintenance": 8.2,
        "annual_maintenance_usd": 560,
        "insurance_factor": 1.05,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "Nine recalls on the 2018, a high count, but they are "
            "lighting, labels, software, power steering and the fuel "
            "pump (20V012000) rather than engine or transmission. "
            "Complaints are low (100) with electrical leading (26).",
            "The 5.7L V8 can seep oil at the cam towers. It is a leak, "
            "not a failure, but it is expensive to reseal; look for "
            "oil on the back of the heads.",
            "Expect 13-15 mpg. Fuel is the real running cost.",
            "Check the frame for rust on trucks from salt states.",
        ],
        "note": "An old design that outlasts its rivals. This is the "
                "Tundra to buy used, well ahead of the 2022 redesign.",
    },
    # ---- Sequoia -----------------------------------------------------
    {
        # NHTSA files this as "Sequoia Hybrid". 2023: 5 recalls, 39
        # complaints.
        "make": "toyota", "model": "sequoia",
        "years": (2023, 2026),
        "generation": "XK80 third gen, hybrid only",
        "engine": "3.4L twin-turbo V6 hybrid (i-Force Max) with "
                  "10-speed automatic",
        "reliability": 6.0,
        "maintenance": 6.5,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.1,
        "tire_set_usd": 1100,
        "risk": "Built on the Tundra's platform around the same "
                "twin-turbo V6 family, which Toyota has recalled for "
                "main bearing failure in the Tundra",
        "known_issues": [
            "Five recalls on the 2023, including the automatic "
            "transmission campaign it shares with the Tundra "
            "(24V125000) and a bumper part (24V640000).",
            "Only 39 complaints on the 2023 with no dominant "
            "component, so the Tundra's engine trouble has not shown "
            "up here at the same rate. It is still the same engine "
            "family: run the VIN for open recalls.",
            "The hybrid battery sits under the third row, which does "
            "not fold flat. Check the cargo space suits you.",
        ],
        "note": "Better on the data than the Tundra it is based on, but "
                "it carries the same question mark. Buy with warranty.",
    },
    {
        # 2018: 5 recalls, 20 complaints. 2020: 2 recalls, 4.
        "make": "toyota", "model": "sequoia",
        "years": (2015, 2022),
        "generation": "XK60 second gen",
        "engine": "5.7L 3UR-FE V8 with 6-speed automatic",
        "reliability": 8.6,
        "maintenance": 8.0,
        "annual_maintenance_usd": 600,
        "insurance_factor": 1.05,
        "tire_set_usd": 1050,
        "risk": None,
        "known_issues": [
            "Very quiet files: 20 complaints on the 2018 and 4 on the "
            "2020. The 2018 has 5 recalls, covering power steering "
            "(21V920000), the fuel pump and stability control software.",
            "Same V8 as the Tundra, so the same cam tower oil seep to "
            "look for, and the same 13-15 mpg.",
            "Trims with air suspension and adaptive dampers cost real "
            "money when those wear out. Simpler trims age better.",
        ],
        "note": "A dated, thirsty and very durable full-size SUV. Costs "
                "more in fuel than in repairs.",
    },
    # ---- 4Runner -----------------------------------------------------
    {
        # 2025: 1 recall, 63 complaints (service brakes 26).
        "make": "toyota", "model": "4runner",
        "years": (2025, 2026),
        "generation": "N500 sixth gen",
        "engine": "2.4L turbo I4 with 8-speed automatic; i-Force Max "
                  "adds a hybrid motor",
        "reliability": 7.2,
        "maintenance": 7.8,
        "annual_maintenance_usd": 540,
        "insurance_factor": 1.02,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "One recall on the 2025 and 63 complaints, with service "
            "brakes a large share (26). Pay attention to pedal feel on "
            "the test drive.",
            "Shares its frame, engine and 8-speed automatic with the "
            "2024 and later Tacoma, which has five recalls a year and "
            "a power train complaint cluster.",
            "First redesign in fifteen years. It gains power, economy "
            "and safety tech and gives up the old truck's simplicity.",
        ],
        "note": "Too new to have the old 4Runner's reputation, and its "
                "Tacoma sibling's record says to wait or buy with "
                "warranty.",
    },
    {
        # 2015: 9 recalls, 86 complaints. 2018: 5 recalls, 60.
        # 2022: 3 recalls, 39.
        "make": "toyota", "model": "4runner",
        "years": (2015, 2024),
        "generation": "N280 fifth gen",
        "engine": "4.0L 1GR-FE V6 with 5-speed automatic",
        "reliability": 9.0,
        "maintenance": 8.6,
        "annual_maintenance_usd": 500,
        "insurance_factor": 1.0,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "Low complaint counts for the whole run: 86 on the 2015, 60 "
            "on the 2018, 39 on the 2022, with no engine or "
            "transmission cluster in any of them.",
            "The recall counts look high (9 on the 2015, 5 on the "
            "2018) but most are distributor-installed accessories and "
            "labels. The ones to confirm are the Takata airbag "
            "inflator on 2015-2016 cars and the fuel pump on 2018-2019.",
            "Body-on-frame, so check the frame for rust. Trims with "
            "the KDSS suspension can leak at the hydraulic cylinders.",
            "About 17 mpg, and it drives like the truck it is.",
        ],
        "note": "One of the most durable vehicles sold in the US, and "
                "priced like it. You pay up front and in fuel, not in "
                "repairs.",
    },
    # ---- Sienna ------------------------------------------------------
    {
        # NHTSA files this as "Sienna Hybrid". 2021: 4 recalls, 45
        # complaints. 2023: 3 recalls, 70 complaints.
        "make": "toyota", "model": "sienna",
        "years": (2021, 2026),
        "generation": "XL40 fourth gen, hybrid only",
        "engine": "2.5L hybrid; AWD adds a rear electric motor",
        "reliability": 8.3,
        "maintenance": 8.4,
        "annual_maintenance_usd": 450,
        "insurance_factor": 0.98,
        "tire_set_usd": 800,
        "risk": None,
        "known_issues": [
            "Two recalls for the second-row seats (25V086000 for "
            "2021-2025 and 26V690000 for 2022-2026). Confirm both are "
            "done; this is where the family sits.",
            "Service brakes lead the 2023 complaints (27 of 70). Check "
            "that the brake pedal feels consistent at low speed.",
            "The hybrid system is the same family used in the RAV4 and "
            "Highlander hybrids and is quiet in the data.",
            "Around 36 mpg, which no other minivan matches. The engine "
            "is loud when pushed with a full load.",
        ],
        "note": "The minivan to buy if you keep cars a long time. Low "
                "fuel bills and a calm record; get the seat recalls done.",
    },
    {
        # 2017: 10 recalls, 160 complaints (power train 39).
        "make": "toyota", "model": "sienna",
        "years": (2015, 2020),
        "generation": "XL30 third gen facelift",
        "engine": "3.5L V6, 6-speed automatic through 2016 and 8-speed "
                  "from 2017; AWD optional",
        "reliability": 8.3,
        "maintenance": 8.4,
        "annual_maintenance_usd": 500,
        "insurance_factor": 0.98,
        "tire_set_usd": 780,
        "risk": None,
        "known_issues": [
            "Ten recalls on the 2017, but several are for wheelchair "
            "conversions by outside companies and for distributor "
            "labels. The factory ones to confirm are the fuel pump "
            "(20V012000, 20V682000).",
            "Power train leads the 2017 complaints (39 of 160), the "
            "first year of the 8-speed automatic. Check for harsh or "
            "delayed shifts at low speed.",
            "Power sliding doors are the classic Sienna fault. Open "
            "and close both several times, on a slope if you can.",
            "AWD cars use run-flat tires and carry no spare.",
        ],
        "note": "A solid used minivan and the only one of its era with "
                "AWD. The 2015-2016 6-speed cars are the smoothest.",
    },
    # ---- Venza -------------------------------------------------------
    {
        # NHTSA returned nothing for "Venza"; the file is under "Venza
        # Hybrid". 2021: 2 recalls, 188 complaints. 2023: 3 recalls, 21.
        "make": "toyota", "model": "venza",
        "years": (2021, 2024),
        "generation": "XU80 second gen, hybrid only",
        "engine": "2.5L hybrid; AWD standard via a rear electric motor",
        "reliability": 8.4,
        "maintenance": 8.4,
        "annual_maintenance_usd": 420,
        "insurance_factor": 1.0,
        "tire_set_usd": 820,
        "risk": None,
        "known_issues": [
            "Visibility is the top complaint on the 2021 (74 of 188), "
            "almost all of it windshields that crack easily. Check the "
            "glass and make sure your policy covers it.",
            "By 2023 the file is down to 21 complaints. Recalls are "
            "minor: turn signal bulbs on the 2021 (22V033000) and "
            "display software on later cars.",
            "A RAV4 Hybrid underneath, with the same proven "
            "drivetrain, less cargo room and a quieter cabin.",
        ],
        "note": "A dressed-up RAV4 Hybrid with nothing worrying in the "
                "data beyond the windshields. Dropped after 2024.",
    },
    # ---- Crown -------------------------------------------------------
    {
        # 2023: 4 recalls. 2024: 3 recalls. The complaints endpoint
        # returned nothing for either year.
        "make": "toyota", "model": "crown",
        "years": (2023, 2026),
        "generation": "S235 sixteenth gen",
        "engine": "2.5L hybrid, or the 2.4L turbo Hybrid Max with "
                  "6-speed automatic; AWD standard",
        "reliability": 8.0,
        "maintenance": 8.0,
        "annual_maintenance_usd": 430,
        "insurance_factor": 1.02,
        "tire_set_usd": 880,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2023 and three on the 2024, all "
            "cameras, displays, the instrument cluster (25V595000) or "
            "labels. Nothing mechanical.",
            "NHTSA returned no complaints at all for the Crown, which "
            "reads as a gap in the data rather than a clean record.",
            "The 2.5L hybrid is the proven drivetrain. The Hybrid Max "
            "is quicker, thirstier and more complex.",
        ],
        "note": "Provisional score, set from the recall list and the "
                "record of the hybrid system it shares with the Camry. "
                "Prefer the 2.5L.",
    },
    {
        # 2025: 3 recalls, complaints endpoint empty.
        "make": "toyota", "model": "crown signia",
        "years": (2025, 2026),
        "generation": "first gen",
        "engine": "2.5L hybrid; AWD standard via a rear electric motor",
        "reliability": 8.0,
        "maintenance": 8.0,
        "annual_maintenance_usd": 430,
        "insurance_factor": 1.02,
        "tire_set_usd": 880,
        "risk": None,
        "known_issues": [
            "Three recalls on the 2025, covering the instrument "
            "cluster (25V595000), the rear camera display (25V744000) "
            "and a label.",
            "NHTSA returned no complaints for it. Too new and too "
            "low-volume to read anything into that.",
            "Only sold with the 2.5L hybrid, the simpler of the two "
            "Crown drivetrains.",
        ],
        "note": "Provisional score. In effect the replacement for the "
                "Venza, with the same proven hybrid layout.",
    },
    # ---- Avalon ------------------------------------------------------
    {
        # 2019: 4 recalls, 71 complaints. 2021: 2 recalls, 21.
        "make": "toyota", "model": "avalon",
        "years": (2019, 2022),
        "generation": "XX50 fifth gen",
        "engine": "3.5L 2GR-FKS V6 with 8-speed automatic; 2.5L "
                  "hybrid, or 2.5L I4 with AWD from 2021",
        "reliability": 8.8,
        "maintenance": 8.9,
        "annual_maintenance_usd": 430,
        "insurance_factor": 0.97,
        "tire_set_usd": 780,
        "risk": None,
        "known_issues": [
            "71 complaints on the 2019 and 21 on the 2021, with no "
            "component dominating either file.",
            "On 2019-2020 cars confirm the fuel pump recall "
            "(20V682000); on 2020-2021 cars the passenger occupant "
            "sensor (23V865000).",
            "The hybrid returns over 40 mpg and is the one to look "
            "for.",
        ],
        "note": "A bigger, quieter Camry with the same running costs. "
                "Discontinued after 2022, which keeps prices fair.",
    },
    {
        # 2016: 3 recalls, 23 complaints.
        "make": "toyota", "model": "avalon",
        "years": (2015, 2018),
        "generation": "XX40 fourth gen",
        "engine": "3.5L 2GR-FE V6 with 6-speed automatic; 2.5L hybrid "
                  "optional",
        "reliability": 9.1,
        "maintenance": 9.0,
        "annual_maintenance_usd": 420,
        "insurance_factor": 0.97,
        "tire_set_usd": 740,
        "risk": None,
        "known_issues": [
            "Only 23 complaints on the 2016. The three recalls that "
            "year are all airbag related (knee airbag, occupant "
            "sensor, control module); confirm they are done.",
            "The port-injected V6 and 6-speed automatic are among "
            "Toyota's most durable pairings.",
            "The touch-sensitive dash buttons are fussy. That is the "
            "most common owner gripe.",
        ],
        "note": "Quietly one of the most dependable large sedans ever "
                "sold. Often owned gently; buy on condition.",
    },
    # ---- C-HR --------------------------------------------------------
    {
        # 2026: 1 recall, no complaints on file yet.
        "make": "toyota", "model": "c-hr",
        "years": (2026, 2026),
        "generation": "second US generation, battery electric",
        "engine": "Dual-motor AWD battery electric, built on the same "
                  "platform as the bZ",
        "reliability": 6.8,
        "maintenance": 7.2,
        "annual_maintenance_usd": 300,
        "insurance_factor": 1.1,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "One recall already on the 2026 (26V570000, electric "
            "propulsion system) and no complaints on file yet. Too new "
            "to judge.",
            "Shares its platform with the bZ, whose earlier years had "
            "wheel hub and defroster recalls and slow fast-charging.",
            "No oil changes, so routine upkeep is cheap. Battery and "
            "charging faults are the costs to watch; check what the "
            "battery warranty covers.",
        ],
        "note": "Provisional score. It shares only a name with the "
                "gas C-HR that ended in 2022.",
    },
    {
        # 2018: 1 recall, 328 complaints, 217 of them power train.
        # 2020: 1 recall, 66 complaints, 51 power train.
        "make": "toyota", "model": "c-hr",
        "years": (2018, 2022),
        "generation": "first gen",
        "engine": "2.0L 3ZR-FAE I4 with CVT; front-wheel drive only",
        "reliability": 6.8,
        "maintenance": 8.2,
        "annual_maintenance_usd": 430,
        "insurance_factor": 1.0,
        "tire_set_usd": 700,
        "risk": "CVT failures: power train is 217 of 328 complaints on "
                "the 2018 and 51 of 66 on the 2020, a lopsided share "
                "that survives the sales-volume problem",
        "known_issues": [
            "Power train is two thirds or more of the complaint file "
            "in both years checked. Owners describe a whine or grind "
            "from the CVT followed by replacement of the whole unit.",
            "Listen for a hum that rises with road speed, and ask for "
            "proof of any transmission replacement.",
            "Only one recall in each year checked, so this is not "
            "covered by a campaign. Out of warranty the bill is yours.",
            "Never offered with AWD in the US, and the back seat is "
            "dark and tight.",
        ],
        "note": "The rare Toyota with a real drivetrain problem. A "
                "Corolla Cross does the same job without it.",
    },
    # ---- bZ4X / bZ ---------------------------------------------------
    {
        # 2026: 1 recall, 5 complaints.
        "make": "toyota", "model": "bz",
        "years": (2026, 2026),
        "generation": "first gen, renamed and updated from the bZ4X",
        "engine": "Battery electric, single-motor FWD or dual-motor "
                  "AWD; NACS charge port",
        "reliability": 6.9,
        "maintenance": 7.2,
        "annual_maintenance_usd": 300,
        "insurance_factor": 1.1,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "One recall on the 2026 (26V393000, electric propulsion "
            "system) and 5 complaints so far.",
            "The update brought bigger batteries and faster charging "
            "than the bZ4X, which answers that car's main weakness on "
            "paper. It has not been on sale long enough to confirm.",
            "No oil changes, so routine upkeep is cheap. Battery and "
            "charging faults are the costs to watch; check what the "
            "battery warranty covers.",
        ],
        "note": "Provisional score. A clear improvement on the bZ4X, "
                "with very little time in owners' hands.",
    },
    {
        # 2023: 4 recalls, 7 complaints. 2024: 3 recalls, 25.
        "make": "toyota", "model": "bz4x",
        "years": (2023, 2025),
        "generation": "first gen",
        "engine": "Battery electric, single-motor FWD or dual-motor "
                  "AWD",
        "reliability": 6.5,
        "maintenance": 7.0,
        "annual_maintenance_usd": 300,
        "insurance_factor": 1.1,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "Launched with recall 22V444000: wheel hub bolts could "
            "loosen and a wheel could come off. Confirm it is done on "
            "any 2023.",
            "Recall 25V577000 (2023-2025): the defroster can fail to "
            "clear the windshield. Also confirm.",
            "DC fast charging is slow, worst on AWD cars and in cold "
            "weather, and winter range drops sharply. Fine if you "
            "charge at home, tiring on road trips.",
            "No oil changes, so routine upkeep is cheap. Electrical is "
            "the top complaint on the 2024 (11 of 25).",
        ],
        "note": "Toyota's first mass-market EV and not a strong one. "
                "Priced low used for a reason; it suits home charging "
                "and short trips.",
    },
    # ---- GR86 / 86 ---------------------------------------------------
    {
        # 2022: 1 recall, 21 complaints (engine 13). 2023: 1 recall,
        # 19 complaints (engine 11).
        "make": "toyota", "model": "gr86",
        "years": (2022, 2026),
        "generation": "ZN8 second gen, built by Subaru",
        "engine": "2.4L Subaru FA24 flat four, 6-speed manual or "
                  "automatic; rear-wheel drive",
        "reliability": 7.0,
        "maintenance": 7.6,
        "annual_maintenance_usd": 520,
        "insurance_factor": 1.2,
        "tire_set_usd": 800,
        "risk": "Engine is more than half of all complaints on the "
                "2022 (13 of 21) and 2023 (11 of 19), matching owner "
                "reports of oil starvation failures in hard driving",
        "known_issues": [
            "Engine dominates a small complaint file in both years "
            "checked. Reports describe oil pressure loss in long "
            "right-hand corners and stray sealant in the oil pickup.",
            "Ask directly whether the car has been tracked or "
            "autocrossed. Many have, and warranty claims after track "
            "use have been disputed.",
            "It is a Subaru underneath, so service it at a shop that "
            "knows flat fours. Insurance is priced as a sports car.",
        ],
        "note": "A brilliant cheap sports car with a real engine "
                "question for hard use. Driven on the street it is "
                "much less of a worry.",
    },
    {
        # 2017: 2 recalls, 2 complaints.
        "make": "toyota", "model": "86",
        "years": (2017, 2020),
        "generation": "ZN6 first gen (formerly the Scion FR-S)",
        "engine": "2.0L Subaru FA20 flat four, 6-speed manual or "
                  "automatic; rear-wheel drive",
        "reliability": 7.6,
        "maintenance": 7.8,
        "annual_maintenance_usd": 500,
        "insurance_factor": 1.18,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "Two recalls and two complaints on the 2017. The file is "
            "too small to read, so this score is provisional.",
            "Most have been driven hard and many are modified. A "
            "stock car with records is worth paying extra for.",
            "A Subaru engine: check for oil leaks at the timing cover "
            "and cam carriers.",
        ],
        "note": "Provisional score. Simple and fun; the individual "
                "car's history matters far more than the model's.",
    },
    # ---- Land Cruiser ------------------------------------------------
    {
        # 2024: 1 recall (a label), complaints endpoint empty.
        # 2025: 0 recalls, 33 complaints (service brakes 11).
        "make": "toyota", "model": "land cruiser",
        "years": (2024, 2026),
        "generation": "J250",
        "engine": "2.4L turbo I4 hybrid (i-Force Max) with 8-speed "
                  "automatic; full-time 4WD",
        "reliability": 7.3,
        "maintenance": 7.4,
        "annual_maintenance_usd": 560,
        "insurance_factor": 1.08,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "No recalls on the 2025 and 33 complaints, a third of them "
            "service brakes (11). Check pedal feel in slow traffic.",
            "Same engine, hybrid system and 8-speed as the Tacoma and "
            "4Runner hybrids, which are having a rough start.",
            "Smaller and far cheaper than the old Land Cruiser, and "
            "not built to the same standard. Do not pay for the "
            "badge's past.",
        ],
        "note": "A capable mid-size 4x4 with a short, so far "
                "unremarkable record. Not the 200 Series, in either "
                "direction.",
    },
    {
        # 2016: 3 recalls, 4 complaints. 2019: 3 recalls, complaints
        # endpoint empty. 2020: nothing returned.
        "make": "toyota", "model": "land cruiser",
        "years": (2015, 2021),
        "generation": "J200 (200 Series)",
        "engine": "5.7L 3UR-FE V8 with 8-speed automatic (6-speed on "
                  "the 2015); full-time 4WD",
        "reliability": 9.0,
        "maintenance": 7.6,
        "annual_maintenance_usd": 650,
        "insurance_factor": 1.1,
        "tire_set_usd": 1100,
        "risk": None,
        "known_issues": [
            "Four complaints on the 2016 and three recalls, two of "
            "them the Takata passenger airbag inflator (17V548000, "
            "18V887000). Confirm those are done.",
            "Sold in small numbers, so the NHTSA file is thin and "
            "returned nothing at all for the 2020.",
            "The KDSS suspension can leak at its hydraulic cylinders, "
            "and the V8 can seep at the cam towers. Both are costly "
            "to put right.",
            "About 14 mpg, and parts are priced like a Lexus.",
        ],
        "note": "Engineered to outlast everything else on this list, "
                "and it costs accordingly to buy, fuel and repair.",
    },
]
