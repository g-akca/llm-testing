import unittest
from typing import List, Union

# Import the function to test
from code import get_positive   # adjust the import path if necessary

Number = Union[int, float]


class TestGetPositive(unittest.TestCase):
    def test_mixed_integers(self):
        """Standard mixed list of positive and negative integers."""
        data: List[int] = [-1, 2, -4, 5, 6]
        expected = [2, 5, 6]
        self.assertEqual(get_positive(data), expected)

    def test_all_non_positives(self):
        """List containing only zero and negative numbers should return empty list."""
        data: List[int] = [0, -1, -2, 0, -5]
        expected: List[int] = []
        self.assertEqual(get_positive(data), expected)

    def test_all_positive_floats_and_ints(self):
        """List containing only positive floats and ints should return itself."""
        data: List[Number] = [1, 2.5, 3.0, 7, 100.1]
        self.assertEqual(get_positive(data), data)

    def test_duplicates_and_zero(self):
        """Ensure duplicates are preserved and zero is not considered positive."""
        data: List[int] = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
        expected = [5, 3, 2, 3, 9, 123, 1]
        self.assertEqual(get_positive(data), expected)


if __name__ == "__main__":
    unittest.main()
