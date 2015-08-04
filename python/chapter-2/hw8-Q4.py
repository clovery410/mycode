class Rlist(object):
    """A recursive list consisting of a first element and the rest.

    >>> s = Rlist(1, Rlist(2, Rlist(3)))
    >>> len(s)
    3
    >>> s[0]
    1
    >>> s[1]
    2
    >>> s[2]
    3
    """
    class EmptyList(object):
        def __len__(self):
            return 0
    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        f = repr(self.first)
        if self.rest is Rlist.empty:
            return 'Rlist({0})'.format(f)
        else:
            return 'Rlist({0}, {1})'.format(f, repr(self.rest))
            
    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.rest[i - 1]

def map_rlist(fn, s):
    """Return an Rlist resulting from mapping fn over the elements of s.

    >>> s = Rlist(1, Rlist(2, Rlist(3)))
    >>> map_rlist(lambda x: x * x, s)
    Rlist(1, Rlist(4, Rlist(9)))
    """
    if s is Rlist.empty:
        return s
    return Rlist(fn(s.first), map_rlist(fn, s.rest))

def deep_map_rlist(fn, s):
    """Return an Rlist with the same structure as s but with fn mapped over its elements. An element that is an Rlist will have fn recursively mapped over its elements.

    >>> s = Rlist(1, Rlist(Rlist(2, Rlist(3)), Rlist(4)))
    >>> deep_map_rlist(lambda x: x * x, s)
    Rlist(1, Rlist(Rlist(4, Rlist(9)), Rlist(16)))
    """
    if s is Rlist.empty:
        return s
    elif type(s) is int:
        return fn(s)
    else:
        return Rlist(deep_map_rlist(fn, s.first), deep_map_rlist(fn, s.rest))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
