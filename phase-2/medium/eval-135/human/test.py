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
can_arrange = getattr(module, "can_arrange")

class TestCanArrange(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(can_arrange([]), -1)

    def test_single_element_array(self):
        self.assertEqual(can_arrange([10]), -1)

    def test_descending_order(self):
        self.assertEqual(can_arrange([5, 4, 3, 2, 1]), 4)

    def test_ascending_order(self):
        self.assertEqual(can_arrange([1, 2, 3, 4, 5]), -1)

    def test_multiple_out_of_order(self):
        self.assertEqual(can_arrange([1, 5, 3, 8, 4, 9]), 4)

if __name__ == "__main__":
    unittest.main()
