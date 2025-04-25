import unittest

from typing import List

# ---- import the function to test ----
# If the implementation is in another module, replace the import statement accordingly,
# e.g. `from grading import numerical_letter_grade`
from __main__ import numerical_letter_grade  


class TestNumericalLetterGrade(unittest.TestCase):

    def test_sample_from_prompt(self):
        """Verify the example given in the docstring."""
        gpas = [4.0, 3, 1.7, 2, 3.5]
        expected = ['A+', 'B', 'C-', 'C', 'A-']
        self.assertEqual(numerical_letter_grade(gpas), expected)

    def test_exact_and_just_over_boundaries(self):
        """Check GPA values that sit exactly on, or infinitesimally above, key boundaries."""
        gpas = [4.0, 3.7, 3.7001, 3.3, 3.3001]
        expected = ['A+',  # exactly 4.0
                    'A-',  # 3.7 should map to A- (not >3.7)
                    'A',   # just above 3.7 should be A
                    'B+',  # 3.3 should map to B+
                    'A-']  # just above 3.3 should be A-
        self.assertEqual(numerical_letter_grade(gpas), expected)

    def test_full_letter_spectrum(self):
        """Cover each distinct letter grade at least once (except A+ handled above)."""
        gpas = [3.9, 3.5, 3.1, 2.9, 2.5, 2.1, 1.8, 1.4, 1.1, 0.8, 0.3]
        expected = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-']
        self.assertEqual(numerical_letter_grade(gpas), expected)

    def test_zero_and_negative(self):
        """0.0 or any negative GPA should map to 'E'."""
        gpas = [0.0, -0.1, -3.5]
        self.assertEqual(numerical_letter_grade(gpas), ['E', 'E', 'E'])


if __name__ == '__main__':
    unittest.main()
