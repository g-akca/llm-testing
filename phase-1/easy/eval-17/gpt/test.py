import unittest
from typing import List
from code import parse_music   # adjust the import path if needed


class TestParseMusic(unittest.TestCase):
    def test_example_sequence(self):
        """Exact example from the docstring."""
        seq = 'o o| .| o| o| .| .| .| .| o o'
        expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
        self.assertEqual(parse_music(seq), expected)

    def test_single_notes(self):
        """Each individual note should map correctly."""
        self.assertEqual(parse_music('o'), [4])
        self.assertEqual(parse_music('o|'), [2])
        self.assertEqual(parse_music('.|'), [1])

    def test_mixed_spacing(self):
        """Extra whitespace (multiple spaces, tabs, newlines) should be ignored."""
        seq = 'o\t o|\n.|   o'
        expected = [4, 2, 1, 4]
        self.assertEqual(parse_music(seq), expected)

    def test_invalid_symbol(self):
        """An unknown symbol should raise ValueError."""
        with self.assertRaises(ValueError):
            parse_music('o x .|')  # 'x' is not a defined note


if __name__ == "__main__":
    unittest.main()
