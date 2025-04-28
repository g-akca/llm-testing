import sys
# Ensure compatibility with Python 3.7 by not using features introduced later
# The provided type hint `List` is imported but not directly used in the
# function signature `(numbers: str) -> str`, which is correct for the task.
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    >>> sort_numbers('nine eight seven six five four three two one zero')
    'zero one two three four five six seven eight nine'
    >>> sort_numbers('one one two three')
    'one one two three'
    >>> sort_numbers('eight')
    'eight'
    >>> sort_numbers('')
    ''
    """
    # Mapping from word to its integer value
    word_to_val: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string by spaces. Handles multiple spaces between words.
    # Filters out empty strings that might result from multiple spaces.
    words = [word for word in numbers.split(' ') if word]

    if not words:
        return "" # Return empty string if input is empty or only spaces

    # Sort the list of words using the integer value as the key
    # The lambda function looks up the value for each word in the dictionary
    sorted_words = sorted(words, key=lambda word: word_to_val[word])

    # Join the sorted words back into a single string delimited by spaces
    return ' '.join(sorted_words)

# Example of running the doctests if the script is executed directly
if __name__ == '__main__':
    import doctest
    # Use sys.stdout.write for compatibility if needed, though print usually works
    # Check Python version for compatibility if necessary, but doctest is standard
    results = doctest.testmod()
    if results.failed == 0:
         print("All doctests passed.")
    else:
         print(f"{results.failed} doctests failed.")
         # Exit with a non-zero status code to indicate failure
         # sys.exit(1) # Uncomment if running in an environment where exit code matters
