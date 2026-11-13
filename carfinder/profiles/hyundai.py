"""Reliability profiles: Hyundai. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

Two brand-wide patterns shape the older cars here. The 2011-2021 Theta
II and Nu four-cylinders have a long record of bearing and piston-ring
failures, and most 2015-2021 cars that start with a turn key have no
engine immobilizer and are stolen far more often than average. Both
are marked on the generations they apply to and nowhere else."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    # ---- Tucson ----------------------------------------------------
    {
        # 271 complaints on the 2025 with 144 FORWARD COLLISION
        # AVOIDANCE: textbook phantom braking, and six recalls.
        "make": "hyundai", "model": "tucson",
        "years": (2022, 2026),
        "generation": "NX4 fourth gen",
        "engine": "2.5L Smartstream I4, 8-speed automatic; hybrid uses "
                  "a 1.6L turbo",
        "reliability": 6.4,
        "maintenance": 7.2,
        "annual_maintenance_usd": 560,
        "insurance_factor": 1.0,
        "tire_set_usd": 720,
        "risk": "144 of 271 complaints on the 2025 are forward-"
                "collision-avoidance: phantom braking",
        "known_issues": [
            "Forward collision avoidance is 53% of the 2025 complaint "
            "file (144 of 271). Owners describe hard automatic braking "
            "with nothing ahead. Drive it on a highway before buying.",
            "Six recalls on the 2025, including 24V877000 (wiring) and "
            "25V549000 (engine critical fasteners).",
            "The 10yr/100k powertrain warranty is original-owner only. "
            "A used buyer gets 5yr/60k.",
            "Genuinely nice interior and a lot of space for the money.",
        ],
        "note": "The phantom-braking cluster is the whole story. If a "
                "long highway test drive stays clean it is a lot of "
                "car; if it does not, walk.",
    },
    {
        # 2017: 3 recalls, 1097 complaints (engine 604, power train
        # 294, 26 fires). 2020: 1 recall, 179 complaints (engine 73).
        "make": "hyundai", "model": "tucson",
        "years": (2016, 2021),
        "generation": "TL third gen",
        "engine": "2.0L Nu GDI I4 with a 6-speed automatic; 1.6L turbo "
                  "with a 7-speed dual-clutch (2016-2018); 2.4L Theta "
                  "II GDI from 2018",
        "reliability": 5.2,
        "maintenance": 7.0,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.2,
        "tire_set_usd": 680,
        "risk": "Engine is 604 of 1097 complaints on the 2017, with 26 "
                "fires reported: oil burning and seized engines on the "
                "2.0L and 2.4L",
        "known_issues": [
            "Engine is 55% of the 2017 complaint file (604 of 1097). "
            "Ask for oil-consumption test records and check the "
            "dipstick yourself before paying.",
            "Recall 20V543000 covers the ABS module, which can short "
            "and start a fire while parked. Confirm it is closed on "
            "the VIN.",
            "Power train is 294 complaints on the 2017, mostly the "
            "1.6T's dual-clutch hesitating from a stop. The 2.0L with "
            "the plain automatic avoids it.",
            "Turn-key cars have no immobilizer and are theft targets. "
            "Confirm the anti-theft software update was done and get "
            "an insurance quote first.",
        ],
        "note": "Cheap for a reason. The engine file and the theft "
                "problem both land on this generation, so buy only "
                "with service records and a closed recall list.",
    },
    {
        # 2015: 1 recall, 229 complaints (engine 120, brakes 67).
        "make": "hyundai", "model": "tucson",
        "years": (2015, 2015),
        "generation": "LM second gen, final year",
        "engine": "2.0L Nu GDI or 2.4L Theta II GDI I4, 6-speed "
                  "automatic",
        "reliability": 5.6,
        "maintenance": 7.2,
        "annual_maintenance_usd": 600,
        "insurance_factor": 1.15,
        "tire_set_usd": 640,
        "risk": "Engine is 120 of 229 complaints on the 2015: the 2.4L "
                "Theta II is the bearing-failure engine",
        "known_issues": [
            "Engine is over half the 2015 complaint file (120 of 229). "
            "Listen for a knock on a cold start and check for oil "
            "burning.",
            "Recall 22V056000 covers the ABS module (fire risk). "
            "Confirm it was performed.",
            "Turn-key cars lack an immobilizer. Ask whether the "
            "anti-theft update was installed.",
        ],
        "note": "An old design with the same engine worry as its "
                "successor. Only worth it cheap, with proof of oil "
                "changes.",
    },
    # ---- Kona ------------------------------------------------------
    {
        "make": "hyundai", "model": "kona",
        "years": (2024, 2026),
        "generation": "SX2 second gen",
        "engine": "2.0L Smartstream I4 with CVT, or the 1.6L turbo "
                  "with an 8-speed; AWD available",
        "reliability": 6.6,
        "maintenance": 7.3,
        "annual_maintenance_usd": 520,
        "insurance_factor": 0.98,
        "tire_set_usd": 680,
        "risk": "Recall 26V069000 on the 2026: front steering knuckles "
                "may crack and break, causing loss of steering control. "
                "Confirm it is closed on the VIN before driving it",
        "known_issues": [
            "The 2026 carries three recalls, and 26V069000 is a "
            "structural one: cracked front steering knuckles, with "
            "loss of steering control as the stated consequence. Not a "
            "software flash.",
            "Also 26V047000 (instrument display fails, a Hyundai-wide "
            "software fault) and 26V452000 (rear center seat belt "
            "buckle may not restrain in a crash).",
            "The 2025 was genuinely clean by comparison: zero recalls "
            "and 28 complaints. The two model years are not "
            "interchangeable on safety, so check the year and the VIN.",
            "Depreciated 18.1%/yr in one Michigan market (Aug 2026), more "
            "than double the Corolla Cross in the same sample. Check the "
            "curve the research phase fits for your area.",
            "Used-buyer warranty is 5yr/60k, not the 10yr/100k the "
            "original owner got.",
        ],
        "note": "Cheap on sticker price, but the 2026 carries a structural "
                "steering recall and resale was weak where it was measured.",
    },
    {
        # 2022: no recalls listed, 102 complaints (engine 33).
        "make": "hyundai", "model": "kona",
        "years": (2022, 2023),
        "generation": "OS first gen, facelift",
        "engine": "2.0L Nu MPI I4 with CVT, or the 1.6L turbo with a "
                  "7-speed dual-clutch; AWD available",
        "reliability": 6.6,
        "maintenance": 7.3,
        "annual_maintenance_usd": 530,
        "insurance_factor": 1.05,
        "tire_set_usd": 660,
        "risk": None,
        "known_issues": [
            "NHTSA lists no recalls for the 2022 and 102 complaints, "
            "with engine the largest cluster at 33. Better than the "
            "2018-2021 cars, not spotless.",
            "The 1.6T's dual-clutch shudders in stop-and-go traffic. "
            "The 2.0L with the CVT is the calmer choice.",
            "Some turn-key 2022 cars still lack an immobilizer. Ask "
            "whether the anti-theft update was installed.",
        ],
        "note": "The facelift fixed the worst of the early engine "
                "trouble. A reasonable small crossover if the price "
                "reflects the badge.",
    },
    {
        # 2019: 1 recall (21V301000, engine), 198 complaints with
        # engine at 138.
        "make": "hyundai", "model": "kona",
        "years": (2018, 2021),
        "generation": "OS first gen",
        "engine": "2.0L Nu MPI I4 with a 6-speed automatic, or the "
                  "1.6L turbo with a 7-speed dual-clutch",
        "reliability": 5.8,
        "maintenance": 7.2,
        "annual_maintenance_usd": 560,
        "insurance_factor": 1.15,
        "tire_set_usd": 660,
        "risk": "Engine is 138 of 198 complaints on the 2019, and "
                "recall 21V301000 covers the 2.0L engine itself",
        "known_issues": [
            "Engine is 70% of the 2019 complaint file (138 of 198). "
            "The 2.0L burns oil, then knocks, then fails. Check the oil "
            "level cold and ask for consumption-test paperwork.",
            "Recall 21V301000 is an engine campaign. Confirm it was "
            "performed, and whether the engine was replaced.",
            "Turn-key cars have no immobilizer. Confirm the anti-theft "
            "update and price insurance before you commit.",
        ],
        "note": "The engine cluster is too lopsided to ignore. Pick a "
                "2022 or later Kona unless this one has a replaced "
                "engine on record.",
    },
    # ---- Elantra ---------------------------------------------------
    {
        "make": "hyundai", "model": "elantra",
        "years": (2021, 2026),
        "generation": "CN7 seventh gen",
        "engine": "2.0L Smartstream I4 with CVT; hybrid pairs a 1.6L "
                  "with a dual-clutch",
        "reliability": 7.3,
        "maintenance": 7.5,
        "annual_maintenance_usd": 500,
        "insurance_factor": 0.96,
        "tire_set_usd": 640,
        "risk": None,
        "known_issues": [
            "Zero recalls on the 2025 and 21 complaints, the largest "
            "cluster being lane departure at 5. A clean file.",
            "Cheap to run and cheap to insure.",
            "Used-buyer warranty is 5yr/60k, not the 10yr/100k the "
            "original owner got.",
        ],
        "note": "Solid, unexciting, cheap. Nothing wrong with it and "
                "nothing that beats the Camry on the numbers.",
    },
    {
        # 2017: 4 recalls, 771 complaints (engine 292, structure 134).
        # 2019: 1 recall (21V301000, engine), 253 complaints (engine
        # 135).
        "make": "hyundai", "model": "elantra",
        "years": (2017, 2020),
        "generation": "AD sixth gen",
        "engine": "2.0L Nu MPI I4 with a 6-speed automatic (CVT for "
                  "2020); 1.4L or 1.6L turbo with a dual-clutch on "
                  "Eco and Sport",
        "reliability": 5.9,
        "maintenance": 7.4,
        "annual_maintenance_usd": 540,
        "insurance_factor": 1.2,
        "tire_set_usd": 600,
        "risk": "Engine leads the complaint file on both years pulled "
                "(292 of 771 on the 2017, 135 of 253 on the 2019), and "
                "recall 21V301000 covers the 2.0L engine",
        "known_issues": [
            "The 2.0L Nu is known for piston noise and oil burning "
            "that ends in a seized engine. Listen for a tick or knock "
            "on a cold start.",
            "Recall 21V301000 on the 2019 is an engine campaign. "
            "Confirm it is closed and ask if the engine was replaced.",
            "Turn-key cars have no immobilizer and are among the most "
            "stolen cars in the country. Some insurers surcharge or "
            "decline them, so get a quote first.",
            "Four recalls on the 2017, including 17V213000 (electric "
            "power steering).",
        ],
        "note": "A cheap commuter with two real problems: the engine "
                "and theft. Fine with records and a garage, risky "
                "without either.",
    },
    {
        # 2015: 3 recalls, 262 complaints (engine 92, brakes 55).
        "make": "hyundai", "model": "elantra",
        "years": (2015, 2016),
        "generation": "MD fifth gen",
        "engine": "1.8L Nu MPI I4, 6-speed automatic",
        "reliability": 6.3,
        "maintenance": 7.6,
        "annual_maintenance_usd": 540,
        "insurance_factor": 1.15,
        "tire_set_usd": 580,
        "risk": "The 1.8L Nu is known for piston slap that can end in "
                "engine replacement; engine is 92 of 262 complaints on "
                "the 2015",
        "known_issues": [
            "Listen for a cold-start ticking that does not fade. That "
            "is the piston noise this engine is known for.",
            "Recall 23V651000 covers the ABS module (fire risk). "
            "Confirm it was performed.",
            "Turn-key cars lack an immobilizer. Ask for proof of the "
            "anti-theft update.",
        ],
        "note": "Simple and cheap to keep going, but at this age "
                "everything depends on how the engine sounds.",
    },
    # ---- Santa Fe --------------------------------------------------
    {
        # 2024: 7 recalls, 165 complaints (power train 47). 2025: 5
        # recalls, 140 complaints.
        "make": "hyundai", "model": "santa fe",
        "years": (2024, 2026),
        "generation": "MX5 fifth gen",
        "engine": "2.5L turbo I4 with an 8-speed wet dual-clutch; "
                  "hybrid uses a 1.6L turbo with a 6-speed automatic",
        "reliability": 5.9,
        "maintenance": 6.8,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.04,
        "tire_set_usd": 860,
        "risk": "Seven recalls on the 2024, including 24V529000 on the "
                "transmission control, and power train leads its "
                "complaints (47 of 165)",
        "known_issues": [
            "Seven recalls on the 2024 and five on the 2025. That is a "
            "high count for a new design.",
            "The dual-clutch gearbox on the 2.5T is the weak point: "
            "24V529000 covers its control unit. The hybrid's regular "
            "automatic avoids it.",
            "Recall 25V549000 on the 2025 covers engine critical "
            "fasteners. Confirm it is closed.",
            "Forward collision avoidance draws 19 to 21 complaints on "
            "each year pulled. Test the driver aids on a highway.",
        ],
        "note": "Roomy and clever inside, with a recall record that is "
                "not settling down yet. The hybrid is the safer pick.",
    },
    {
        # 2022: 5 recalls, 204 complaints (power train 57, engine 54).
        "make": "hyundai", "model": "santa fe",
        "years": (2021, 2023),
        "generation": "TM fourth gen, facelift",
        "engine": "2.5L Smartstream I4 with an 8-speed automatic; 2.5L "
                  "turbo with an 8-speed wet dual-clutch; hybrid uses "
                  "a 1.6L turbo",
        "reliability": 6.3,
        "maintenance": 7.0,
        "annual_maintenance_usd": 590,
        "insurance_factor": 1.05,
        "tire_set_usd": 800,
        "risk": "Recall 22V746000 on the 2022 covers the automatic "
                "transmission: the 2.5T's dual-clutch can lose drive",
        "known_issues": [
            "Five recalls on the 2022, including 22V746000 "
            "(transmission) and 22V197000 (engine). Confirm both are "
            "closed on the VIN.",
            "Power train is the largest named cluster on the 2022 (57 "
            "of 204). The non-turbo 2.5L with the plain automatic "
            "avoids the dual-clutch.",
            "Recall 23V181000 covers the tow hitch wiring, a fire "
            "risk. Check it if the car has a factory hitch.",
        ],
        "note": "Better than the 2019-2020 cars on engines. Buy the "
                "non-turbo or the hybrid and it is a decent family "
                "SUV.",
    },
    {
        # 2020: 2 recalls, 218 complaints (engine 81, 9 fires).
        "make": "hyundai", "model": "santa fe",
        "years": (2019, 2020),
        "generation": "TM fourth gen",
        "engine": "2.4L Theta II GDI I4 or 2.0L turbo, 8-speed "
                  "automatic",
        "reliability": 6.0,
        "maintenance": 7.0,
        "annual_maintenance_usd": 600,
        "insurance_factor": 1.12,
        "tire_set_usd": 780,
        "risk": "Still uses the 2.4L Theta II; engine is the largest "
                "cluster on the 2020 (81 of 218 complaints) with nine "
                "fires reported",
        "known_issues": [
            "These are the last years of the Theta II engines. Ask "
            "for oil-change records and whether the knock-sensor "
            "software update was done.",
            "Nine fire complaints on the 2020. Run the VIN for open "
            "recalls before buying.",
            "Turn-key trims have no immobilizer. Confirm the "
            "anti-theft update.",
        ],
        "note": "A fair SUV carrying an engine family with a bad "
                "record. A 2021 or later one costs a little more and "
                "drops that worry.",
    },
    {
        # 2017: 6 recalls, 976 complaints (engine 654, power train
        # 166, 23 fires).
        "make": "hyundai", "model": "santa fe",
        "years": (2015, 2018),
        "generation": "NC third gen, three-row",
        "engine": "3.3L Lambda II GDI V6, 6-speed automatic",
        "reliability": 5.6,
        "maintenance": 6.8,
        "annual_maintenance_usd": 640,
        "insurance_factor": 1.15,
        "tire_set_usd": 780,
        "risk": "Engine is 654 of 976 complaints on the 2017 with 23 "
                "fires, and recall 17V578000 covers the engine",
        "known_issues": [
            "Engine is two thirds of the 2017 complaint file. Some of "
            "that is Santa Fe Sport owners filing under this name, "
            "but 17V578000 is an engine recall on this car.",
            "Six recalls on the 2017, including 22V056000 (ABS module, "
            "fire risk) and 17V358000 (hood latch).",
            "Turn-key cars have no immobilizer. Confirm the "
            "anti-theft update and get an insurance quote.",
        ],
        "note": "The V6 is sturdier than the four in the Santa Fe "
                "Sport, but the recall and fire record still asks for "
                "a careful VIN check.",
    },
    {
        # 2017: 3 recalls, 358 complaints (engine 208, brakes 57).
        "make": "hyundai", "model": "santa fe sport",
        "years": (2015, 2018),
        "generation": "DM third gen, two-row",
        "engine": "2.4L Theta II GDI I4 or 2.0L Theta II turbo, "
                  "6-speed automatic",
        "reliability": 4.8,
        "maintenance": 6.8,
        "annual_maintenance_usd": 660,
        "insurance_factor": 1.2,
        "tire_set_usd": 740,
        "risk": "Both engines are Theta II units known for rod-bearing "
                "failure; engine is 208 of 358 complaints on the 2017",
        "known_issues": [
            "Engine is 58% of the 2017 complaint file. A knock, a "
            "flashing oil light or metal in the oil means a new "
            "engine.",
            "Ask a Hyundai dealer to confirm the knock-sensor software "
            "campaign and the extended engine warranty apply to the "
            "VIN.",
            "Recall 22V056000 covers the ABS module, which can catch "
            "fire while parked.",
            "Turn-key cars have no immobilizer and are theft targets.",
        ],
        "note": "One of the worst-affected Theta II cars. Skip it "
                "unless the engine has already been replaced and you "
                "have the paperwork.",
    },
    # ---- Palisade --------------------------------------------------
    {
        # 2026: 3 recalls, 131 complaints (seats 49, electrical 35).
        "make": "hyundai", "model": "palisade",
        "years": (2026, 2026),
        "generation": "LX3 second gen",
        "engine": "3.5L V6 with an 8-speed automatic, or a 2.5L turbo "
                  "hybrid",
        "reliability": 6.2,
        "maintenance": 6.6,
        "annual_maintenance_usd": 640,
        "insurance_factor": 1.06,
        "tire_set_usd": 950,
        "risk": "Recall 26V160000 on the 2026 covers the power-"
                "adjusting second and third row seats, and seats are "
                "49 of 131 complaints",
        "known_issues": [
            "Seats are the largest complaint cluster on the 2026 (49 "
            "of 131). Confirm 26V160000 is closed and keep children "
            "clear of the power-folding seats until it is.",
            "Also 26V047000 (instrument display) and 26V169000 (rear "
            "seat belt buckle).",
            "First model year of a new design, so the score is "
            "provisional.",
        ],
        "note": "Three recalls and 131 complaints in its first year. "
                "Let it settle, or buy only with the seat recall "
                "closed.",
    },
    {
        # 2023: 5 recalls, 412 complaints (brakes 85, seat belts 78,
        # wipers 53).
        "make": "hyundai", "model": "palisade",
        "years": (2023, 2025),
        "generation": "LX2 first gen, facelift",
        "engine": "3.8L Lambda II GDI V6, 8-speed automatic",
        "reliability": 6.8,
        "maintenance": 6.9,
        "annual_maintenance_usd": 610,
        "insurance_factor": 1.04,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "Five recalls on the 2023, including 23V415000 (brake "
            "power assist) and 23V526000 (transmission fluid pump). "
            "Confirm both are closed.",
            "Recall 25V607000 covers rear seat belt buckles and "
            "26V034000 the side curtain air bags.",
            "Brakes (85) and seat belts (78) lead the 2023 complaint "
            "file of 412. Check pedal feel on the test drive.",
            "The V6 and regular automatic are the simple, proven part "
            "of the car.",
        ],
        "note": "A well-liked three-row with an ordinary engine and a "
                "longer recall list than a Highlander. Good if the "
                "campaigns are done.",
    },
    {
        # 2020: 5 recalls, 543 complaints (engine 134, wipers 115,
        # suspension 61).
        "make": "hyundai", "model": "palisade",
        "years": (2020, 2022),
        "generation": "LX2 first gen",
        "engine": "3.8L Lambda II GDI V6, 8-speed automatic",
        "reliability": 6.8,
        "maintenance": 6.9,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.05,
        "tire_set_usd": 900,
        "risk": "Recall 22V633000: the tow hitch wiring can short and "
                "start a fire while parked. Confirm it is closed",
        "known_issues": [
            "Five recalls on the 2020, including 22V633000 (tow hitch "
            "wiring, fire) and 22V627000 (wiper motor).",
            "543 complaints on the 2020, led by engine (134) and "
            "wipers (115). Ask about oil use and test the wipers.",
            "A few 2020-2021 turn-key trims lack an immobilizer. Most "
            "Palisades have push-button start and are not affected.",
        ],
        "note": "First-year cars carry the most complaints. A 2021 or "
                "2022 with the hitch recall done is the better buy.",
    },
    # ---- Sonata ----------------------------------------------------
    {
        # 2020: 4 recalls, 183 complaints (fuel/propulsion 47,
        # electrical 41). 2023: 2 recalls, 88 complaints.
        "make": "hyundai", "model": "sonata",
        "years": (2020, 2026),
        "generation": "DN8 eighth gen",
        "engine": "2.5L Smartstream I4 or 1.6L turbo, 8-speed "
                  "automatic; hybrid uses a 2.0L",
        "reliability": 7.2,
        "maintenance": 7.6,
        "annual_maintenance_usd": 510,
        "insurance_factor": 1.02,
        "tire_set_usd": 740,
        "risk": "Recall 25V796000 covers the fuel system on the 2020 "
                "and 2023 pulled. Confirm it was performed",
        "known_issues": [
            "Fuel/propulsion is the largest cluster on both years "
            "pulled (47 of 183 on the 2020, 37 of 88 on the 2023), and "
            "25V796000 is the matching recall.",
            "Recall 23V526000 on the 2023 covers the transmission "
            "fluid pump.",
            "Used-buyer warranty is 5yr/60k unless the car is "
            "certified pre-owned.",
            "This generation is not in the group of turn-key cars "
            "without an immobilizer, so the theft problem of older "
            "Sonatas does not apply.",
        ],
        "note": "A clear step up from the old Sonata: no Theta II, a "
                "plain automatic, and a modest complaint file.",
    },
    {
        # 2015: 9 recalls, 1157 complaints (engine 632, 48 fires).
        # 2017: 3 recalls, 769 complaints (engine 386, steering 173).
        "make": "hyundai", "model": "sonata",
        "years": (2015, 2019),
        "generation": "LF seventh gen",
        "engine": "2.4L Theta II GDI I4 or 2.0L Theta II turbo, "
                  "6-speed automatic; 1.6L turbo with a dual-clutch on "
                  "Eco",
        "reliability": 4.8,
        "maintenance": 7.0,
        "annual_maintenance_usd": 640,
        "insurance_factor": 1.22,
        "tire_set_usd": 700,
        "risk": "Theta II rod-bearing failure: engine is 632 of 1157 "
                "complaints on the 2015 with 48 fires reported",
        "known_issues": [
            "Engine is more than half of the complaint file on both "
            "the 2015 and the 2017. Failure is sudden: a knock, then "
            "a stall at speed.",
            "Have a Hyundai dealer confirm the knock-sensor software "
            "campaign and the extended engine warranty on the VIN.",
            "Nine recalls on the 2015. Steering draws 173 complaints "
            "on the 2017, so check for a click or play in the wheel.",
            "Turn-key cars have no immobilizer. Some insurers "
            "surcharge or refuse them.",
        ],
        "note": "The car at the center of the Theta II story. Only "
                "worth buying with a replaced engine on record and a "
                "low price.",
    },
    # ---- Ioniq 5 / Ioniq 6 -----------------------------------------
    {
        # 2022: 3 recalls, 407 complaints (electrical 307). 2024: 3
        # recalls, 226 complaints (electrical 179).
        "make": "hyundai", "model": "ioniq 5",
        "years": (2022, 2026),
        "generation": "NE first gen (E-GMP)",
        "engine": "Electric, single rear motor or dual-motor AWD; "
                  "58 to 84 kWh battery, 800-volt charging",
        "reliability": 6.2,
        "maintenance": 6.4,
        "annual_maintenance_usd": 330,
        "insurance_factor": 1.12,
        "tire_set_usd": 950,
        "risk": "The charging control unit (ICCU) can fail and stop "
                "charging the 12-volt battery, leaving the car without "
                "drive power: recalls 24V204000 and 24V868000",
        "known_issues": [
            "Electrical is 75% of the 2022 complaint file (307 of "
            "407) and 79% of the 2024 (179 of 226). Nearly all of it "
            "is the ICCU and 12-volt battery.",
            "Confirm both ICCU recalls are closed, and ask if the unit "
            "was replaced or only reflashed.",
            "No oil changes, so yearly upkeep is low, but it is heavy "
            "on tires. Ask for a battery health report.",
            "Recall 26V432000 on the 2024 covers the traction "
            "battery. Check it on the VIN.",
        ],
        "note": "Fast charging and a great cabin, held back by one "
                "repeating electrical fault. Fine once the ICCU work "
                "is documented.",
    },
    {
        # 2023: 5 recalls, 56 complaints (electrical 33). 2024: 5
        # recalls, 38 complaints.
        "make": "hyundai", "model": "ioniq 6",
        "years": (2023, 2026),
        "generation": "CE first gen (E-GMP)",
        "engine": "Electric, single rear motor or dual-motor AWD; "
                  "53 or 77 kWh battery, 800-volt charging",
        "reliability": 6.4,
        "maintenance": 6.4,
        "annual_maintenance_usd": 320,
        "insurance_factor": 1.1,
        "tire_set_usd": 900,
        "risk": "Shares the Ioniq 5's charging control unit fault: "
                "recalls 24V204000 and 24V868000, plus 25V606000 on "
                "the charging system",
        "known_issues": [
            "Five recalls on both the 2023 and the 2024. Three are on "
            "the charging and 12-volt system, so confirm each is "
            "closed.",
            "Electrical is 33 of 56 complaints on the 2023. The file "
            "is small because few were sold.",
            "Recall 24V065000 on the 2023 covers the driveshaft, and "
            "24V283000 on the 2024 the differential.",
            "Low running costs: no oil service, and brakes last a "
            "long time.",
        ],
        "note": "Same hardware and same weak spot as the Ioniq 5 in a "
                "more efficient shape. Buy with the recall list "
                "closed.",
    },
    # ---- Santa Cruz ------------------------------------------------
    {
        # 2022: 4 recalls, 187 complaints (power train 91). 2024: 1
        # recall, 36 complaints.
        "make": "hyundai", "model": "santa cruz",
        "years": (2022, 2026),
        "generation": "NX4 OB first gen",
        "engine": "2.5L Smartstream I4 with an 8-speed automatic, or "
                  "2.5L turbo with an 8-speed wet dual-clutch",
        "reliability": 6.4,
        "maintenance": 7.0,
        "annual_maintenance_usd": 590,
        "insurance_factor": 1.02,
        "tire_set_usd": 780,
        "risk": "Recall 22V746000 on the 2022 covers the turbo's "
                "dual-clutch transmission; power train is 91 of 187 "
                "complaints that year",
        "known_issues": [
            "Power train is nearly half of the 2022 complaint file. "
            "The turbo's dual-clutch is the cause; confirm 22V746000 "
            "was performed.",
            "The non-turbo 2.5L uses a regular automatic and avoids "
            "that failure, at the cost of slow acceleration.",
            "The 2024 pulled much cleaner: one recall (24V412000, "
            "power steering) and 36 complaints.",
            "Recall 23V181000 covers tow hitch wiring on the 2022.",
        ],
        "note": "Handy small truck. Later years or the non-turbo "
                "engine are the safer picks.",
    },
    # ---- Venue -----------------------------------------------------
    {
        # 2023: no recalls listed, 24 complaints (electrical 13).
        "make": "hyundai", "model": "venue",
        "years": (2022, 2026),
        "generation": "QX first gen",
        "engine": "1.6L Smartstream MPI I4 with CVT; front-wheel "
                  "drive only",
        "reliability": 7.5,
        "maintenance": 7.8,
        "annual_maintenance_usd": 470,
        "insurance_factor": 0.98,
        "tire_set_usd": 600,
        "risk": None,
        "known_issues": [
            "NHTSA lists no recalls for the 2023 and only 24 "
            "complaints, 13 of them electrical.",
            "Port injection and no turbo: little to go wrong, and "
            "cheap when it does.",
            "No AWD on any trim, and it is slow on the highway.",
        ],
        "note": "Basic, slow and honest. One of the quieter records "
                "in the Hyundai range.",
    },
    {
        # 2020: 1 recall (22V458000, front seat belts), 42 complaints.
        "make": "hyundai", "model": "venue",
        "years": (2020, 2021),
        "generation": "QX first gen, early cars",
        "engine": "1.6L Smartstream MPI I4 with CVT (a 6-speed manual "
                  "was offered in 2020)",
        "reliability": 7.3,
        "maintenance": 7.8,
        "annual_maintenance_usd": 480,
        "insurance_factor": 1.12,
        "tire_set_usd": 600,
        "risk": None,
        "known_issues": [
            "One recall on the 2020 (22V458000, front seat belt "
            "pretensioners) and 42 complaints. Confirm the recall is "
            "closed.",
            "Turn-key 2020-2021 cars lack an immobilizer. Confirm the "
            "anti-theft update and get an insurance quote first.",
            "Front-wheel drive only.",
        ],
        "note": "Mechanically as sound as the later cars. The only "
                "real mark against it is the theft exposure.",
    },
    # ---- Accent ----------------------------------------------------
    {
        # 2019: 1 recall, 31 complaints (engine 19). 2021: 4 recalls,
        # 16 complaints.
        "make": "hyundai", "model": "accent",
        "years": (2018, 2022),
        "generation": "HC fifth gen",
        "engine": "1.6L Gamma I4 (GDI through 2019, MPI with CVT from "
                  "2020)",
        "reliability": 7.3,
        "maintenance": 8.0,
        "annual_maintenance_usd": 450,
        "insurance_factor": 1.15,
        "tire_set_usd": 540,
        "risk": None,
        "known_issues": [
            "Small complaint files: 31 on the 2019 (19 engine) and 16 "
            "on the 2021.",
            "Four recalls on the 2021, covering front seat belts "
            "(22V069000, 22V354000), the steering column (22V311000) "
            "and brakes (21V937000). Confirm all four.",
            "Turn-key cars have no immobilizer and are theft targets. "
            "Price insurance before buying.",
        ],
        "note": "About as cheap to run as a car gets. Theft exposure "
                "is the main cost that does not show on the sticker.",
    },
    {
        # 2016: no recalls listed, 103 complaints (engine 33, air
        # bags 30).
        "make": "hyundai", "model": "accent",
        "years": (2015, 2017),
        "generation": "RB fourth gen",
        "engine": "1.6L Gamma GDI I4, 6-speed automatic or manual",
        "reliability": 7.0,
        "maintenance": 8.0,
        "annual_maintenance_usd": 470,
        "insurance_factor": 1.12,
        "tire_set_usd": 520,
        "risk": None,
        "known_issues": [
            "NHTSA lists no recalls for the 2016 and 103 complaints, "
            "led by engine (33) and air bags (30).",
            "Check that the air bag warning light goes out after "
            "starting.",
            "Turn-key cars lack an immobilizer. Ask about the "
            "anti-theft update.",
        ],
        "note": "Old and plain, but it avoided the big engine "
                "failures of its larger siblings.",
    },
    # ---- Veloster --------------------------------------------------
    {
        # 2019: 2 recalls (21V301000 engine, 19V311000 door latch),
        # 42 complaints (engine 18).
        "make": "hyundai", "model": "veloster",
        "years": (2019, 2022),
        "generation": "JS second gen",
        "engine": "2.0L Nu MPI I4, 1.6L turbo, or the 2.0L turbo in "
                  "the N (the only version sold for 2022)",
        "reliability": 6.5,
        "maintenance": 7.0,
        "annual_maintenance_usd": 580,
        "insurance_factor": 1.18,
        "tire_set_usd": 760,
        "risk": "Recall 21V301000 on the 2019 covers the 2.0L Nu "
                "engine. Confirm it was performed",
        "known_issues": [
            "The base 2.0L is the engine under recall 21V301000. The "
            "1.6T and the N use different engines.",
            "42 complaints on the 2019, 18 of them engine. A small "
            "file for a low-volume car.",
            "Many were driven hard or modified. Look for a stock car "
            "with records, above all on the N.",
            "Turn-key 2019-2021 cars lack an immobilizer.",
        ],
        "note": "Fun and practical for a hatchback. Buy the 1.6T or "
                "the N over the base engine.",
    },
    {
        # 2016: 1 recall (20V746000, engine), 226 complaints (engine
        # 134, power train 43). No 2018 model year was sold.
        "make": "hyundai", "model": "veloster",
        "years": (2015, 2017),
        "generation": "FS first gen",
        "engine": "1.6L Gamma GDI I4 or 1.6L turbo; 6-speed "
                  "dual-clutch on the base car",
        "reliability": 5.8,
        "maintenance": 7.0,
        "annual_maintenance_usd": 600,
        "insurance_factor": 1.2,
        "tire_set_usd": 700,
        "risk": "Engine is 134 of 226 complaints on the 2016, and "
                "recall 20V746000 is an engine campaign",
        "known_issues": [
            "Engine is 59% of the 2016 complaint file. Confirm "
            "20V746000 is closed and listen for knock.",
            "The base car's dual-clutch draws power-train complaints "
            "(43 on the 2016). Check for shudder pulling away.",
            "Turn-key cars have no immobilizer and are theft targets.",
        ],
        "note": "Cheap and quirky, with an engine file that argues "
                "for the newer generation.",
    },
    # ---- Kona Electric ---------------------------------------------
    {
        # 2024: 1 recall (26V452000, rear seat belt buckle), 15
        # complaints.
        "make": "hyundai", "model": "kona electric",
        "years": (2024, 2026),
        "generation": "SX2 second gen",
        "engine": "Electric, single front motor; 48.6 or 64.8 kWh "
                  "battery, 400-volt charging",
        "reliability": 7.0,
        "maintenance": 6.8,
        "annual_maintenance_usd": 310,
        "insurance_factor": 1.05,
        "tire_set_usd": 740,
        "risk": None,
        "known_issues": [
            "One recall on the 2024 (26V452000, rear center seat belt "
            "buckle) and 15 complaints, 10 of them electrical.",
            "Charges slower than the Ioniq 5 on a road trip: it is a "
            "400-volt car.",
            "No oil service, so upkeep is mostly tires and cabin "
            "filters. Ask for a battery health report on a used one.",
        ],
        "note": "A quiet file so far, on thin data. The score is "
                "provisional.",
    },
    {
        # 2019: 4 recalls, 54 complaints (electrical 42). Complaints
        # for 2021 came back empty under this model name.
        "make": "hyundai", "model": "kona electric",
        "years": (2019, 2023),
        "generation": "OS first gen",
        "engine": "Electric, single front motor; 64 kWh battery",
        "reliability": 6.0,
        "maintenance": 6.6,
        "annual_maintenance_usd": 340,
        "insurance_factor": 1.08,
        "tire_set_usd": 720,
        "risk": "Traction battery fire recalls 20V630000 and 21V127000 "
                "on the 2019: the pack was replaced on affected cars. "
                "Get proof",
        "known_issues": [
            "Two of the four recalls on the 2019 are on the high-"
            "voltage battery. Ask the dealer for the date the pack "
            "was replaced; a new pack is a real plus.",
            "Recall 22V941000 on the 2021 is also a battery campaign, "
            "and 20V748000 covers the electric brake booster.",
            "Electrical is 42 of 54 complaints on the 2019.",
            "Low upkeep with no oil service, but it eats front tires.",
        ],
        "note": "Good range for the money if the battery recall work "
                "is documented. Without that paperwork, pass. "
                "Provisional: the complaint data is patchy.",
    },
]
