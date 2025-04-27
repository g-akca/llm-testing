import unittest
# Assuming the code is saved in a file named 'main.py'
# If not, replace 'main' with the actual filename
from generated_code import intersection

class TestIntersection(unittest.TestCase):

    def test_example_1(self):
        """Tests intersection((1, 2), (2, 3)) -> NO (length 0)"""
        self.assertEqual(intersection((1, 2), (2, 3)), "NO")

    def test_example_2(self):
        """Tests intersection((-1, 1), (0, 4)) -> NO (length 1)"""
        self.assertEqual(intersection((-1, 1), (0, 4)), "NO")

    def test_example_3_prime(self):
        """Tests intersection((-3, -1), (-5, 5)) -> YES (length 2)"""
        self.assertEqual(intersection((-3, -1), (-5, 5)), "YES")

    def test_no_intersection(self):
        """Tests intervals that do not intersect"""
        self.assertEqual(intersection((5, 10), (1, 4)), "NO")
        self.assertEqual(intersection((1, 2), (3, 4)), "NO")

    def test_prime_length_greater_than_2(self):
        """Tests intersection with a prime length > 2"""
        # Intersection is (2, 5), length is 3 (prime)
        self.assertEqual(intersection((1, 5), (2, 6)), "YES")
        # Intersection is (3, 8), length is 5 (prime)
        self.assertEqual(intersection((0, 8), (3, 10)), "YES")

# This allows running the tests directly from the command line
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
