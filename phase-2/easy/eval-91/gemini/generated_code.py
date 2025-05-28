import re

def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.

    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    >>> is_bored("I think. Therefore I am.")
    1
    >>> is_bored("I. I? I!")
    3
    >>> is_bored("   I am happy.  But I am also tired.")
    2
    >>> is_bored("No sentences here")
    0
    >>> is_bored("")
    0
    """
    # Split the string into potential sentences using '.', '?', or '!' as delimiters
    # The regex '[.?!]' matches any one of the characters inside the brackets.
    sentences = re.split(r"[.?!]", S)

    boredom_count = 0
    for sentence in sentences:
        # Remove leading/trailing whitespace from the potential sentence
        trimmed_sentence = sentence.strip()

        # Check if the trimmed sentence is not empty and starts with "I"
        # We need to check for "I " (followed by a space) or just "I"
        # (if the sentence is only "I").
        if trimmed_sentence: # Ensure it's not an empty string resulting from split
            if trimmed_sentence == "I" or trimmed_sentence.startswith("I "):
                boredom_count += 1

    return boredom_count

# Example Usage (from docstring):
# print(is_bored("Hello world"))
# print(is_bored("The sky is blue. The sun is shining. I love this weather"))
# print(is_bored("I think. Therefore I am."))
# print(is_bored("I. I? I!"))
# print(is_bored("   I am happy.  But I am also tired."))
# print(is_bored("No sentences here"))
# print(is_bored(""))
