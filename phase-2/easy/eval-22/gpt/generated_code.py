from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter the given list for elements that are plain integers
    (booleans are excluded since `bool` is a subclass of `int`).

    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [item for item in values
            if isinstance(item, int) and not isinstance(item, bool)]


if __name__ == "__main__":
    # Quick sanity checks
    print(filter_integers(['a', 3.14, 5]))             # -> [5]
    print(filter_integers([1, 2, 3, 'abc', {}, []]))   # -> [1, 2, 3]
