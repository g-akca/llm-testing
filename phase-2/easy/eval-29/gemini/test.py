import unittest
from typing import List
from generated_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        """Test filtering an empty list."""
        self.assertEqual(filter_by_prefix([], "a"), [])
        self.assertEqual(filter_by_prefix([], ""), [])

    def test_no_matches(self):
        """Test when no strings match the prefix."""
        strings = ["apple", "banana", "cherry"]
        prefix = "d"
        self.assertEqual(filter_by_prefix(strings, prefix), [])

    def test_all_matches(self):
        """Test when all strings match the prefix."""
        strings = ["apple", "apricot", "application"]
        prefix = "app"
        self.assertEqual(filter_by_prefix(strings, prefix), strings)

    def test_mixed_matches(self):
        """Test a mix of matching and non-matching strings."""
        strings = ["abc", "bcd", "abe", "xyz", "abacus"]
        prefix = "ab"
        expected = ["abc", "abe", "abacus"]
        self.assertEqual(filter_by_prefix(strings, prefix), expected)

    def test_empty_prefix(self):
        """Test filtering with an empty prefix (should return all strings)."""
        strings = ["one", "two", "three"]
        prefix = ""
        self.assertEqual(filter_by_prefix(strings, prefix), strings)

    def test_case_sensitivity(self):
        """Test that filtering is case-sensitive."""
        strings = ["Apple", "apple", "Apricot", "apricot"]
        prefix = "A"
        expected = ["Apple", "Apricot"]
        self.assertEqual(filter_by_prefix(strings, prefix), expected)
        prefix_lower = "a"
        expected_lower = ["apple", "apricot"]
        self.assertEqual(filter_by_prefix(strings, prefix_lower), expected_lower)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
