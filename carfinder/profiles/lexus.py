"""Reliability profiles: Lexus. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

NHTSA files Lexus by badge ("RX350", "RX 350", "ES 300H") rather than
by model line, and the spelling changes from year to year. Counts
quoted here name the badge they were pulled under. Several lookups
came back empty or split across badges, so Lexus files are thinner
than they should be: read low counts as "little data", not "clean".

Lexus also sells few cars next to Toyota, so complaint totals are
small everywhere. The scores lean on the Toyota hardware each model
shares and on the recall campaigns that name it."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    # ---- RX ----------------------------------------------------------
    {
        # "RX 350" 2023: 66 complaints. 2024: 62 complaints.
        # "RX" 2023: 3 recalls.
        "make": "lexus", "model": "rx",
        "years": (2023, 2026),
        "generation": "AL30 fifth gen",
        "engine": "RX 350: 2.4L turbo I4 with 8-speed automatic. RX "
                  "350h: 2.5L hybrid. Also the 450h+ plug-in and the "
                  "500h turbo hybrid",
        "reliability": 7.9,
        "maintenance": 7.6,
        "annual_maintenance_usd": 560,
        "insurance_factor": 1.08,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "The RX 350 badge has 66 complaints on the 2023 and 62 on "
            "the 2024. Power train (13) and engine (11) lead the 2023; "
            "electrical leads the 2024 (19).",
            "Three recalls on the 2023, including 25V040000 (steering "
            "column) and two rear camera campaigns. On a 2024 also "
            "confirm 24V482000 (front head restraints).",
            "The turbo four replaced a V6 with a very long record. The "
            "RX 350h uses the proven 2.5L hybrid and is the safer "
            "choice.",
        ],
        "note": "Still a good luxury SUV, but no longer the automatic "
                "pick the V6 car was. Choose the 350h.",
    },
    {
        # "RX350" 2017: 3 recalls, 94 complaints. "RX 350" 2020: 55
        # complaints (air bags 21).
        "make": "lexus", "model": "rx",
        "years": (2016, 2022),
        "generation": "AL20 fourth gen",
        "engine": "3.5L 2GR-FKS V6 with 8-speed automatic; RX 450h "
                  "pairs a 3.5L V6 with hybrid motors",
        "reliability": 8.8,
        "maintenance": 8.0,
        "annual_maintenance_usd": 540,
        "insurance_factor": 1.05,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "94 complaints on the 2017 RX350 with service brakes (20) "
            "and engine (16) on top but no dominant cluster; 55 on the "
            "2020 with air bags leading (21).",
            "On 2017-2019 cars confirm the fuel pump recalls "
            "(20V012000, 20V682000); on 2020-2021 cars the passenger "
            "occupant sensor (23V865000).",
            "The 8-speed can feel hesitant at low speed. That is how "
            "it is tuned, not a fault, but check you can live with it.",
            "The touchpad infotainment is awkward. Later cars gained "
            "a touchscreen.",
        ],
        "note": "The safe choice in used luxury SUVs. The 450h is "
                "just as durable and uses much less fuel.",
    },
    {
        # "RX350" 2015: 1 recall, 63 complaints.
        "make": "lexus", "model": "rx",
        "years": (2015, 2015),
        "generation": "AL10 third gen, final year",
        "engine": "3.5L 2GR-FE V6 with 6-speed automatic; RX 450h "
                  "hybrid optional",
        "reliability": 9.0,
        "maintenance": 8.2,
        "annual_maintenance_usd": 520,
        "insurance_factor": 1.03,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "One recall on the 2015 RX350 (14V576000, a fuel line) "
            "and 63 complaints with no dominant component.",
            "The port-injected V6 and 6-speed automatic are among the "
            "most durable drivetrains Toyota has built.",
            "At this age look for oil seeping at the timing cover and "
            "for worn suspension bushings.",
        ],
        "note": "Old, plain and very hard to wear out. Buy on service "
                "records.",
    },
    # ---- NX ----------------------------------------------------------
    {
        # "NX" 2022: 3 recalls, 16 complaints. "NX" 2024: 5 recalls.
        # "NX 250" 2023: 17 complaints.
        "make": "lexus", "model": "nx",
        "years": (2022, 2026),
        "generation": "AZ20 second gen",
        "engine": "NX 250: 2.5L I4. NX 350: 2.4L turbo I4. NX 350h: "
                  "2.5L hybrid. NX 450h+: plug-in hybrid",
        "reliability": 8.2,
        "maintenance": 7.8,
        "annual_maintenance_usd": 520,
        "insurance_factor": 1.06,
        "tire_set_usd": 880,
        "risk": None,
        "known_issues": [
            "Five recalls listed on the 2024 and three on the 2022, "
            "mostly rear camera software and the instrument cluster "
            "(26V687000). Electronics, not mechanical parts.",
            "Complaint counts are small (16 on the 2022, 17 on the "
            "2023 NX 250) with nothing standing out.",
            "It is a RAV4 underneath. The 250 and 350h share that "
            "car's proven engines; the 350's turbo four is newer.",
            "Electronic door latches and a touchscreen for nearly "
            "everything. Try both before you commit.",
        ],
        "note": "A sound small luxury SUV. The 350h is the one to "
                "have for both economy and record.",
    },
    {
        # "NX200T" 2016: 0 recalls, 24 complaints. "NX300" 2019: 1
        # recall, 36 complaints.
        "make": "lexus", "model": "nx",
        "years": (2015, 2021),
        "generation": "AZ10 first gen",
        "engine": "NX 200t / NX 300: 2.0L turbo I4 with 6-speed "
                  "automatic. NX 300h: 2.5L hybrid",
        "reliability": 8.6,
        "maintenance": 8.0,
        "annual_maintenance_usd": 520,
        "insurance_factor": 1.05,
        "tire_set_usd": 850,
        "risk": None,
        "known_issues": [
            "No recalls and 24 complaints on the 2016 NX200T; one "
            "recall and 36 complaints on the 2019 NX300.",
            "Fuel system is the top complaint on the 2019 (9 of 36) "
            "and the one recall is the fuel pump (20V682000). Confirm "
            "it is done.",
            "The 2.0L turbo is direct and port injected and has aged "
            "well. The 300h is slower and even more durable.",
        ],
        "note": "A low-drama used luxury SUV. Small inside; check the "
                "cargo area suits you.",
    },
    # ---- ES ----------------------------------------------------------
    {
        # NHTSA returned nothing for the 2026 ES.
        "make": "lexus", "model": "es",
        "years": (2026, 2026),
        "generation": "eighth gen",
        "engine": "ES 350h: 2.5L hybrid. ES 350e and ES 500e: battery "
                  "electric",
        "reliability": 7.8,
        "maintenance": 7.8,
        "annual_maintenance_usd": 470,
        "insurance_factor": 1.05,
        "tire_set_usd": 880,
        "risk": None,
        "known_issues": [
            "First year of a full redesign, and NHTSA had nothing on "
            "file for it when this was written. Too new to judge.",
            "No V6 any more. The hybrid uses Toyota's long-proven "
            "2.5L system; the electric versions are new ground for "
            "the ES.",
            "On the electric cars routine upkeep is cheaper, and "
            "battery and charging faults are the costs to watch.",
        ],
        "note": "Provisional score. If you want the ES for its "
                "record, that record belongs to the 2019-2025 car.",
    },
    {
        # "ES 350" 2019: 33 complaints. 2023: 11. 2024: 9.
        # "ES" 2019: 1 recall. "ES" 2020: 1 recall, 18 complaints.
        "make": "lexus", "model": "es",
        "years": (2019, 2025),
        "generation": "XZ10 seventh gen",
        "engine": "ES 350: 3.5L V6 with 8-speed automatic. ES 300h: "
                  "2.5L hybrid. ES 250: 2.5L I4 with AWD, from 2021",
        "reliability": 9.1,
        "maintenance": 8.5,
        "annual_maintenance_usd": 480,
        "insurance_factor": 1.02,
        "tire_set_usd": 800,
        "risk": None,
        "known_issues": [
            "Small files throughout: 33 complaints on the 2019 ES 350, "
            "11 on the 2023, 9 on the 2024, and no recalls returned "
            "for 2022 onward.",
            "Fuel system leads the 2019 complaints (12 of 33). On "
            "2019-2020 cars ask the dealer to confirm the fuel pump "
            "recall status for the VIN.",
            "Also on the 2019: recall 19V288000 (knee airbag).",
            "The ES 250 AWD is slow. The 300h does 44 mpg and is the "
            "one most owners are happiest with.",
        ],
        "note": "A Camry and Avalon in a better suit, with the same "
                "running costs. One of the lowest-risk luxury cars "
                "you can buy used.",
    },
    {
        # "ES350" 2015: 1 recall, 16 complaints. 2017: 1 recall, 22.
        "make": "lexus", "model": "es",
        "years": (2015, 2018),
        "generation": "XV60 sixth gen",
        "engine": "ES 350: 3.5L 2GR-FE V6 with 6-speed automatic. ES "
                  "300h: 2.5L hybrid",
        "reliability": 9.3,
        "maintenance": 8.6,
        "annual_maintenance_usd": 470,
        "insurance_factor": 1.0,
        "tire_set_usd": 760,
        "risk": None,
        "known_issues": [
            "One recall and 16 complaints on the 2015 ES350; one "
            "recall and 22 complaints on the 2017.",
            "The 2017 recall is 17V415000 (a steering tie rod). The "
            "2015 one covers the pre-collision braking system "
            "(15V728000). Confirm whichever applies.",
            "Same V6 and 6-speed as the Avalon of the time. Nothing "
            "in the data points at either.",
        ],
        "note": "About as dependable as a luxury sedan gets. Soft, "
                "quiet and uneventful to own.",
    },
    # ---- GX ----------------------------------------------------------
    {
        # "GX 550" 2024: 20 complaints. 2025: 13 complaints. The
        # recall lookup returned nothing under this badge.
        "make": "lexus", "model": "gx",
        "years": (2024, 2026),
        "generation": "J250 third gen",
        "engine": "GX 550: 3.4L twin-turbo V6 (V35A-FTS) with "
                  "10-speed automatic; full-time 4WD",
        "reliability": 6.6,
        "maintenance": 6.8,
        "annual_maintenance_usd": 680,
        "insurance_factor": 1.12,
        "tire_set_usd": 1050,
        "risk": "Uses the same twin-turbo V6 family as the Toyota "
                "Tundra, which Toyota has recalled for main bearing "
                "failure caused by machining debris",
        "known_issues": [
            "20 complaints on the 2024 GX 550, with engine and "
            "electrical tied on top (5 each); 13 on the 2025.",
            "The recall lookup returned nothing under the GX 550 "
            "badge. Given how Lexus is filed, that is not proof there "
            "are none: have a dealer run the VIN.",
            "Ask specifically whether the engine is covered by, or "
            "has been replaced under, Toyota's V35A engine recalls.",
            "Replaces a V8 with one of the best records of any "
            "engine. This one has to earn that.",
        ],
        "note": "A far better truck to drive than the GX 460, with a "
                "real question over its engine. Buy with warranty.",
    },
    {
        # "GX460" 2015: 3 recalls, 11 complaints. 2017: 3 recalls, 15.
        # "GX 460" 2022: 0 recalls, 7 complaints.
        "make": "lexus", "model": "gx",
        "years": (2015, 2023),
        "generation": "J150 second gen",
        "engine": "GX 460: 4.6L 1UR-FE V8 with 6-speed automatic; "
                  "full-time 4WD",
        "reliability": 9.2,
        "maintenance": 7.8,
        "annual_maintenance_usd": 620,
        "insurance_factor": 1.08,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "Tiny files for the whole run: 11 complaints on the 2015, "
            "15 on the 2017, 7 on the 2022, 6 on the 2023.",
            "The recalls on 2015-2017 trucks are the Takata passenger "
            "airbag inflator (19V005000, 19V741000). Confirm they "
            "are done.",
            "Higher trims have rear air suspension and KDSS, both of "
            "which leak with age and cost four figures to fix.",
            "About 16 mpg on premium fuel. Check the frame for rust.",
        ],
        "note": "A Land Cruiser Prado with leather. Thirsty, dated "
                "inside and close to unbreakable.",
    },
    # ---- IS ----------------------------------------------------------
    {
        # "IS 300" 2022: 0 recalls, 5 complaints. 2023: 5 complaints.
        "make": "lexus", "model": "is",
        "years": (2021, 2026),
        "generation": "XE30 third gen, 2021 rework",
        "engine": "IS 300: 2.0L turbo I4 (RWD) or 3.5L V6 (AWD). IS "
                  "350: 3.5L V6. IS 500: 5.0L V8",
        "reliability": 9.0,
        "maintenance": 7.8,
        "annual_maintenance_usd": 560,
        "insurance_factor": 1.15,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "No recalls returned and 5 complaints each on the 2022 "
            "and 2023 IS 300. There is very little in the file.",
            "Every engine here is naturally aspirated or a "
            "long-running turbo, with a conventional automatic. The "
            "platform dates from 2014 and its faults were found "
            "years ago.",
            "Tight back seat, small trunk and dated infotainment. "
            "Staggered tires on some trims cannot be rotated.",
        ],
        "note": "The dependable choice among small sport sedans. You "
                "give up space and tech, not sleep.",
    },
    {
        # "IS250" 2015: 0 recalls, 16 complaints. "IS" 2017: 0
        # recalls, 11 complaints.
        "make": "lexus", "model": "is",
        "years": (2015, 2020),
        "generation": "XE30 third gen",
        "engine": "IS 250: 2.5L V6 (2015). IS 200t / IS 300: 2.0L "
                  "turbo I4 from 2016. IS 350: 3.5L V6",
        "reliability": 8.7,
        "maintenance": 7.8,
        "annual_maintenance_usd": 560,
        "insurance_factor": 1.15,
        "tire_set_usd": 900,
        "risk": None,
        "known_issues": [
            "No recalls returned and 16 complaints on the 2015 IS250; "
            "none and 11 on the 2017.",
            "The 2.5L V6 in the IS 250 is direct injected only and "
            "can build carbon on the intake valves, which shows up "
            "as a rough idle. The IS 350 does not have the problem.",
            "Fuel system leads the 2017 complaints (6 of 11). Ask "
            "about any fuel smell or fuel pump work.",
        ],
        "note": "A well-built small sedan. The IS 350 is the engine "
                "to have; the IS 250 is slow and the least clean.",
    },
    # ---- TX ----------------------------------------------------------
    {
        # "TX 350" 2024: 48 complaints (air bags 17). "TX" 2024: 4
        # recalls.
        "make": "lexus", "model": "tx",
        "years": (2024, 2026),
        "generation": "first gen",
        "engine": "TX 350: 2.4L turbo I4 with 8-speed automatic. TX "
                  "500h: turbo hybrid. TX 550h+: V6 plug-in hybrid",
        "reliability": 7.3,
        "maintenance": 7.4,
        "annual_maintenance_usd": 560,
        "insurance_factor": 1.08,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "Four recalls on the 2024, the main one being 24V461000: "
            "the driver side curtain airbag may not deploy properly "
            "with the window open. Air bags lead the 2024 complaints "
            "(17 of 48). Confirm it is done.",
            "The others cover the instrument cluster (25V595000) and "
            "the rear camera display.",
            "It is a Toyota Grand Highlander underneath and shares "
            "that car's first-year troubles. No simple 2.5L hybrid "
            "is offered here.",
        ],
        "note": "The roomiest Lexus and a new design still settling. "
                "A 2025 or later car is the better bet.",
    },
    # ---- UX ----------------------------------------------------------
    {
        # "UX200" 2019: 1 recall, no complaints returned. "UX" 2021:
        # 4 complaints. 2023: nothing returned.
        "make": "lexus", "model": "ux",
        "years": (2019, 2026),
        "generation": "first gen",
        "engine": "UX 200: 2.0L I4 with CVT (through 2022). UX 250h, "
                  "later UX 300h: 2.0L hybrid, AWD optional",
        "reliability": 8.7,
        "maintenance": 8.2,
        "annual_maintenance_usd": 460,
        "insurance_factor": 1.03,
        "tire_set_usd": 780,
        "risk": None,
        "known_issues": [
            "NHTSA returned almost nothing: one recall on the 2019 "
            "UX200 (fuel pump, 20V682000) and 4 complaints on the "
            "2021. That is a thin file, not a verdict.",
            "Mechanically a Corolla and Corolla Cross underneath, "
            "with the same engines and hybrid system, which have "
            "good records.",
            "Very small back seat and cargo area, and it rides on "
            "run-flat tires with no spare on most trims.",
        ],
        "note": "Provisional score, set mostly from the Toyota parts "
                "it shares. A cheap way into a Lexus if it is big "
                "enough for you.",
    },
    # ---- LX ----------------------------------------------------------
    {
        # "LX 600" 2022: 5 complaints (4 engine cooling). 2023: 14
        # complaints (engine 9). 2024: 4. 2025: 3. The recall lookup
        # returned nothing under this badge.
        "make": "lexus", "model": "lx",
        "years": (2022, 2026),
        "generation": "J310 fourth gen",
        "engine": "LX 600: 3.4L twin-turbo V6 (V35A-FTS) with "
                  "10-speed automatic. LX 700h hybrid from 2025",
        "reliability": 6.4,
        "maintenance": 6.4,
        "annual_maintenance_usd": 800,
        "insurance_factor": 1.2,
        "tire_set_usd": 1200,
        "risk": "Uses the same twin-turbo V6 family as the Toyota "
                "Tundra, which Toyota has recalled for main bearing "
                "failure, and engine is 9 of the 14 complaints on "
                "the 2023",
        "known_issues": [
            "Engine trouble makes up most of a small file: 4 of 5 "
            "complaints on the 2022 name engine cooling, and engine "
            "is 9 of 14 on the 2023.",
            "The recall lookup returned nothing under the LX 600 "
            "badge, yet other campaigns name the 2022 LX 600. Have a "
            "dealer run the VIN rather than trusting an empty list.",
            "Ask whether the engine has been replaced under Toyota's "
            "V35A recalls, and get the paperwork if so.",
            "Hydraulic height-adjustable suspension is standard on "
            "most trims and expensive to repair out of warranty.",
        ],
        "note": "A six-figure SUV with an open engine question. Buy "
                "one only with factory powertrain warranty left.",
    },
    {
        # "LX570" 2016: 1 recall, 2 complaints. "LX 570" 2020: 1
        # complaint.
        "make": "lexus", "model": "lx",
        "years": (2015, 2021),
        "generation": "J200 third gen",
        "engine": "LX 570: 5.7L 3UR-FE V8 with 8-speed automatic "
                  "(6-speed on the 2015); full-time 4WD",
        "reliability": 9.0,
        "maintenance": 7.0,
        "annual_maintenance_usd": 780,
        "insurance_factor": 1.15,
        "tire_set_usd": 1150,
        "risk": None,
        "known_issues": [
            "Two complaints on the 2016 and one on the 2020. It sold "
            "in very small numbers, so the file says little.",
            "The one recall on the 2016 is the Takata passenger "
            "airbag inflator (18V887000). Confirm it is done.",
            "The hydraulic suspension (AHC) loses pressure with age; "
            "new accumulators and fluid service run well into four "
            "figures. Check that it raises and lowers evenly.",
            "About 14 mpg on premium fuel.",
        ],
        "note": "A Land Cruiser 200 underneath and just as durable. "
                "The suspension and the fuel are the bills.",
    },
]
