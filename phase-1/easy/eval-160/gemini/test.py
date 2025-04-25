import unittest
from generated_code import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_example_case(self):
        """Tests the example provided in the docstring."""
        operators = ['+', '*', '-']
        operands = [2, 3, 4, 5]
        # Expression: 2 + 3 * 4 - 5 = 2 + 12 - 5 = 9
        self.assertEqual(do_algebra(operators, operands), 9)

    def test_exponentiation_and_floor_division(self):
        """Tests exponentiation and floor division."""
        operators = ['**', '//']
        operands = [2, 3, 6]
        # Expression: 2 ** 3 // 6 = 8 // 6 = 1
        self.assertEqual(do_algebra(operators, operands), 1)

    def test_mixed_operations_precedence(self):
        """Tests operator precedence with mixed operations."""
        operators = ['-', '//', '+', '*']
        operands = [10, 4, 2, 5, 3]
        # Expression: 10 - 4 // 2 + 5 * 3 = 10 - 2 + 15 = 8 + 15 = 23
        self.assertEqual(do_algebra(operators, operands), 23)

    def test_with_zero_operand(self):
        """Tests the function with zero as an operand."""
        operators = ['*', '+', '-']
        operands = [5, 0, 3, 2]
        # Expression: 5 * 0 + 3 - 2 = 0 + 3 - 2 = 1
        self.assertEqual(do_algebra(operators, operands), 1)
        
        operators_div_zero = ['+', '//']
        operands_div_zero = [5, 10, 0]
        # Expression: 5 + 10 // 0 should raise ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            do_algebra(operators_div_zero, operands_div_zero)

    def test_longer_expression(self):
        """Tests a longer sequence of operations."""
        operators = ['+', '*', '//', '-', '**']
        operands = [1, 2, 3, 4, 5, 2]
        # Expression: 1 + 2 * 3 // 4 - 5 ** 2
        # = 1 + 6 // 4 - 25
        # = 1 + 1 - 25
        # = 2 - 25 = -23
        self.assertEqual(do_algebra(operators, operands), -23)

# To run the tests from the command line:
# python -m unittest your_test_file_name.py
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
