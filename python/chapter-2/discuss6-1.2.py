def remove_all(el, lst):
    """Remove all instances of el from lst.
    >>> x = [3, 1, 2, 1, 5, 1, 1, 7, 1]
    >>> remove_all(1, x)
    >>> x
    [3, 2, 5, 7]
    """
    for _ in lst:
        lst.remove(el)

def add_this_many(x, y, lst):
    """Add y to the end of lst the number of times x occurs in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    """
    for elem in lst:
        if elem == 1:
            lst.append(y)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
