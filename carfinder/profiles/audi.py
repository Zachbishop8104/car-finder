"""Reliability profiles: Audi. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

The e-tron SUV was renamed Q8 e-tron for 2024; both names are profiled
because dealer feeds use both.
"""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "audi", "model": "a4",
        "years": (2017, 2025),
        "generation": "B9",
        "engine": "2.0L TFSI turbo I4, 7-speed dual-clutch automatic, FWD or "
                  "quattro",
        "reliability": 7.0,
        "maintenance": 5.0,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.15,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "One recall each on the 2017 and 2018; three each on the 2020 "
            "and 2022.",
            "128 complaints on the 2020, a lopsided file: electrical (91) "
            "and back over prevention (43), which is the screen and rear "
            "camera going blank. Check for a software update.",
            "84 complaints on the 2017, led by air bags (26). NHTSA's "
            "complaints endpoint returned nothing for the 2022, which is an "
            "API gap, not a clean record.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "A short recall list for a German sedan. The 2020 facelift's "
                "screen faults are the one thing to check.",
    },
    {
        "make": "audi", "model": "a4",
        "years": (2015, 2016),
        "generation": "B8 facelift",
        "engine": "2.0L TFSI turbo I4; CVT (FWD) or 8-speed automatic "
                  "(quattro)",
        "reliability": 6.3,
        "maintenance": 5.0,
        "annual_maintenance_usd": 980,
        "insurance_factor": 1.12,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "No recalls came back for the 2015, and 44 complaints, led by "
            "engine (16).",
            "Front-drive cars use a CVT with a poor record. The quattro cars "
            "have a conventional 8-speed automatic and are the ones to buy.",
            "Check oil level and ask how often it needs topping up; earlier "
            "versions of this engine burned oil.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "Dated but decent with quattro. Avoid the front-drive CVT.",
    },
    {
        "make": "audi", "model": "a3",
        "years": (2022, 2026),
        "generation": "8Y",
        "engine": "2.0L TFSI turbo I4 with mild hybrid, 7-speed dual-clutch "
                  "automatic",
        "reliability": 6.8,
        "maintenance": 5.2,
        "annual_maintenance_usd": 850,
        "insurance_factor": 1.1,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2022, the first year, and two on the 2023.",
            "NHTSA's complaints endpoint returned nothing for the 2022 and "
            "2023, which is an API gap, not a clean record.",
            "The dual-clutch gearbox can hesitate from a stop. Drive it in "
            "slow traffic.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "Provisional on the complaint side. It shares its parts with "
                "the Golf, which is a reasonable sign.",
    },
    {
        "make": "audi", "model": "a3",
        "years": (2015, 2020),
        "generation": "8V",
        "engine": "1.8L or 2.0L TFSI turbo I4, 6-speed or 7-speed "
                  "dual-clutch automatic",
        "reliability": 6.5,
        "maintenance": 5.2,
        "annual_maintenance_usd": 850,
        "insurance_factor": 1.1,
        "tire_set_usd": 800,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2015, three on the 2016 and two on the 2018.",
            "Air bags are a lopsided share of complaints on every year "
            "checked: 83 of 180 on the 2015, 52 of 115 on the 2016 and 24 of "
            "44 on the 2018. It is the passenger seat sensor; confirm the "
            "air bag recall is closed.",
            "The dual-clutch gearbox needs its fluid changed on schedule. "
            "Ask for the record.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "A Golf in a suit, with one well-known air bag sensor fault. "
                "Otherwise an average, affordable used Audi.",
    },
    {
        "make": "audi", "model": "a5",
        "years": (2025, 2026),
        "generation": "B10",
        "engine": "2.0L TFSI turbo I4 or 3.0L turbo V6 (S5), 7-speed "
                  "dual-clutch automatic",
        "reliability": 6.4,
        "maintenance": 4.8,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.18,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "Two recalls and one complaint on the 2025, the first year of "
            "this generation.",
            "An all-new platform and electronics. It replaces both the old "
            "A4 and A5, so there is no history yet.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "Provisional: too new and too few on the road for a firm "
                "number.",
    },
    {
        "make": "audi", "model": "a5",
        "years": (2018, 2024),
        "generation": "B9",
        "engine": "2.0L TFSI turbo I4, 7-speed dual-clutch automatic, "
                  "quattro",
        "reliability": 6.9,
        "maintenance": 5.0,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.18,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2018, four on the 2020 and two on the 2022.",
            "60 complaints on the 2020, led by electrical (41) and back over "
            "prevention (15): the same blank screen and rear camera fault as "
            "the 2020 A4. Only nine complaints on the 2018.",
            "On the Sportback, check the powered hatch; on the cabriolet, "
            "run the roof through a full cycle.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "Mechanically an A4, with the same decent record and the "
                "same 2020 screen fault.",
    },
    {
        "make": "audi", "model": "a5",
        "years": (2015, 2017),
        "generation": "8T",
        "engine": "2.0L TFSI turbo I4, 6-speed manual or 8-speed automatic, "
                  "quattro",
        "reliability": 6.4,
        "maintenance": 5.0,
        "annual_maintenance_usd": 980,
        "insurance_factor": 1.18,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "Three recalls and nine complaints on the 2015: a small file for "
            "a car that sold in small numbers.",
            "Check oil level and ask how often it needs topping up; earlier "
            "versions of this engine burned oil.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "An ageing coupe with a short file. Condition and service "
                "history decide whether a given car is a good one.",
    },
    {
        "make": "audi", "model": "q3",
        "years": (2026, 2026),
        "generation": "third gen",
        "engine": "2.0L TFSI turbo I4, 7-speed dual-clutch automatic, "
                  "quattro",
        "reliability": 6.3,
        "maintenance": 5.2,
        "annual_maintenance_usd": 880,
        "insurance_factor": 1.1,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "No NHTSA data was pulled for the 2026, and a redesign has no "
            "history to lean on.",
            "Check the build date and recall status by VIN; first-year cars "
            "collect campaigns in their first months.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "Provisional: scored a little below the outgoing Q3 until a "
                "file builds up.",
    },
    {
        "make": "audi", "model": "q3",
        "years": (2019, 2025),
        "generation": "F3",
        "engine": "2.0L TFSI turbo I4, 8-speed automatic, quattro",
        "reliability": 6.5,
        "maintenance": 5.2,
        "annual_maintenance_usd": 880,
        "insurance_factor": 1.1,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2019, three on the 2020 and five on the "
            "2022.",
            "66 complaints on the 2020, led by electrical (22) and engine "
            "(20); 10 on the 2019. NHTSA's complaints endpoint returned "
            "nothing for the 2022, which is an API gap, not a clean record.",
            "The base engine tune is slow and thirsty for the class. Try the "
            "stronger 45 TFSI version before settling.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "A sensible small luxury SUV with an average file.",
    },
    {
        "make": "audi", "model": "q3",
        "years": (2015, 2018),
        "generation": "8U",
        "engine": "2.0L TFSI turbo I4, 6-speed automatic",
        "reliability": 6.8,
        "maintenance": 5.4,
        "annual_maintenance_usd": 850,
        "insurance_factor": 1.08,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "Three recalls on the 2016 and one on the 2018.",
            "29 complaints on the 2016 and 26 on the 2018, led by electrical "
            "and engine with no lopsided component.",
            "An old design even when new, with a conventional automatic and "
            "few surprises. Check for coolant leaks at the water pump.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "Small and dated, but one of the less troublesome used "
                "Audis.",
    },
    {
        "make": "audi", "model": "q5",
        "years": (2025, 2026),
        "generation": "third gen",
        "engine": "2.0L TFSI turbo I4 with mild hybrid, 7-speed dual-clutch "
                  "automatic, quattro",
        "reliability": 6.3,
        "maintenance": 4.8,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.15,
        "tire_set_usd": 1050,
        "risk": None,
        "known_issues": [
            "One recall on the 2025, the first year of this generation.",
            "49 complaints on the 2025 already, led by forward collision "
            "avoidance (25) and electrical (22).",
            "Check that the driver-assist software is current and try the "
            "automatic braking and cruise on a test drive.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "Too new for a firm number. The early complaints are about "
                "electronics, not the engine.",
    },
    {
        "make": "audi", "model": "q5",
        "years": (2018, 2024),
        "generation": "FY",
        "engine": "2.0L TFSI turbo I4, 7-speed dual-clutch automatic, "
                  "quattro",
        "reliability": 6.8,
        "maintenance": 5.0,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.15,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2018, five on the 2019, eight on the 2021 "
            "and five on the 2023.",
            "209 complaints on the 2018, the first year, led by electrical "
            "(74); 54 on the 2019, 75 on the 2021 and 39 on the 2023.",
            "The plug-in hybrid (55 TFSI e) has campaigns of its own. Check "
            "that VIN separately.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "A steady, popular luxury SUV. Skip the 2018 and the record "
                "is respectable.",
    },
    {
        "make": "audi", "model": "q5",
        "years": (2015, 2017),
        "generation": "8R",
        "engine": "2.0L TFSI turbo I4 or 3.0L supercharged V6, 8-speed "
                  "automatic, quattro",
        "reliability": 6.2,
        "maintenance": 5.0,
        "annual_maintenance_usd": 1000,
        "insurance_factor": 1.12,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2015 and five on the 2016.",
            "100 complaints on the 2015 and 78 on the 2016, with engine the "
            "largest group on both (38 and 26).",
            "Check oil level and ask about oil consumption, and look for "
            "water in the footwells from blocked sunroof drains.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "Comfortable and cheap to buy now. Engine complaints lead "
                "the file, so a full service history matters.",
    },
    {
        "make": "audi", "model": "q7",
        "years": (2020, 2026),
        "generation": "4M facelift",
        "engine": "2.0L turbo I4 or 3.0L turbo V6 with mild hybrid, 8-speed "
                  "automatic, quattro",
        "reliability": 6.4,
        "maintenance": 4.2,
        "annual_maintenance_usd": 1200,
        "insurance_factor": 1.25,
        "tire_set_usd": 1300,
        "risk": None,
        "known_issues": [
            "Five recalls on the 2020 and three each on the 2022 and 2024.",
            "29 complaints on the 2020, led by electrical (11), and two on "
            "the 2024. NHTSA's complaints endpoint returned nothing for the "
            "2022, which is an API gap, not a clean record.",
            "Air suspension, where fitted, is the expensive item as these "
            "age. Check the car sits level.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "A quieter file than the early cars. Running costs are high, "
                "as with any large German SUV.",
    },
    {
        "make": "audi", "model": "q7",
        "years": (2017, 2019),
        "generation": "4M",
        "engine": "2.0L turbo I4 or 3.0L supercharged V6, 8-speed automatic, "
                  "quattro",
        "reliability": 6.0,
        "maintenance": 4.2,
        "annual_maintenance_usd": 1200,
        "insurance_factor": 1.25,
        "tire_set_usd": 1250,
        "risk": None,
        "known_issues": [
            "Seven recalls on the 2017, the first year, and three on the "
            "2018.",
            "324 complaints on the 2017, with exterior lighting a lopsided "
            "share (135): the LED headlights flicker or fail. Engine is next "
            "(61). The 2018 has 145.",
            "Check both headlights on low and high beam, and ask whether "
            "they have been replaced; the units are expensive.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "The first years of this generation carry the long file. A "
                "2019 or later is the better buy. There was no 2016 model "
                "year.",
    },
    {
        "make": "audi", "model": "q7",
        "years": (2015, 2015),
        "generation": "4L",
        "engine": "3.0L supercharged V6 or 3.0L TDI diesel, 8-speed "
                  "automatic, quattro",
        "reliability": 5.8,
        "maintenance": 4.0,
        "annual_maintenance_usd": 1300,
        "insurance_factor": 1.2,
        "tire_set_usd": 1200,
        "risk": None,
        "known_issues": [
            "Two recalls and 46 complaints on the 2015, led by engine (13) "
            "and fuel system (8).",
            "The last year of a design from 2007. TDI diesels were part of "
            "the emissions settlement; confirm the fix.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "Old, heavy and thirsty. Only with a full history and a low "
                "price.",
    },
    {
        "make": "audi", "model": "q8",
        "years": (2019, 2026),
        "generation": "first gen",
        "engine": "3.0L turbo V6 with 48-volt mild hybrid, 8-speed "
                  "automatic, quattro",
        "reliability": 6.2,
        "maintenance": 4.0,
        "annual_maintenance_usd": 1300,
        "insurance_factor": 1.3,
        "tire_set_usd": 1500,
        "risk": None,
        "known_issues": [
            "Five recalls on the 2019, the first year, and three each on the "
            "2020, 2022 and 2024.",
            "111 complaints on the 2019, led by power train (44) and "
            "electrical (44); 28 on the 2020 and 26 on the 2024.",
            "Big wheels mean expensive tires, and the 48-volt system and air "
            "suspension are the costly items out of warranty.",
            "Audi parts and labour are priced like other German luxury "
            "brands. Water pump and thermostat housing leaks on the 2.0T are "
            "the routine repair; an independent VW and Audi specialist keeps "
            "bills down.",
        ],
        "note": "A Q7 in a sharper suit. Avoid the 2019 and the record is "
                "fair for the class.",
    },
    {
        "make": "audi", "model": "e-tron",
        "years": (2019, 2023),
        "generation": "first gen (SUV and Sportback)",
        "engine": "dual-motor AWD; 95 kWh battery",
        "reliability": 6.0,
        "maintenance": 4.2,
        "annual_maintenance_usd": 600,
        "insurance_factor": 1.3,
        "tire_set_usd": 1300,
        "risk": None,
        "known_issues": [
            "Five recalls on the 2019, 10 across the 2021 e-tron and "
            "Sportback, and six on the 2022.",
            "84 complaints on the 2019, led by electrical (37), with three "
            "fires reported; 41 on the 2021, again led by electrical (29).",
            "Range is short for the battery size and it charges best on DC "
            "fast chargers. Check real range against your commute.",
            "Servicing is light for an Audi, but air suspension is standard "
            "and crash repair is expensive. Battery warranty is 8 years or "
            "100,000 miles.",
        ],
        "note": "Comfortable and well built, with a modest range and a "
                "middling electrical file. There was no 2020 e-tron SUV.",
    },
    {
        "make": "audi", "model": "q8 e-tron",
        "years": (2024, 2025),
        "generation": "first gen, renamed and updated",
        "engine": "dual-motor AWD; 114 kWh battery",
        "reliability": 6.4,
        "maintenance": 4.2,
        "annual_maintenance_usd": 600,
        "insurance_factor": 1.3,
        "tire_set_usd": 1350,
        "risk": None,
        "known_issues": [
            "One recall and one complaint on the 2024: a very small file for "
            "a car that sold in small numbers.",
            "It is the e-tron with a bigger battery and better range, so the "
            "earlier car's electrical record is the best guide.",
            "Servicing is light, but air suspension is standard and crash "
            "repair is expensive. Battery warranty is 8 years or 100,000 "
            "miles.",
        ],
        "note": "Provisional on a small file. Discontinued after 2025, so "
                "check parts and dealer support near you.",
    },
    {
        "make": "audi", "model": "q4 e-tron",
        "years": (2022, 2026),
        "generation": "first gen",
        "engine": "single-motor RWD or dual-motor AWD; about 82 kWh battery",
        "reliability": 5.9,
        "maintenance": 5.0,
        "annual_maintenance_usd": 450,
        "insurance_factor": 1.2,
        "tire_set_usd": 1100,
        "risk": None,
        "known_issues": [
            "Five recalls on the 2022 and four each on the 2023 and 2024.",
            "22 complaints on the 2024, with electrical a lopsided share "
            "(15). NHTSA's complaints endpoint returned nothing for the 2022 "
            "and 2023, which is an API gap, not a clean record.",
            "It shares its platform and software with the Volkswagen ID.4, "
            "whose file is about half electrical complaints.",
            "Servicing is cheap (no oil changes). Battery warranty is 8 "
            "years or 100,000 miles; check the software version and the "
            "12-volt battery date.",
        ],
        "note": "An ID.4 with a nicer cabin and the same electrical weak "
                "spot. Cheap to run; buy with every update done.",
    },
]
