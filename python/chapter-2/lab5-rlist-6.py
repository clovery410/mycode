empty_rlist = None

def rlist(first, rest=empty_rlist):
    return (first, rest)

def first(rlist):
    return rlist[0]

def rest(rlist):
    return rlist[1]

def tup_to_rlist(tup):
    if not tup:
        return empty_rlist
    return rlist(tup[0], tup_to_rlist(tup[1:]))

def len_rlist(lst):
    """Return the length of the rlist.

    >>> lst = tup_to_rlist((1, 2, 3, 4))
    >>> len_rlist(lst)
    4
    >>> lst = tup_to_rlist(())
    >>> len_rlist(lst)
    0
    """
    if not lst:
        return 0
    return 1 + len_rlist(rest(lst))

def getitem_rlist(i, lst):
    """Return the ith item in the rlist. If the index exceeds the length of the rlist, return 'Error'.

    >>> lst = tup_to_rlist((1, 2, 3, 4))
    >>> getitem_rlist(0, lst)
    1
    >>> getitem_rlist(3, lst)
    4
    >>> getitem_rlist(4, lst)
    'Error'
    """
    if i > len_rlist(lst) - 1:
        return 'Error'
    elif i == 0:
        return first(lst)
    else:
        return getitem_rlist(i - 1, rest(lst))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
