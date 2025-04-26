from typing import List

# Mapping from number words to their corresponding numeric values
_NUM_WORD_TO_INT = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

# Reverse mapping for quick lookup back to the word form
_INT_TO_NUM_WORD = {v: k for k, v in _NUM_WORD_TO_INT.items()}


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five',
    'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.

    >>> sort_numbers('three one five')
    'one three five'
    """
    if not numbers:
        return ""

    # Split the incoming string on whitespace and map to integers
    try:
        numeric_values: List[int] = [_NUM_WORD_TO_INT[word] for word in numbers.split()]
    except KeyError as exc:
        raise ValueError(f"Invalid token in input: {exc.args[0]!r}") from None

    # Sort the numeric values and map back to their word representations
    sorted_words: List[str] = [_INT_TO_NUM_WORD[val] for val in sorted(numeric_values)]

    # Join the sorted words back into a space-delimited string
    return " ".join(sorted_words)


if __name__ == "__main__":
    # Simple manual test
    example = "three one five"
    print(f"Input : {example}")
    print(f"Output: {sort_numbers(example)}")
