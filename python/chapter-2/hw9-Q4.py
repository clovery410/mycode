class Rlist(object):
    """A recursive list consisting of a first element and the rest."""

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
        return self.rest[i-1]

class Tree(object):
    """A tree with internal values."""

    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right

    def __repr__(self):
        args = repr(self.entry)
        if self.left or self.right:
            args += ', {0}, {1}'.format(repr(self.left), repr(self.right))
        return 'Tree({0})'.format(args)

def big_tree(left, right):
    """Return a tree of elements between left and right.

    >>> big_tree(0, 12)
    Tree(6, Tree(2, Tree(0), Tree(4)), Tree(10, Tree(8), Tree(12)))
    """
    if left > right:
        return None
    split = left + (right - left)//2
    return Tree(split, big_tree(left, split-2), big_tree(split+2, right))

def tree_to_ordered_sequence(s):
    """Return an ordered sequence containing the elements of tree set s.

    >>> b = big_tree(0, 9)
    >>> tree_to_ordered_sequence(b)
    Rlist(1, Rlist(4, Rlist(7, Rlist(9))))
    """
    if s.left is None and s.right is None:
        return s.entry
    if s.left is None and s.right is not None:
        right = tree_to_ordered_sequence(s.right)
        return Rlist(s.entry, Rlist(right))
    elif s.left is not None and s.right is None:
        left = tree_to_ordered_sequence(s.left)
        return Rlist(left, Rlist(s.entry))
    else:
        left = tree_to_ordered_sequence(s.left)
        right = tree_to_ordered_sequence(s.right)
        return Rlist(left, Rlist(s.entry, right))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
