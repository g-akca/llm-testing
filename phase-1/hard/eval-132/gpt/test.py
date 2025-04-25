import unittest
from code import is_nested

class TestIsNested(unittest.TestCase):

    def test_single_nested_pair(self):
        # Basic positive case: one clearly-nested pair
        self.assertTrue(is_nested('[[]]'))

    def test_no_nesting_flat_pairs(self):
        # Two balanced pairs side-by-side → no nesting
        self.assertFalse(is_nested('[][]'))

    def test_balanced_but_shallow(self):
        # Single balanced pair with depth 1 only
        self.assertFalse(is_nested('[]'))

    def test_mixed_balanced_and_unbalanced(self):
        # First segment has nesting, trailing “[[" is extra but allowed
        self.assertTrue(is_nested('[[]][['))

    def test_unbalanced_closing_then_balanced(self):
        # Starts with stray closings → reset; later segment is shallow, so still False
        self.assertFalse(is_nested(']]][[]'))
        

if __name__ == '__main__':
    unittest.main()
