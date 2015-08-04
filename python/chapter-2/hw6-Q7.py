def make_accumulator_nonlocal():
    """Return an accumulator function that takes a single numeric argument and accumulates that argument into total, then returns total.

    >>> acc = make_accumulator_nonlocal()
    >>> acc(15)
    15
    >>> acc(10)
    25
    >>> acc2 = make_accumulator_nonlocal()
    >>> acc2(7)
    7
    >>> acc3 = acc2
    >>> acc3(6)
    13
    >>> acc2(5)
    18
    >>> acc(4)
    29
    """
    total = 0
    def accumulator(num):
        nonlocal total
        total = total + num
        return total
    return accumulator


if __name__ == "__main__":
    import doctest
    doctest.testmod()
