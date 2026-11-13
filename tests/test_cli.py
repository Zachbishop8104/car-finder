"""Runs the real command line on the bundled demo data.

Every run gets its own empty data folder through CAR_FINDER_HOME and has
no API key, so nothing here can reach the listings API or touch a real
user's config, results or cache.
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

from tests import ROOT

RUN = os.path.join(ROOT, "run.py")


class CommandLine(unittest.TestCase):
    def setUp(self):
        self.home = tempfile.mkdtemp()
        self.cwd = tempfile.mkdtemp()

    def run_cli(self, *args):
        env = dict(os.environ, CAR_FINDER_HOME=self.home,
                   PYTHONIOENCODING="utf-8")
        env.pop("MARKETCHECK_API_KEY", None)
        return subprocess.run(
            [sys.executable, RUN, *args], cwd=self.cwd, env=env,
            capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=120)

    def latest(self):
        with open(os.path.join(self.home, "output", "latest.json"),
                  encoding="utf-8") as f:
            return json.load(f)

    def test_demo_search_needs_no_config_or_key(self):
        done = self.run_cli("--sample", "search")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        run = self.latest()
        self.assertTrue(run["by_vin"])
        self.assertTrue(os.path.exists(
            os.path.join(self.home, "output", "latest.html")))

    def test_results_go_to_the_data_folder_only(self):
        self.run_cli("--sample", "search")
        self.assertEqual(os.listdir(self.cwd), [])

    def test_shortlist_keeps_cars_from_the_last_search(self):
        self.run_cli("--sample", "search")
        vin = next(iter(self.latest()["by_vin"]))
        done = self.run_cli("shortlist", vin, "NOT-A-REAL-VIN")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        with open(os.path.join(self.home, "output", "shortlist.json"),
                  encoding="utf-8") as f:
            saved = json.load(f)
        self.assertEqual([r["vin"] for r in saved["listings"]], [vin])

    def test_year_filter_is_enforced(self):
        self.run_cli("--sample", "search", "--year-min", "2022")
        years = [r["year"] for r in self.latest()["by_vin"].values()]
        self.assertTrue(years)
        self.assertTrue(all(y >= 2022 for y in years))

    def test_bad_filter_values_are_refused(self):
        for args in (("--powertrain", "warp"),
                     ("--year-min", "2025", "--year-max", "2020")):
            with self.subTest(args=args):
                done = self.run_cli("--sample", "search", *args)
                self.assertNotEqual(done.returncode, 0)

    def test_where_works_before_any_setup(self):
        done = self.run_cli("where")
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        self.assertIn(self.home, done.stdout)
        self.assertIn("not set", done.stdout)

    def test_live_search_without_a_key_stops_and_says_why(self):
        done = self.run_cli("search", "--zip", "60601", "--body-type", "SUV")
        self.assertNotEqual(done.returncode, 0)
        self.assertIn("MARKETCHECK_API_KEY", done.stdout + done.stderr)

    def test_search_without_config_or_options_explains_itself(self):
        done = self.run_cli("search")
        self.assertNotEqual(done.returncode, 0)
        self.assertIn("research", done.stdout)


if __name__ == "__main__":
    unittest.main()
