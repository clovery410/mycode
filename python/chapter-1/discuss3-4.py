# 1. Write a higher order function rev_curry2 that reverses the order of the arguments of a curried function.

def rev_curry2(f):
    """
    Return a curried version of the given curried function, with the arguments reversed.

    >>> f = rev_curry2(curry2(lambda x, y: x / y))
    >>> f(4)(2)
    0.5
    >>> f(3)(9)
    3.0
    """
    def h(y):
        def g(x):
            return f(x)(y)
        return g
    return h

def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g


if __name__ == "__main__":
    import doctest
    doctest.testmod()
