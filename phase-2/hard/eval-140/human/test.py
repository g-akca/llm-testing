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
fix_spaces = getattr(module, "fix_spaces")

class TestFixSpaces(unittest.TestCase):
    def test_no_space(self):
        self.assertEqual(fix_spaces(""), "")
        self.assertEqual(fix_spaces("Software"), "Software")
        self.assertEqual(fix_spaces("SoftwareQualityandTesting2"), "SoftwareQualityandTesting2")
    
    def test_one_space(self):
        self.assertEqual(fix_spaces(" "), "_")
        self.assertEqual(fix_spaces("Software Quality and Testing"), "Software_Quality_and_Testing")
        self.assertEqual(fix_spaces(" Software Qualityand "), "_Software_Qualityand_")
    
    def test_two_spaces(self):
        self.assertEqual(fix_spaces("  "), "__")
        self.assertEqual(fix_spaces("Software  Quality and Testing"), "Software__Quality_and_Testing")
        self.assertEqual(fix_spaces("  Software Quality  "), "__Software_Quality__")
        self.assertEqual(fix_spaces("Software  Quality"), "Software__Quality")

    def test_three_spaces(self):
        self.assertEqual(fix_spaces("   "), "-")
        self.assertEqual(fix_spaces("Software   Quality and  Testing"), "Software-Quality_and__Testing")
        self.assertEqual(fix_spaces("   Software Quality   "), "-Software_Quality-")
        self.assertEqual(fix_spaces("Software   Quality"), "Software-Quality")

if __name__ == "__main__":
    unittest.main()
