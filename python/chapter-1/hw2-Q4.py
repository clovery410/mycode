def repeated(f, n):
    """Return the function that computes the nth application of f.

    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)
    625
    >>> repeated(square, 4)(5)
    152587890625
    """
    k = 1
    func = f
    def compose1(f, g):
        """Return a function h, such that h(x) = f(g(x))."""
        def h(x):
            return f(g(x))
        return h
    
    while k < n:
        func = compose1(f, func)
        k += 1

    return func

def square(x):
    return x * x

if __name__ == "__main__":
    import doctest
    doctest.testmod()
