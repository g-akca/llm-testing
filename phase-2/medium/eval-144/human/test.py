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
simplify = getattr(module, "simplify")

class TestSimplify(unittest.TestCase):
    def test_non_integer_product(self):
        self.assertFalse(simplify("4/9", "3/2"))

    def test_whole_number_result(self):
        self.assertTrue(simplify("1/5", "5/1"))

    def test_same_numerator_and_denominator(self):
        self.assertTrue(simplify("6/6", "5/5"))

if __name__ == "__main__":
    unittest.main()
