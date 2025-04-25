import unittest
from typing import List

# Assume the function is imported from the module where it is defined.
# from your_module import separate_paren_groups

# For this example, we redefine it here so the tests are self-contained.
def separate_paren_groups(paren_string: str) -> List[str]:
    cleaned = paren_string.replace(" ", "")
    groups, current, depth = [], [], 0

    for ch in cleaned:
        if ch not in "()":
            continue
        current.append(ch)
        depth += 1 if ch == "(" else -1
        if depth == 0:                     # end of a balanced group
            groups.append("".join(current))
            current = []
    return groups


class TestSeparateParenGroups(unittest.TestCase):

    def test_docstring_example(self):
        """Matches the example in the function’s docstring."""
        s = "( ) (( )) (( )( ))"
        expected = ["()", "(())", "(()())"]
        self.assertEqual(separate_paren_groups(s), expected)

    def test_adjacent_groups_no_spaces(self):
        """Handles adjacent groups without any separating whitespace."""
        s = "(())()(((())))"
        expected = ["(())", "()", "(((())))"]
        self.assertEqual(separate_paren_groups(s), expected)

    def test_ignores_non_paren_characters(self):
        """Non-parenthesis characters should be ignored entirely."""
        s = "  (a) ((b)) "
        expected = ["()", "(())"]
        self.assertEqual(separate_paren_groups(s), expected)

    def test_empty_input(self):
        """Returns an empty list for an empty input string."""
        self.assertEqual(separate_paren_groups(""), [])


if __name__ == "__main__":
    unittest.main()
