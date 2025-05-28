import unittest
from generated_code import sort_numbers

class TestSortNumbers(unittest.TestCase):

    def test_basic_sorting(self):
        """Tests sorting a simple string of numbers."""
        self.assertEqual(sort_numbers('three one five'), 'one three five')
        self.assertEqual(sort_numbers('two four zero'), 'zero two four')

    def test_full_range_reverse(self):
        """Tests sorting all numbers from nine down to zero."""
        input_str = 'nine eight seven six five four three two one zero'
        expected_str = 'zero one two three four five six seven eight nine'
        self.assertEqual(sort_numbers(input_str), expected_str)

    def test_with_duplicates(self):
        """Tests sorting a string containing duplicate numbers."""
        self.assertEqual(sort_numbers('one three one two three'), 'one one two three three')
        self.assertEqual(sort_numbers('nine nine eight'), 'eight nine nine')

    def test_single_number(self):
        """Tests sorting a string with only one number."""
        self.assertEqual(sort_numbers('eight'), 'eight')
        self.assertEqual(sort_numbers('zero'), 'zero')

    def test_empty_string(self):
        """Tests sorting an empty input string."""
        self.assertEqual(sort_numbers(''), '')
        # Also test with only spaces
        self.assertEqual(sort_numbers('   '), '')

    def test_extra_spaces(self):
        """Tests sorting with multiple spaces between numbers."""
        self.assertEqual(sort_numbers(' six  two   nine '), 'two six nine')


# This allows running the tests directly when the script is executed
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
