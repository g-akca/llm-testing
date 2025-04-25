import unittest
from generated_code import can_arrange

class TestCanArrange(unittest.TestCase):

    def test_example_1(self):
        """Tests the first example provided in the docstring."""
        self.assertEqual(can_arrange([1, 2, 4, 3, 5]), 3)

    def test_example_2(self):
        """Tests the second example (sorted array) provided in the docstring."""
        self.assertEqual(can_arrange([1, 2, 3]), -1)

    def test_empty_array(self):
        """Tests an empty array."""
        self.assertEqual(can_arrange([]), -1)

    def test_single_element_array(self):
        """Tests an array with a single element."""
        self.assertEqual(can_arrange([10]), -1)

    def test_descending_order(self):
        """Tests an array sorted in descending order."""
        self.assertEqual(can_arrange([5, 4, 3, 2, 1]), 4)

    def test_multiple_out_of_order(self):
        """Tests an array with multiple out-of-order elements, expecting the largest index."""
        self.assertEqual(can_arrange([1, 5, 3, 8, 4, 9]), 4)


# To run the tests from the command line:
# python -m unittest your_test_file_name.py
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
