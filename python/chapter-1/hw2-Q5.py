from operator import add, mul, pow

def zero(f):
    return lambda x: x

def square(x):
    return x * x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    """Church numeral 1."""
    return lambda x: f(x)

def two(f):
    """Church numeral 2."""
    return lambda x: f(f(x))

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    """
    return n(next_num)(0)

def next_num(x):
    return x + 1

def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> three = successor(two)
    >>> church_to_int(add_church(two, three))
    5
    """
    return lambda f: lambda x: n(f)(m(f)(x))
    
    # n = one, m = two
    # = lambda f: lambda x: two(f)(one(f)(x))
    # = lambda f: lambda x: two(f)(f(x))
    # = lambda f: lambda x: (lambda y: f(f(y)))(f(x))
    # = lambda f: lambda x: f(f(f(x)))

def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> three = successor(two)
    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    return lambda f: lambda x: n(m(f))(x)

    # n = three, m = two
    # = lambda f: lambda x: two(three(f))(x)
    # = lambda f: lambda x: two(lambda y: f(f(f(y))))(x)
    # = lambda f: lambda x: (lambda z: (lambda y: f(f(f(y))))((lambda y: f(f(f(y))))(z)))(x)
    # = lambda f: lambda x: (lambda z: (three(f)(three(f)(z))(x)
    # = lambda f: lambda x: (lambda z: f(f(f(f(f(f(z)))))))(x)
    # = lambda f: lambda x: f(f(f(f(f(f(x))))))
    # = lambda x: f(f(f(f(f(f(x))))))

def pow_church(m, n):
    """Return the Church numeral for m ** n, for Church numerals m and n.

    >>> three = successor(two)
    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    return lambda f: lambda x: n(m)(f)(x)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
