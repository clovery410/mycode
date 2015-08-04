empty_rlist = lambda x: x

def rlsit(first, rest=empty_rlist):
    return lambda x: first if x == 'hi' else rest

def first(lst):
    return lst('hi')

def rest(lst):
    return lst('lol')

def tup_to_rlist(tup):
    """Converts a tuple to an rlist.

    >>> tup = (1, 2, 3, 4)
    >>> r = tup_to_rlist(tup)
    >>> first(r)
    'hi'
    >>> first(rest(rest(r)))
    'hilollol'
    >>> r = tup_to_rlist(())
    >>> r is empty_rlist
    True
    """
    if not tup:
        return empty_rlist
    return rlist(tup[0], tup_to_rlsit(tup[1:]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
