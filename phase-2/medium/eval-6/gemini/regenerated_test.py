import unittest

from regenerated_code import parse_nested_parens

class TestParseNestedParens(unittest.TestCase):
    def test_docstring_example(self):
        self.assertEqual(
            parse_nested_parens("(()()) ((())) () ((())()())"), [2, 3, 1, 3]
        )

    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(""), [])

    def test_string_with_only_spaces(self):
        self.assertEqual(parse_nested_parens("   "), [])

    def test_single_group_various_depths(self):
        self.assertEqual(parse_nested_parens("()"), [1])
        self.assertEqual(parse_nested_parens("(())"), [2])
        self.assertEqual(parse_nested_parens("((()))"), [3])
        self.assertEqual(parse_nested_parens("(()(()))"), [3])
        self.assertEqual(parse_nested_parens("(((())))"), [4])

    def test_multiple_groups_with_spaces_and_empty_strings(self):
        self.assertEqual(
            parse_nested_parens(" (())  ()   ((())) "), [2, 1, 3]
        )
        self.assertEqual(parse_nested_parens("() ()"), [1, 1])
        self.assertEqual(
            parse_nested_parens("  ((()))   (()())  "), [3, 2]
        )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
