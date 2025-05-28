import unittest

# Import the function from the module where it’s defined.
# If the implementation is in the same file, this import can be skipped.
from generated_code import split_words

class TestSplitWords(unittest.TestCase):

    def test_whitespace_split(self):
        self.assertEqual(
            split_words("Hello world!"),
            ["Hello", "world!"]
        )

    def test_comma_split(self):
        self.assertEqual(
            split_words("hi,there,friend"),
            ["hi", "there", "friend"]
        )

    def test_whitespace_priority_over_comma(self):
        # Contains both whitespace and commas: whitespace should take precedence
        self.assertEqual(
            split_words("Hello, world,again"),
            ["Hello,", "world,again"]
        )

    def test_odd_lowercase_count(self):
        # "abcdef" → odd-indexed lower-case letters: b (1), d (3), f (5)
        self.assertEqual(split_words("abcdef"), 3)
        # Mixed case: only lower-case 'z' (25) is odd-indexed
        self.assertEqual(split_words("aCz"), 1)


if __name__ == "__main__":
    unittest.main()
