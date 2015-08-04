from operator import mul, sub
#fact = lambda n: 1 if n == 1 else mul(n, fact(sub(n, 1)))
#print(fact(5))

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    
    return lambda n: 1 if n == 1 else mul(n, make_anonymous_factorial()(sub(n, 1)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
