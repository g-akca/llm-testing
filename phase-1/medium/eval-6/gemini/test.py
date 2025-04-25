import unittest
import sys

# Ensure compatibility with Python 3.7 by adding List from typing
if sys.version_info < (3, 9):
    from typing import List
else:
    from builtins import list as List

from generated_code import parse_nested_parens

class TestParseNestedParens(unittest.TestCase):

    def test_example_from_docstring(self):
        """Tests the primary example provided in the docstring."""
        input_string = '(()()) ((())) () ((())()())'
        expected_output = [2, 3, 1, 3]
        self.assertEqual(parse_nested_parens(input_string), expected_output)

    def test_empty_string(self):
        """Tests behavior with an empty input string."""
        input_string = ''
        # Splitting an empty string results in a list containing one empty string
        expected_output = [0]
        self.assertEqual(parse_nested_parens(input_string), expected_output)

    def test_single_group_deep_nesting(self):
        """Tests a single group with deeper nesting."""
        input_string = '(((())))'
        expected_output = [4]
        self.assertEqual(parse_nested_parens(input_string), expected_output)

    def test_multiple_groups_varied_depth(self):
        """Tests multiple groups with increasing nesting depth."""
        input_string = '() (()) ((())) (((())))'
        expected_output = [1, 2, 3, 4]
        self.assertEqual(parse_nested_parens(input_string), expected_output)

    def test_string_with_only_spaces(self):
        """Tests input containing only spaces, resulting in empty groups."""
        input_string = '   ' # Three spaces -> four empty strings when split
        expected_output = [0, 0, 0, 0]
        self.assertEqual(parse_nested_parens(input_string), expected_output)

    def test_mixed_valid_and_empty_groups(self):
        """Tests input with valid groups separated by multiple spaces."""
        input_string = '()  (()) ' # Note the double space and trailing space
        # '()', '', '(())', ''
        expected_output = [1, 0, 2, 0]
        self.assertEqual(parse_nested_parens(input_string), expected_output)


# To run the tests from the command line:
# python -m unittest your_test_file_name.py
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
