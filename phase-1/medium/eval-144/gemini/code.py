import math

def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    # Parse the first fraction x
    num_x_str, den_x_str = x.split('/')
    num_x = int(num_x_str)
    den_x = int(den_x_str)

    # Parse the second fraction n
    num_n_str, den_n_str = n.split('/')
    num_n = int(num_n_str)
    den_n = int(den_n_str)

    # Multiply the fractions: (num_x / den_x) * (num_n / den_n) = (num_x * num_n) / (den_x * den_n)
    result_num = num_x * num_n
    result_den = den_x * den_n

    # Check if the result is a whole number
    # This occurs if the resulting numerator is perfectly divisible by the resulting denominator
    # Using the modulo operator is an efficient way to check for divisibility
    if result_num % result_den == 0:
        return True
    else:
        return False

# Example Usage (from docstring):
# print(f"'1/5', '5/1' -> {simplify('1/5', '5/1')}") # Expected: True
# print(f"'1/6', '2/1' -> {simplify('1/6', '2/1')}") # Expected: False
# print(f"'7/10', '10/2' -> {simplify('7/10', '10/2')}") # Expected: False
# print(f"'2/4', '4/2' -> {simplify('2/4', '4/2')}") # Expected: True (1/2 * 2 = 1)
# print(f"'3/5', '10/3' -> {simplify('3/5', '10/3')}") # Expected: True (3/5 * 10/3 = 30/15 = 2)
# print(f"'5/7', '7/10' -> {simplify('5/7', '7/10')}") # Expected: False (5/7 * 7/10 = 35/70 = 1/2)

