"""Reliability profiles: Kia. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

Two brand-wide patterns shape the older cars here. The 2011-2021 Theta
II, Nu and Gamma four-cylinders have a long record of bearing failures
and engine fires, and most 2015-2021 cars that start with a turn key
have no engine immobilizer and are stolen far more often than average.
Both are marked on the generations they apply to and nowhere else."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    # ---- K5 / Optima -----------------------------------------------
    {
        # Written 2026-08-14 from a `run.py research` pull: VIN decode
        # (engine + plant), NHTSA recalls and complaints for 2024. The
        # cost figures are estimates in the same spirit as the others.
        # Replace them if you get real quotes.
        "make": "kia", "model": "k5",
        "years": (2021, 2024),
        "generation": "DL3, pre-facelift",
        "engine": "1.6L Gamma II turbo (the AWD engine on these years)",
        "reliability": 7.5,
        "maintenance": 7.8,
        "annual_maintenance_usd": 520,
        "insurance_factor": 1.02,
        "tire_set_usd": 780,
        "risk": "Recall 25V794000 (fuel tank can expand into hot exhaust "
                "and melt) covers 2021-2024. Confirm it was performed",
        "known_issues": [
            "Two open recalls on 2024s: the fuel-tank check valve above, "
            "and rear window trim that can detach (25V493000). Both are "
            "free dealer fixes, so get proof they were done.",
            "Engine is the largest NHTSA complaint cluster for 2024 "
            "(8 of 28 filings), followed by body/structure.",
            "Kia's 10yr/100k powertrain warranty is FIRST-OWNER ONLY. As a "
            "second owner you get 5yr/60k unless the car is sold as "
            "certified pre-owned, which restores the original term.",
            "Turbo four, so oil service history matters more than it "
            "would on a naturally-aspirated engine.",
        ],
        "note": "Well-equipped for the money and an 8-speed automatic "
                "rather than a CVT. Newer nameplate than the Japanese "
                "options, so less long-term data. Buy on service records "
                "and CPO status.",
    },
    {
        "make": "kia", "model": "k5",
        "years": (2025, 2026),
        "generation": "DL3, facelift",
        "engine": "2.5L Smartstream naturally aspirated (AWD moved to this "
                  "engine for 2025, so a GT-Line badge means something "
                  "different than it did in 2024)",
        "reliability": 7.2,
        "maintenance": 8.2,
        "annual_maintenance_usd": 470,
        "insurance_factor": 1.02,
        "tire_set_usd": 780,
        "risk": None,
        "known_issues": [
            "Facelift year with limited track record. The reliability "
            "score here is provisional, not observed over time.",
            "49 NHTSA complaints already, more than the 2024 despite less "
            "time on the road, clustered in tires (12) and electrical (11).",
            "No turbo, which is one fewer expensive thing to fail than the "
            "2021-2024 AWD cars.",
            "Same first-owner-only powertrain warranty caveat as above.",
        ],
        "note": "Simpler engine than the 1.6T it replaced and slightly "
                "cheaper to maintain, but a first-year facelift with a thin "
                "reliability record. Test drive both: they don't feel alike.",
    },
    {
        # 2016: 5 recalls, 763 complaints (engine 429, 20 fires).
        # 2019: 1 recall, 214 complaints (engine 93, forward collision
        # avoidance 36).
        "make": "kia", "model": "optima",
        "years": (2016, 2020),
        "generation": "JF fourth gen",
        "engine": "2.4L Theta II GDI I4 or 2.0L Theta II turbo, "
                  "6-speed automatic; 1.6L turbo with a dual-clutch on "
                  "LX 1.6T",
        "reliability": 5.0,
        "maintenance": 7.0,
        "annual_maintenance_usd": 630,
        "insurance_factor": 1.22,
        "tire_set_usd": 720,
        "risk": "Theta II rod-bearing failure: engine is 429 of 763 "
                "complaints on the 2016 with 20 fires reported",
        "known_issues": [
            "Engine is 56% of the 2016 complaint file and still the "
            "largest cluster on the 2019 (93 of 214).",
            "Have a Kia dealer confirm the knock-sensor software "
            "campaign and the extended engine warranty on the VIN.",
            "Recall 18V907000 on the 2016 covers a fuel pipe that can "
            "leak after an engine replacement. Confirm it is closed.",
            "Turn-key cars have no immobilizer. Some insurers "
            "surcharge or refuse them, so quote it first.",
        ],
        "note": "Looks like a bargain against a Camry of the same age "
                "and is not one. Only with a replaced engine on "
                "record.",
    },
    {
        # 2015: 4 recalls, 1011 complaints (engine 624, 74 fires).
        "make": "kia", "model": "optima",
        "years": (2015, 2015),
        "generation": "TF third gen, final year",
        "engine": "2.4L Theta II GDI I4 or 2.0L Theta II turbo, "
                  "6-speed automatic",
        "reliability": 4.3,
        "maintenance": 7.0,
        "annual_maintenance_usd": 660,
        "insurance_factor": 1.25,
        "tire_set_usd": 700,
        "risk": "Engine is 624 of 1011 complaints on the 2015 with 74 "
                "fires reported: Theta II bearing failure",
        "known_issues": [
            "Engine is 62% of the 2015 complaint file, and 74 "
            "complaints mention fire. This is the worst file among "
            "the Kia profiles.",
            "All four recalls on the 2015 are fire-related: "
            "18V907000 (fuel pipe) and ABS module campaigns 20V519000, "
            "21V331000 and 23V652000. Confirm every one.",
            "Turn-key cars have no immobilizer and are theft targets.",
        ],
        "note": "Avoid unless it is nearly free and the engine has "
                "already been replaced under the warranty extension.",
    },
    # ---- Seltos ----------------------------------------------------
    {
        # 42 complaints on the 2024, but note the transmission-pump
        # recall: that one is mechanical, not software.
        "make": "kia", "model": "seltos",
        "years": (2021, 2026),
        "generation": "SP2 first gen / SP3 second gen from 2024",
        "engine": "2.0L Smartstream I4 with CVT, or the 1.6L turbo "
                  "with a dual-clutch; AWD available",
        "reliability": 7.2,
        "maintenance": 7.4,
        "annual_maintenance_usd": 520,
        "insurance_factor": 0.98,
        "tire_set_usd": 690,
        "risk": None,
        "known_issues": [
            "Recall 23V531000 covers the automatic transmission fluid "
            "pump, a mechanical campaign and not a software flash. "
            "Confirm it was performed.",
            "42 complaints on the 2024, electrical the largest cluster "
            "at 16. Unremarkable for the class.",
            "Recall 23V830000 covers airbags.",
            "AWD is available.",
            "The 1.6L turbo's dual-clutch is jerky at low speed. The "
            "naturally aspirated 2.0L with the CVT is the smoother, "
            "duller, more durable choice.",
        ],
        "note": "Roomy for the size and usually cheap.",
    },
    # ---- Sportage --------------------------------------------------
    {
        # 2023: 6 recalls, 196 complaints (electrical 46, engine 40).
        # 2025: 1 recall, 55 complaints.
        "make": "kia", "model": "sportage",
        "years": (2023, 2026),
        "generation": "NQ5 fifth gen",
        "engine": "2.5L Smartstream I4, 8-speed automatic; hybrid and "
                  "plug-in hybrid use a 1.6L turbo",
        "reliability": 6.7,
        "maintenance": 7.2,
        "annual_maintenance_usd": 550,
        "insurance_factor": 1.0,
        "tire_set_usd": 740,
        "risk": None,
        "known_issues": [
            "Six recalls on the first-year 2023, including 23V531000 "
            "(transmission fluid pump) and 23V410000 (brake power "
            "assist). Confirm they are closed.",
            "The 2025 pulled much cleaner: one recall (25V874000, tow "
            "hitch) and 55 complaints.",
            "Forward collision avoidance draws 10 of the 55 complaints "
            "on the 2025. Test the driver aids on a highway.",
            "Used-buyer warranty is 5yr/60k unless certified "
            "pre-owned.",
        ],
        "note": "A clean break from the old Sportage's engines. Skip "
                "the 2023 if a 2024 or newer is within reach.",
    },
    {
        # 2017: 4 recalls, 404 complaints (engine 222, 28 fires).
        # 2020: 2 recalls, 171 complaints (engine 81, 13 fires).
        "make": "kia", "model": "sportage",
        "years": (2017, 2022),
        "generation": "QL fourth gen",
        "engine": "2.4L Theta II GDI I4 or 2.0L Theta II turbo, "
                  "6-speed automatic",
        "reliability": 5.2,
        "maintenance": 7.0,
        "annual_maintenance_usd": 630,
        "insurance_factor": 1.22,
        "tire_set_usd": 720,
        "risk": "Engine is 222 of 404 complaints on the 2017 with 28 "
                "fires, and 81 of 171 on the 2020 with 13 fires",
        "known_issues": [
            "Engine is the largest cluster on both years pulled. Oil "
            "burning comes first, then a knock, then a seized engine.",
            "Recall 21V137000 covers the ABS module, which can short "
            "and start a fire while parked. Confirm it is closed.",
            "Turn-key cars have no immobilizer and are theft targets. "
            "Confirm the anti-theft update and price insurance first.",
            "Ask a Kia dealer whether the extended engine warranty "
            "applies to the VIN.",
        ],
        "note": "The fire count is the part to take seriously. Buy "
                "only with full service records and every recall "
                "closed.",
    },
    {
        # 2015: 2 recalls, 146 complaints (engine 84, 11 fires).
        "make": "kia", "model": "sportage",
        "years": (2015, 2016),
        "generation": "SL third gen",
        "engine": "2.4L Theta II GDI I4 or 2.0L Theta II turbo, "
                  "6-speed automatic",
        "reliability": 5.3,
        "maintenance": 7.0,
        "annual_maintenance_usd": 630,
        "insurance_factor": 1.18,
        "tire_set_usd": 700,
        "risk": "Theta II engines: engine is 84 of 146 complaints on "
                "the 2015 with 11 fires reported",
        "known_issues": [
            "Engine is 58% of the 2015 complaint file. Listen for "
            "knock and check for oil burning.",
            "Recalls 18V907000 (fuel pipe) and 22V051000 (ABS module) "
            "are both fire-related. Confirm each one.",
            "Turn-key cars lack an immobilizer.",
        ],
        "note": "Same engine risk as the later car in an older body. "
                "Hard to recommend at any normal price.",
    },
    # ---- Sorento ---------------------------------------------------
    {
        # 2021: 4 recalls, 27 complaints (power train 23). 2023: 3
        # recalls, 128 complaints. 2025: 3 recalls, 77 complaints.
        "make": "kia", "model": "sorento",
        "years": (2021, 2026),
        "generation": "MQ4 fourth gen",
        "engine": "2.5L Smartstream I4 with an 8-speed automatic; 2.5L "
                  "turbo with an 8-speed wet dual-clutch; hybrid uses "
                  "a 1.6L turbo",
        "reliability": 6.5,
        "maintenance": 7.0,
        "annual_maintenance_usd": 590,
        "insurance_factor": 1.03,
        "tire_set_usd": 820,
        "risk": "Recall 22V760000 on the 2021 covers the 2.5T's "
                "dual-clutch transmission, which can lose drive",
        "known_issues": [
            "Power train is 23 of the 27 complaints on the 2021. The "
            "turbo's dual-clutch is the cause; confirm 22V760000 was "
            "performed.",
            "The non-turbo 2.5L and the hybrid use regular automatics "
            "and avoid that gearbox.",
            "Recall 25V649000 covers wiring and fuses on the 2021 and "
            "2023, and 25V548000 engine critical fasteners on the "
            "2025.",
            "Some turn-key 2021-2022 base trims lack an immobilizer.",
        ],
        "note": "Useful three-row at a two-row price. Pick the engine "
                "with care and it is a decent buy.",
    },
    {
        # 2016: 8 recalls, 1263 complaints (engine 698, 50 fires).
        # 2019: 2 recalls, 437 complaints (engine 161, 19 fires).
        "make": "kia", "model": "sorento",
        "years": (2016, 2020),
        "generation": "UM third gen",
        "engine": "2.4L Theta II GDI I4, 2.0L Theta II turbo "
                  "(2016-2018), or 3.3L Lambda II V6",
        "reliability": 4.9,
        "maintenance": 6.8,
        "annual_maintenance_usd": 660,
        "insurance_factor": 1.2,
        "tire_set_usd": 780,
        "risk": "Engine is 698 of 1263 complaints on the 2016 with 50 "
                "fires reported; the four-cylinders are Theta II "
                "units",
        "known_issues": [
            "Engine is 55% of the 2016 complaint file. The V6 is the "
            "engine to have; the 2.4L and 2.0T are the bearing-"
            "failure ones.",
            "Eight recalls on the 2016, including 18V907000 (fuel "
            "pipe) and 22V703000 (tow hitch wiring, fire).",
            "19 fire complaints on the 2019. Run the VIN and park "
            "outside until open recalls are closed.",
            "Turn-key cars have no immobilizer and are theft targets.",
        ],
        "note": "A V6 with records is tolerable. A four-cylinder "
                "without them is a gamble on a five-figure engine "
                "bill.",
    },
    {
        # 2015: 3 recalls, 755 complaints (engine 363, 14 fires).
        "make": "kia", "model": "sorento",
        "years": (2015, 2015),
        "generation": "XM second gen, final year",
        "engine": "2.4L Theta II GDI I4 or 3.3L Lambda II V6, 6-speed "
                  "automatic",
        "reliability": 5.0,
        "maintenance": 6.8,
        "annual_maintenance_usd": 660,
        "insurance_factor": 1.18,
        "tire_set_usd": 760,
        "risk": "Engine is 363 of 755 complaints on the 2015; the "
                "2.4L is a Theta II bearing-failure engine",
        "known_issues": [
            "Engine is nearly half of the 2015 complaint file. Prefer "
            "the V6.",
            "All three recalls on the 2015 are fire-related: "
            "18V907000 (fuel pipe), 20V519000 and 21V331000 (ABS "
            "module).",
            "Turn-key cars lack an immobilizer.",
        ],
        "note": "Old, and sharing the engine problems of its "
                "successor. Only as a cheap V6.",
    },
    # ---- Telluride -------------------------------------------------
    {
        # 2020: 7 recalls, 783 complaints (exterior lighting 186,
        # engine 154, wipers 137). 2023: 6 recalls, 215 complaints.
        # 2025: 3 recalls, 127 complaints (engine 51).
        "make": "kia", "model": "telluride",
        "years": (2020, 2026),
        "generation": "ON first gen (facelift 2023)",
        "engine": "3.8L Lambda II GDI V6, 8-speed automatic; AWD "
                  "available",
        "reliability": 6.8,
        "maintenance": 6.9,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.05,
        "tire_set_usd": 900,
        "risk": "Recall 22V626000 on the 2020: the tow hitch wiring "
                "can short and start a fire while parked. Confirm it "
                "is closed",
        "known_issues": [
            "Seven recalls on the 2020 and six on the 2023. Two on "
            "the 2023 cover the front power seats (24V407000, "
            "26V430000) and one the driveshaft (24V214000).",
            "Exterior lighting is the largest cluster on the 2020 "
            "(186 of 783): headlights going dark. Recall 24V148000 "
            "covers it.",
            "Engine draws 154 complaints on the 2020 and 51 of 127 on "
            "the 2025. Check oil level and ask about oil use.",
            "Every Telluride has an immobilizer, so the Kia theft "
            "problem does not apply.",
        ],
        "note": "Deservedly popular and built on a plain V6, with "
                "more recalls than its reputation suggests. A 2022 or "
                "later with the list closed is the pick.",
    },
    # ---- Forte / K4 ------------------------------------------------
    {
        # 2025: 2 recalls, 53 complaints (electrical 16).
        "make": "kia", "model": "k4",
        "years": (2025, 2026),
        "generation": "CL4 first gen (replaces the Forte)",
        "engine": "2.0L I4 with CVT, or 1.6L turbo with an 8-speed "
                  "automatic on GT-Line Turbo",
        "reliability": 7.0,
        "maintenance": 7.6,
        "annual_maintenance_usd": 490,
        "insurance_factor": 1.0,
        "tire_set_usd": 660,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2025: 25V548000 (engine critical "
            "fasteners) and 26V046000 (instrument display). Confirm "
            "both are closed.",
            "53 complaints on the 2025, electrical the largest "
            "cluster at 16.",
            "New nameplate, so the score is provisional.",
        ],
        "note": "A lot of equipment for the money on a carried-over "
                "engine. Too new to call, so the score is "
                "provisional.",
    },
    {
        # 2022: 1 recall (22V304000, steering column), 28 complaints.
        "make": "kia", "model": "forte",
        "years": (2022, 2024),
        "generation": "BD third gen, facelift",
        "engine": "2.0L Nu MPI I4 with CVT; 1.6L turbo with a "
                  "dual-clutch on GT",
        "reliability": 7.0,
        "maintenance": 7.7,
        "annual_maintenance_usd": 490,
        "insurance_factor": 1.02,
        "tire_set_usd": 620,
        "risk": None,
        "known_issues": [
            "One recall on the 2022 (22V304000, steering column) and "
            "28 complaints. A quiet file.",
            "The CVT had early failures in 2019-2020 cars. Check for "
            "a whine or slipping, and ask about fluid service.",
            "Immobilizer is standard from 2022, so the theft problem "
            "of earlier Fortes does not apply.",
        ],
        "note": "Cheap, simple and by now fairly sorted. A sound "
                "budget commuter.",
    },
    {
        # 2019: 2 recalls, 150 complaints (power train 48, engine 38).
        "make": "kia", "model": "forte",
        "years": (2019, 2021),
        "generation": "BD third gen",
        "engine": "2.0L Nu MPI I4 with CVT; 1.6L turbo with a "
                  "dual-clutch on GT",
        "reliability": 6.3,
        "maintenance": 7.6,
        "annual_maintenance_usd": 520,
        "insurance_factor": 1.2,
        "tire_set_usd": 620,
        "risk": "Power train leads the 2019 complaint file (48 of "
                "150): early CVT failures",
        "known_issues": [
            "The first-year CVT is the largest cluster on the 2019. "
            "Drive it from cold and check for slipping, shudder or a "
            "whine.",
            "Engine is next at 38 complaints. Check oil level and "
            "service history.",
            "Turn-key cars have no immobilizer and are among the most "
            "stolen cars in the country. Get an insurance quote "
            "first.",
        ],
        "note": "Low price, but the early CVT and the theft exposure "
                "both cost money. A 2022 or later Forte is the better "
                "one.",
    },
    {
        # 2015: 1 recall, 262 complaints. 2017: 3 recalls, 305
        # complaints. The 2016 complaint pull returned only 5, which
        # looks like an API gap and is not used.
        "make": "kia", "model": "forte",
        "years": (2015, 2018),
        "generation": "YD second gen",
        "engine": "1.8L Nu MPI or 2.0L Nu GDI I4, 6-speed automatic",
        "reliability": 6.2,
        "maintenance": 7.6,
        "annual_maintenance_usd": 540,
        "insurance_factor": 1.2,
        "tire_set_usd": 600,
        "risk": "Nu four-cylinders in these years are known for "
                "piston noise and oil burning that can end in engine "
                "replacement",
        "known_issues": [
            "262 complaints on the 2015 and 305 on the 2017. Listen "
            "for a cold-start knock and check the oil level.",
            "Recall 21V622000 on the 2016 covers the trunk latch.",
            "Turn-key cars have no immobilizer and are theft targets. "
            "Confirm the anti-theft update.",
        ],
        "note": "Basic transport with an engine worth listening to "
                "closely. Provisional: the complaint data had a gap.",
    },
    # ---- Soul ------------------------------------------------------
    {
        # 2023: 4 recalls, 55 complaints. 2025: no recalls listed, 14
        # complaints.
        "make": "kia", "model": "soul",
        "years": (2023, 2025),
        "generation": "SK3 third gen, facelift",
        "engine": "2.0L Nu MPI I4 with CVT; front-wheel drive only",
        "reliability": 6.8,
        "maintenance": 7.6,
        "annual_maintenance_usd": 500,
        "insurance_factor": 1.02,
        "tire_set_usd": 640,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2023, including 25V099000 (engine "
            "internal parts) and 23V531000 (transmission fluid pump). "
            "Confirm both are closed.",
            "55 complaints on the 2023 and 14 on the 2025, with no "
            "recalls listed for the 2025.",
            "Immobilizer is standard on these years.",
        ],
        "note": "The Soul finally got quiet in its last years. "
                "Practical and cheap if the engine recall is done.",
    },
    {
        # 2020: 1 recall (21V259000, engine), 393 complaints (engine
        # 248, power train 91).
        "make": "kia", "model": "soul",
        "years": (2020, 2022),
        "generation": "SK3 third gen",
        "engine": "2.0L Nu MPI I4 with CVT; 1.6L turbo with a "
                  "dual-clutch on GT-Line Turbo",
        "reliability": 5.6,
        "maintenance": 7.4,
        "annual_maintenance_usd": 540,
        "insurance_factor": 1.2,
        "tire_set_usd": 640,
        "risk": "Engine is 248 of 393 complaints on the 2020, and "
                "recall 21V259000 covers the 2.0L engine",
        "known_issues": [
            "Engine is 63% of the 2020 complaint file. The 2.0L "
            "burns oil and can seize. Confirm 21V259000 and ask if "
            "the engine was replaced.",
            "Power train is another 91 complaints: the CVT. Check "
            "for slipping and a whine.",
            "Turn-key cars have no immobilizer and are theft targets. "
            "Price insurance before buying.",
        ],
        "note": "New body, old problem. Choose a 2023 or later Soul "
                "unless this one has a new engine on record.",
    },
    {
        # 2015: 4 recalls, 909 complaints (engine 633, 84 fires).
        # 2018: 1 recall, 222 complaints (engine 143, 14 fires).
        "make": "kia", "model": "soul",
        "years": (2015, 2019),
        "generation": "PS second gen",
        "engine": "1.6L Gamma GDI I4, 2.0L Nu GDI I4, or 1.6L turbo "
                  "with a dual-clutch",
        "reliability": 4.6,
        "maintenance": 7.2,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.25,
        "tire_set_usd": 620,
        "risk": "Engine is 633 of 909 complaints on the 2015 with 84 "
                "fires reported; recalls 19V120000 and 20V750000 are "
                "both engine campaigns",
        "known_issues": [
            "Engine is 70% of the 2015 complaint file, and 84 "
            "complaints mention fire. That is the highest fire count "
            "among the Kia profiles.",
            "Confirm both engine recalls are closed, and ask if the "
            "engine or catalytic converter was replaced.",
            "Still 143 of 222 complaints on the 2018, so later years "
            "of this generation did not fix it.",
            "Turn-key cars have no immobilizer and are among the most "
            "stolen cars in the country.",
        ],
        "note": "Engine failure, fire and theft all land on this "
                "generation. Avoid.",
    },
    # ---- Carnival / Sedona -----------------------------------------
    {
        # 2022: 6 recalls, 139 complaints (structure 34). 2024: 2
        # recalls, 76 complaints. 2025: 1 recall, 128 complaints
        # (electrical 85).
        "make": "kia", "model": "carnival",
        "years": (2022, 2026),
        "generation": "KA4 first gen (facelift 2025)",
        "engine": "3.5L Smartstream V6, 8-speed automatic; hybrid "
                  "with a 1.6L turbo from 2025",
        "reliability": 6.6,
        "maintenance": 6.9,
        "annual_maintenance_usd": 600,
        "insurance_factor": 1.0,
        "tire_set_usd": 820,
        "risk": None,
        "known_issues": [
            "Six recalls on the first-year 2022, including 23V236000 "
            "(power sliding doors) and 21V277000 (fuel injection). "
            "Test both sliding doors repeatedly.",
            "Recall 26V232000 covers fuel hoses on the 2022, 2024 "
            "and 2025. Confirm it is closed.",
            "Electrical is 85 of 128 complaints on the facelifted "
            "2025. Check every screen and switch on the test drive.",
            "No AWD on any trim.",
        ],
        "note": "A good van with first-year teething and a new "
                "electrical cluster on the facelift. A 2023 or 2024 "
                "V6 is the calm middle.",
    },
    {
        # 2016: 4 recalls, 299 complaints (engine 148, 14 fires).
        # 2019: 2 recalls, 40 complaints.
        "make": "kia", "model": "sedona",
        "years": (2015, 2021),
        "generation": "YP third gen",
        "engine": "3.3L Lambda II GDI V6; 6-speed automatic, 8-speed "
                  "from 2019",
        "reliability": 6.4,
        "maintenance": 6.8,
        "annual_maintenance_usd": 630,
        "insurance_factor": 1.1,
        "tire_set_usd": 760,
        "risk": "Engine is 148 of 299 complaints on the 2016 with 14 "
                "fires reported; later years are much quieter",
        "known_issues": [
            "The 2016 file is half engine. The 2019 has 40 complaints "
            "in total, so favor 2019 and later.",
            "Recall 18V338000 on the 2016 covers the power sliding "
            "doors and 19V109000 the wiring. Confirm both.",
            "Turn-key trims have no immobilizer. Confirm the "
            "anti-theft update.",
        ],
        "note": "An honest, cheap minivan. Buy late in the run and "
                "check the sliding doors.",
    },
    # ---- Rio -------------------------------------------------------
    {
        # 2019: 1 recall, 22 complaints. 2022: 1 recall, 12
        # complaints.
        "make": "kia", "model": "rio",
        "years": (2018, 2023),
        "generation": "YB fourth gen",
        "engine": "1.6L Gamma I4 (GDI with a 6-speed automatic "
                  "through 2019, MPI with CVT from 2020)",
        "reliability": 7.5,
        "maintenance": 8.0,
        "annual_maintenance_usd": 440,
        "insurance_factor": 1.1,
        "tire_set_usd": 540,
        "risk": None,
        "known_issues": [
            "Small files: 22 complaints on the 2019 and 12 on the "
            "2022, one recall each (21V622000 trunk latch, 22V304000 "
            "steering column).",
            "Turn-key 2018-2021 cars lack an immobilizer. Confirm "
            "the anti-theft update and price insurance; 2022 and "
            "later are not affected.",
            "Cheap parts and very little to go wrong.",
        ],
        "note": "One of the best records in the Kia range, simply "
                "because there is so little car.",
    },
    {
        # 2016: 2 recalls, 80 complaints (engine 39, brakes 18).
        "make": "kia", "model": "rio",
        "years": (2015, 2017),
        "generation": "UB third gen",
        "engine": "1.6L Gamma GDI I4, 6-speed automatic or manual",
        "reliability": 6.6,
        "maintenance": 8.0,
        "annual_maintenance_usd": 470,
        "insurance_factor": 1.15,
        "tire_set_usd": 520,
        "risk": None,
        "known_issues": [
            "Engine is 39 of 80 complaints on the 2016. Check for "
            "oil burning and a rattling catalytic converter.",
            "Recall 23V652000 covers the ABS module (fire risk). "
            "Confirm it was performed.",
            "Turn-key cars lack an immobilizer.",
        ],
        "note": "Cheap to keep going. Engine condition and theft "
                "exposure decide whether a given car is worth it.",
    },
    # ---- Stinger ---------------------------------------------------
    {
        # 2018: 4 recalls, 72 complaints (engine 24). 2022: 1 recall
        # (24V169000, engine), 18 complaints.
        "make": "kia", "model": "stinger",
        "years": (2018, 2023),
        "generation": "CK first gen",
        "engine": "2.0L turbo I4 (2.5L turbo from 2022) or 3.3L "
                  "twin-turbo V6, 8-speed automatic; RWD or AWD",
        "reliability": 7.0,
        "maintenance": 6.0,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.2,
        "tire_set_usd": 1100,
        "risk": "Recall 24V169000 covers the engine on both the 2018 "
                "and 2022 pulled. Confirm it was performed",
        "known_issues": [
            "Four recalls on the 2018, including 18V754000 (underhood "
            "wiring), 20V518000 (ABS module) and 23V634000 (fuel "
            "pump).",
            "Small complaint files (72 on the 2018, 18 on the 2022) "
            "because few were sold.",
            "Staggered performance tires and big brakes make it "
            "costly to run next to a K5.",
            "Many were driven hard or tuned. Look for a stock car "
            "with records.",
        ],
        "note": "A real sport sedan with a decent record for the "
                "type. Budget for tires, brakes and insurance.",
    },
    # ---- Niro ------------------------------------------------------
    {
        # 2023: 2 recalls, 44 complaints. 2024: 1 recall, 10
        # complaints.
        "make": "kia", "model": "niro",
        "years": (2023, 2026),
        "generation": "SG2 second gen",
        "engine": "1.6L hybrid with a 6-speed dual-clutch; plug-in "
                  "hybrid and EV versions also sold",
        "reliability": 7.4,
        "maintenance": 7.2,
        "annual_maintenance_usd": 480,
        "insurance_factor": 1.0,
        "tire_set_usd": 680,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2023 (23V298000 instrument display, "
            "25V024000 seats) and 44 complaints. One recall and 10 "
            "complaints on the 2024.",
            "The dual-clutch feels different from a Toyota hybrid: "
            "some low-speed hesitation is normal.",
            "On the Niro EV there is no oil service and upkeep is "
            "lower. Ask for a battery health report.",
        ],
        "note": "Very efficient and so far quiet. A good value "
                "against a Prius if the gearbox feel suits you.",
    },
    {
        # 2017: 4 recalls (three on the hybrid system). 2020: 1
        # recall. The complaints endpoint returned nothing for either
        # year: an API gap, not a clean record.
        "make": "kia", "model": "niro",
        "years": (2017, 2022),
        "generation": "DE first gen",
        "engine": "1.6L hybrid with a 6-speed dual-clutch; plug-in "
                  "hybrid and EV versions also sold",
        "reliability": 7.0,
        "maintenance": 7.0,
        "annual_maintenance_usd": 500,
        "insurance_factor": 1.02,
        "tire_set_usd": 660,
        "risk": "Three of four recalls on the 2017 are on the hybrid "
                "system (18V257000, 18V666000, 22V836000), with fire "
                "as a risk. Confirm all three",
        "known_issues": [
            "Run the VIN: the hybrid power relay and control unit "
            "campaigns on 2017-2018 cars are fire-related.",
            "Recall 23V534000 covers the transmission on the 2017 "
            "and 2020. Check for shudder pulling away.",
            "Ask for a hybrid battery health check on a car this "
            "old.",
            "NHTSA returned no complaint data for these years, so "
            "this score rests on recalls only.",
        ],
        "note": "Efficient and generally liked. Provisional: scored "
                "from recall campaigns because the complaint file "
                "came back empty.",
    },
    # ---- EV6 / EV9 -------------------------------------------------
    {
        # 2022: 4 recalls, 280 complaints (electrical 213). 2024: 3
        # recalls, 78 complaints (electrical 56).
        "make": "kia", "model": "ev6",
        "years": (2022, 2026),
        "generation": "CV first gen (E-GMP)",
        "engine": "Electric, single rear motor or dual-motor AWD; "
                  "58 to 84 kWh battery, 800-volt charging",
        "reliability": 6.2,
        "maintenance": 6.4,
        "annual_maintenance_usd": 330,
        "insurance_factor": 1.12,
        "tire_set_usd": 950,
        "risk": "The charging control unit (ICCU) can fail and stop "
                "charging the 12-volt battery, leaving the car without "
                "drive power: recalls 24V200000 and 24V867000",
        "known_issues": [
            "Electrical is 76% of the 2022 complaint file (213 of "
            "280), nearly all ICCU and 12-volt battery.",
            "Confirm both ICCU recalls are closed, and ask if the "
            "unit was replaced or only reflashed.",
            "Recall 26V431000 covers the traction battery on the "
            "2022 and 2024. Check it on the VIN.",
            "No oil service, so upkeep is low, but it is heavy on "
            "tires. Ask for a battery health report.",
        ],
        "note": "Quick, quick-charging, and carrying the same single "
                "electrical fault as the Ioniq 5. Fine once that work "
                "is documented.",
    },
    {
        # 2024: 7 recalls, 212 complaints (electrical 104, forward
        # collision avoidance 26). 2025: 4 recalls, 14 complaints.
        "make": "kia", "model": "ev9",
        "years": (2024, 2026),
        "generation": "MV first gen (E-GMP)",
        "engine": "Electric, single rear motor or dual-motor AWD; "
                  "76 or 100 kWh battery, 800-volt charging",
        "reliability": 5.8,
        "maintenance": 6.0,
        "annual_maintenance_usd": 380,
        "insurance_factor": 1.18,
        "tire_set_usd": 1150,
        "risk": "Seven recalls on the first-year 2024, including "
                "24V962000 (seat mounting bolts) and 26V431000 "
                "(traction battery)",
        "known_issues": [
            "Seven recalls on the 2024 is a high count. They cover "
            "seats, seat belts, the parking brake, the display and "
            "the battery. Confirm every one on the VIN.",
            "Electrical is 104 of 212 complaints on the 2024.",
            "The 2025 pulled four recalls and only 14 complaints so "
            "far. Prefer it over a 2024.",
            "Low upkeep with no oil service, but it is very heavy "
            "and tires are large and costly.",
        ],
        "note": "The only three-row EV near its price, with a rough "
                "first year. Buy a 2025 or later, and expect dealer "
                "visits.",
    },
]
