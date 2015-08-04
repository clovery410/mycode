class Rlist(object):
    """A mutable rlist class.

    >>> r = Rlist(3, Rlist(2, Rlist(1)))
    >>> len(r)
    3
    >>> len(r.rest)
    2
    >>> r[0]
    3
    >>> r[1]
    2
    >>> Rlist(1, Rlist(2, Rlist(3)))
    Rlist(1, Rlist(2, Rlist(3)))
    >>> Rlist(1)
    Rlist(1)
    >>> repr(Rlist(1))
    'Rlist(1)'
    """
    class EmptyList(object):
        def __len__(self):
            return 0
    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __len__(self):
        return 1 + len(self.rest)
    
    ##iterative
    # def __len__(self):
    #     lenght = 0
    #     curr = self
    #     while curr is not Rlist.empty:
    #         length = length + 1
    #         curr = curr.rest
    #     return length

    def __getitem__(self, index):
        if index == 0:
            return self.first
        elif self.rest is Rlist.empty:
            print('Index out of bounds')
        else:
            return self.rest[index - 1]
        
    ## iterative
    # def __getitem__(self, index):
    #     curr = self
    #     while index > 0 and curr is not Rlist.empty:
    #         curr = curr.rest
    #         index = index - 1
    #     if curr is Rlist.empty:
    #         print('Index out of bounds')
    #     else:
    #         return curr.first

    def __repr__(self):
        if self.rest is Rlist.empty:
            return 'Rlist({0})'.format(self.first)
        else:
            rest = repr(self.rest)
        return 'Rlist({0}, {1})'.format(self.first, rest)

def insert(rlist, value, index):
    """Insert VALUE into the RLIST at the given INDEX.

    >>> rlist = Rlist(1, Rlist(2, Rlist(3)))
    >>> insert(rlist, 9001, 0)
    >>> rlist
    Rlist(9001, Rlist(1, Rlist(2, Rlist(3))))
    >>> insert(rlist, 100, 2)
    >>> rlist
    Rlist(9001, Rlist(1, Rlist(100, Rlist(2, Rlist(3)))))
    """
    ## recursive
    # if index == 0:
    #     rlist.rest = Rlist(rlist.first, rlist.rest)
    #     rlist.first = value
    # elif rlist.rest is Rlist.empty:
    #     print('Index out of bounds')
    # else:
    #     return insert(rlist.rest, value, index - 1)

    ## interative
    while index > 0 and rlist.rest is not Rlist.empty:
        rlist = rlist.rest
        index = index - 1
    if index == 0:
        rlist.rest = Rlist(rlist.first, rlist.rest)
        rlist.first = value
    else:
        print('Index out of bounds')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
