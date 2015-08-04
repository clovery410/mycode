def divide_by_fact(dividend, n):
    """Recursively divise dividend by the factorial of n.
    
    >>> divide_by_fact(120, 4)
    5.0
    """
    if n == 1:
        return dividend
    return divide_by_fact(dividend / n, n - 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
