import math
import operator as op_module

def do_algebra(operator: list, operand: list) -> int:
    """
    Given two lists operator, and operand. The first list has basic algebra 
    operations, and the second list is a list of integers. Use the two given 
    lists to build the algebric expression and return the evaluation of this 
    expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least 
        two operands.

    Args:
        operator: A list of strings representing algebraic operations.
        operand: A list of non-negative integers.

    Returns:
        An integer representing the result of the evaluated expression.
    """

    # Basic validation based on notes
    if not operator or not operand:
        raise ValueError("Operator and operand lists cannot be empty.")
    if len(operator) != len(operand) - 1:
        raise ValueError(
            "Length of operator list must be one less than the length of "
            "operand list."
        )
    if not all(isinstance(x, int) and x >= 0 for x in operand):
         raise ValueError("Operands must be non-negative integers.")

    # Map operator strings to actual functions (safer than eval)
    # Although eval would work given the constraints, this is generally better practice.
    # However, eval directly handles operator precedence, which is complex to replicate manually.
    # Given the prompt's structure and example, building a string and using eval is the most
    # straightforward way to respect standard mathematical operator precedence.

    expression_str = str(operand[0])
    for i in range(len(operator)):
        # Ensure the operator is one of the allowed ones
        if operator[i] not in ['+', '-', '*', '//', '**']:
            raise ValueError(f"Invalid operator found: {operator[i]}")
            
        # Append the operator and the next operand to the string
        # Add spaces for clarity, although eval usually handles it
        expression_str += f" {operator[i]} {str(operand[i+1])}"

    try:
        # Evaluate the constructed string expression
        # Note: Using eval can be risky if inputs are not strictly controlled.
        # In this specific case, we've added checks for allowed operators,
        # and operands are integers, making it relatively safe within the problem's scope.
        result = eval(expression_str)
        
        # Ensure the result is an integer (floor division might produce float in some contexts,
        # though eval with // on integers should yield int in Python 3)
        if not isinstance(result, int):
             # This case might occur if intermediate results become floats, 
             # although standard operations on integers should maintain integer types
             # except for true division (/), which isn't used here.
             # Floor division (//) and exponentiation (**) on integers yield integers
             # (or potentially large integers).
             # We'll explicitly cast just in case, though it might be redundant.
             return int(result) 
        return result

    except Exception as e:
        # Catch potential errors during evaluation (e.g., division by zero if allowed)
        # Although the prompt implies non-negative integers, 0 is possible.
        # Floor division by zero will raise ZeroDivisionError.
        print(f"Error evaluating expression: {expression_str}")
        raise e

# Example usage from the docstring:
# operator_list = ['+', '*', '-']
# operand_list = [2, 3, 4, 5]
# print(do_algebra(operator_list, operand_list)) # Output: 9

# Another example:
# operator_list = ['**', '//']
# operand_list = [2, 3, 6]
# print(do_algebra(operator_list, operand_list)) # Output: 1 (2**3 = 8, 8//6 = 1)
