import unittest
from typing import List
from code import parse_nested_parens   # replace with the actual module name

class TestParseNestedParens(unittest.TestCase):

    def test_mixed_groups(self):
        """Example from the docstring."""
        s = '(()()) ((())) () ((())()())'
        expected = [2, 3, 1, 3]
        self.assertEqual(parse_nested_parens(s), expected)

    def test_single_group_no_nesting(self):
        """A single pair of parentheses has depth 1."""
        self.assertEqual(parse_nested_parens('()'), [1])

    def test_deep_nesting(self):
        """Verify correct depth for a deeply-nested group."""
        self.assertEqual(parse_nested_parens('(((((())))))'), [5])

    def test_extra_whitespace(self):
        """Parser should ignore leading, trailing, and repeated spaces."""
        s = '  (())   ()  ((()))  '
        expected = [2, 1, 3]
        self.assertEqual(parse_nested_parens(s), expected)

    def test_multiple_adjacent_groups(self):
        """Adjacent groups without spaces should still be treated as one group."""
        # The input spec says groups are separated by spaces. This confirms behaviour
        # when caller provides no space (treated as a single larger group).
        self.assertEqual(parse_nested_parens('()()()'), [1])  # whole string is one group

if __name__ == '__main__':
    unittest.main()
