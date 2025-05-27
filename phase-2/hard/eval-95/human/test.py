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
check_dict_case = getattr(module, "check_dict_case")

class TestCheckDictCase(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual(check_dict_case({}), False)
    
    def test_nonstring_key(self):
        self.assertEqual(check_dict_case({8: "eight"}), False)
        self.assertEqual(check_dict_case({74: "num", "fruit": "apple"}), False)
        self.assertEqual(check_dict_case({None: "oop", "a": "b", "b": "c"}), False)

    def test_single_key(self):
        self.assertEqual(check_dict_case({"f": "apple"}), True)
        self.assertEqual(check_dict_case({"FRUIT": "appLe"}), True)
        self.assertEqual(check_dict_case({"Fruit": "apple"}), False)
        self.assertEqual(check_dict_case({"frUIT": "Apple"}), False)

    def test_multiple_key(self):
        self.assertEqual(check_dict_case({"fruit": "apple", "FRUIT": "orange"}), False)
        self.assertEqual(check_dict_case({"fruit": "apple", "fr": "uit"}), True)
        self.assertEqual(check_dict_case({"NAME": "gok", "SURNAME": "ak", "ID": 999}), True)

if __name__ == "__main__":
    unittest.main()
