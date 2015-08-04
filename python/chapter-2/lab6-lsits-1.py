def add_matrices(a, b):
    """
    >>> add_matrices([[1, 3], [2, 0]], [[-3, 0], [1, 2]])
    [[-2, 3], [3, 2]]
    """
    assert len(a) == len(b)
    return [[a[x][y] + b[x][y] for y in range(len(a[0]))] for x in range(len(a))]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
