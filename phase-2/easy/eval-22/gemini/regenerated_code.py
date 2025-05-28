from typing import List, Any

# adding this prompt the the original prompt, the model generated the correct code:
# Make sure to exclude boolean values (True/False) from the result, as they should not be considered as integers for this function.

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    >>> filter_integers([1, True, 0, False, 4.5, 10])
    [1, 0, 10]
    """
    result = []
    for value in values:
        if isinstance(value, int) and not isinstance(value, bool):
            result.append(value)
    return result
