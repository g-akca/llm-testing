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
valid_date = getattr(module, "valid_date")

class TestValidDate(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(valid_date(""), False)

    def test_invalid_day(self):
        self.assertEqual(valid_date("01-00-2000"), False)
        self.assertEqual(valid_date("01-32-2000"), False)
        self.assertEqual(valid_date("02-00-2000"), False)
        self.assertEqual(valid_date("02-30-2000"), False)
        self.assertEqual(valid_date("03-00-2012"), False)
        self.assertEqual(valid_date("03-32-2012"), False)
        self.assertEqual(valid_date("04-00-2000"), False)
        self.assertEqual(valid_date("04-31-2000"), False)
        self.assertEqual(valid_date("05-00-1996"), False)
        self.assertEqual(valid_date("05-32-1996"), False)
        self.assertEqual(valid_date("06-00-2000"), False)
        self.assertEqual(valid_date("06-31-2000"), False)
        self.assertEqual(valid_date("07-00-1800"), False)
        self.assertEqual(valid_date("07-32-1800"), False)
        self.assertEqual(valid_date("08-00-2008"), False)
        self.assertEqual(valid_date("08-32-2008"), False)
        self.assertEqual(valid_date("09-00-2000"), False)
        self.assertEqual(valid_date("09-31-2000"), False)
        self.assertEqual(valid_date("10-00-2000"), False)
        self.assertEqual(valid_date("10-32-2000"), False)
        self.assertEqual(valid_date("11-00-2000"), False)
        self.assertEqual(valid_date("11-31-2000"), False)
        self.assertEqual(valid_date("12-00-2025"), False)
        self.assertEqual(valid_date("12-32-2025"), False)
        self.assertEqual(valid_date("01-100-1000"), False)
        self.assertEqual(valid_date("05-1-1955"), False)
        self.assertEqual(valid_date("06-78-1800"), False)

    def test_invalid_month(self):
        self.assertEqual(valid_date("0-10-1900"), False)
        self.assertEqual(valid_date("13-20-2000"), False)
        self.assertEqual(valid_date("180-50-2000"), False)
    
    def test_invalid_format(self):
        self.assertEqual(valid_date("05/05/2005"), False)
        self.assertEqual(valid_date("05052005"), False)
        self.assertEqual(valid_date("01-2000"), False)
        self.assertEqual(valid_date("01-01-200"), False)
        self.assertEqual(valid_date("abcd"), False)

    def test_valid_date(self):
        self.assertEqual(valid_date("03-22-2008"), True)
        self.assertEqual(valid_date("02-01-1302"), True)

    def test_boundary_date(self):
        self.assertEqual(valid_date("01-01-2000"), True)
        self.assertEqual(valid_date("01-31-2000"), True)
        self.assertEqual(valid_date("02-01-2000"), True)
        self.assertEqual(valid_date("02-29-2000"), True)
        self.assertEqual(valid_date("03-01-2012"), True)
        self.assertEqual(valid_date("03-31-2012"), True)
        self.assertEqual(valid_date("04-01-2000"), True)
        self.assertEqual(valid_date("04-30-2000"), True)
        self.assertEqual(valid_date("05-01-1996"), True)
        self.assertEqual(valid_date("05-31-1996"), True)
        self.assertEqual(valid_date("06-01-2000"), True)
        self.assertEqual(valid_date("06-30-2000"), True)
        self.assertEqual(valid_date("07-01-1800"), True)
        self.assertEqual(valid_date("07-31-1800"), True)
        self.assertEqual(valid_date("08-01-2008"), True)
        self.assertEqual(valid_date("08-31-2008"), True)
        self.assertEqual(valid_date("09-01-2000"), True)
        self.assertEqual(valid_date("09-30-2000"), True)
        self.assertEqual(valid_date("10-01-2000"), True)
        self.assertEqual(valid_date("10-30-2000"), True)
        self.assertEqual(valid_date("11-01-2000"), True)
        self.assertEqual(valid_date("11-30-2000"), True)
        self.assertEqual(valid_date("12-01-2025"), True)
        self.assertEqual(valid_date("12-31-2025"), True)

if __name__ == "__main__":
    unittest.main()
