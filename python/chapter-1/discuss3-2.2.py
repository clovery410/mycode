# 2. Using a lambda function, complete the make_offsetter definition so that it returns a function. The new function should take one argument and returns that argument added to some num.

def make_offsetter(num):
    """
    Returns a function that takes one argument and returns num + some offset.

    >>> x = make_offsetter(3)
    >>> y = make_offsetter(8)
    >>> x(2)
    5
    >>> y(-1)
    7
    """
    return lambda x: num + x


if __name__ == "__main__":
    import doctest
    doctest.testmod()
