import re

def fix_spaces(text: str) -> str:
    """
    Replace spaces in *text* according to the rules:

    1. A single space → "_"
    2. A run of exactly two spaces → "__"
    3. A run of **three or more** consecutive spaces → "-"

    Examples
    --------
    >>> fix_spaces("Example")
    'Example'
    >>> fix_spaces("Example 1")
    'Example_1'
    >>> fix_spaces(" Example 2")
    '_Example_2'
    >>> fix_spaces(" Example   3")
    '_Example-3'
    """
    def _sub(match: re.Match) -> str:
        spaces = match.group(0)
        return "-" if len(spaces) > 2 else "_" * len(spaces)

    # Substitute every run of spaces with the appropriate replacement
    return re.sub(r" +", _sub, text)
