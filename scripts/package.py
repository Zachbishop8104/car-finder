#!/usr/bin/env python3
"""
Build dist/car-finder.zip for a skill marketplace.

The zip holds exactly one top-level folder, car-finder/, with SKILL.md at
its root. Only files git can see (tracked, or untracked and not ignored)
are included, so config.yaml, .env, output/ and .cache/ cannot end up in
it. The build refuses to proceed if anything personal or binary slips
through anyway.

    python scripts/package.py
"""
import os
import re
import subprocess
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = "car-finder"
OUT = os.path.join(ROOT, "dist", NAME + ".zip")

# Never ship these, whatever git thinks of them.
FORBIDDEN = re.compile(r"(^|/)(\.env|config\.yaml|config\.(?!example\.)[^/]*\.yaml)$")
# For people working on the repository, not for someone using the skill.
SKIP = {".gitignore", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md"}
SKIP_DIRS = (".github/", "tests/", "scripts/")
SECRET = re.compile(r"MARKETCHECK_API_KEY\s*=\s*(?!your_key_here)[A-Za-z0-9]{16,}")


def main():
    files = subprocess.run(
        ["git", "ls-files", "-co", "--exclude-standard"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout.split("\n")
    files = sorted(f for f in files
                   if f and f not in SKIP and not f.startswith(SKIP_DIRS))

    problems = []
    for f in files:
        if FORBIDDEN.search(f):
            problems.append(f"{f}: personal file, must not ship")
            continue
        with open(os.path.join(ROOT, f), "rb") as fh:
            blob = fh.read()
        if b"\0" in blob:
            problems.append(f"{f}: binary file")
        elif SECRET.search(blob.decode("utf-8", errors="replace")):
            problems.append(f"{f}: looks like it contains a real API key")
    if "SKILL.md" not in files:
        problems.append("SKILL.md is missing")
    if problems:
        print("Not packaging:\n  " + "\n  ".join(problems))
        return 1

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(os.path.join(ROOT, f), f"{NAME}/{f}")

    print(f"{OUT}\n  {len(files)} files, {os.path.getsize(OUT) / 1024:.0f} KB")
    for f in files:
        print(f"  {NAME}/{f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
