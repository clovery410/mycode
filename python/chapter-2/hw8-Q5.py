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
    >>> s = Rlist(1, Rlist(2, Rlist(3)))
    >>> s.rest.rest.rest = s
    >>> s[20]
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

def has_cycle(s):
    """Return whether Rlist s contains a cycle.

    >>> s = Rlist(1, Rlist(2, Rlist(3, Rlist(4, Rlist(5)))))
    >>> s.rest.rest.rest.rest.rest = s.rest.rest
    >>> has_cycle(s)
    True
    >>> t = Rlist(1, Rlist(2, Rlist(3, Rlist(4, Rlist(5)))))
    >>> has_cycle(t)
    False
    """
    t = s
    while t is not Rlist.empty:
        t = t.rest
        if t is Rlist.empty:
            return False
        t = t.rest
        s = s.rest
        if t == s:
            return True

def has_cycle_constant(s):
    """Return whether Rlist s contains a cycle.

    >>> s = Rlist(1, Rlist(2, Rlist(3, Rlist(4, Rlist(5)))))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Rlist(1, Rlist(2, Rlist(3, Rlist(4, Rlist(5)))))
    >>> has_cycle_constant(t)
    False
    """
    t = s
    while t is not Rlist.empty:
        t = t.rest
        if t is Rlist.empty:
            return False
        t = t.rest
        s = s.rest
        if t == s:
            return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
