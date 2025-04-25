import math

def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    # Handle the edge case where n is 1
    # n^k can only be 1 if n is 1.
    if n == 1:
        return x == 1

    # Handle the edge case where x is 1
    # n^0 is 1 for any n != 0 (we already handled n=1)
    # Assuming n > 0 based on examples.
    if x == 1:
        return True

    # Iterate through powers of n
    power = 1
    while power < x:
        power *= n
        # Optimization: if power becomes non-integer due to potential
        # float issues with very large numbers, though unlikely with standard ints
        # if not isinstance(power, int):
        #     return False

    # Check if the final power equals x
    return power == x

# Example usage (based on the docstring)
print(f"is_simple_power(1, 4) => {is_simple_power(1, 4)}")
print(f"is_simple_power(2, 2) => {is_simple_power(2, 2)}")
print(f"is_simple_power(8, 2) => {is_simple_power(8, 2)}")
print(f"is_simple_power(3, 2) => {is_simple_power(3, 2)}")
print(f"is_simple_power(3, 1) => {is_simple_power(3, 1)}")
print(f"is_simple_power(5, 3) => {is_simple_power(5, 3)}")
# Additional test cases
print(f"is_simple_power(9, 3) => {is_simple_power(9, 3)}")
print(f"is_simple_power(27, 3) => {is_simple_power(27, 3)}")
print(f"is_simple_power(10, 3) => {is_simple_power(10, 3)}")
print(f"is_simple_power(16, 4) => {is_simple_power(16, 4)}")
print(f"is_simple_power(1, 1) => {is_simple_power(1, 1)}")
print(f"is_simple_power(100, 1) => {is_simple_power(100, 1)}")
