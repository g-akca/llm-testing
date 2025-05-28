import unittest
# Assuming the code generated previously is saved in a file named 'vowel_counter.py'
# If not, replace 'vowel_counter' with the actual filename.
from generated_code import vowels_count

class TestVowelsCount(unittest.TestCase):

    def test_empty_string(self):
        """Test case for an empty string."""
        self.assertEqual(vowels_count(""), 0, "Should return 0 for empty string")

    def test_standard_vowels(self):
        """Test case with standard vowels only."""
        self.assertEqual(vowels_count("aeiouAEIOU"), 10, "Should count all standard vowels, case-insensitive")

    def test_y_at_end(self):
        """Test case with 'y' at the end considered a vowel."""
        self.assertEqual(vowels_count("ACEDY"), 3, "Should count A, E, and Y at the end")
        self.assertEqual(vowels_count("fly"), 1, "Should count Y at the end as the only vowel")
        self.assertEqual(vowels_count("beauty"), 4, "Should count e, a, u, and y at the end")

    def test_y_not_at_end(self):
        """Test case with 'y' not at the end (not a vowel)."""
        self.assertEqual(vowels_count("yellow"), 2, "Should count e and o, but not y")
        self.assertEqual(vowels_count("rhythm"), 0, "Should count no vowels (y not at end)")
        self.assertEqual(vowels_count("syzygy"), 1, "Should only count the final y")

    def test_no_vowels(self):
        """Test case with strings containing no vowels."""
        self.assertEqual(vowels_count("rhythm"), 0, "Should return 0 for string with no standard vowels and y not at end")
        self.assertEqual(vowels_count("xyz"), 0, "Should return 0 for string with no vowels")
        self.assertEqual(vowels_count("Hmph"), 0, "Should return 0 for string with consonants only")


# This allows running the tests directly from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
