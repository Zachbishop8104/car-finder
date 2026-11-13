"""Reliability profiles: Dodge. The format and the caveats on reading
these numbers are in carfinder/reliability.py."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    {
        "make": "dodge", "model": "charger",
        "years": (2015, 2023),
        "generation": "LD seventh gen, facelifted",
        "engine": "3.6L Pentastar V6, or 5.7L, 6.4L and supercharged "
                  "6.2L Hemi V8, 8-speed automatic",
        "reliability": 6.8,
        "maintenance": 7.0,
        "annual_maintenance_usd": 680,
        "insurance_factor": 1.3,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "Six recalls on the 2016, five on the 2019 and two each "
            "on the 2021 and 2023. A short list for a nine-year run.",
            "Complaint files are small: 182 on the 2016, 120 on the "
            "2019 (49 of them air bags) and 35 on the 2021.",
            "It is one of the most stolen cars in the US, which is "
            "why insurance is high. Get a quote before you commit.",
            "On a 5.7L, listen for a steady lifter tick at cold "
            "idle. On any V8, assume hard use and check tires, "
            "brakes and the rear differential.",
        ],
        "note": "An old platform with its faults long since worked "
                "out. The V6 is a sound, cheap-to-fix big sedan; the "
                "cost is insurance.",
    },
    {
        "make": "dodge", "model": "charger",
        "years": (2024, 2026),
        "generation": "eighth gen (Daytona electric, Sixpack gas "
                      "from 2026)",
        "engine": "Dual-motor electric AWD with a 100 kWh battery, or "
                  "3.0L Hurricane twin turbo I6 from 2026",
        "reliability": 4.8,
        "maintenance": 4.8,
        "annual_maintenance_usd": 600,
        "insurance_factor": 1.35,
        "tire_set_usd": 1300,
        "risk": "Three recalls on the 2025 electric car, including "
                "loss of the park function (25V574000), and "
                "electrical is 29 of its 43 complaints (67%)",
        "known_issues": [
            "NHTSA files the electric car as Charger EV: three "
            "recalls on both the 2024 and 2025, covering the "
            "instrument cluster, a backup warning and the park pawl.",
            "43 complaints on the 2025 with electrical at 29: "
            "software faults, warning lights and loss of drive.",
            "EV: confirm it charges at home and on a DC fast "
            "charger, and that the battery warranty transfers.",
            "The gas Sixpack is new for 2026 and has almost no file "
            "yet (one recall, three complaints).",
        ],
        "note": "Provisional. A new platform, a first electric "
                "drivetrain and an early file that is mostly "
                "electrical. Lease it or wait.",
    },
    {
        "make": "dodge", "model": "challenger",
        "years": (2015, 2023),
        "generation": "LA third gen, facelifted",
        "engine": "3.6L Pentastar V6, or 5.7L, 6.4L and supercharged "
                  "6.2L Hemi V8, 8-speed automatic or 6-speed manual",
        "reliability": 7.0,
        "maintenance": 7.0,
        "annual_maintenance_usd": 680,
        "insurance_factor": 1.3,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "Two recalls on the 2016, three on the 2019 and two each "
            "on the 2021 and 2023.",
            "Complaint files are small and spread out: 78 on the "
            "2016, 58 on the 2019, 19 on the 2021.",
            "A top theft target, so insurance is expensive. Quote "
            "it first, especially for V8 trims.",
            "Check for signs of track or drag use: uneven rear tire "
            "wear, clutch slip on manuals, and aftermarket tunes.",
        ],
        "note": "The cleanest record in the Dodge range. Simple, "
                "heavy and proven; the V6 is cheap to run and the "
                "V8s are honest about what they cost.",
    },
    {
        "make": "dodge", "model": "durango",
        "years": (2015, 2020),
        "generation": "WD third gen",
        "engine": "3.6L Pentastar V6 or 5.7L Hemi V8, 8-speed "
                  "automatic",
        "reliability": 6.2,
        "maintenance": 6.6,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.06,
        "tire_set_usd": 920,
        "risk": None,
        "known_issues": [
            "Three recalls on the 2016 and five on the 2018, "
            "including two brake campaigns on the 2018 (22V426000, "
            "24V838000).",
            "234 complaints on the 2018: electrical 88 and exterior "
            "lighting 57. The full-width LED tail lamp fills with "
            "water and fails.",
            "Check the tail lamp for moisture and dead segments, "
            "and the rear air conditioning lines for leaks.",
            "On the 5.7L, listen for a lifter tick at cold idle. "
            "The V6 is the lower-risk engine.",
        ],
        "note": "A solid three-row with real towing ability. Faults "
                "are mostly lighting and electrical, not "
                "drivetrain.",
    },
    {
        "make": "dodge", "model": "durango",
        "years": (2021, 2026),
        "generation": "WD third gen, facelift",
        "engine": "3.6L Pentastar V6, or 5.7L, 6.4L and supercharged "
                  "6.2L Hemi V8, 8-speed automatic",
        "reliability": 6.0,
        "maintenance": 6.5,
        "annual_maintenance_usd": 780,
        "insurance_factor": 1.1,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "Eight recalls on the 2021 and two on the 2023, "
            "including two on the liftgate (23V115000, 26V528000).",
            "208 complaints on the 2021 with exterior lighting at 94 "
            "(45%): the same tail lamp failure as earlier years.",
            "The 2023 is quieter at 39 complaints, still led by "
            "exterior lighting (15).",
            "V8 trims are theft targets and cost more to insure. "
            "Quote before you buy.",
        ],
        "note": "An aging design that is still decent value. Budget "
                "for a tail lamp and check the recalls; the "
                "mechanical parts are proven.",
    },
    {
        "make": "dodge", "model": "hornet",
        "years": (2023, 2025),
        "generation": "first gen (Alfa Romeo Tonale based)",
        "engine": "2.0L turbo I4 with 9-speed automatic (GT), or 1.3L "
                  "turbo plug-in hybrid with 6-speed automatic (R/T); "
                  "AWD",
        "reliability": 4.9,
        "maintenance": 5.2,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.1,
        "tire_set_usd": 850,
        "risk": "Seven recalls on the 2024, including a brake pedal "
                "that can collapse (24V752000) and a high-voltage "
                "cable campaign on the plug-in (23V623000)",
        "known_issues": [
            "Five recalls on the 2023 and seven on the 2024, a lot "
            "for a low-volume car in its first two years.",
            "Complaint files are small (26 on the 2023, 31 on the "
            "2024), led by collision-avoidance false alarms and "
            "electrical faults.",
            "R/T plug-in: about 30 miles of electric range, and "
            "high-voltage repairs are dealer-only. Confirm the "
            "battery warranty transfers.",
            "Built in Italy and discontinued after 2025, so expect "
            "slow parts and steep depreciation.",
        ],
        "note": "Quick and good-looking, but a short-lived model "
                "with a recall list out of proportion to its sales. "
                "Only at a deep discount.",
    },
    {
        "make": "dodge", "model": "journey",
        "years": (2015, 2020),
        "generation": "JC first gen",
        "engine": "2.4L World I4 with 4-speed automatic, or 3.6L "
                  "Pentastar V6 with 6-speed automatic",
        "reliability": 5.4,
        "maintenance": 7.4,
        "annual_maintenance_usd": 640,
        "insurance_factor": 1.0,
        "tire_set_usd": 680,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2016 and one on the 2019.",
            "389 complaints on the 2016: engine 114, power train 87, "
            "electrical 85. The 2019 is down to 103.",
            "The four-cylinder with the 4-speed automatic is slow "
            "and strained. The V6 is the better car in every way.",
            "Front brakes wear quickly, and the key fob and "
            "ignition module cause no-start faults. Test both keys.",
        ],
        "note": "A dated design sold on price. Tolerable as cheap "
                "family transport with the V6; do not expect "
                "refinement or resale.",
    },
    {
        "make": "dodge", "model": "grand caravan",
        "years": (2015, 2020),
        "generation": "RT fifth gen",
        "engine": "3.6L Pentastar V6, 6-speed automatic",
        "reliability": 5.6,
        "maintenance": 7.6,
        "annual_maintenance_usd": 650,
        "insurance_factor": 0.97,
        "tire_set_usd": 640,
        "risk": "The 62TE 6-speed automatic is the weak point, and "
                "power train is 251 of 1,159 complaints on the 2016",
        "known_issues": [
            "Six recalls on the 2016 and four on the 2019.",
            "1,159 complaints on the 2016: electrical 354, power "
            "train 251, structure 234. The 2019 has 48.",
            "Check transmission fluid condition and for harsh or "
            "slipping shifts, especially on ex-fleet and rental "
            "vans.",
            "Look for an oil leak from the filter housing on top of "
            "the engine, and for rust on the rocker panels and "
            "sliding door tracks.",
        ],
        "note": "The cheapest way into a minivan, and every shop "
                "knows it. Later years are better; buy on "
                "transmission condition.",
    },
    {
        "make": "dodge", "model": "dart",
        "years": (2015, 2016),
        "generation": "PF first gen",
        "engine": "2.0L or 2.4L Tigershark I4 with 6-speed automatic, "
                  "or 1.4L turbo with dual-clutch automatic",
        "reliability": 4.6,
        "maintenance": 6.4,
        "annual_maintenance_usd": 700,
        "insurance_factor": 1.02,
        "tire_set_usd": 600,
        "risk": "Power train is 186 of 534 complaints on the 2015, "
                "and two recalls cover a shifter cable that detaches "
                "from the transmission (19V293000, 25V674000)",
        "known_issues": [
            "Six recalls on the 2015 and five on the 2016.",
            "534 complaints on the 2015: power train 186, engine "
            "141, electrical 118.",
            "Avoid the 1.4L turbo with the dual-clutch automatic. "
            "It shudders at low speed and is costly to put right.",
            "The 2.4L burns oil. Check the level before the test "
            "drive, and confirm both shifter cable recalls are "
            "closed.",
        ],
        "note": "Avoid unless it is very cheap and has the 2.4L with "
                "the conventional automatic. Discontinued after "
                "2016 for good reason.",
    },
]
