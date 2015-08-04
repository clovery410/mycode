def reverse_iter(tup):
    """Return the reverse of the given tuple.

    >>> reverse_iter((1, 2, 3, 4))
    (4, 3, 2, 1)
    """
    new = ()
    i = -1
    for _ in tup:
        new = new + (tup[i],)
        i = i - 1
    return new

def reverse_recursive(tup):
    """Return the reverse of the given tuple.

    >>> reverse_recursive((1, 2, 3, 4))
    (4, 3, 2, 1)
    """
    if not tup:
        return ()
    return reverse_recursive(tup[1:]) + (tup[0],) 

if __name__ == "__main__":
    import doctest
    doctest.testmod()
