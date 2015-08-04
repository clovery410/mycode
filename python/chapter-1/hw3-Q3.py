def g(n):
    """Return the value of G(n), computed recursively.
    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n <=3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.
    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    def g_total(a, b, c, count):
        while count > 1:
            a, b, c = a + 2 * b + 3 * c, a, b
            count = count - 1
        return c

    def g_total_1(a, b, c, count):
        if count == 1:
            return c
        elif count == 2:
            return b
        elif count == 3:
            return a
        else:
            while count > 3:
                a, b, c = a + 2 * b + 3 * c, a, b
                count = count - 1
        return a
    return g_total_1(3, 2, 1, n)
            
if __name__ == "__main__":
    import doctest
    doctest.testmod()

print(g(8))
print(g_iter(8))
print(g_iter(1))
print(g_iter(2))
print(g_iter(3))
print(g_iter(4))
print(g_iter(5))
