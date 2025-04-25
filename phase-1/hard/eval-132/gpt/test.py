import unittest

# Assume `is_nested` is defined in the same directory in a file named `is_nested.py`
from generated_code import is_nested


class TestIsNested(unittest.TestCase):
    def test_properly_nested(self):
        """Basic case: clearly nested brackets."""
        self.assertTrue(is_nested("[[]]"))

    def test_no_nesting_but_balanced(self):
        """Two adjacent but non-nested pairs should be False."""
        self.assertFalse(is_nested("[][]"))

    def test_no_nesting_single_pair(self):
        """A single pair cannot be nested."""
        self.assertFalse(is_nested("[]"))

    def test_nested_with_unbalanced_tail(self):
        """
        Unbalanced string that *does* contain a nested subsequence
        ('[[]]' in the prefix) should return True.
        """
        self.assertTrue(is_nested("[[]][["))

    def test_empty_string(self):
        """Empty string has no brackets, therefore no nesting."""
        self.assertFalse(is_nested(""))

        
if __name__ == "__main__":
    unittest.main()
