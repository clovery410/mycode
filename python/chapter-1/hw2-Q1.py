def product(n, term):
    """Return the product of the first n terms in a sequence.

    term -- a function that takes one argument

    >>> product(4, square)
    576
    """
    total, k = 1, 1
    while k <= n:
        total, k = total * term(k), k + 1
    return total

def square(x):
    return x * x


def factorial(n):
    """Return n factorial by calling product.

    >>> factorial(4)
    24
    """
    return product(n, identity)

def identity(k):
    return k


if __name__ == "__main__":
    import doctest
    doctest.testmod()
