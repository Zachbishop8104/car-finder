"""Reliability profiles: Tesla. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

Tesla recall counts need care. A campaign is still opened per defect,
but most Tesla campaigns are closed by an over-the-air software update,
so a count of 20 does not mean 20 shop visits. NHTSA's complaints
endpoint also returned nothing for Model S, Model X and most Model Y
years while returning full files for Model 3; those profiles lean on
recalls and are marked provisional.

All of these are EVs: annual_maintenance_usd is low because there is
little to service, while insurance_factor and tire_set_usd are high
because crash repair is costly and heavy cars wear tires quickly.
"""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "tesla", "model": "model 3",
        "years": (2017, 2023),
        "generation": "first gen, before the 2024 refresh",
        "engine": "single-motor RWD or dual-motor AWD; roughly 50 to 82 kWh "
                  "battery",
        "reliability": 6.6,
        "maintenance": 5.6,
        "annual_maintenance_usd": 330,
        "insurance_factor": 1.25,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "22 recalls on the 2021 and 19 on the 2018. Most Tesla recall "
            "campaigns are closed by an over-the-air software update with no "
            "shop visit, so the raw count overstates the trouble next to a "
            "Ford or Volkswagen number.",
            "Forward collision avoidance is the top complaint component on "
            "the 2021 (411 of 677): unexpected braking on Autopilot and "
            "cruise. Test it on a highway drive.",
            "Suspension is second on the 2018 (194 of 1,039). Front upper "
            "control arms creak and wear; listen over speed bumps at low "
            "speed.",
            "Almost no routine servicing, but body repair is slow and costly "
            "and insurers price that in. Check what is left of the 8-year "
            "battery and drive unit warranty (100,000 or 120,000 miles by "
            "version).",
        ],
        "note": "Cheap to run and the drivetrain has held up. The weak "
                "points are build quality, suspension wear and the cost of "
                "fixing one after a crash.",
    },
    {
        "make": "tesla", "model": "model 3",
        "years": (2024, 2026),
        "generation": "refresh (Highland)",
        "engine": "single-motor RWD or dual-motor AWD; roughly 60 to 82 kWh "
                  "battery",
        "reliability": 7.2,
        "maintenance": 5.6,
        "annual_maintenance_usd": 320,
        "insurance_factor": 1.25,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "Five recalls on the 2024 and three on the 2025 so far, against "
            "22 on the 2021. Most Tesla recall campaigns are closed by an "
            "over-the-air software update with no shop visit, so the raw "
            "count overstates the trouble next to a Ford or Volkswagen "
            "number.",
            "224 complaints on the 2024 with no lopsided component: forward "
            "collision avoidance (49), electrical (47) and steering (40) "
            "lead.",
            "The refresh moved the turn signals to steering-wheel buttons "
            "and the gear selector to the screen. Drive one before you "
            "commit.",
            "Servicing is minimal, but crash repair still runs through a "
            "small approved-shop network, which keeps insurance above a "
            "Camry or Accord.",
        ],
        "note": "The better-built Model 3: quieter, fewer campaigns and the "
                "same low running costs. Insurance is the main cost to "
                "check.",
    },
    {
        "make": "tesla", "model": "model y",
        "years": (2020, 2024),
        "generation": "first gen, before the 2025 refresh",
        "engine": "single-motor RWD or dual-motor AWD; roughly 60 to 81 kWh "
                  "battery",
        "reliability": 6.5,
        "maintenance": 5.6,
        "annual_maintenance_usd": 340,
        "insurance_factor": 1.25,
        "tire_set_usd": 1050,
        "risk": None,
        "known_issues": [
            "23 recalls on the 2021 and 17 on the 2023. Most Tesla recall "
            "campaigns are closed by an over-the-air software update with no "
            "shop visit, so the raw count overstates the trouble next to a "
            "Ford or Volkswagen number.",
            "NHTSA's complaints endpoint returned nothing for the 2021 and "
            "2023. That is an API gap, not a clean record, so this score "
            "leans on recalls and on the closely related Model 3.",
            "2020 and 2021 builds had the roughest panel fit and paint. "
            "Check door and hatch gaps, and look for water in the trunk "
            "well.",
            "Servicing is minimal, but tires wear quickly on a heavy AWD car "
            "and body repair is costly.",
        ],
        "note": "Provisional on the complaint side. Mechanically close to "
                "the Model 3: cheap to run, uneven build quality, costly to "
                "repair after a crash.",
    },
    {
        "make": "tesla", "model": "model y",
        "years": (2025, 2026),
        "generation": "refresh (Juniper); some 2025s are the old body",
        "engine": "single-motor RWD or dual-motor AWD; roughly 60 to 82 kWh "
                  "battery",
        "reliability": 6.9,
        "maintenance": 5.6,
        "annual_maintenance_usd": 330,
        "insurance_factor": 1.25,
        "tire_set_usd": 1050,
        "risk": None,
        "known_issues": [
            "Three recalls on the 2025 and already eight on the 2026. Most "
            "Tesla recall campaigns are closed by an over-the-air software "
            "update with no shop visit, so the raw count overstates the "
            "trouble next to a Ford or Volkswagen number.",
            "115 complaints on the 2025, led by forward collision avoidance "
            "(50) and lane departure (23): driver-assist behaviour, not "
            "hardware.",
            "The 2025 model year covers both the old and the refreshed body. "
            "Confirm which one a listing is from the photos (full-width "
            "light bar front and rear on the new one).",
            "Servicing is minimal; insurance and tires are the real costs.",
        ],
        "note": "Too new for a firm number. The early signs match the "
                "refreshed Model 3, but eight campaigns on the 2026 is worth "
                "watching.",
    },
    {
        "make": "tesla", "model": "model s",
        "years": (2015, 2020),
        "generation": "first gen, before the 2021 interior refresh",
        "engine": "single-motor RWD or dual-motor AWD; 60 to 100 kWh battery",
        "reliability": 5.3,
        "maintenance": 4.4,
        "annual_maintenance_usd": 600,
        "insurance_factor": 1.35,
        "tire_set_usd": 1300,
        "risk": "Out of warranty these cars can need a touchscreen computer, "
                "air suspension parts or a drive unit, each a four-figure "
                "repair",
        "known_issues": [
            "10 recalls on the 2016 and 11 on the 2018, including Tesla's "
            "campaign for the touchscreen computer whose memory wears out. "
            "Confirm that one has been done.",
            "NHTSA's complaints endpoint returned nothing for these years: "
            "an API gap, not a clean record.",
            "Retracting door handles and air suspension are the common "
            "repeat repairs. Work every handle and check the car sits level.",
            "The 8-year battery and drive unit warranty has expired or is "
            "close to it on most of these. Get a battery health reading "
            "before buying.",
        ],
        "note": "Provisional. A lot of car for the money, but an old Model S "
                "is bought on the strength of its battery report and its "
                "repair history.",
    },
    {
        "make": "tesla", "model": "model s",
        "years": (2021, 2026),
        "generation": "interior refresh (Long Range, Plaid)",
        "engine": "dual or tri-motor AWD; roughly 100 kWh battery",
        "reliability": 6.1,
        "maintenance": 4.4,
        "annual_maintenance_usd": 520,
        "insurance_factor": 1.4,
        "tire_set_usd": 1500,
        "risk": None,
        "known_issues": [
            "20 recalls on the 2022 and six on the 2024. Most Tesla recall "
            "campaigns are closed by an over-the-air software update with no "
            "shop visit, so the raw count overstates the trouble next to a "
            "Ford or Volkswagen number.",
            "NHTSA's complaints endpoint returned nothing for these years: "
            "an API gap, not a clean record.",
            "Many 2021 to 2022 cars have the yoke steering wheel. Check "
            "which wheel is fitted and whether you can live with it.",
            "Plaid cars go through rear tires and brakes quickly, and "
            "insurance is priced for a very fast, very expensive-to-repair "
            "car.",
        ],
        "note": "Provisional. Newer hardware than the early cars and still "
                "under battery warranty, but repair and insurance costs are "
                "luxury-car level.",
    },
    {
        "make": "tesla", "model": "model x",
        "years": (2016, 2020),
        "generation": "first gen, before the 2021 interior refresh",
        "engine": "dual-motor AWD; 60 to 100 kWh battery",
        "reliability": 4.7,
        "maintenance": 4.0,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.4,
        "tire_set_usd": 1400,
        "risk": "Falcon-wing doors, front half shafts and air suspension are "
                "repeat repairs, and all of it is Tesla-only work",
        "known_issues": [
            "10 recalls on the 2017 and eight on the 2019. Most Tesla recall "
            "campaigns are closed by an over-the-air software update with no "
            "shop visit, so the raw count overstates the trouble next to a "
            "Ford or Volkswagen number.",
            "NHTSA's complaints endpoint returned nothing for these years: "
            "an API gap, not a clean record.",
            "Open and close both falcon-wing doors several times, and "
            "accelerate hard from a stop to feel for front-end shudder (worn "
            "half shafts).",
            "The battery and drive unit warranty has expired or is close to "
            "it on most of these. Get a battery health reading before "
            "buying.",
        ],
        "note": "Provisional. The least dependable Tesla of its era: the "
                "doors and the front driveline are the reasons.",
    },
    {
        "make": "tesla", "model": "model x",
        "years": (2021, 2026),
        "generation": "interior refresh (Long Range, Plaid)",
        "engine": "dual or tri-motor AWD; roughly 100 kWh battery",
        "reliability": 5.6,
        "maintenance": 4.0,
        "annual_maintenance_usd": 600,
        "insurance_factor": 1.45,
        "tire_set_usd": 1500,
        "risk": None,
        "known_issues": [
            "22 recalls on the 2022 and eight on the 2024. Most Tesla recall "
            "campaigns are closed by an over-the-air software update with no "
            "shop visit, so the raw count overstates the trouble next to a "
            "Ford or Volkswagen number.",
            "NHTSA's complaints endpoint returned nothing for these years: "
            "an API gap, not a clean record.",
            "The falcon-wing doors are still the part most likely to need "
            "adjustment. Check the seals and that both doors close flush.",
            "Tires for the staggered 20 or 22 inch wheels are expensive and "
            "wear fast on a car this heavy.",
        ],
        "note": "Provisional. Better than the early cars, but still the most "
                "complex Tesla and the one with the longest recall list.",
    },
    {
        "make": "tesla", "model": "cybertruck",
        "years": (2024, 2026),
        "generation": "first gen",
        "engine": "dual or tri-motor AWD (single-motor RWD from 2025); about "
                  "123 kWh battery",
        "reliability": 4.8,
        "maintenance": 3.8,
        "annual_maintenance_usd": 550,
        "insurance_factor": 1.5,
        "tire_set_usd": 1800,
        "risk": "Eleven recalls on the 2024, its first model year, and "
                "several are physical faults (body trim, structure, "
                "lighting) that need a shop visit, not a software update",
        "known_issues": [
            "Eleven recalls on the 2024 and three on the 2025. Unlike most "
            "Tesla campaigns, a good share of these needed hands-on repair.",
            "179 complaints on the 2024, led by electrical (56) and "
            "structure (37), with two fires reported.",
            "Stainless panels cannot be filled and repainted like steel. Few "
            "shops repair them, so a small dent can mean a new panel.",
            "Servicing is minimal, but 35-inch tires on a truck this heavy "
            "are expensive and insurers quote it well above other pickups.",
        ],
        "note": "A first-year design with a heavy physical recall list and "
                "costly body repair. Buy it because you want it, not because "
                "it is sensible.",
    },
]
