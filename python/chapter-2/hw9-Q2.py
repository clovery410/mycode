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
    return len(s) == 0

def set_contains2(s, v):
    """Return true if set s contains value v as an element.

    >>> set_contains2(s, 2)
    True
    >>> set_contains2(s, 5)
    False
    """
    if empty(s) or s.first > v:
        return False
    if s.first == v:
        return True
    return set_contains2(s.rest, v)

def intersect_set2(set1, set2):
    """Return a set containing all elements common to set1 and set2.

    >>> t = Rlist(2, Rlist(3, Rlist(4)))
    >>> intersect_set2(s, t)
    Rlist(2, Rlist(3))
    """
    if empty(set1) or empty(set2):
        return Rlist.empty
    e1, e2 = set1.first, set2.first
    if e1 == e2:
        return Rlist(e1, intersect_set2(set1.rest, set2.rest))
    if e1 < e2:
        return intersect_set2(set1.rest, set2)
    if e2 < e1:
        return intersect_set2(set1, set2.rest)

def union_set2(set1, set2):
    """Return a set containing all elements either in set1 or set2.

    >>> t = Rlist(1, Rlist(3, Rlist(5)))
    >>> union_set2(s, t)
    Rlist(1, Rlist(2, Rlist(3, Rlist(5))))
    """
    if empty(set1):
        return set2
    elif empty(set2):
        return set1
    elif set1.first == set2.first:
        rest = union_set2(set1.rest, set2.rest)
        return Rlist(set1.first, rest)
    elif set1.first < set2.first:
        rest = union_set2(set1.rest, set2)
        return Rlist(set1.first, rest)
    elif set1.first > set2.first:
        rest = union_set2(set1, set2.rest)
        return Rlist(set2.first, rest)

s = Rlist(1, Rlist(2, Rlist(3)))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
