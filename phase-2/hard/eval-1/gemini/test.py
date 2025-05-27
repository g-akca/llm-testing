import unittest
# Assuming the function separate_paren_groups is in a file named paren_separator.py
# If it's in the same file, you can remove the 'paren_separator.' prefix.
from generated_code import separate_paren_groups

class TestSeparateParenGroups(unittest.TestCase):

    def test_basic_example(self):
        """Tests the example provided in the docstring."""
        input_str = '( ) (( )) (( )( ))'
        expected = ['()', '(())', '(()())']
        self.assertEqual(separate_paren_groups(input_str), expected)

    def test_empty_string(self):
        """Tests behavior with an empty input string."""
        input_str = ''
        expected = []
        self.assertEqual(separate_paren_groups(input_str), expected)

    def test_string_with_only_spaces(self):
        """Tests behavior with a string containing only spaces."""
        input_str = '   '
        expected = []
        self.assertEqual(separate_paren_groups(input_str), expected)

    def test_consecutive_simple_groups(self):
        """Tests multiple non-nested groups."""
        input_str = '()()()'
        expected = ['()', '()', '()']
        self.assertEqual(separate_paren_groups(input_str), expected)

    def test_mixed_complexity_with_spaces(self):
        """Tests a mix of nested and simple groups with spaces."""
        input_str = '  (()()) ((())) () '
        expected = ['(()())', '((()))', '()']
        self.assertEqual(separate_paren_groups(input_str), expected)

    # Optional: Test for unbalanced parentheses (should ignore unbalanced parts)
    def test_unbalanced_input(self):
        """Tests input with unbalanced parentheses."""
        input_str = '()) (() (('
        expected = ['()'] # Only the first balanced group should be returned
        self.assertEqual(separate_paren_groups(input_str), expected)


# This allows running the tests directly when the script is executed
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
