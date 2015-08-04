def make_fib():
    """Write a function make_fib that returns a function that returns the next Fibonacci number each time it is called.
    >>> fib = make_fib()
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib()
    5
    >>> fib()
    8
    """
    pred = 0
    curr = 1
    def fib():
        nonlocal pred, curr
        pred, curr = curr, pred + curr
        return pred
    return fib


if __name__ == "__main__":
    import doctest
    doctest.testmod()
        
