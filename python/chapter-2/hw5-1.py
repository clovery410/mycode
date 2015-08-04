empty_rlist = None

def rlist(first, rest):
    """Construct a recursive list from its first element and the rest."""
    return (first, rest)

def first(s):
    """Return the first element of a recursive list s."""
    return s[0]

def rest(s):
    """Return the rest of the elements of a recursive list s."""
    return s[1]

def reverse_rlist_iterative(s):
    """Return a reversed version of a recursive list s.

    >>> primes = rlist(2, rlist(3, rlist(5, rlist(7, empty_rlist))))
    >>> reverse_rlist_iterative(primes)
    (7, (5, (3, (2, None))))
    """
    reverse_s = None
    while s != empty_rlist:
        reverse_s = rlist(first(s), reverse_s)
        s = rest(s)
    return reverse_s
    
def reverse_rlist_recursive1(s):
    """Return a reversed version of a recursive list s.
    
    >>> primes = rlist(2, rlist(3, rlist(5, rlist(7, empty_rlist))))
    >>> reverse_rlist_recursive1(primes)
    (7, (5, (3, (2, None))))
    """

    if s == None:
        return s
    else:
        return rlist(
            first(s),
            reverse_rlist_recursive1(rest(s)))

def reverse_rlist_recursive(s):
    """Return a reversed version of a recursive list s.
    
    >>> primes = rlist(2, rlist(3, rlist(5, rlist(7, empty_rlist))))
    >>> reverse_rlist_recursive(primes)
    (7, (5, (3, (2, None))))
    """
    def help_func(s, reverse_s):
        if s == empty_rlist:
            return reverse_s
        reverse_s = rlist(first(s), reverse_s)
        return help_func(rest(s), reverse_s)

    return help_func(s, reverse_s = None)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
