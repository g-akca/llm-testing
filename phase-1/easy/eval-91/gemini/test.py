import unittest
import re # Import the 're' module used in the function

# Assume the function is_bored is defined in a file named 'boredom_detector.py'
# If it's in the same file, you don't need the import below.
from generated_code import is_bored

class TestIsBored(unittest.TestCase):

    def test_no_boredoms(self):
        """Test a string with no sentences starting with 'I'."""
        self.assertEqual(is_bored("Hello world. How are you? Great!"), 0)
        self.assertEqual(is_bored("This is just a regular sentence."), 0)
        self.assertEqual(is_bored("No delimiters here"), 0) # No sentences

    def test_single_boredom(self):
        """Test strings with exactly one boredom."""
        self.assertEqual(
            is_bored("The sky is blue. The sun is shining. I love this weather"),
            1,
        )
        self.assertEqual(is_bored("I am testing this function."), 1)
        self.assertEqual(is_bored("Is it working? I hope so!"), 1)

    def test_multiple_boredoms(self):
        """Test strings with multiple boredoms using various delimiters."""
        self.assertEqual(is_bored("I think. Therefore I am."), 1) # "Therefore" doesn't start with "I"
        self.assertEqual(is_bored("I like cats. I also like dogs? I love animals!"), 3)
        self.assertEqual(is_bored("I. I? I!"), 3)

    def test_leading_trailing_spaces(self):
        """Test strings with extra whitespace around sentences."""
        self.assertEqual(is_bored("   I am happy.  But I am also tired. "), 2)
        self.assertEqual(is_bored("  Hello there.   I wonder... What's next?"), 1)
        self.assertEqual(is_bored(" I. "), 1)

    def test_empty_and_no_sentence_strings(self):
        """Test empty strings and strings without valid sentence structure."""
        self.assertEqual(is_bored(""), 0)
        self.assertEqual(is_bored("      "), 0)
        self.assertEqual(is_bored("Just words no punctuation"), 0)
        self.assertEqual(is_bored(".?!"), 0) # Only delimiters


# To run the tests if this script is executed directly
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
