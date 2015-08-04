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


class Tree(object):
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

def set_contains3(s, v):
    """Return true if set s contains value v as an element.

    >>> t = Tree(2, Tree(1), Tree(3))
    >>> set_contains3(t, 3)
    True
    >>> set_contains3(t, 0)
    False
    >>> set_contains3(big_tree(20, 60), 34)
    True
    """
    if s is None:
        return False
    if s.entry == v:
        return True
    if s.entry < v:
        return set_contains3(s.right, v)
    if s.entry > v:
        return set_contains3(s.left, v)

def adjoin_set3(s, v):
    """Return a set containing all elements of s and element v.

    >>> b = big_tree(0, 9)
    >>> b
    Tree(4, Tree(1), Tree(7, None, Tree(9)))
    >>> adjoin_set3(b, 5)
    Tree(4, Tree(1), Tree(7, Tree(5), Tree(9)))
    """
    if s is None:
        return Tree(v)
    if s.entry == v:
        return s
    if s.entry < v:
        return Tree(s.entry, s.left, adjoin_set3(s.right, v))
    if s.entry > v:
        return Tree(s.entry, adjoin_set3(s.left, v), s.right)

def depth(s, v):
    """Return the depth of the value v in tree set s.

    The depth of a value is the number of branches followed to reach the value.
    The depth of the root of a tree is always 0.

    >>> b = big_tree(0, 9)
    >>> depth(b, 4)
    0
    >>> depth(b, 7)
    1
    >>> depth(b, 9)
    2
    """
    d = 0
    while v != s.entry and s is not None:
        if v < s.entry:
            s = s.left
        elif v > s.entry:
            s = s.right
        d += 1
    if v == s.entry:
        return d
    else:
        print('Index out of bounds.')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
