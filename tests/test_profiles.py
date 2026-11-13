import collections
import re
import unittest

import tests  # noqa: F401  (puts the repo root on sys.path)
from carfinder import reliability

NUMBER = (int, float)
REQUIRED = {
    "make": str, "model": str, "years": tuple, "generation": str,
    "engine": str, "reliability": NUMBER, "maintenance": NUMBER,
    "annual_maintenance_usd": NUMBER, "insurance_factor": NUMBER,
    "tire_set_usd": NUMBER, "known_issues": list, "note": str,
}
# Things that belong to one person's own car search, not to a profile.
PERSONAL = re.compile(
    r"you (liked|saw|ruled)|this (search|comparison)|local lot", re.I)
VIN = re.compile(r"\b(?=[A-HJ-NPR-Z0-9]*\d{3})[A-HJ-NPR-Z0-9]{17}\b")


def _label(p):
    return f'{p.get("make")} {p.get("model")} {p.get("years")}'


def _text(p):
    return " ".join([str(p.get("risk") or ""), str(p.get("note") or "")]
                    + [str(x) for x in p.get("known_issues") or []])


class Profiles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profiles = reliability.all_profiles()

    def test_there_are_profiles(self):
        self.assertGreater(len(self.profiles), 100)

    def test_every_profile_has_every_field(self):
        for p in self.profiles:
            for key, kind in REQUIRED.items():
                with self.subTest(profile=_label(p), field=key):
                    self.assertIn(key, p)
                    self.assertIsInstance(p[key], kind)

    def test_values_are_in_range(self):
        for p in self.profiles:
            with self.subTest(profile=_label(p)):
                lo, hi = p["years"]
                self.assertTrue(1990 <= lo <= hi <= 2030)
                self.assertTrue(0 <= p["reliability"] <= 10)
                self.assertTrue(0 <= p["maintenance"] <= 10)
                self.assertTrue(100 <= p["annual_maintenance_usd"] <= 4000)
                self.assertTrue(0.5 <= p["insurance_factor"] <= 2.0)
                self.assertTrue(300 <= p["tire_set_usd"] <= 3000)
                self.assertEqual(p["make"], p["make"].lower())
                self.assertEqual(p["model"], p["model"].lower())
                self.assertTrue(all(isinstance(i, str)
                                    for i in p["known_issues"]))

    def test_each_file_holds_one_make(self):
        for make in {p["make"] for p in self.profiles}:
            with self.subTest(make=make):
                found = reliability.profiles_for(make)
                self.assertTrue(found)
                self.assertTrue(all(p["make"] == make for p in found))

    def test_year_ranges_for_a_model_do_not_overlap(self):
        by_model = collections.defaultdict(list)
        for p in self.profiles:
            key = (p["make"], reliability._model_key(p["model"]))
            by_model[key].append(p["years"])
        for key, ranges in by_model.items():
            ranges.sort()
            for a, b in zip(ranges, ranges[1:]):
                with self.subTest(model=key):
                    self.assertLess(a[1], b[0])

    def test_no_personal_wording_or_vins(self):
        for p in self.profiles:
            with self.subTest(profile=_label(p)):
                self.assertIsNone(PERSONAL.search(_text(p)))
                self.assertIsNone(VIN.search(_text(p)))


class Lookup(unittest.TestCase):
    def test_finds_a_profile_by_year(self):
        p = reliability.get_profile("Toyota", "Camry", 2021)
        self.assertFalse(p["unrated"])
        lo, hi = p["years"]
        self.assertTrue(lo <= 2021 <= hi)

    def test_ignores_punctuation_and_case(self):
        a = reliability.get_profile("Ford", "F-150", 2020)
        b = reliability.get_profile("FORD", "f150", 2020)
        self.assertFalse(a["unrated"])
        self.assertEqual(a["years"], b["years"])

    def test_hybrid_listing_falls_back_to_the_base_model(self):
        base = reliability.get_profile("Honda", "CR-V", 2021)
        hybrid = reliability.get_profile("Honda", "CR-V Hybrid", 2021)
        self.assertFalse(hybrid["unrated"])
        self.assertEqual(hybrid["make"], base["make"])

    def test_unknown_car_is_unrated_not_guessed(self):
        p = reliability.get_profile("Nonexistent", "Fakecar", 2020)
        self.assertTrue(p["unrated"])
        self.assertIsNone(p["reliability"])


if __name__ == "__main__":
    unittest.main()
