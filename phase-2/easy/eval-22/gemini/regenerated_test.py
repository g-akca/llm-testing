import unittest
from regenerated_code import filter_integers

class TestFilterIntegers(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_integers([]), [])

    def test_list_with_only_integers(self):
        self.assertEqual(filter_integers([1, 2, 3, 0, -5]), [1, 2, 3, 0, -5])

    def test_mixed_list_with_integers_and_other_types(self):
        self.assertEqual(
            filter_integers(['a', 3.14, 5, 'hello', 100, {}]), [5, 100]
        )

    def test_list_with_booleans(self):
        self.assertEqual(
            filter_integers([1, True, 0, False, 42, True, -10]),
            [1, 0, 42, -10],
        )

    def test_list_with_no_integers(self):
        self.assertEqual(
            filter_integers(['abc', 3.14, None, [], {'key': 'value'}, True]), []
        )


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
