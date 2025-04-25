import unittest
from generated_code import is_simple_power

class TestIsSimplePower(unittest.TestCase):

    def test_simple_powers(self):
        """Tests cases where x is a simple power of n."""
        self.assertTrue(is_simple_power(8, 2), "Test Case 1 Failed: 8 is 2^3")
        self.assertTrue(is_simple_power(27, 3), "Test Case 2 Failed: 27 is 3^3")
        self.assertTrue(is_simple_power(16, 4), "Test Case 3 Failed: 16 is 4^2")
        self.assertTrue(is_simple_power(2, 2), "Test Case 4 Failed: 2 is 2^1")

    def test_not_simple_powers(self):
        """Tests cases where x is not a simple power of n."""
        self.assertFalse(is_simple_power(3, 2), "Test Case 5 Failed: 3 is not a power of 2")
        self.assertFalse(is_simple_power(10, 3), "Test Case 6 Failed: 10 is not a power of 3")
        self.assertFalse(is_simple_power(15, 4), "Test Case 7 Failed: 15 is not a power of 4")

    def test_base_one(self):
        """Tests edge cases involving n=1."""
        self.assertTrue(is_simple_power(1, 1), "Test Case 8 Failed: 1 is 1^k")
        self.assertFalse(is_simple_power(3, 1), "Test Case 9 Failed: 3 is not 1^k")
        self.assertFalse(is_simple_power(0, 1), "Test Case 10 Failed: 0 is not 1^k") # Assuming x > 0

    def test_exponent_zero(self):
        """Tests edge cases where the exponent would be 0 (x=1)."""
        self.assertTrue(is_simple_power(1, 4), "Test Case 11 Failed: 1 is 4^0")
        self.assertTrue(is_simple_power(1, 10), "Test Case 12 Failed: 1 is 10^0")
        # is_simple_power(1, 1) is handled by test_base_one

    def test_large_numbers(self):
        """Tests with larger numbers."""
        self.assertTrue(is_simple_power(1024, 2), "Test Case 13 Failed: 1024 is 2^10")
        self.assertTrue(is_simple_power(65536, 4), "Test Case 14 Failed: 65536 is 4^8")
        self.assertFalse(is_simple_power(1000, 3), "Test Case 15 Failed: 1000 is not a power of 3")


# This allows running the tests directly when the script is executed
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
