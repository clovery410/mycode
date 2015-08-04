def index_largest(seq):
    """Return the index of the largest element in the sequence.
    
    >>> index_largest([8, 5, 7, 3, 1])
    0
    >>> index_largest((4, 3, 7, 2, 1))
    2
    """
    assert len(seq) > 0
    max_i = 0
    max_elem = seq[0]
    for i in range(len(seq)):
        if seq[i] > max_elem:
            max_elem = seq[i]
            max_i = i
    return max_i


if __name__ == "__main__":
    import doctest
    doctest.testmod()
