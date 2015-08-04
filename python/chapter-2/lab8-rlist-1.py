class Rlist(object):
    class EmptyList(object):
        def __len__(self):
            return 0

    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest


def rlist_to_list(rlist):
    """Take an RLIST and returns a Python list with the same elements.

    >>> rlist = Rlist(1, Rlist(2, Rlist(3, Rlist(4))))
    >>> rlist_to_list(rlist)
    [1, 2, 3, 4]
    >>> rlist_to_list(Rlist.empty)
    []
    """
    ##iterative
    # lst = []
    # while rlist is not Rlist.empty:
    #     lst.append(rlist.first)
    #     rlist = rlist.rest
    # return lst


    ##recursive 
    if rlist is Rlist.empty:
        return []
    result, rest = [rlist.first], rlist_to_list(rlist.rest)
    result.extend(rest)
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
