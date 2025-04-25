import unittest
from typing import List

# Import the function under test.  If this file lives in the same directory
# as the module containing `separate_paren_groups`, adjust the import below
# (e.g., `from my_module import separate_paren_groups`).
from generated_code import separate_paren_groups


class TestSeparateParenGroups(unittest.TestCase):
    # --- 1. Example given in the docstring ---------------------------------
    def test_docstring_example(self) -> None:
        self.assertEqual(
            separate_paren_groups('( ) (( )) (( )( ))'),
            ['()', '(())', '(()())'],
        )

    # --- 2. No spaces, back-to-back groups ---------------------------------
    def test_compact_groups(self) -> None:
        self.assertEqual(
            separate_paren_groups('(()())()'),
            ['(()())', '()'],
        )

    # --- 3. Deep nesting and interspersed spaces ---------------------------
    def test_deep_nesting_with_spaces(self) -> None:
        self.assertEqual(
            separate_paren_groups('( ( ( ) ) ( ( ( ) ) ) )'),
            ['((())((())) )'.replace(' ', '')]  # single deeply-nested group
        )

    # --- 4. Error handling: unbalanced input -------------------------------
    def test_unbalanced_parentheses_raises(self) -> None:
        with self.assertRaises(ValueError):
            separate_paren_groups('(()')   # missing closing ')'


if __name__ == '__main__':
    unittest.main()
