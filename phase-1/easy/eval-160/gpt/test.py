import unittest

# Assuming `do_algebra` is defined in the same module; if it lives elsewhere,
# replace the import accordingly, e.g.:
# from my_module import do_algebra
from generated_code import do_algebra


class TestDoAlgebra(unittest.TestCase):

    def test_basic_mixed_ops(self):
        # 2 + 3 * 4 - 5 = 2 + 12 - 5 = 9
        self.assertEqual(do_algebra(['+', '*', '-'], [2, 3, 4, 5]), 9)

    def test_exponent_then_add(self):
        # 2 ** 3 + 1 = 8 + 1 = 9
        self.assertEqual(do_algebra(['**', '+'], [2, 3, 1]), 9)

    def test_floor_division(self):
        # 10 // 3 - 1 = 3 - 1 = 2
        self.assertEqual(do_algebra(['//', '-'], [10, 3, 1]), 2)

    def test_invalid_length_error(self):
        with self.assertRaises(ValueError):
            do_algebra(['+'], [1, 2, 3])  # mismatched lengths

    def test_unsupported_operator_error(self):
        with self.assertRaises(ValueError):
            do_algebra(['+','%'], [4, 5, 2])  # '%' not allowed


if __name__ == "__main__":
    unittest.main()
