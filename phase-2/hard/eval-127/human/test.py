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
intersection = getattr(module, "intersection")

class TestIntersection(unittest.TestCase):
    def test_prime_intersection(self):
        self.assertEqual(intersection((1, 3), (1, 3)), "YES")
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")
        self.assertEqual(intersection((10, 100), (15, 22)), "YES")

    def test_nonprime_intersection(self):
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")
        self.assertEqual(intersection((1, 3), (2, 4)), "NO")
        self.assertEqual(intersection((10, 18), (5, 1892)), "NO")
        self.assertEqual(intersection((6, 6), (0, 18)), "NO")

    def test_no_intersection(self):
        self.assertEqual(intersection((-1, 2), (8, 9)), "NO")
        self.assertEqual(intersection((-5, -2), (78, 100)), "NO")

if __name__ == "__main__":
    unittest.main()
