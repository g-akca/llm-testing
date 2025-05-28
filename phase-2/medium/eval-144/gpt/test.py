import unittest
from generated_code import simplify   # assumes the function above is saved in simplify.py


class TestSimplify(unittest.TestCase):

    def test_given_examples(self):
        self.assertTrue(simplify("1/5", "5/1"))
        self.assertFalse(simplify("1/6", "2/1"))
        self.assertFalse(simplify("7/10", "10/2"))

    def test_inverse_fractions(self):
        # (2/3) * (3/2) = 1
        self.assertTrue(simplify("2/3", "3/2"))

    def test_non_integer_product(self):
        # (4/9) * (3/2) = 12/18 = 2/3 (not whole)
        self.assertFalse(simplify("4/9", "3/2"))


if __name__ == "__main__":
    unittest.main()
