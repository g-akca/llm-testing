import unittest

# Import the function you want to test.
# Adjust the import path/name as needed if your code lives in a different module.
from generated_code import specialFilter


class TestSpecialFilter(unittest.TestCase):
    def test_examples_given_1(self):
        """First example from the prompt."""
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)

    def test_examples_given_2(self):
        """Second example from the prompt."""
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

    def test_mixed_values(self):
        """
        Mixed list: some valid (11, 99, 1357) and some invalid
        (22, 20). Expected count is 3.
        """
        self.assertEqual(specialFilter([11, 22, 99, 1357, 20]), 3)

    def test_all_small_numbers(self):
        """All numbers ≤ 10 should return 0."""
        self.assertEqual(specialFilter([1, 7, 9, 10]), 0)

    def test_no_valid_numbers(self):
        """
        Contains negatives and even‐digit numbers > 10, but none satisfy
        all criteria, so result should be 0.
        """
        self.assertEqual(specialFilter([-111, 12, 24, 68]), 0)


if __name__ == "__main__":
    unittest.main()
