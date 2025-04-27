import unittest
# Assuming the previously generated code is saved in a file named 'nested_brackets.py'
# If not, replace 'nested_brackets' with the actual filename or paste the function here.
from generated_code import is_nested

class TestIsNested(unittest.TestCase):

    def test_simple_nested(self):
        """Tests a simple valid nested case."""
        self.assertTrue(is_nested('[[]]'), "Should return True for '[[]]'")

    def test_no_nesting_multiple(self):
        """Tests multiple non-nested pairs."""
        self.assertFalse(is_nested('[][]'), "Should return False for '[][]'")

    def test_complex_nested(self):
        """Tests a more complex nested structure."""
        self.assertTrue(is_nested('[[][]]'), "Should return True for '[[][]]'")

    def test_unbalanced_but_nested(self):
        """Tests an unbalanced string that still contains nesting."""
        # This covers the example '[[]][['
        self.assertTrue(is_nested('[[]][['), "Should return True for '[[]][['")
        # Also testing the potentially confusing example from the docstring
        # Based on the function's logic, a nested subsequence '[[]]' exists.
        self.assertTrue(is_nested('[]]]]]]][[[[[]'), "Should return True for '[]]]]]]][[[[[]'")

    def test_no_nesting_single(self):
        """Tests a single non-nested pair."""
        self.assertFalse(is_nested('[]'), "Should return False for '[]'")

    def test_empty_string(self):
        """Tests an empty string."""
        self.assertFalse(is_nested(''), "Should return False for an empty string")

    def test_only_opening_nested(self):
        """Tests only opening brackets forming nesting."""
        self.assertTrue(is_nested('[[['), "Should return True for '[[['")

    def test_only_closing(self):
        """Tests only closing brackets."""
        self.assertFalse(is_nested(']]]'), "Should return False for ']]]'")


# To run the tests from the command line:
# python -m unittest your_test_file_name.py
if __name__ == '__main__':
    unittest.main()
