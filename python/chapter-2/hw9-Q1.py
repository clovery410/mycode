class Rlist(object):
    class EmptyList(object):
        def __len__(self):
            return 0
    empty = EmptyList()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest
    def __repr__(self):
        args = repr(self.first)
        if self.rest is not Rlist.empty:
            args += ', {0}'.format(repr(self.rest))
        return 'Rlist({0})'.format(args)
    def __len__(self):
        return 1 + len(self.rest)
    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i - 1]

def empty(s):
    return s is Rlist.empty

def adjoin_set2(s, v):
    """Return a set containing all elements of s and element v.

    >>> adjoin_set2(s, 2.5)
    Rlist(1, Rlist(2, Rlist(2.5, Rlist(3))))
    """
    if s.first > v:
        return Rlist(v, s)
    elif s.first == v:
        return s
    rest = adjoin_set2(s.rest, v)
    return Rlist(s.first, rest)

s = Rlist(1, Rlist(2, Rlist(3)))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
