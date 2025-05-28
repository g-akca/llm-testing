import unittest
from generated_code import specialFilter

class TestSpecialFilter(unittest.TestCase):

    def test_example_1(self):
        """Tests the first example from the docstring."""
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)

    def test_example_2(self):
        """Tests the second example from the docstring."""
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

    def test_empty_list(self):
        """Tests an empty input list."""
        self.assertEqual(specialFilter([]), 0)

    def test_no_qualifying_numbers(self):
        """Tests a list with numbers that don't meet the criteria."""
        self.assertEqual(specialFilter([1, 5, 10, 12, 21, 24, 42, -11, -35]), 0)
        
    def test_all_qualifying_numbers(self):
        """Tests a list where all numbers meet the criteria."""
        self.assertEqual(specialFilter([11, 33, 55, 77, 99, 131, 353, 979]), 8)

# To run the tests if the script is executed directly
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
