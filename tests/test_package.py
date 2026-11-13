"""The marketplace zip: right shape, and nothing in it that shouldn't be."""
import os
import shutil
import subprocess
import sys
import unittest
import zipfile

from tests import ROOT

PACKAGE = os.path.join(ROOT, "scripts", "package.py")
ZIP = os.path.join(ROOT, "dist", "car-finder.zip")


@unittest.skipUnless(shutil.which("git") and os.path.isdir(
    os.path.join(ROOT, ".git")), "needs a git checkout")
class Package(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.build = subprocess.run(
            [sys.executable, PACKAGE], cwd=ROOT, capture_output=True,
            text=True, encoding="utf-8", errors="replace", timeout=120)
        cls.names = []
        if cls.build.returncode == 0:
            with zipfile.ZipFile(ZIP) as z:
                cls.names = z.namelist()

    def test_it_builds(self):
        self.assertEqual(self.build.returncode, 0,
                         self.build.stdout + self.build.stderr)

    def test_one_top_level_folder_with_the_skill_at_its_root(self):
        self.assertTrue(self.names)
        self.assertTrue(all(n.startswith("car-finder/") for n in self.names))
        for needed in ("SKILL.md", "run.py", "LICENSE", "README.md",
                       "config.example.yaml", "carfinder/paths.py",
                       "carfinder/profiles/toyota.py"):
            with self.subTest(file=needed):
                self.assertIn("car-finder/" + needed, self.names)

    def test_repository_only_files_are_left_out(self):
        for n in self.names:
            rel = n[len("car-finder/"):]
            with self.subTest(file=rel):
                self.assertFalse(rel.startswith((".github/", "tests/",
                                                 "scripts/", "dist/")))
                self.assertNotIn(rel, ("CONTRIBUTING.md", "SECURITY.md",
                                       "CODE_OF_CONDUCT.md", ".gitignore"))

    def test_nothing_personal_is_shipped(self):
        for n in self.names:
            rel = n[len("car-finder/"):]
            with self.subTest(file=rel):
                self.assertNotIn(rel, (".env", "config.yaml", "config.json"))
                self.assertFalse(rel.startswith(("output/", ".cache/")))
                self.assertFalse(rel.endswith((".pyc", ".zip")))


if __name__ == "__main__":
    unittest.main()
