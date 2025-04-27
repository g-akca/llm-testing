import collections.abc

def check_dict_case(dict_input):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if not dict_input:  # Check if the dictionary is empty
        return False

    all_keys_lower = True
    all_keys_upper = True

    for key in dict_input.keys():
        if not isinstance(key, str):
            return False  # Found a non-string key, immediately return False

        # Check if the current key breaks the all_lower condition
        if not key.islower():
            all_keys_lower = False

        # Check if the current key breaks the all_upper condition
        if not key.isupper():
            all_keys_upper = False

        # Optimization: If neither condition can possibly be true anymore, exit early
        if not all_keys_lower and not all_keys_upper:
            return False

    # If the loop completes, it means all keys were strings.
    # Return True if either all keys were lower OR all keys were upper.
    return all_keys_lower or all_keys_upper

