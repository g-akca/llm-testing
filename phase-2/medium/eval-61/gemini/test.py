import unittest
from generated_code import correct_bracketing

class TestCorrectBracketing(unittest.TestCase):

    def test_empty_string(self):
        """Test an empty string should be considered correctly bracketed."""
        self.assertTrue(correct_bracketing(""), "Empty string failed")

    def test_simple_valid(self):
        """Test a simple valid case '()'."""
        self.assertTrue(correct_bracketing("()"), "Simple valid case '()' failed")

    def test_nested_valid(self):
        """Test a nested valid case '(())()'."""
        self.assertTrue(correct_bracketing("(())()"), "Nested valid case '(())()' failed")

    def test_invalid_starts_closing(self):
        """Test an invalid case starting with a closing bracket ')('."""
        self.assertFalse(correct_bracketing(")("), "Invalid case ')(' failed")

    def test_invalid_unbalanced(self):
        """Test an invalid case with unbalanced brackets '(()'."""
        self.assertFalse(correct_bracketing("(()"), "Invalid unbalanced case '(()' failed")

    # Optional: Add more test cases if needed
    # def test_invalid_extra_closing(self):
    #     """Test an invalid case with extra closing brackets '())'."""
    #     self.assertFalse(correct_bracketing("())"), "Invalid extra closing case '())' failed")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
