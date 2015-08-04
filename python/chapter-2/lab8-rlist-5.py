class Rlist(object):
    class EmptyList(object):
        def __len__(self):
            return 0
    
    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __len__(self):
        return 1 + len(self.rest)

    def __getitem__(self, index):
        if index == 0:
            return self.first
        elif self.rest is Rlist.empty:
            print('Index out of bounds')
        else:
            return self.rest[index - 1]
    
    def __repr__(self):
        if self.rest is Rlist.empty:
            return 'Rlist({0})'.format(self.first)
        else:
            rest = repr(self.rest)
            return 'Rlist({0}, {1})'.format(self.first, rest)


def reverse(rlist):
    """Return an Rlist that is the reverse of the original.

    >>> Rlist(1).rest is Rlist.empty
    True
    >>> rlist = Rlist(1, Rlist(2, Rlist(3)))
    >>> reverse(rlist)
    Rlist(3, Rlist(2, Rlist(1)))
    >>> reverse(Rlist(1))
    Rlist(1)
    """
    ## iterative
    new = Rlist.empty
    while rlist is not Rlist.empty:
        new = Rlist(rlist.first, new)
        rlist = rlist.rest
    return new

    ## recursive
    if rlist.rest is not Rlist.empty:
        second, last = rlist.rest, rlist
        rlist = reverse(second)
        second.rest, last.rest = last, Rlist.empty
    return rlist

if __name__ == "__main__":
    import doctest
    doctest.testmod()
