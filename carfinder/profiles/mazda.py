"""Reliability profiles: Mazda. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

Two Mazda families behave differently in the NHTSA data: the
naturally aspirated 2.5L cars are quiet, while the 2.5L turbo
(cracked cylinder heads) and the new inline-six CX-70 and CX-90
(recalls) are not. The engine a car has matters more than the badge."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "mazda", "model": "mazda3",
        "years": (2019, 2026),
        "generation": "BP fourth gen",
        "engine": "2.5L Skyactiv-G I4",
        "reliability": 8.4,
        "maintenance": 8.0,
        "annual_maintenance_usd": 430,
        "insurance_factor": 1.05,
        "tire_set_usd": 800,
        "risk": None,
        "known_issues": [
            "AWD only on the 2.5L, and not on every trim; verify per VIN.",
            "18-inch tires cost more to replace than the Camry's.",
            "Rear visibility and back-seat room are genuinely tight.",
        ],
        "note": "Driver's pick. AWD offered 2019+. Reliable and well-built; "
                "parts a touch pricier than Toyota but not painful.",
    },
    {
        # 2016: 6 recalls, 103 complaints. 2018: 4 recalls, 110.
        # 2015: 4 recalls, 129 complaints.
        "make": "mazda", "model": "mazda3",
        "years": (2014, 2018),
        "generation": "BM/BN third gen",
        "engine": "2.0L or 2.5L Skyactiv-G I4, 6-speed automatic or "
                  "manual",
        "reliability": 8.2,
        "maintenance": 8.2,
        "annual_maintenance_usd": 440,
        "insurance_factor": 1.03,
        "tire_set_usd": 650,
        "risk": None,
        "known_issues": [
            "Four to six recalls on each year pulled (2015, 2016, "
            "2018). None is a drivetrain defect, but run the VIN.",
            "Complaints sit around 100 to 130 a year with electrical "
            "leading (30 of 110 on the 2018): the touchscreen can "
            "register touches by itself. Ask if it was replaced.",
            "Front-wheel drive only in this generation.",
            "Thin paint and a low nose: look for chips and for rust "
            "starting at the rear arches on salted-road cars.",
        ],
        "note": "A simple engine and a conventional automatic. One "
                "of the safest cheap used cars to buy.",
    },
    {
        # 0 recalls on both years pulled, and the lowest complaint
        # totals of any compact SUV profiled here (41 for 2024, 25 for
        # 2025) with no single component dominating.
        "make": "mazda", "model": "cx-5",
        "years": (2022, 2026),
        "generation": "KF second gen, facelifted",
        "engine": "2.5L Skyactiv-G I4, conventional 6-speed automatic: "
                  "no CVT, no turbo triple",
        "reliability": 8.6,
        "maintenance": 8.0,
        "annual_maintenance_usd": 460,
        "insurance_factor": 1.0,
        "tire_set_usd": 760,
        "risk": None,
        "known_issues": [
            "No open recalls on 2024 or 2025.",
            "Brake complaints are the largest single cluster (8 of 41 "
            "for 2024, 9 of 25 for 2025), mostly noise and early pad "
            "wear rather than failure.",
            "Infotainment is a rotary-dial system with no touchscreen "
            "while moving. Some people hate it, so try it before "
            "buying.",
            "Cargo space trails a RAV4 or CR-V; it is the sportier "
            "drive and the plainer load-hauler.",
        ],
        "note": "The conservative engineering choice among small SUVs: a "
                "naturally aspirated four and a torque-converter "
                "automatic, both long-proven. AWD is available.",
    },
    {
        # 2019: 2 recalls, 274 complaints, 133 ENGINE. 2021: 150
        # complaints, 81 ENGINE; the recall endpoint returned
        # nothing. 2017: 1 recall, 150 complaints.
        "make": "mazda", "model": "cx-5",
        "years": (2017, 2021),
        "generation": "KF second gen",
        "engine": "2.5L Skyactiv-G I4 (2.5L turbo optional from "
                  "2019), 6-speed automatic",
        "reliability": 7.7,
        "maintenance": 7.8,
        "annual_maintenance_usd": 480,
        "insurance_factor": 1.0,
        "tire_set_usd": 740,
        "risk": "Cracked cylinder head leaking oil or coolant: 133 "
                "of 274 complaints on the 2019 and 81 of 150 on the "
                "2021 are ENGINE, and the repair is a new head",
        "known_issues": [
            "ENGINE is about half the file on both the 2019 and the "
            "2021. Most of the 2019 engine complaints mention the "
            "cylinder head or an oil leak.",
            "Look at the back of the engine for fresh oil, check the "
            "coolant level cold, and sniff for burning oil after "
            "the drive.",
            "The 2017 has no such cluster (16 ENGINE of 150).",
            "Ask the dealer whether any cylinder head work or "
            "extended coverage applies to the VIN.",
        ],
        "note": "Still a good car, but not the clean record its "
                "reputation suggests. Inspect the engine before "
                "buying a 2018 to 2021.",
    },
    {
        # 2016: 5 recalls, 512 complaints, 161 EXTERIOR LIGHTING.
        # 2015: 4 recalls, 133 complaints.
        "make": "mazda", "model": "cx-5",
        "years": (2013, 2016),
        "generation": "KE first gen",
        "engine": "2.0L or 2.5L Skyactiv-G I4, 6-speed automatic "
                  "(manual on base 2.0L)",
        "reliability": 7.9,
        "maintenance": 8.0,
        "annual_maintenance_usd": 480,
        "insurance_factor": 0.98,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "161 of 512 complaints on the 2016 are EXTERIOR "
            "LIGHTING: the LED daytime running lights fail. Check "
            "both light up.",
            "Five recalls on the 2016, four on the 2015. Run the "
            "VIN, including the liftgate strut and fuel filler "
            "campaigns if listed.",
            "The 2.0L in 2013 cars is slow. The 2.5L from 2014 is "
            "the one to look for.",
        ],
        "note": "Simple and durable underneath. The faults in the "
                "file are lights and recalls, not engines.",
    },
    {
        # 29 complaints for 2024, two software-fix recalls. Same
        # Skyactiv mechanicals as the CX-5 in a subcompact body: the
        # closest true size match to the Envista that is also a
        # genuinely proven design.
        "make": "mazda", "model": "cx-30",
        "years": (2020, 2026),
        "generation": "DM first gen",
        "engine": "2.5L Skyactiv-G I4, 6-speed automatic; AWD standard "
                  "on most trims from 2021",
        "reliability": 8.4,
        "maintenance": 7.8,
        "annual_maintenance_usd": 470,
        "insurance_factor": 1.0,
        "tire_set_usd": 720,
        "risk": None,
        "known_issues": [
            "29 complaints for 2024 with no dominant component: the "
            "flattest, least worrying distribution of the small SUVs "
            "profiled here.",
            "Two recalls, both software: 24V649000 (lane-departure "
            "camera) and 25V357000 (airbag control module). Confirm "
            "both were flashed; neither is a hardware job.",
            "Back seat and cargo hold are genuinely small, even for a "
            "subcompact SUV.",
            "Firm ride. That is the trade for the handling.",
        ],
        "note": "Standard AWD and a naturally aspirated four in a subcompact "
                "body. Better engineering than most rivals, worse back seat.",
    },
    {
        # 2023: 2 recalls, 65 complaints. 2024: 1 recall, 37.
        # 2025: 4 recalls, 50 complaints.
        "make": "mazda", "model": "cx-50",
        "years": (2023, 2026),
        "generation": "first gen",
        "engine": "2.5L Skyactiv-G I4 or 2.5L turbo, 6-speed "
                  "automatic; AWD standard. Hybrid from 2025 uses a "
                  "Toyota system",
        "reliability": 7.9,
        "maintenance": 7.6,
        "annual_maintenance_usd": 490,
        "insurance_factor": 1.02,
        "tire_set_usd": 820,
        "risk": None,
        "known_issues": [
            "Complaints are modest and spread out: 65 on the 2023, "
            "led by brakes (16) and collision avoidance (14).",
            "Four recalls on the 2025 against one on the 2024. "
            "Check a 2025 by VIN.",
            "The 2.5L turbo is the engine behind the cracked "
            "cylinder head complaints on older Mazdas. The "
            "non-turbo is the lower-risk choice.",
            "Firm ride and a wide body. Try it in a tight parking lot.",
        ],
        "note": "CX-5 mechanicals in a wider, more rugged body. "
                "Pick the non-turbo or the hybrid for the long run.",
    },
    {
        # 2018: 2 recalls, 128 complaints, 76 ENGINE. 2016: 99
        # complaints, 61 ENGINE; the recall endpoint returned
        # nothing. 2021: 1 recall, 41 complaints, 21 ENGINE.
        "make": "mazda", "model": "cx-9",
        "years": (2016, 2023),
        "generation": "TC second gen",
        "engine": "2.5L Skyactiv-G turbo I4, 6-speed automatic",
        "reliability": 6.8,
        "maintenance": 7.0,
        "annual_maintenance_usd": 580,
        "insurance_factor": 1.03,
        "tire_set_usd": 950,
        "risk": "Cracked cylinder head with coolant loss on the 2.5L "
                "turbo: ENGINE is 76 of 128 complaints on the 2018 "
                "and 61 of 99 on the 2016, and the fix is a new "
                "head",
        "known_issues": [
            "ENGINE is roughly 60% of the file on the 2016 and 2018 "
            "and half on the 2021. Most 2018 engine complaints "
            "describe coolant loss.",
            "Check the coolant level cold, look for dried coolant "
            "at the back of the engine near the exhaust, and ask "
            "for any head replacement invoice.",
            "Ask the dealer whether extended cylinder head coverage "
            "applies to the VIN, and until when.",
            "The third row is small for the size of the car.",
        ],
        "note": "Lovely to drive and let down by one expensive "
                "fault. Buy with proof of a replaced head or a "
                "clean inspection, and price in the risk.",
    },
    {
        # 2015: 2 recalls, 35 complaints, 17 ENGINE.
        "make": "mazda", "model": "cx-9",
        "years": (2010, 2015),
        "generation": "TB first gen",
        "engine": "3.7L V6 (Ford-derived), 6-speed automatic",
        "reliability": 6.4,
        "maintenance": 6.5,
        "annual_maintenance_usd": 680,
        "insurance_factor": 1.0,
        "tire_set_usd": 900,
        "risk": "Internal water pump failure on the 3.7L V6 can put "
                "coolant into the oil and destroy the engine",
        "known_issues": [
            "17 of 35 complaints on the 2015 are ENGINE. The water "
            "pump is driven by the timing chain; when it leaks, "
            "coolant reaches the oil.",
            "Ask if the water pump has been replaced. It is a big "
            "labor job done as prevention around 100k miles.",
            "On AWD cars, check the transfer case for leaks and a "
            "burning smell after a drive.",
        ],
        "note": "A Ford-era Mazda and not built like the later "
                "ones. Only with water pump paperwork.",
    },
    {
        # 2024: 11 recalls; 381 complaints filed under CX-90-MHEV,
        # 201 of them STEERING. 2025: 2 recalls, 38 complaints.
        "make": "mazda", "model": "cx-90",
        "years": (2024, 2026),
        "generation": "first gen",
        "engine": "3.3L turbo inline-six mild hybrid, or 2.5L "
                  "plug-in hybrid; 8-speed automatic, AWD",
        "reliability": 5.8,
        "maintenance": 6.0,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.1,
        "tire_set_usd": 1100,
        "risk": "Eleven recalls on the 2024, its first year, and "
                "201 STEERING complaints on the 2024 mild hybrid "
                "alone",
        "known_issues": [
            "Eleven recalls on the 2024. Recalls are counted per "
            "defect, so that is a genuinely bad launch.",
            "201 of 381 complaints filed under the 2024 mild hybrid "
            "are STEERING. Feel for heavy or sticky steering at "
            "parking speeds.",
            "The 2025 is far calmer so far: 2 recalls and 38 "
            "complaints.",
            "New engine, new gearbox, new platform, all at once. "
            "Get a printout showing every recall closed.",
        ],
        "note": "Ambitious and good to drive, with a rough first "
                "year. A 2025 or later is a different proposition "
                "from a 2024.",
    },
    {
        # 2025: 4 recalls, 53 complaints, 20 LANE DEPARTURE.
        "make": "mazda", "model": "cx-70",
        "years": (2025, 2026),
        "generation": "first gen (two-row CX-90)",
        "engine": "3.3L turbo inline-six mild hybrid, or 2.5L "
                  "plug-in hybrid; 8-speed automatic, AWD",
        "reliability": 6.4,
        "maintenance": 6.0,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.1,
        "tire_set_usd": 1100,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2025.",
            "20 of 53 complaints on the 2025 are LANE DEPARTURE: "
            "blind-spot and lane warnings going off with nothing "
            "there. Drive it on a highway before buying.",
            "Mechanically a CX-90 without the third row, launched a "
            "year later, so it missed the worst of that car's "
            "first-year recalls.",
        ],
        "note": "The CX-90's hardware after a year of fixes. "
                "Provisional: one model year of data.",
    },
    {
        # 2016: 3 recalls, 48 complaints. 2018: 1 recall, 10.
        # 2020: 1 recall, 1 complaint.
        "make": "mazda", "model": "cx-3",
        "years": (2016, 2021),
        "generation": "DK first gen",
        "engine": "2.0L Skyactiv-G I4, 6-speed automatic",
        "reliability": 8.3,
        "maintenance": 8.0,
        "annual_maintenance_usd": 440,
        "insurance_factor": 0.98,
        "tire_set_usd": 680,
        "risk": None,
        "known_issues": [
            "A small, quiet file: 48 complaints on the 2016, 10 on "
            "the 2018, one on the 2020.",
            "Three recalls on the 2016, one on later years.",
            "Very tight back seat and trunk. Sit in the back before "
            "you fall for it.",
        ],
        "note": "A Mazda2 on stilts with a proven engine. Cheap to "
                "run, if it is big enough for you.",
    },
    {
        # 2018: 2 recalls, 60 complaints, 34 ENGINE. 2020: 2
        # complaints; the recall endpoint returned nothing.
        "make": "mazda", "model": "mazda6",
        "years": (2018, 2021),
        "generation": "GL third gen, facelifted",
        "engine": "2.5L Skyactiv-G I4 or 2.5L turbo, 6-speed "
                  "automatic",
        "reliability": 7.8,
        "maintenance": 7.8,
        "annual_maintenance_usd": 470,
        "insurance_factor": 1.03,
        "tire_set_usd": 820,
        "risk": None,
        "known_issues": [
            "34 of 60 complaints on the 2018 are ENGINE, and half "
            "of those mention the cylinder head. Check the back of "
            "the engine for oil and the coolant level cold.",
            "Two recalls on the 2018.",
            "The base non-turbo car has less to go wrong than the "
            "turbo trims.",
        ],
        "note": "A handsome, roomy sedan. Mostly sound, with the "
                "same cylinder head question as other 2018 to 2021 "
                "Mazdas.",
    },
    {
        # 2015: 3 recalls, 60 complaints. 2016: 1 recall, 78.
        "make": "mazda", "model": "mazda6",
        "years": (2014, 2017),
        "generation": "GJ third gen",
        "engine": "2.5L Skyactiv-G I4, 6-speed automatic or manual",
        "reliability": 8.3,
        "maintenance": 8.0,
        "annual_maintenance_usd": 460,
        "insurance_factor": 1.03,
        "tire_set_usd": 780,
        "risk": None,
        "known_issues": [
            "60 complaints on the 2015 and 78 on the 2016, spread "
            "across brakes, electrical and power train with nothing "
            "dominant.",
            "Three recalls on the 2015, one on the 2016.",
            "Road noise is high and the infotainment is slow. "
            "Neither costs money to live with.",
        ],
        "note": "One engine, one conventional automatic, no known "
                "expensive fault. A strong used sedan.",
    },
    {
        # NHTSA files this car as MX-5. 2016: 3 recalls, 34
        # complaints, 11 POWER TRAIN. 2019: 2 recalls, 11
        # complaints. 2022: 1 recall, 5 complaints.
        "make": "mazda", "model": "mx-5 miata",
        "years": (2016, 2026),
        "generation": "ND fourth gen",
        "engine": "2.0L Skyactiv-G I4, 6-speed manual or automatic",
        "reliability": 8.6,
        "maintenance": 8.0,
        "annual_maintenance_usd": 450,
        "insurance_factor": 1.12,
        "tire_set_usd": 700,
        "risk": None,
        "known_issues": [
            "11 of 34 complaints on the 2016 are POWER TRAIN: early "
            "manual gearboxes failed on hard-driven cars. On a 2016 "
            "to 2018 manual, feel for notchy second and third.",
            "Tiny files after that: 11 complaints on the 2019, 5 on "
            "the 2022.",
            "Check the soft top for wear at the folds and the "
            "drains behind the seats for blockage.",
            "Look for track use: tires, brake wear, roll bar holes.",
        ],
        "note": "Light, simple and cheap to keep. 2019 and later "
                "cars have the stronger engine and gearbox.",
    },
    {
        # 2015: 1 complaint; the recall endpoint returned nothing.
        "make": "mazda", "model": "mx-5 miata",
        "years": (2009, 2015),
        "generation": "NC third gen",
        "engine": "2.0L MZR I4, 5 or 6-speed manual or 6-speed "
                  "automatic",
        "reliability": 8.4,
        "maintenance": 8.2,
        "annual_maintenance_usd": 460,
        "insurance_factor": 1.08,
        "tire_set_usd": 650,
        "risk": None,
        "known_issues": [
            "The plastic coolant expansion tank goes brittle and "
            "splits with age. Replace it if it has yellowed.",
            "NHTSA returned one complaint and no recalls for the "
            "2015. Low sales, so that is not evidence either way.",
            "Rust in the rear sills and arches on salted-road cars. "
            "Look underneath.",
        ],
        "note": "An old, well-understood sports car. Provisional: "
                "scored on reputation, not on the thin NHTSA file.",
    },
]
