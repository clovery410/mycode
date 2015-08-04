empty_rlist = None

def rlist(first, rest=empty_rlist):
    return (first, rest)

def first(rlist):
    return rlist[0]

def rest(rlist):
    return rlist[1]

def tup_to_rlist(tup):
    """Converts a tuple to an rlist.

    >>> tup = (1, 2, 3, 4)
    >>> r = tup_to_rlist(tup)
    >>> first(r)
    1
    >>> first(rest(rest(r)))
    3
    >>> r = tup_to_rlist(())
    >>> r is empty_rlist
    True
    """
    if not tup:
        return empty_rlist
    return rlist(tup[0], tup_to_rlist(tup[1:]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
        
