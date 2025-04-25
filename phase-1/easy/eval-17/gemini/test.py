import unittest
from typing import List
from generated_code import parse_music

class TestParseMusic(unittest.TestCase):

    def test_docstring_example(self):
        """Tests the example provided in the function's docstring."""
        music_string = 'o o| .| o| o| .| .| .| .| o o'
        expected_beats = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
        self.assertEqual(parse_music(music_string), expected_beats)

    def test_empty_string(self):
        """Tests parsing an empty input string."""
        music_string = ''
        expected_beats = []
        self.assertEqual(parse_music(music_string), expected_beats)

    def test_single_notes(self):
        """Tests parsing strings with only one note of each type."""
        self.assertEqual(parse_music('o'), [4])
        self.assertEqual(parse_music('o|'), [2])
        self.assertEqual(parse_music('.|'), [1])

    def test_mixed_notes(self):
        """Tests a different combination of notes."""
        music_string = '.| o o| .| o|'
        expected_beats = [1, 4, 2, 1, 2]
        self.assertEqual(parse_music(music_string), expected_beats)

    def test_extra_spaces(self):
        """Tests parsing with leading, trailing, and multiple spaces."""
        music_string = '  o   o| .|  '
        expected_beats = [4, 2, 1]
        self.assertEqual(parse_music(music_string), expected_beats)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
