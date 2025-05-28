import collections

def reverse_delete(s, c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    # Create a set of characters to delete for efficient O(1) average time lookup
    chars_to_delete = set(c)

    # Build the result string by keeping only characters not in chars_to_delete
    # Using a generator expression with ''.join() is generally efficient
    result_s = "".join(char for char in s if char not in chars_to_delete)

    # Check if the resulting string is a palindrome
    # A string is a palindrome if it reads the same forwards and backwards
    is_palindrome = result_s == result_s[::-1]

    # Return the tuple containing the result string and the boolean check
    return (result_s, is_palindrome)

