import unittest
from generated_code import split_words

class TestSplitWords(unittest.TestCase):

    def test_split_on_whitespace(self):
        """Tests splitting on whitespace (standard case)."""
        self.assertEqual(split_words("Hello world!"), ["Hello", "world!"])
        self.assertEqual(split_words("Multiple   spaces"), ["Multiple", "spaces"])
        self.assertEqual(split_words(" leading and trailing "), ["leading", "and", "trailing"])

    def test_split_on_comma(self):
        """Tests splitting on commas when no whitespace is present."""
        self.assertEqual(split_words("Hello,world!"), ["Hello", "world!"])
        self.assertEqual(split_words("one,two,three"), ["one", "two", "three"])
        self.assertEqual(split_words("no,delimiters,here"), ["no", "delimiters", "here"])

    def test_count_odd_lowercase(self):
        """Tests counting odd-ordered lowercase letters when no delimiters are present."""
        self.assertEqual(split_words("abcdef"), 3) # b (1), d (3), f (5)
        self.assertEqual(split_words("Programming"), 4) # r(17), g(6 - even), r(17), m(12 - even), m(12 - even), n(13), g(6 - even) -> r, r, n -> 3? No, P(15), r(17), o(14), g(6), r(17), a(0), m(12), m(12), i(8), n(13), g(6) -> P, r, r, n -> 4
        self.assertEqual(split_words("XYZ"), 0) # No lowercase
        self.assertEqual(split_words("123!@#"), 0) # No letters
        self.assertEqual(split_words(""), 0) # Empty string

    def test_whitespace_precedence(self):
        """Tests that whitespace splitting takes precedence over comma splitting."""
        self.assertEqual(split_words("comma,separated but with spaces"), ["comma,separated", "but", "with", "spaces"])

    def test_mixed_case_counting(self):
        """Tests counting with mixed upper and lower case letters."""
        self.assertEqual(split_words("AbCdEf"), 3) # b (1), d (3), f (5)

# To run the tests from the command line:
# python -m unittest your_test_file_name.py
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
