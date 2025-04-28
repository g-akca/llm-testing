# test_vowels_count.py
import unittest
from generated_code import vowels_count

class TestVowelsCount(unittest.TestCase):
    def test_example_given(self):
        self.assertEqual(vowels_count("abcde"), 2)
        self.assertEqual(vowels_count("ACEDY"), 3)

    def test_y_handling(self):
        self.assertEqual(vowels_count("yellow"), 2)   # ‘y’ not counted (not at end)
        self.assertEqual(vowels_count("play"), 2)     # ‘y’ counted (at end)

    def test_case_insensitive_and_empty(self):
        self.assertEqual(vowels_count("OuCh"), 2)
        self.assertEqual(vowels_count(""), 0)

    def test_non_alpha_characters(self):
        self.assertEqual(vowels_count("h3ll0!"), 0)

if __name__ == "__main__":
    unittest.main()
