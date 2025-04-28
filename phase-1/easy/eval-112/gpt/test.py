import unittest
from generated_code import reverse_delete   # assumes the function is in reverse_delete.py

class TestReverseDelete(unittest.TestCase):

    def test_given_examples(self):
        # Example 1
        self.assertEqual(reverse_delete("abcde", "ae"), ("bcd", False))
        # Example 2
        self.assertEqual(reverse_delete("abcdef", "b"), ("acdef", False))
        # Example 3
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ("cdedc", True))

    def test_empty_c_string(self):
        # Nothing gets removed; palindrome depends solely on s
        self.assertEqual(reverse_delete("level", ""), ("level", True))
        self.assertEqual(reverse_delete("python", ""), ("python", False))

    def test_empty_s_string(self):
        # Removing from an empty string should yield empty palindrome
        self.assertEqual(reverse_delete("", "abc"), ("", True))

    def test_all_chars_removed(self):
        # All characters deleted → empty string (palindrome by definition)
        self.assertEqual(reverse_delete("aaaa", "a"), ("", True))

if __name__ == "__main__":
    unittest.main()
