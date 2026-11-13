"""Reliability profiles: Lincoln. The format and the caveats on reading
these numbers are in carfinder/reliability.py.

Lincolns share platforms and engines with Fords (Corsair with Escape,
Nautilus with Edge, Aviator with Explorer, Navigator with Expedition),
so their recall lists run in parallel. Recall and complaint counts
quoted here were pulled from NHTSA's public API in Nov 2026 and each
names the model year it is for. Lincoln sells in small numbers, so the
complaint totals are small; the recall counts are the signal."""

# Ordered; the first match on (model, year) wins.
PROFILES = [
    # --------------------------------------------------------- Corsair
    {
        "make": "lincoln", "model": "corsair",
        "years": (2020, 2026),
        "generation": "first gen (shares the Ford Escape platform)",
        "engine": "2.0L turbo I4 (2.3L turbo to 2022), 8-speed "
                  "automatic; Grand Touring is a 2.5L plug-in hybrid",
        "reliability": 6.0,
        "maintenance": 6.3,
        "annual_maintenance_usd": 780,
        "insurance_factor": 1.08,
        "tire_set_usd": 900,
        "risk": "16 recalls on the 2020, the launch year, several of "
                "them shared with the Ford Escape",
        "known_issues": [
            "16 recalls on the 2020 and 8 on the 2023. Later years "
            "are the calmer buy, and either way run the VIN.",
            "62 complaints on the 2020, led by the rear camera (18) "
            "and electrical (12). On the 2023 the file is only 15.",
            "The plug-in Grand Touring shares its hybrid hardware "
            "with the Escape plug-in, which has had engine and "
            "battery recalls. Confirm those are closed.",
            "Check the rear camera and every screen on the test "
            "drive. Electronics, not engines, fill this file.",
        ],
        "note": "A quiet, comfortable small SUV on Escape bones. "
                "Prefer a 2022 or later, and the 2.0L over the "
                "plug-in if you want fewer surprises.",
    },
    # -------------------------------------------------------- Nautilus
    {
        "make": "lincoln", "model": "nautilus",
        "years": (2024, 2026),
        "generation": "second gen (built in China)",
        "engine": "2.0L turbo I4 with 8-speed automatic, or 2.0L "
                  "turbo hybrid; AWD standard",
        "reliability": 6.2,
        "maintenance": 6.0,
        "annual_maintenance_usd": 850,
        "insurance_factor": 1.1,
        "tire_set_usd": 1000,
        "risk": None,
        "known_issues": [
            "7 recalls on the 2024, the first year of the redesign.",
            "23 complaints on the 2024 with electrical on top at 7. "
            "A small file with no dominant fault so far.",
            "The dash-wide screen runs most functions. Check it "
            "boots quickly and that phone pairing, cameras and "
            "climate controls all respond.",
            "A new design with a short history. Keep it under "
            "factory warranty.",
        ],
        "note": "Provisional: too new for a long-term read. A "
                "handsome, tech-heavy car whose risks are in the "
                "electronics.",
    },
    {
        "make": "lincoln", "model": "nautilus",
        "years": (2019, 2023),
        "generation": "first gen (a renamed, facelifted MKX)",
        "engine": "2.0L turbo I4 or 2.7L twin-turbo V6; 8-speed "
                  "automatic",
        "reliability": 6.6,
        "maintenance": 6.3,
        "annual_maintenance_usd": 820,
        "insurance_factor": 1.08,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "8 recalls on the 2019.",
            "106 complaints on the 2019, with power train (29) and "
            "electrical (29) tied on top. The power train share is "
            "the 8-speed it shares with the Ford Edge.",
            "Drive it until fully warm and feel for harsh or "
            "slipping shifts.",
            "The 2.7L V6 is strong and smooth. It costs more to "
            "service than the 2.0L but is not known as a problem.",
        ],
        "note": "The most settled Lincoln crossover of these years. "
                "A fair used buy if the transmission behaves.",
    },
    # --------------------------------------------------------- Aviator
    {
        "make": "lincoln", "model": "aviator",
        "years": (2023, 2026),
        "generation": "first gen, later build (facelifted for 2025)",
        "engine": "3.0L twin-turbo V6, 10-speed automatic; Grand "
                  "Touring plug-in hybrid offered through 2023",
        "reliability": 5.4,
        "maintenance": 5.4,
        "annual_maintenance_usd": 1000,
        "insurance_factor": 1.15,
        "tire_set_usd": 1100,
        "risk": "16 recalls on the 2023, four model years after "
                "launch, on a car with air suspension and a "
                "twin-turbo V6 that are costly to fix",
        "known_issues": [
            "16 recalls on the 2023. Better than the launch years, "
            "still a long list.",
            "24 complaints on the 2023, led by electrical (7) and "
            "the rear camera (5). A small file.",
            "If it has air suspension, check that it sits level "
            "after being parked overnight. A sagging corner is an "
            "expensive repair.",
            "Shares its platform with the Ford Explorer, which has "
            "the longest recall lists of any Ford profiled.",
        ],
        "note": "Lovely to drive and sit in, and improved over the "
                "early cars. Budget for luxury-car repair bills and "
                "buy with warranty.",
    },
    {
        "make": "lincoln", "model": "aviator",
        "years": (2020, 2022),
        "generation": "first gen, early build",
        "engine": "3.0L twin-turbo V6, 10-speed automatic; Grand "
                  "Touring adds a plug-in hybrid system",
        "reliability": 4.6,
        "maintenance": 5.3,
        "annual_maintenance_usd": 1050,
        "insurance_factor": 1.15,
        "tire_set_usd": 1100,
        "risk": "30 recalls on the 2020, the longest list of any "
                "Lincoln profiled here",
        "known_issues": [
            "30 recalls on the 2020. Recall count does not scale "
            "with sales, and Lincoln sells few cars, so this is a "
            "very bad number.",
            "111 complaints on the 2020, led by electrical (39) and "
            "power train (23), with the rear camera at 16.",
            "Make the seller show every recall closed, and check "
            "the cameras, screens and driver-assist features work.",
            "The plug-in Grand Touring adds a second drivetrain to "
            "the most recalled car in the range. Avoid it used.",
        ],
        "note": "One of the worst launch years in this file. If you "
                "want an Aviator, buy a 2023 or later.",
    },
    # ------------------------------------------------------- Navigator
    {
        "make": "lincoln", "model": "navigator",
        "years": (2025, 2026),
        "generation": "fifth gen",
        "engine": "3.5L twin-turbo V6, 10-speed automatic",
        "reliability": 6.0,
        "maintenance": 5.5,
        "annual_maintenance_usd": 1000,
        "insurance_factor": 1.22,
        "tire_set_usd": 1250,
        "risk": None,
        "known_issues": [
            "7 recalls on the 2025 already, the first year of the "
            "redesign.",
            "14 complaints on the 2025 with no component above 4. "
            "Too small a file to read.",
            "Engine and transmission carry over from the previous "
            "truck, so the history below still applies.",
        ],
        "note": "Provisional: a first-year redesign with almost no "
                "record yet. Keep it under factory warranty.",
    },
    {
        "make": "lincoln", "model": "navigator",
        "years": (2018, 2024),
        "generation": "fourth gen, aluminum body",
        "engine": "3.5L twin-turbo V6, 10-speed automatic",
        "reliability": 5.9,
        "maintenance": 5.5,
        "annual_maintenance_usd": 1000,
        "insurance_factor": 1.2,
        "tire_set_usd": 1200,
        "risk": "Cam phaser rattle on the 3.5L twin-turbo V6 and "
                "harsh shifting on the 10-speed are both common on "
                "the 2018 to 2020 trucks and costly out of warranty",
        "known_issues": [
            "12 recalls on the 2018 and 12 on the 2021.",
            "52 complaints on the 2018, led by power train (20) and "
            "engine (12). Same engine and transmission as the Ford "
            "Expedition and F-150, and the same faults.",
            "Listen for a rattle in the first two seconds of a cold "
            "start. That is the cam phasers.",
            "Check every power feature: running boards, folding "
            "seats, liftgate. Each is a costly part on its own.",
        ],
        "note": "A very comfortable truck with Expedition mechanicals "
                "and Lincoln repair prices. Prefer a 2021 or later.",
    },
    {
        "make": "lincoln", "model": "navigator",
        "years": (2015, 2017),
        "generation": "third gen, facelifted, steel body",
        "engine": "3.5L twin-turbo V6, 6-speed automatic",
        "reliability": 6.6,
        "maintenance": 5.8,
        "annual_maintenance_usd": 950,
        "insurance_factor": 1.1,
        "tire_set_usd": 1100,
        "risk": None,
        "known_issues": [
            "4 recalls on the 2016 and only 25 complaints, with no "
            "component above 7.",
            "An old design by these years, which is why the file is "
            "quiet. The 6-speed is the more trusted transmission.",
            "The older 3.5L twin-turbo stretches timing chains if "
            "oil changes were skipped. Ask for records.",
        ],
        "note": "Dated inside but calmer than the truck that "
                "replaced it. Buy on service history.",
    },
    # ------------------------------------------------------------- MKZ
    {
        "make": "lincoln", "model": "mkz",
        "years": (2017, 2020),
        "generation": "second gen, facelifted (Ford Fusion platform)",
        "engine": "2.0L turbo I4, 3.0L twin-turbo V6 or 2.0L "
                  "hybrid; 6-speed automatic (eCVT on hybrid)",
        "reliability": 6.3,
        "maintenance": 6.6,
        "annual_maintenance_usd": 720,
        "insurance_factor": 1.05,
        "tire_set_usd": 800,
        "risk": "Engine is more than half the 2017 complaint file. "
                "The 2.0L turbo shares the Fusion's coolant leak "
                "into the cylinders, which ends in a new engine",
        "known_issues": [
            "4 recalls on the 2017, but 142 complaints with engine "
            "at 76. The recall list does not cover it.",
            "On a 2.0L turbo, check the coolant level cold and look "
            "for white smoke at startup.",
            "The hybrid uses a different, non-turbo engine and is "
            "the dependable choice.",
        ],
        "note": "Buy the hybrid. It is a quiet, cheap-to-run luxury "
                "sedan; the 2.0L turbo is the gamble.",
    },
    {
        "make": "lincoln", "model": "mkz",
        "years": (2015, 2016),
        "generation": "second gen, pre-facelift (Ford Fusion "
                      "platform)",
        "engine": "2.0L turbo I4, 3.7L V6 or 2.0L hybrid; 6-speed "
                  "automatic (eCVT on hybrid)",
        "reliability": 6.2,
        "maintenance": 6.7,
        "annual_maintenance_usd": 720,
        "insurance_factor": 1.03,
        "tire_set_usd": 780,
        "risk": None,
        "known_issues": [
            "11 recalls on the 2015, a long list. Run the VIN and "
            "confirm the steering and door latch work is done.",
            "84 complaints on the 2015, spread across electrical "
            "(16), service brakes (16) and the rear camera (12). "
            "No single dominant fault.",
            "The 3.7L V6 and the hybrid are both simpler than the "
            "2.0L turbo.",
        ],
        "note": "More recalls than the later cars but no dominant "
                "failure. The V6 and the hybrid are the ones to "
                "look for.",
    },
    # ------------------------------------------------------------- MKC
    {
        "make": "lincoln", "model": "mkc",
        "years": (2015, 2019),
        "generation": "first gen (Ford Escape platform)",
        "engine": "2.0L or 2.3L turbo I4, 6-speed automatic",
        "reliability": 5.4,
        "maintenance": 6.5,
        "annual_maintenance_usd": 760,
        "insurance_factor": 1.03,
        "tire_set_usd": 820,
        "risk": "Engine is more than half the 2017 complaint file. "
                "These turbo fours share the Escape's coolant leak "
                "into the cylinders, which ends in a new engine",
        "known_issues": [
            "12 recalls on the 2015 and 3 on the 2017.",
            "195 complaints on the 2017 with engine at 110. On the "
            "2015 the file is 131, again led by engine (33).",
            "Check the coolant level cold, look for white smoke at "
            "startup, and ask for any misfire history.",
            "One recall covers an underhood electrical fault on "
            "2015 to 2019 cars. Confirm it is closed on the VIN.",
        ],
        "note": "A cheap way into a Lincoln with an engine problem "
                "the price reflects. Only with proof the engine is "
                "healthy or already replaced.",
    },
    # ------------------------------------------------------------- MKX
    {
        "make": "lincoln", "model": "mkx",
        "years": (2016, 2018),
        "generation": "second gen (Ford Edge platform)",
        "engine": "3.7L V6 or 2.7L twin-turbo V6; 6-speed automatic",
        "reliability": 6.3,
        "maintenance": 6.3,
        "annual_maintenance_usd": 800,
        "insurance_factor": 1.05,
        "tire_set_usd": 920,
        "risk": None,
        "known_issues": [
            "7 recalls on the 2016, two of them for the brakes.",
            "157 complaints on the 2016 with service brakes at 62, "
            "well ahead of engine (32) and electrical (27).",
            "Check the brake pedal is firm, look at the front brake "
            "hoses for leaks, and confirm the brake recalls are "
            "closed.",
            "The 3.7L non-turbo V6 is the simple, durable engine.",
        ],
        "note": "Became the Nautilus in 2019. Sound with the 3.7L "
                "V6 once the brake recalls are done.",
    },
    # ----------------------------------------------------- Continental
    {
        "make": "lincoln", "model": "continental",
        "years": (2017, 2020),
        "generation": "tenth gen",
        "engine": "3.7L V6, 2.7L or 3.0L twin-turbo V6; 6-speed "
                  "automatic",
        "reliability": 6.6,
        "maintenance": 5.8,
        "annual_maintenance_usd": 880,
        "insurance_factor": 1.15,
        "tire_set_usd": 950,
        "risk": None,
        "known_issues": [
            "4 recalls on the 2017, one of them for the electronic "
            "door latches.",
            "75 complaints on the 2017, led by structure (20) and "
            "latches (15). Both are the doors: they can fail to "
            "latch or fail to open.",
            "Open and close every door from inside and outside, "
            "several times, and confirm the latch recall is closed.",
            "Sold in small numbers and now discontinued, so trim "
            "and body parts can be slow and costly to get.",
        ],
        "note": "A comfortable big sedan with a quiet drivetrain "
                "record and one odd weak point in the doors.",
    },
]
