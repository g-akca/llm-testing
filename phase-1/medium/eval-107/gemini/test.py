import unittest
from typing import Tuple
from generated_code import even_odd_palindrome

class TestEvenOddPalindrome(unittest.TestCase):

    def test_example_1(self):
        """Tests the first example from the docstring (n=3)."""
        self.assertEqual(even_odd_palindrome(3), (1, 2))

    def test_example_2(self):
        """Tests the second example from the docstring (n=12)."""
        self.assertEqual(even_odd_palindrome(12), (4, 6))

    def test_lower_bound(self):
        """Tests the lower bound of the constraint (n=1)."""
        self.assertEqual(even_odd_palindrome(1), (0, 1))

    def test_medium_case(self):
        """Tests a case within the constraints (n=100)."""
        # Palindromes up to 100: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99
        # Even: 2, 4, 6, 8, 22, 44, 66, 88 (8)
        # Odd: 1, 3, 5, 7, 9, 11, 33, 55, 77, 99 (10)
        self.assertEqual(even_odd_palindrome(100), (8, 10))

    def test_upper_bound_constraint(self):
        """Tests the upper bound of the constraint (n=1000)."""
        # Calculation:
        # 1-9: 4 even, 5 odd
        # 11-99: 4 even, 5 odd
        # 101-999 (form aba):
        #   a=even (2,4,6,8): 4 * 10 (b=0-9) = 40 even
        #   a=odd (1,3,5,7,9): 5 * 10 (b=0-9) = 50 odd
        # Total Even = 4 + 4 + 40 = 48
        # Total Odd = 5 + 5 + 50 = 60
        # 1000 is not a palindrome.
        self.assertEqual(even_odd_palindrome(1000), (48, 60))


# To run the tests from the command line:
# python -m unittest your_file_name.py
if __name__ == "__main__":
    unittest.main()
