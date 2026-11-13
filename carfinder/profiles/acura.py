"""Reliability profiles: Acura. The format and the caveats on reading
these numbers are in carfinder/reliability.py."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        # 163 complaints on the 2022 with POWER TRAIN at 75; 42 on
        # the 2024; 118 on the 2025. Three recalls on each.
        "make": "acura", "model": "mdx",
        "years": (2022, 2026),
        "generation": "fourth gen",
        "engine": "3.5L J35Y5 V6, 10-speed automatic; Type S uses a "
                  "3.0L turbo V6",
        "reliability": 7.0,
        "maintenance": 6.6,
        "annual_maintenance_usd": 690,
        "insurance_factor": 1.12,
        "tire_set_usd": 1050,
        "risk": None,
        "known_issues": [
            "Recall count is low: 3 on each of the 2022, 2024 and "
            "2025. 26V721000 (loss of power steering assist, "
            "2022-2024) and 25V391000 (brake pedal, 2023-2025) are "
            "the ones to confirm.",
            "Power train is 75 of 163 complaints on the 2022, the "
            "first year. Drive it cold and feel for harsh or delayed "
            "shifts.",
            "The 2025 has 118 complaints against 42 on the 2024, "
            "mostly tagged engine and electrical. Look for warning "
            "lights and stored codes on a 2025.",
            "The Type S turbo V6 is also under recall 25V031000 for "
            "an engine stall from fuel injection software.",
        ],
        "note": "A clear step up from the generation before it. "
                "Later years are better than the 2022. There was no "
                "2021 MDX.",
    },
    {
        # 378 complaints on the 2016: ENGINE 163, POWER TRAIN 113.
        # Seven recalls on the 2016, nine on the 2019.
        "make": "acura", "model": "mdx",
        "years": (2014, 2020),
        "generation": "third gen",
        "engine": "3.5L J35Y5 direct-injected V6; 6-speed automatic "
                  "on 2014-2015, ZF 9-speed from 2016",
        "reliability": 6.3,
        "maintenance": 6.6,
        "annual_maintenance_usd": 720,
        "insurance_factor": 1.08,
        "tire_set_usd": 980,
        "risk": "Recall 23V751000 covers connecting rod bearings that "
                "can seize the engine on 2016-2020 cars, and the ZF "
                "9-speed automatic fitted from 2016 has a long record "
                "of rough shifting",
        "known_issues": [
            "Engine (163) and power train (113) make up most of the "
            "378 complaints on the 2016, the year the 9-speed "
            "arrived. Drive it from cold and in traffic.",
            "Seven recalls on the 2016 and nine on the 2019. Two "
            "cover water getting into the tail lights (19V256000, "
            "25V259000).",
            "Recall 26V365000 covers rear subframe corrosion on "
            "2014-2020 cars sold in salt-belt states. Inspect it on "
            "a lift.",
            "Timing belt and water pump are due around 100,000 "
            "miles. Ask for the receipt.",
        ],
        "note": "Comfortable and well equipped, but the engine "
                "recall and the 9-speed make it a buy-on-records car. "
                "The 2014-2015 6-speed cars avoid the gearbox issue.",
    },
    {
        # 441 complaints on the 2019 (first year) against 118 on the
        # 2021, 12 on the 2024 and 31 on the 2025.
        "make": "acura", "model": "rdx",
        "years": (2019, 2026),
        "generation": "third gen",
        "engine": "2.0L K20C4 turbo I4, 10-speed automatic; AWD "
                  "available",
        "reliability": 7.0,
        "maintenance": 6.8,
        "annual_maintenance_usd": 640,
        "insurance_factor": 1.1,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "The 2019 is the year to avoid or check hard: 441 "
            "complaints, with visibility and wipers (97) and engine "
            "(91) the named clusters. Sudden loss of power under "
            "acceleration is the engine story.",
            "Recall count is low throughout: 5 on the 2019, 3 on the "
            "2021, 2 on the 2024, 1 on the 2025.",
            "Recall 25V582000 on the 2025 covers the electric power "
            "steering, and most of that year's 31 complaints "
            "mention steering. Confirm it is closed.",
            "Recall 24V114000 covers a steering gearbox that can "
            "let water in on the 2024.",
        ],
        "note": "A good compact luxury SUV once past its first "
                "year. Buy 2020 or later.",
    },
    {
        # 41 complaints and 2 recalls on the 2016; 78 and 1 on the
        # 2018. A very small file.
        "make": "acura", "model": "rdx",
        "years": (2013, 2018),
        "generation": "second gen",
        "engine": "3.5L J35 V6, 6-speed automatic; AWD available",
        "reliability": 8.3,
        "maintenance": 7.2,
        "annual_maintenance_usd": 610,
        "insurance_factor": 1.03,
        "tire_set_usd": 860,
        "risk": None,
        "known_issues": [
            "Very few complaints: 41 on the 2016 and 78 on the 2018, "
            "with no component standing out on the 2016.",
            "Both recalls on the 2016 are driver air bag inflator "
            "campaigns (16V061000, 19V182000). Do not buy one with "
            "an open inflator recall.",
            "The one recall on the 2018 is fuel pump campaign "
            "23V858000, and fuel system is that year's top "
            "complaint. Confirm the pump was replaced.",
            "Timing belt and water pump are due around 100,000 "
            "miles, and the V6 has cylinder deactivation, so check "
            "the oil level.",
        ],
        "note": "The quiet, dependable Acura of its decade. An old "
                "design even when new, which is why it holds up.",
    },
    {
        # 210 complaints on the 2023 with STEERING at 191; 64 on the
        # 2024 with STEERING at 52.
        "make": "acura", "model": "integra",
        "years": (2023, 2026),
        "generation": "fifth gen, Civic-based",
        "engine": "1.5L L15 turbo I4, CVT or 6-speed manual; Type S "
                  "uses a 2.0L turbo with manual only",
        "reliability": 7.0,
        "maintenance": 7.8,
        "annual_maintenance_usd": 500,
        "insurance_factor": 1.12,
        "tire_set_usd": 780,
        "risk": "Recall 24V744000 covers the electric power steering "
                "on 2023-2025 cars; steering is 191 of 210 complaints "
                "on the 2023, so verify the recall is closed",
        "known_issues": [
            "Steering is nearly the whole complaint file: 191 of 210 "
            "on the 2023 and 52 of 64 on the 2024. The wheel sticks "
            "just off center at highway speed. Drive it on a "
            "straight fast road.",
            "Recall count is low: 2 on the 2023, 3 on the 2024, 1 on "
            "the 2025. Apart from the steering: an ABS control unit "
            "(23V430000) and seat fasteners (24V859000, 26V054000).",
            "Take the steering away and almost nothing is left in "
            "the file, which says the rest of the car is sound.",
        ],
        "note": "A nicer Civic with the Civic's steering fault. "
                "Fine once the recall work is confirmed on that VIN.",
    },
    {
        # 75 complaints and 5 recalls on the 2021; 12 and 4 on the
        # 2023.
        "make": "acura", "model": "tlx",
        "years": (2021, 2025),
        "generation": "second gen",
        "engine": "2.0L turbo I4, 10-speed automatic; Type S "
                  "uses a 3.0L turbo V6",
        "reliability": 7.3,
        "maintenance": 6.6,
        "annual_maintenance_usd": 660,
        "insurance_factor": 1.15,
        "tire_set_usd": 980,
        "risk": None,
        "known_issues": [
            "Few complaints: 75 on the 2021, with power train on top "
            "at 30, and 12 on the 2023.",
            "Five recalls on the 2021 and four on the 2023. Confirm "
            "26V721000 (loss of power steering assist), 25V391000 "
            "(brake pedal) and 24V950000 (fuel filler neck, "
            "2021-2023).",
            "The Type S is also under recall 25V031000 for an "
            "engine stall from fuel injection software.",
            "Heavy for its size and firm riding on the larger "
            "wheels, which are also costly to re-tire.",
        ],
        "note": "A sound car with a short complaint file. Dropped "
                "after 2025, so it tends to be priced below its "
                "rivals.",
    },
    {
        # 344 complaints on the 2015 (first year) with POWER TRAIN at
        # 161; 98 on the 2018.
        "make": "acura", "model": "tlx",
        "years": (2015, 2020),
        "generation": "first gen",
        "engine": "2.4L K24W I4 with 8-speed dual-clutch, or 3.5L V6 "
                  "with ZF 9-speed automatic",
        "reliability": 6.5,
        "maintenance": 6.8,
        "annual_maintenance_usd": 650,
        "insurance_factor": 1.08,
        "tire_set_usd": 820,
        "risk": "Recall 23V751000 covers connecting rod bearings that "
                "can seize the V6 on 2015-2020 cars, and power train "
                "is 161 of 344 complaints on the 2015",
        "known_issues": [
            "Transmission trouble is concentrated in the 2015: two "
            "recalls (14V779000, park may not engage on the V6; "
            "16V640000, may shift to neutral) plus 161 power train "
            "complaints.",
            "Six recalls on the 2015 and four on the 2018. Complaints "
            "fall from 344 to 98 over the same span.",
            "The four-cylinder with the 8-speed dual-clutch avoids "
            "both the V6 engine recall and the 9-speed automatic. It "
            "is the version to look for.",
            "On a V6, the timing belt is due around 100,000 miles.",
        ],
        "note": "Avoid the 2015. A 2018-2020 four-cylinder is a "
                "reasonable, inexpensive used luxury sedan.",
    },
    {
        # 52 complaints and 6 recalls on the 2016; 36 and 5 on the
        # 2019; 11 complaints and no recalls returned for the 2021.
        "make": "acura", "model": "ilx",
        "years": (2016, 2022),
        "generation": "first gen, facelifted",
        "engine": "2.4L I4, 8-speed dual-clutch automatic",
        "reliability": 7.8,
        "maintenance": 7.5,
        "annual_maintenance_usd": 520,
        "insurance_factor": 1.08,
        "tire_set_usd": 680,
        "risk": None,
        "known_issues": [
            "A small complaint file: 52 on the 2016, 36 on the 2019, "
            "11 on the 2021. Service brakes lead on the 2016 (17) "
            "and the 2019 (13).",
            "Recall 25V859000 covers a brake master cylinder seal on "
            "2016-2020 cars, which matches those brake complaints. "
            "Confirm it is closed and check pedal feel.",
            "Six recalls on the 2016, among them 19V424000 "
            "(driveshaft) and 19V052000 (deformed fuel tank). The "
            "recalls endpoint returned none for the 2021 or 2022.",
            "The dual-clutch gearbox needs its fluid changed on "
            "schedule. Feel for judder pulling away from a stop.",
        ],
        "note": "An older Civic in a suit, with a non-turbo engine "
                "that gives little trouble. Dated inside, cheap to "
                "own.",
    },
    {
        # Only the 2015 was pulled: 19 complaints, 4 recalls.
        "make": "acura", "model": "ilx",
        "years": (2013, 2015),
        "generation": "first gen",
        "engine": "2.0L I4 with 5-speed automatic, or 2.4L with "
                  "6-speed manual",
        "reliability": 7.9,
        "maintenance": 7.8,
        "annual_maintenance_usd": 500,
        "insurance_factor": 1.03,
        "tire_set_usd": 640,
        "risk": None,
        "known_issues": [
            "Only 19 complaints on the 2015, and 12 of them are air "
            "bags.",
            "Two of the four recalls on the 2015 are driver air bag "
            "inflator campaigns (16V061000, 19V182000). Do not buy "
            "one with an open inflator recall.",
            "Recall 20V770000 covers driveshaft corrosion on "
            "2013-2015 cars, and 19V052000 a deformed fuel tank.",
            "The 2.0L is slow but simple. At this age, condition "
            "and rust matter more than the model year.",
        ],
        "note": "Plain and durable. Worth buying only with the air "
                "bag recalls confirmed closed.",
    },
    {
        # 64 complaints and 5 recalls on the 2024. Both endpoints
        # returned nothing for the 2025.
        "make": "acura", "model": "zdx",
        "years": (2024, 2025),
        "generation": "second use of the name, built by GM on the "
                      "Ultium platform",
        "engine": "Battery electric, 102 kWh; single motor RWD or "
                  "dual motor AWD",
        "reliability": 5.8,
        "maintenance": 5.8,
        "annual_maintenance_usd": 360,
        "insurance_factor": 1.22,
        "tire_set_usd": 1300,
        "risk": "Five recalls on the 2024, its first year, including "
                "24V614000 (anti-lock brake control unit), 25V018000 "
                "(propulsion system cable) and 25V234000 (front "
                "stabilizer bar)",
        "known_issues": [
            "Five separate campaigns on one model year of a "
            "low-volume car is a poor start. Two more cover the "
            "rearview camera (26V112000, 26V306000).",
            "64 complaints on the 2024, led by forward collision "
            "avoidance (26) and service brakes (22). Test the "
            "automatic braking and watch for sudden unprompted "
            "braking.",
            "It is a GM electric car under the skin and was sold "
            "for only two model years. Ask the dealer about battery "
            "warranty dates, software updates and parts supply "
            "before buying.",
            "Routine costs are low (no oil, light brake wear), but "
            "it is very heavy and the tires are large and "
            "expensive.",
        ],
        "note": "Provisional: one year of data and none for the "
                "2025. Buy only at a steep discount and with every "
                "recall closed.",
    },
]
