class Rlist(object):
    class EmptyList(object):
        def __len__(self):
            return 0

    empty = EmptyList()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Rlist.empty:
            return 'Rlist({0})'.format(self.first)
        else:
            rest = repr(self.rest)
            return 'Rlist({0}, {1})'.format(self.first, rest)

def rlist_to_list(rlist):
    if rlist is Rlist.empty:
        return []
    result = [rlist.first]
    rest = rlist_to_list(rlist.rest)
    result.extend(rest)
    return result

def extend_lst(lst1, lst2):
    lst1.extend(lst2)

def extend_rlist_to_lst(lst, rlist):
    lst.extend(rlist_to_list(rlist))

def extend_lst_to_rlist(rlist, lst):
    if len(lst) == 0:
        return
    elif rlist.rest is Rlist.empty:
        rlist.rest = Rlist(lst[0])
        lst = lst[1:]
    extend_lst_to_rlist(rlist.rest, lst)

def extend_rlist(rlist1, rlist2):
    if rlist1.rest is Rlist.empty:
        rlist1.rest = rlist2
    else:
        extend_rlist(rlist1.rest, rlist2)

def type_tag(x):
    return type_tag.tags[type(x)]

type_tag.tags = {list: 'list', Rlist: 'Rlist'}

def extend(seq1, seq2):
    """Takes the elements of seq2 and adds them to the end of seq1.

    >>> rlist = Rlist(4, Rlist(5, Rlist(6)))
    >>> lst = [1, 2, 3]
    >>> extend(lst, rlist)
    >>> lst
    [1, 2, 3, 4, 5, 6]
    >>> rlist
    Rlist(4, Rlist(5, Rlist(6)))
    >>> extend(rlist, [7, 8])
    >>> rlist
    Rlist(4, Rlist(5, Rlist(6, Rlist(7, Rlist(8)))))
    >>> extend(lst, [7, 8, 9])
    >>> lst
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    types = (type_tag(seq1), type_tag(seq2))
    return extend.impl[types](seq1, seq2)

extend.impl = {('list', 'list'): extend_lst, ('list', 'Rlist'): extend_rlist_to_lst, ('Rlist', 'list'): extend_lst_to_rlist, ('Rlist', 'Rlist'): extend_rlist}


if __name__ == "__main__":
    import doctest
    doctest.testmod()
