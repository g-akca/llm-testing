# @Authors
# Student Names: Barış Türker, Gökçe Akca, Necip Baha Sağıroğlu
# Student IDs: 150170113, 150210046, 150220727

import sys
import os
import importlib
import unittest

if len(sys.argv) != 2 or sys.argv[1] not in ["gpt", "gemini"]:
    print("Usage: python test.py [gpt|gemini]")
    sys.exit(1)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
prompt = sys.argv.pop(1)
module_name = f"{prompt}.generated_code"
module = importlib.import_module(module_name)
closest_integer = getattr(module, "closest_integer")

class TestClosestInteger(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(closest_integer("50"), 50)
        self.assertEqual(closest_integer("-5.0"), -5)
        self.assertEqual(closest_integer("0"), 0)
        self.assertEqual(closest_integer("04"), 4)

    def test_round_up(self):
        self.assertEqual(closest_integer("5.56"), 6)
        self.assertEqual(closest_integer("1.99"), 2)
        self.assertEqual(closest_integer("-2.6"), -3)
        self.assertEqual(closest_integer("-28.78999"), -29)

    def test_round_down(self):
        self.assertEqual(closest_integer("14.01"), 14)
        self.assertEqual(closest_integer("0.11"), 0)
        self.assertEqual(closest_integer("-0.4"), 0)
        self.assertEqual(closest_integer("-8.25"), -8)

    def test_equidistant(self):
        self.assertEqual(closest_integer("55.50"), 56)
        self.assertEqual(closest_integer("0.5"), 1)
        self.assertEqual(closest_integer("-0.5"), -1)
        self.assertEqual(closest_integer("-55.5"), -56)

if __name__ == "__main__":
    unittest.main()
