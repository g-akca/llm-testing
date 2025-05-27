def check_dict_case(dct):
    """
    Given a dictionary, return True if **all** keys are strings that are
    either entirely lower-case **or** entirely upper-case.  
    Return False otherwise, including the case where the dictionary is empty.

    Examples
    --------
    >>> check_dict_case({"a": "apple", "b": "banana"})
    True
    >>> check_dict_case({"a": "apple", "A": "banana", "B": "banana"})
    False
    >>> check_dict_case({"a": "apple", 8: "banana", "a": "again"})
    False
    >>> check_dict_case({"Name": "John", "Age": "36", "City": "Houston"})
    False
    >>> check_dict_case({"STATE": "NC", "ZIP": "12345"})
    True
    """
    # The dictionary must be non-empty
    if not dct:
        return False

    # All keys must be strings
    if not all(isinstance(k, str) for k in dct):
        return False

    # Check whether all keys are lower-case strings
    all_lower = all(k == k.lower() for k in dct)

    # Check whether all keys are upper-case strings
    all_upper = all(k == k.upper() for k in dct)

    return all_lower or all_upper
