from math import gcd

def simplify(x: str, n: str) -> bool:
    """
    Determine whether the product of two fractional strings is a whole number.

    Parameters
    ----------
    x : str
        Fraction in the form "numerator/denominator", e.g. "3/4"
    n : str
        Fraction in the form "numerator/denominator", e.g. "2/5"

    Returns
    -------
    bool
        True  – if x * n is an integer  
        False – otherwise

    Examples
    --------
    >>> simplify("1/5", "5/1")
    True
    >>> simplify("1/6", "2/1")
    False
    >>> simplify("7/10", "10/2")
    False
    """
    # Parse the fractions
    x_num, x_den = map(int, x.split("/"))
    n_num, n_den = map(int, n.split("/"))

    # Multiply the fractions: (a/b) * (c/d) = (a*c)/(b*d)
    prod_num = x_num * n_num
    prod_den = x_den * n_den

    # Reduce the product fraction to lowest terms
    g = gcd(prod_num, prod_den)
    prod_den //= g

    # If the reduced denominator is 1, the product is a whole number
    return prod_den == 1
