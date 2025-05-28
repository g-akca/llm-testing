import unittest
# Assuming the function reverse_delete is in a file named 'solution.py'
from generated_code import reverse_delete


class TestReverseDelete(unittest.TestCase):

    def test_example_1(self):
        """Tests the first example from the docstring."""
        s = "abcde"
        c = "ae"
        expected = ('bcd', False)
        self.assertEqual(reverse_delete(s, c), expected)

    def test_example_3_palindrome(self):
        """Tests the third example resulting in a palindrome."""
        s = "abcdedcba"
        c = "ab"
        expected = ('cdedc', True)
        self.assertEqual(reverse_delete(s, c), expected)

    def test_empty_string_s(self):
        """Tests with an empty input string s."""
        s = ""
        c = "abc"
        # An empty string is considered a palindrome
        expected = ('', True)
        self.assertEqual(reverse_delete(s, c), expected)

    def test_empty_string_c(self):
        """Tests with an empty character set c (no deletions)."""
        s = "racecar"
        c = ""
        expected = ('racecar', True)
        self.assertEqual(reverse_delete(s, c), expected)
        s2 = "hello"
        c2 = ""
        expected2 = ('hello', False)
        self.assertEqual(reverse_delete(s2, c2), expected2)

    def test_all_chars_deleted(self):
        """Tests the case where all characters in s are deleted."""
        s = "aaaaa"
        c = "a"
        # Result is an empty string, which is a palindrome
        expected = ('', True)
        self.assertEqual(reverse_delete(s, c), expected)

# To run the tests from the command line:
# python -m unittest your_test_file_name.py
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
