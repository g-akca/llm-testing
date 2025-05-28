import unittest
from generated_code import filter_by_prefix


class TestFilterByPrefix(unittest.TestCase):
    def test_empty_input(self):
        """Empty list should always give an empty list."""
        self.assertEqual(filter_by_prefix([], "a"), [])

    def test_basic_match(self):
        """Returns only strings that begin with the prefix."""
        data = ["abc", "bcd", "cde", "array"]
        expected = ["abc", "array"]
        self.assertEqual(filter_by_prefix(data, "a"), expected)

    def test_no_match(self):
        """Prefix not present at all should return an empty list."""
        data = ["foo", "bar", "baz"]
        self.assertEqual(filter_by_prefix(data, "qux"), [])

    def test_empty_prefix_returns_original(self):
        """Empty prefix should return a shallow copy of the original list."""
        data = ["alpha", "beta"]
        result = filter_by_prefix(data, "")
        # same contents, but not the same object
        self.assertEqual(result, data)
        self.assertIsNot(result, data)


if __name__ == "__main__":
    unittest.main()
