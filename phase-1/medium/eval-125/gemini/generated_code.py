import string

def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3
    '''
    # Check for any whitespace character
    has_whitespace = any(c.isspace() for c in txt)

    if has_whitespace:
        # Split on whitespace (default behavior of split())
        return txt.split()
    elif ',' in txt:
        # Split on commas if no whitespace exists
        return txt.split(',')
    else:
        # Count lowercase letters with odd alphabetical order
        count = 0
        for char in txt:
            # Check if the character is a lowercase letter
            if 'a' <= char <= 'z':
                # Calculate 0-based order (a=0, b=1, ...)
                order = ord(char) - ord('a')
                # Check if the order is odd
                if order % 2 != 0:
                    count += 1
        return count

