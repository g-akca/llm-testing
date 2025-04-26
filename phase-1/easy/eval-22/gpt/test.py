import unittest
from code import filter_integers   # assumes the function is in filter_integers.py

class TestFilterIntegers(unittest.TestCase):

    def test_mixed_types(self):
        """Mixed literals should return only the integer 5."""
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])

    def test_all_integers(self):
        """A list containing only integers remains unchanged."""
        self.assertEqual(filter_integers([1, 2, 3]), [1, 2, 3])

    def test_integers_and_bools(self):
        """Booleans must be excluded even though isinstance(True, int) is True."""
        self.assertEqual(filter_integers([True, False, 7, 0, -3]), [7, -3])

    def test_empty_and_nested(self):
        """Empty list returns empty; nested lists and dicts are ignored."""
        self.assertEqual(filter_integers([]), [])
        self.assertEqual(filter_integers([[1, 2], {'a': 1}, 10]), [10])

if __name__ == '__main__':
    unittest.main()
