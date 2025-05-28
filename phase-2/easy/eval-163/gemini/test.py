import unittest
# Assuming the function generate_integers is in a file named 'solution.py'
from generated_code import generate_integers 


class TestGenerateIntegers(unittest.TestCase):

    def test_standard_case(self):
        """Test with a < b and multiple even digits in range."""
        self.assertEqual(generate_integers(2, 8), [2, 4, 6, 8])

    def test_reversed_case(self):
        """Test with a > b and multiple even digits in range."""
        self.assertEqual(generate_integers(8, 2), [2, 4, 6, 8])

    def test_no_even_digits_in_range(self):
        """Test with a range containing no single even digits."""
        self.assertEqual(generate_integers(10, 14), [])
        self.assertEqual(generate_integers(1, 1), [])
        self.assertEqual(generate_integers(3, 5), [4]) # Corrected expectation

    def test_edge_cases(self):
        """Test edge cases like including 0 or only one even digit."""
        self.assertEqual(generate_integers(0, 5), [0, 2, 4])
        self.assertEqual(generate_integers(3, 4), [4])
        self.assertEqual(generate_integers(0, 9), [0, 2, 4, 6, 8])

    def test_identical_bounds(self):
        """Test when a and b are the same."""
        self.assertEqual(generate_integers(4, 4), [4])
        self.assertEqual(generate_integers(5, 5), [])
        self.assertEqual(generate_integers(0, 0), [0])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
