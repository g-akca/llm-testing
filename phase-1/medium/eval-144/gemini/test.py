import unittest
from generated_code import simplify # Assuming the code is saved in 'your_module.py'

class TestSimplifyFunction(unittest.TestCase):

    def test_whole_number_result(self):
        """Tests if the function correctly identifies a whole number result."""
        self.assertTrue(simplify("1/5", "5/1"), "Test Case 1 Failed: 1/5 * 5/1 should be True")
        self.assertTrue(simplify("3/2", "4/3"), "Test Case 2 Failed: 3/2 * 4/3 = 12/6 = 2 should be True")
        self.assertTrue(simplify("10/1", "1/5"), "Test Case 3 Failed: 10/1 * 1/5 = 10/5 = 2 should be True")

    def test_fractional_result(self):
        """Tests if the function correctly identifies a non-whole number result."""
        self.assertFalse(simplify("1/6", "2/1"), "Test Case 4 Failed: 1/6 * 2/1 = 2/6 = 1/3 should be False")
        self.assertFalse(simplify("7/10", "10/2"), "Test Case 5 Failed: 7/10 * 10/2 = 70/20 = 7/2 should be False")
        self.assertFalse(simplify("2/3", "4/5"), "Test Case 6 Failed: 2/3 * 4/5 = 8/15 should be False")

    def test_simplification_leading_to_whole(self):
        """Tests cases where fractions simplify during multiplication to yield a whole number."""
        self.assertTrue(simplify("2/4", "4/2"), "Test Case 7 Failed: 2/4 * 4/2 = 8/8 = 1 should be True")
        self.assertTrue(simplify("6/3", "5/10"), "Test Case 8 Failed: 6/3 * 5/10 = 30/30 = 1 should be True")

    def test_large_numbers_whole(self):
        """Tests with larger numerators/denominators resulting in a whole number."""
        self.assertTrue(simplify("100/25", "50/2"), "Test Case 9 Failed: 100/25 * 50/2 = 5000/50 = 100 should be True")

    def test_large_numbers_fractional(self):
        """Tests with larger numerators/denominators resulting in a fraction."""
        self.assertFalse(simplify("99/17", "17/3"), "Test Case 10 Failed: 99/17 * 17/3 = 1683/51 = 33/1 should be True, but the simplified form is 33. Oh wait, 1683/51 is exactly 33. Let's fix this test.")
        # Corrected test case 10:
        self.assertTrue(simplify("99/17", "17/3"), "Test Case 10 Failed: 99/17 * 17/3 = 33 should be True")
        # New test case 11 for fractional large numbers:
        self.assertFalse(simplify("101/10", "5/2"), "Test Case 11 Failed: 101/10 * 5/2 = 505/20 should be False")


if __name__ == '__main__':
    # Replace 'your_module' with the actual filename where you saved the simplify function
    # Example: If saved as 'simplify_fractions.py', import as:
    # from simplify_fractions import simplify
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
