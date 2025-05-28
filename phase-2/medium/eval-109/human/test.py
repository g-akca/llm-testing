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
move_one_ball = getattr(module, "move_one_ball")

class TestMoveOneBall(unittest.TestCase):
    def test_empty_array(self):
        self.assertTrue(move_one_ball([]))

    def test_single_element(self):
        self.assertTrue(move_one_ball([42]))

    def test_rotation_succeeds(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))

    def test_rotation_fails(self):
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]))

    def test_already_sorted(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))

if __name__ == "__main__":
    unittest.main()
