import os
import tempfile
import unittest

from tests import ROOT
from carfinder import config

EXAMPLE = os.path.join(ROOT, "config.example.yaml")


def _write(text, name="config.yaml"):
    folder = tempfile.mkdtemp()
    path = os.path.join(folder, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


class BuiltInReader(unittest.TestCase):
    def setUp(self):
        with open(EXAMPLE, encoding="utf-8") as f:
            self.text = f.read()

    def test_reads_the_template(self):
        cfg = config.parse_simple_yaml(self.text)
        self.assertIsInstance(cfg["search"]["zip"], str)
        self.assertIsInstance(cfg["search"]["price_max"], int)
        self.assertIsInstance(cfg["targets"], list)
        self.assertIn("make", cfg["targets"][0])
        self.assertIsInstance(cfg["scoring"]["weight_value"], float)

    def test_agrees_with_pyyaml_when_it_is_installed(self):
        try:
            import yaml
        except ModuleNotFoundError:
            self.skipTest("PyYAML not installed")
        self.assertEqual(config.parse_simple_yaml(self.text),
                         yaml.safe_load(self.text))

    def test_comments_and_quotes(self):
        cfg = config.parse_simple_yaml(
            'a: "x # not a comment"   # a comment\n'
            "b: [1, 'two, still two', 3]\n"
            "c:\n  - make: Kia\n    model: K5\n  - make: BMW\n")
        self.assertEqual(cfg["a"], "x # not a comment")
        self.assertEqual(cfg["b"], [1, "two, still two", 3])
        self.assertEqual(cfg["c"], [{"make": "Kia", "model": "K5"},
                                    {"make": "BMW"}])


class LoadConfig(unittest.TestCase):
    def test_template_loads_with_defaults_filled(self):
        cfg = config.load_config(EXAMPLE)
        self.assertEqual(cfg["ownership"]["years"], 5)
        self.assertIn("call_limit", cfg["api"])
        self.assertTrue(cfg["targets"])

    def test_unquoted_zip_keeps_its_leading_zero(self):
        path = _write("search:\n  zip: 02134\ntargets:\n  - make: Toyota\n")
        self.assertEqual(config.load_config(path)["search"]["zip"], "02134")

    def test_no_targets_means_an_open_search(self):
        path = _write('search:\n  zip: "60601"\n')
        self.assertEqual(config.load_config(path)["targets"], [{}])

    def test_json_config(self):
        path = _write('{"search": {"zip": "60601"}}', "config.json")
        self.assertEqual(config.load_config(path)["search"]["zip"], "60601")

    def test_year_range_must_be_in_order(self):
        path = _write('search:\n  zip: "60601"\n  year_min: 2024\n'
                      "  year_max: 2020\n")
        with self.assertRaises(ValueError):
            config.load_config(path)

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            config.load_config(os.path.join(tempfile.mkdtemp(), "nope.yaml"))


if __name__ == "__main__":
    unittest.main()
