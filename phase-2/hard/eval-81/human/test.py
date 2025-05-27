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
numerical_letter_grade = getattr(module, "numerical_letter_grade")

class TestNumericalLetterGrade(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(numerical_letter_grade([]), [])

    def test_single_grade(self):
        self.assertEqual(numerical_letter_grade([2.4]), ["B-"])

    def test_single_grade_boundary(self):
        self.assertEqual(numerical_letter_grade([4]), ["A+"])

    def test_multiple_grades(self):
        self.assertEqual(numerical_letter_grade([3.8, 3.2, 3.6, 2.5, 2, 2.0, 1.3]), ["A", "B+", "A-", "B-", "C", "C", "D+"])

    def test_all_grades(self):
        self.assertEqual(numerical_letter_grade([2.3, 4, 2.85, 0.3, 3.5, 2.6, 1.8, 0, 3.75, 1.3, 0.9, 3.1, 4, 1.4, 2.1]), ["C+", "A+", "B", "D-", "A-", "B-", "C", "E", "A", "D+", "D", "B+", "A+", "C-", "C+"])
    
    def test_boundary_values(self):
        self.assertEqual(numerical_letter_grade([4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0.7, 0]), ["A+", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"])

if __name__ == "__main__":
    unittest.main()
