"""Tests. Standard library only, no API key, no network.

    python -m unittest discover -s tests -v
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
