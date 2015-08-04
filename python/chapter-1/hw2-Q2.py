from operator import add, mul
def accumulate(combiner, start, n, term):
    """Return the result of combining the first n terms in a sequence."""
    k = start
    total = term(k)
    while k < n:
        k = k + 1
        total = combiner(total, term(k))
    return total

def square(x):
    return x * x

def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate.

    >>> summation_using_accumulate(4, square)
    30
    """
    return accumulate(add, 1, n, term)

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    """
    return accumulate(mul, 1, n, term)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
