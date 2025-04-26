import unittest
from code import correct_bracketing   # adjust import path as needed

class TestCorrectBracketing(unittest.TestCase):

    def test_single_open(self):
        self.assertFalse(correct_bracketing("("))          # unmatched open

    def test_simple_pair(self):
        self.assertTrue(correct_bracketing("()"))          # one matched pair

    def test_nested_balanced(self):
        self.assertTrue(correct_bracketing("(()())"))      # multiple nested pairs

    def test_unbalanced_close_first(self):
        self.assertFalse(correct_bracketing(")(()"))       # closes before any open

if __name__ == "__main__":
    unittest.main()
