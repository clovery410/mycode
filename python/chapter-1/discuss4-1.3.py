# Write a procedure expt(base, power), which implements the exponent function. For example, expt(3, 2) returns 9, and expt(2, 3) returns 8. Use recursion.
def expt(base, power):
    """
    >>> expt(3, 2)
    9
    >>> expt(2, 3)
    8
    """
    if power == 0:
        return 1
    elif power < 0:
        return expt(base, power + 1) / base
    else:
        return expt(base, power - 1) * base


if __name__ == "__main__":
    import doctest
    doctest.testmod()
