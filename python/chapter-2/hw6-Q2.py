def group(seq):
    """Divide a sequenceof of at least 12 elements into groups of 4 or 5. Groups of 5 will be at the end. Return a tuple of sequences, each corresponding to a group.

    >>> group(range(14))
    (range(0, 4), range(4, 9), range(9, 14))
    >>> group(tuple(range(17)))
    ((0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15, 16))
    """
    num = len(seq)
    assert num >= 12
    i = 0
    new = ()
    tail = ()
    # if num % 4 != 0:
    #     return group(seq[:-5]) + (seq[-5:],)
    # else:
    #    while i < num:
    #        new = new + (seq[i:i+4],)
    #        i = i + 4
    
    if num % 4 == 1:
        tail = (seq[-5:],)
        j = num - 5
    elif num % 4 == 2:
        tail = (seq[-10:-5],) + (seq[-5:],)
        j = num - 10
    elif num % 4 == 3:
        tail = (seq[-15:-1],) + (seq[-10:-5],) + (seq[-5:],)
        j = num - 15
    
    while i < j:
        new = new + (seq[i:i+4],)
        i = i + 4

    return new + tail

if __name__ == "__main__":
    import doctest
    doctest.testmod()
