import unittest
from generated_code import intersection

class TestIntersection(unittest.TestCase):
    def test_point_intersection_non_prime(self):
        """Intersection length is 0 → not prime."""
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")

    def test_non_overlapping_intervals(self):
        """Completely disjoint intervals should return NO."""
        self.assertEqual(intersection((1, 1), (2, 2)), "NO")

    def test_prime_length_two(self):
        """Intersection length 2 → prime."""
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

    def test_prime_length_three(self):
        """Intersection length 3 → prime."""
        self.assertEqual(intersection((0, 5), (2, 6)), "YES")

    def test_non_prime_length_one(self):
        """Intersection length 1 → not prime."""
        self.assertEqual(intersection((1, 3), (2, 4)), "NO")


if __name__ == "__main__":
    unittest.main()
