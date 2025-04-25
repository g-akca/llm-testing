import unittest

# Import the function you wrote; adjust the import as needed.
# from my_module import numerical_letter_grade
from generated_code import numerical_letter_grade   # if it's in `numerical_letter_grade.py`

class TestNumericalLetterGrade(unittest.TestCase):

    def test_example_case(self):
        """Example given in the doc-string."""
        gpas = [4.0, 3, 1.7, 2, 3.5]
        expected = ['A+', 'B', 'C-', 'C', 'A-']
        self.assertEqual(numerical_letter_grade(gpas), expected)

    def test_boundary_values(self):
        """GPAs that sit exactly on the cut-off points."""
        gpas = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0,
                1.7, 1.3, 1.0, 0.7, 0.0]
        expected = ['A+', 'A-', 'B+', 'B', 'B-', 'C+',
                    'C', 'C-', 'D+', 'D', 'D-', 'E']
        self.assertEqual(numerical_letter_grade(gpas), expected)

    def test_empty_list(self):
        """No GPAs → empty output."""
        self.assertEqual(numerical_letter_grade([]), [])

    def test_invalid_and_overflow_values(self):
        """Negative GPA should map to 'E'; >4.0 should grade like >3.7 (i.e., 'A')."""
        gpas = [-0.5, 5.0]
        expected = ['E', 'A']
        self.assertEqual(numerical_letter_grade(gpas), expected)


if __name__ == "__main__":
    unittest.main()
