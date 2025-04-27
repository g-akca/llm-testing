import unittest
from typing import List # Import List for type hinting if needed in the function

from generated_code import by_length

class TestByLengthFunction(unittest.TestCase):

    def test_basic_example(self):
        """Tests the primary example provided in the docstring."""
        arr = [2, 1, 1, 4, 5, 8, 2, 3]
        expected = ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
        self.assertEqual(by_length(arr), expected)

    def test_empty_list(self):
        """Tests the function with an empty input list."""
        arr = []
        expected = []
        self.assertEqual(by_length(arr), expected)

    def test_ignore_invalid_numbers(self):
        """Tests that numbers outside the 1-9 range are ignored."""
        arr = [1, -1, 55, 0, 10, 4]
        # Valid: [1, 4] -> Sort: [1, 4] -> Reverse: [4, 1] -> Map: ["Four", "One"]
        expected = ["Four", "One"]
        self.assertEqual(by_length(arr), expected)

    def test_no_valid_numbers(self):
        """Tests the case where the input list contains no valid numbers (1-9)."""
        arr = [-2, 0, 10, 100]
        expected = []
        self.assertEqual(by_length(arr), expected)

    def test_all_valid_numbers_descending(self):
        """Tests a list containing all valid numbers already in descending order."""
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
        self.assertEqual(by_length(arr), expected)


# This allows running the tests directly when the script is executed
if __name__ == '__main__':
    # Using argv and exit=False makes it friendlier for some environments like Jupyter
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
