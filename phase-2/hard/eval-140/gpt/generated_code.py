import re


def fix_spaces(text: str) -> str:
    """
    Given a string *text*, replace all spaces in it with underscores,
    except when there are **more than two consecutive spaces** – in that
    case, replace the entire run of spaces with a single hyphen “-”.

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
    # Replace every run of one-or-more spaces:
    #   • If its length > 2  → "-"
    #   • Otherwise          → "_" repeated the same length
    return re.sub(
        r' +',
        lambda m: '-' if len(m.group(0)) > 2 else '_' * len(m.group(0)),
        text,
    )
