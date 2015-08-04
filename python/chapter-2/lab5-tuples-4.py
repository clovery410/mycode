def deep_len_iter(tup):
    """Return the deep length of the tuple.

    >>> deep_len_iter((1, 2, 3))     #normal tuple
    3
    >>> x = (1, (2, 3), 4)      #deep tuple
    >>> deep_len_iter(x)
    4
    >>> y = ((1, (1, 1)), 1, (1, 1))  #deep tuple
    >>> deep_len_iter(y)
    6
    """
    count = 0
    while tup:
        if type(tup[0]) == tuple:
            tup = tup[0] + tup[1:]
        else:
            count = count + 1
            tup = tup[1:]
    return count

def deep_len_recursive(tup):
    """Return the deep length of the tuple.

    >>> deep_len_recursive((1, 2, 3))   # normal tuple
    3
    >>> x = (1, (2, 3), 4)  # deep tuple
    >>> deep_len_recursive(x)
    4
    >>> y = ((1, (1, 1)), 1, (1, 1))  # deep tuple
    >>> deep_len_recursive(y)
    6
    """
    if not tup:
        return 0
    elif type(tup[0]) == tuple:
        return deep_len_recursive(tup[0]) + deep_len_recursive(tup[1:])
    return 1 + deep_len_recursive(tup[1:])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
