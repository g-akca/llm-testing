import math

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    odd_digits = {1, 3, 5, 7, 9}

    for num in nums:
        # Check condition 1: Number must be greater than 10
        if num > 10:
            # Since num > 10, it's positive, no need for abs() for digits
            
            # Check condition 3: Last digit must be odd
            last_digit = num % 10
            if last_digit in odd_digits:
                
                # Check condition 2: First digit must be odd
                # Convert to string to easily get the first digit
                s_num = str(num)
                first_digit = int(s_num[0])
                
                if first_digit in odd_digits:
                    # All conditions met
                    count += 1
                    
    return count

