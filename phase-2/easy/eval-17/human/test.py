# @Authors
# Student Names: Barış Türker, Gökçe Akca, Necip Baha Sağıroğlu
# Student IDs: 150170113, 150210046, 150220727

import sys
import os
import importlib
import unittest

if len(sys.argv) != 2 or sys.argv[1] not in ["gpt", "gemini"]:
    print("Usage: python test.py [gpt|gemini]")
    sys.exit(1)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
prompt = sys.argv.pop(1)
module_name = f"{prompt}.generated_code"
module = importlib.import_module(module_name)
parse_music = getattr(module, "parse_music")

""" Input to this function is a string representing musical notes in a special ASCII format.
Your task is to parse this string and return list of integers corresponding to how many beats does each
not last.

Here is a legend:
'o' - whole note, lasts four beats
'o|' - half note, lasts two beats
'.|' - quater note, lasts one beat

>>> parse_music('o o| .| o| o| .| .| .| .| o o')
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
"""

class TestParseMusic(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(parse_music(""), [])

    def test_mixed_notes(self):
        self.assertEqual(parse_music("o o| .| o| o| .| .| .| .| o o"), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])
    
    def test_single_notes(self):
        self.assertEqual(parse_music("o"), [4])
        self.assertEqual(parse_music("o|"), [2])
        self.assertEqual(parse_music(".|"), [1])

    def test_extra_spaces(self):
        self.assertEqual(parse_music("  o   o| .|  "), [4, 2, 1])

if __name__ == "__main__":
    unittest.main()
