import unittest

# Assume the `intersection` function is defined in the same module.
# If it lives in a different file (e.g. my_module.py), replace the next line with:

from generated_code import intersection

class TestIntersection(unittest.TestCase):

    def test_prime_length(self):
        # Intersection length is 2 (prime) → "YES"
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

    def test_non_prime_length(self):
        # Intersection length is 1 (not prime) → "NO"
        self.assertEqual(intersection((1, 3), (2, 4)), "NO")

    def test_no_intersection(self):
        # Disjoint intervals → "NO"
        self.assertEqual(intersection((1, 2), (3, 4)), "NO")

    def test_single_point_intersection(self):
        # Touching at a single point → length 0 → "NO"
        self.assertEqual(intersection((0, 1), (1, 2)), "NO")


if __name__ == "__main__":
    unittest.main()
