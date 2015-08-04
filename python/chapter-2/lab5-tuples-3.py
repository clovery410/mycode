def merge_iter(tup1, tup2):
    """Merges two sorted tuples.

    >>> merge_iter((1, 3, 5), (2, 4, 6))
    (1, 2, 3, 4, 5, 6)
    >>> merge_iter((), (2, 4, 6))
    (2, 4, 6)
    >>> merge_iter((1, 2, 3), ())
    (1, 2, 3)
    """
    new = ()
    while tup1 and tup2:
        if tup1[0] < tup2[0]:
            new  = new + (tup1[0],)
            tup1 = tup1[1:]
        else:
            new  = new + (tup2[0],)
            tup2  = tup2[1:]
    if tup1:
        return new + tup1
    else:
        return new + tup2

def merge_recursive(tup1, tup2):
    """Merge two sorted tuples.

    >>> merge_recursive((1, 3, 5), (2, 4, 6))
    (1, 2, 3, 4, 5, 6)
    >>> merge_recursive((), (2, 4, 6))
    (2, 4, 6)
    >>> merge_recursive((1, 2, 3), ())
    (1, 2, 3)
    """
    if not tup1 or not tup2:
        return tup1 + tup2
    elif tup1[0] < tup2[0]:
        return (tup1[0],) + merge_recursive(tup1[1:], tup2)
    else:
        return (tup2[0],) + merge_recursive(tup1, tup2[1:])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
