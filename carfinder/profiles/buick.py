"""Reliability profiles: Buick. The format and the caveats on reading
these numbers are in carfinder/reliability.py."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        # Written 2026-08-15 from NHTSA recalls + complaints for 2024/2025
        # and a VIN decode of a 2024 example (engine LIH, Bupyeong KR).
        # Split from the 2025+ profile below only because the instrument-
        # cluster recall is 2024-only. Same generation, same engine.
        "make": "buick", "model": "envista",
        "years": (2024, 2024),
        "generation": "first gen, FWD-only subcompact SUV",
        "engine": "1.2L LIH turbo I3, 6-speed automatic (shared with the "
                  "Chevrolet Trax and Buick Encore GX)",
        "reliability": 7.0,
        "maintenance": 8.5,
        "annual_maintenance_usd": 430,
        "insurance_factor": 0.95,
        "tire_set_usd": 680,
        "risk": "Recall 23V744000 (instrument panel can go blank at "
                "startup or while driving): confirm the VCU software "
                "update was applied; it is free and can be done OTA",
        "known_issues": [
            "Electrical is more than half the complaint volume: 25 of 49 "
            "NHTSA filings. Much of that traces to the VCU/instrument "
            "cluster recall above, which has a free software fix, so "
            "confirm it was performed before reading the cluster as "
            "hardware trouble.",
            "The powertrain is quiet in the data: 7 engine and 3 power "
            "train filings out of 49. That is the reassuring part.",
            "Turbo three-cylinder, so oil service history matters more "
            "than displacement alone suggests.",
            "Only two model years on the road, so this reliability score is "
            "provisional, not observed over a full ownership cycle.",
        ],
        "note": "Mechanically a Trax in a nicer suit: high-volume GM parts, "
                "any dealer can work on it, cheap to run at 30 mpg "
                "combined. FWD only, so budget winter tires rather than "
                "expecting AWD traction.",
    },
    {
        # Same generation, no recalls on 2025+. Note the engine code
        # changes: a 2024 VIN decodes to LIH, a 2025 to LBP. Same 1.2L
        # turbo triple by displacement and output; treat the re-code as a
        # running change until something says otherwise.
        "make": "buick", "model": "envista",
        "years": (2025, 2026),
        "generation": "first gen, FWD-only subcompact SUV",
        "engine": "1.2L LBP turbo I3, 6-speed automatic (LIH on 2024 cars; "
                  "shared with the Chevrolet Trax and Buick Encore GX)",
        "reliability": 7.3,
        "maintenance": 8.5,
        "annual_maintenance_usd": 430,
        "insurance_factor": 0.95,
        "tire_set_usd": 680,
        "risk": None,
        "known_issues": [
            "No open recalls, and 29 complaints against the 2024's 49.",
            "Electrical is still the largest cluster (11 of 29) but a "
            "smaller share than 2024, and without a recall behind it.",
            "Turbo three-cylinder: keep the oil service records.",
            "Provisional score; too new for a long-term verdict.",
        ],
        "note": "The 2024 with its recall sorted and the 2025 are close to "
                "the same car. Buy on price and mileage, not model year.",
    },
    {
        # 29 complaints on the 2024, only the shared VCU recall.
        "make": "buick", "model": "encore gx",
        "years": (2024, 2026),
        "generation": "second gen",
        "engine": "1.2L turbo I3 or the optional 1.3L turbo I3; AWD "
                  "available, unlike the Envista",
        "reliability": 7.4,
        "maintenance": 8.4,
        "annual_maintenance_usd": 450,
        "insurance_factor": 0.96,
        "tire_set_usd": 690,
        "risk": None,
        "known_issues": [
            "29 complaints on the 2024 against the Trax's 165 and the "
            "Envista's 49, on a smaller sales base than either: the "
            "quietest file of the three GM cars.",
            "Same 23V744000 VCU recall. Confirm the software fix.",
            "Electrical is still the top cluster (18 of 29), which is "
            "the family trait across all three.",
            "The 1.3L is the one to want if you find it: noticeably "
            "less strained than the 1.2L.",
            "Taller and boxier than the Envista, and it loses the "
            "swoopy roofline that is half the Envista's appeal.",
        ],
        "note": "The Envista's sibling with AWD on the options list. In a "
                "snow state that is worth a test drive on its own.",
    },
    {
        "make": "buick", "model": "envision",
        "years": (2021, 2026),
        "generation": "second gen",
        "engine": "2.0L LSY turbo I4, 9-speed automatic; AWD available",
        "reliability": 7.5,
        "maintenance": 7.4,
        "annual_maintenance_usd": 560,
        "insurance_factor": 1.0,
        "tire_set_usd": 740,
        "risk": None,
        "known_issues": [
            "23 complaints on the 2023 and a single software recall "
            "(22V903000, lighting control module). A genuinely quiet "
            "file.",
            "Depreciated 14.7%/yr in one Michigan market (Aug 2026), "
            "mid-pack, and much better "
            "than the GMC pair.",
            "The 2.0L turbo is the strongest engine among the small "
            "GM crossovers here, and it is built in China, which some "
            "buyers care about and the badge does not advertise.",
            "Noticeably nicer inside than a Terrain or Equinox.",
        ],
        "note": "The best-behaved GM crossover on the data.",
    },
    # Added profiles: other generations and models. Counts are
    # from NHTSA for the model year named in each line.
    {
        "make": "buick", "model": "enclave",
        "years": (2015, 2017),
        "generation": "first gen, late years",
        "engine": "3.6L V6, 6-speed automatic",
        "reliability": 6.4,
        "maintenance": 6.8,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.0,
        "tire_set_usd": 820,
        "risk": None,
        "known_issues": [
            "Air bags are 110 of 142 complaints on the 2016, and two of its "
            "4 recalls are frontal air bag campaigns (21V782000, 23V334000). "
            "Run the VIN and confirm they are closed.",
            "Away from the air bags the file is small: power train 11, "
            "engine 10.",
            "The 3.6L wants clean oil. Stretched timing chains show up on "
            "engines with long oil change intervals, and the job is "
            "expensive.",
            "Power steering and A/C leaks are common at this age. Look under "
            "it.",
        ],
        "note": "An old design by these years, with most early faults worked "
                "out. Comfortable and cheap to buy, not cheap to fix.",
    },
    {
        "make": "buick", "model": "enclave",
        "years": (2018, 2024),
        "generation": "second gen",
        "engine": "3.6L V6, 9-speed automatic; AWD available",
        "reliability": 6.9,
        "maintenance": 7.0,
        "annual_maintenance_usd": 660,
        "insurance_factor": 1.02,
        "tire_set_usd": 860,
        "risk": None,
        "known_issues": [
            "66 complaints on the 2018 and 27 on the 2021, with no dominant "
            "cluster on either. Service brakes lead both (21 and 7).",
            "2 recalls on the 2021, both air bag related. The API returned "
            "none for the 2018.",
            "The related Chevrolet Traverse had a rough 2018 for the "
            "transmission and a 'Shift to Park' fault, so test both on an "
            "early Enclave.",
            "Avenir trims add adaptive dampers and bigger wheels that cost "
            "more to replace.",
        ],
        "note": "The quietest file of GM's three-row crossovers in these "
                "years. A 2020 or later is the comfortable choice.",
    },
    {
        "make": "buick", "model": "enclave",
        "years": (2025, 2026),
        "generation": "third gen",
        "engine": "2.5L turbo I4, 8-speed automatic",
        "reliability": 6.5,
        "maintenance": 7.0,
        "annual_maintenance_usd": 660,
        "insurance_factor": 1.04,
        "tire_set_usd": 920,
        "risk": None,
        "known_issues": [
            "39 complaints on the 2025, led by service brakes (16). The "
            "related 2024-2025 Acadia and Traverse show the same brake-heavy "
            "shape.",
            "The API returned no recalls for the 2025. Ask the dealer "
            "whether a brake bulletin applies to the VIN.",
            "A new engine and transmission for this generation, with no "
            "long-term record yet. Provisional score.",
        ],
        "note": "Too new to call. Quiet and well finished; let the first "
                "years prove the new four-cylinder.",
    },
    {
        "make": "buick", "model": "encore",
        "years": (2015, 2022),
        "generation": "first gen",
        "engine": "1.4L turbo I4, 6-speed automatic; AWD available",
        "reliability": 6.5,
        "maintenance": 7.8,
        "annual_maintenance_usd": 540,
        "insurance_factor": 0.95,
        "tire_set_usd": 640,
        "risk": None,
        "known_issues": [
            "Engine leads the file: 41 of 81 complaints on the 2016 and 33 "
            "of 88 on the 2019. Turbo, coolant leak and PCV faults are the "
            "usual stories.",
            "2 recalls on each of the 2016 and 2019, including 20V668000 "
            "(automatic transmission) on the 2019.",
            "The 2021 is far quieter: 9 complaints and no recalls returned.",
            "Check the coolant level cold and look for oil around the turbo.",
        ],
        "note": "A Chevrolet Trax with a quieter cabin. Late years are sound "
                "cheap transport; early ones need a careful look at the "
                "engine.",
    },
    {
        "make": "buick", "model": "encore gx",
        "years": (2020, 2023),
        "generation": "first gen, before the 2024 facelift",
        "engine": "1.2L or 1.3L turbo I3; CVT on FWD, 9-speed automatic on "
                  "AWD",
        "reliability": 7.2,
        "maintenance": 8.3,
        "annual_maintenance_usd": 460,
        "insurance_factor": 0.96,
        "tire_set_usd": 690,
        "risk": None,
        "known_issues": [
            "The file shrinks each year: 70 complaints on the 2020, 55 on "
            "the 2021 and 34 on the 2022, with no dominant cluster.",
            "2 recalls on the 2020 and 2021, including 20V588000 (brakes) on "
            "both, and 1 on the 2022.",
            "Turbo three-cylinder, so oil service history matters.",
            "AWD cars get the 9-speed automatic in place of the CVT, which "
            "is the better pairing.",
        ],
        "note": "A sound small SUV after a slightly noisy first year. Prefer "
                "2021 or later.",
    },
    {
        "make": "buick", "model": "envision",
        "years": (2016, 2020),
        "generation": "first gen",
        "engine": "2.5L I4 or 2.0L turbo I4; 6-speed automatic, 9-speed on "
                  "the turbo from 2019",
        "reliability": 7.2,
        "maintenance": 7.4,
        "annual_maintenance_usd": 580,
        "insurance_factor": 1.0,
        "tire_set_usd": 740,
        "risk": None,
        "known_issues": [
            "81 complaints on the 2017, led by electrical (25) and service "
            "brakes (23). 23 on the 2019 with no cluster.",
            "4 recalls on the 2017, including 18V358000 (fuel pump). The API "
            "returned none for the 2019.",
            "The 2.0L turbo is the one to want; the base 2.5L is adequate.",
            "Built in China and sold in modest numbers, so some trim and "
            "body parts take longer to source.",
        ],
        "note": "A quiet, comfortable compact SUV with a modest file. Later "
                "years are the better buy.",
    },
]
