empty_rlist = None

def rlist(first, rest):
    return (first, rest)

def first(s):
    return s[0]

def rest(s):
    return s[1]

def len_rlist(s):
    length = 0
    while s != empty_rlist:
        s, length = rest(s), length + 1
    return length

def reverse_rlist_iterative(s):
    reverse_s= None
    while s != empty_rlist:
        reverse_s = rlist(first(s), reverse_s)
        s = rest(s)
    return reverse_s

def append(s, num):
    return reverse_rlist_iterative(rlist(num, reverse_rlist_iterative(s)))

def append_rlist(s0, s1):
    """
    >>> evens = rlist(2, rlist(4, rlist(6, rlist(8, empty_rlist))))
    >>> odds = rlist(1, rlist(3, empty_rlist))
    >>> append_rlist(odds, evens)
    (1, (3, (2, (4, (6, (8, None))))))
    """
    if s1 == empty_rlist:
        return s0
    return append_rlist(append(s0, first(s1)), rest(s1))

def interleave_recursive(s0, s1):
    """Interleave recursive lists s0 and s1 to produce a new recursive list.

    >>> evens = rlist(2, rlist(4, rlist(6, rlist(8, empty_rlist))))
    >>> odds = rlist(1, rlist(3, empty_rlist))
    >>> interleave_recursive(odds, evens)
    (1, (2, (3, (4, (6, (8, None))))))
    >>> interleave_recursive(evens, odds)
    (2, (1, (4, (3, (6, (8, None))))))
    >>> interleave_recursive(odds, odds)
    (1, (1, (3, (3, None))))
    """
    def interleave_help(s0, s1, interleave_s, n):
        if s0 == empty_rlist and s1 == empty_rlist:
            return interleave_s

        elif n % 2 == 0:
            if s0 == empty_rlist:
                interleave_s = rlist(first(s1), interleave_s)
                return interleave_help(s0, rest(s1), interleave_s, n)
            interleave_s = rlist(first(s0), interleave_s)
            return interleave_help(rest(s0), s1, interleave_s, n+1)

        else:
            if s1 == empty_rlist:
                interleave_s = rlist(first(s0), interleave_s)
                return interleave_help(rest(s0), s1, interleave_s, n)
            interleave_s = rlist(first(s1), interleave_s)
            return interleave_help(s0, rest(s1), interleave_s, n+1)

    ss = interleave_help(s0, s1, interleave_s=None, n=0)
    return reverse_rlist_iterative(ss)

def interleave_iterative(s0, s1):
    """Interleave recursive lists s0 and s1 to produce a new recursive list.

    >>> evens = rlist(2, rlist(4, rlist(6, rlist(8, empty_rlist))))
    >>> odds = rlist(1, rlist(3, empty_rlist))
    >>> interleave_iterative(odds, evens)
    (1, (2, (3, (4, (6, (8, None))))))
    >>> interleave_iterative(evens, odds)
    (2, (1, (4, (3, (6, (8, None))))))
    >>> interleave_iterative(odds, odds)
    (1, (1, (3, (3, None))))
    """
    interleave_s = None
    if len_rlist(s0) > len_rlist(s1):
        while s0 != empty_rlist:
            while s1 != empty_rlist:
                interleave_s = rlist(first(s0), interleave_s)
                s0 = rest(s0)
                interleave_s = rlist(first(s1), interleave_s)
                s1 = rest(s1)
            interleave_s = rlist(first(s0), interleave_s)
            s0 = rest(s0)
    while s1 != empty_rlist:
        while s0 != empty_rlist:
            interleave_s = rlist(first(s0), interleave_s)
            s0 = rest(s0)
            interleave_s = rlist(first(s1), interleave_s)
            s1 = rest(s1)
            if s1 == empty_rlist:
                return reverse_rlist_iterative(interleave_s)
        interleave_s = rlist(first(s1), interleave_s)
        s1 = rest(s1)

    return reverse_rlist_iterative(interleave_s)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    
