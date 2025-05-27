import unittest
# Assuming the code generated previously is saved in a file named 'space_fixer.py'
# If not, replace 'space_fixer' with the actual filename or paste the function here.
from generated_code import fix_spaces 

class TestFixSpaces(unittest.TestCase):

    def test_no_spaces(self):
        """Tests input string with no spaces."""
        self.assertEqual(fix_spaces("Example"), "Example")
        self.assertEqual(fix_spaces("AnotherExample"), "AnotherExample")

    def test_single_spaces(self):
        """Tests input string with single spaces."""
        self.assertEqual(fix_spaces("Example 1"), "Example_1")
        self.assertEqual(fix_spaces(" Hello World "), "_Hello_World_")
        self.assertEqual(fix_spaces("Multiple words here"), "Multiple_words_here")

    def test_multiple_consecutive_spaces(self):
        """Tests input string with 3 or more consecutive spaces."""
        self.assertEqual(fix_spaces("Example   3"), "Example-3")
        self.assertEqual(fix_spaces("More    Spaces"), "More-Spaces")
        self.assertEqual(fix_spaces(" Leading   and   trailing "), "_Leading-and-trailing_")

    def test_double_consecutive_spaces(self):
        """Tests input string with exactly 2 consecutive spaces."""
        # According to the logic, 3+ spaces are replaced first, then single spaces.
        # So, two spaces remain as two spaces and are then replaced by underscores.
        self.assertEqual(fix_spaces("Example  2"), "Example__2")
        self.assertEqual(fix_spaces("  Two Spaces"), "__Two_Spaces")
        self.assertEqual(fix_spaces("Two  Spaces  "), "Two__Spaces__")

    def test_mixed_spaces(self):
        """Tests input string with a mix of single, double, and triple+ spaces."""
        self.assertEqual(fix_spaces("Mix of  spaces   here."), "Mix_of__spaces-here.")
        self.assertEqual(fix_spaces("  Leading triple   double  single "), "__Leading_triple-double__single_")
        self.assertEqual(fix_spaces("Test   with  double  spaces"), "Test-with__double__spaces")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
