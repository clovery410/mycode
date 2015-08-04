def double(f):
    """Return a function that applies f twice.

    f -- a function that takes one argument

    >>> double(square)(2)
    16
    """
    def h(x):
        return f(f(x))
    return h

def square(x):
    return x * x


if __name__ == "__main__":
    import doctest
    doctest.testmod()
