def one(mississippi):
    """
    >>> one(1)
    1
    >>> one(2)
    4
    >>> one(3)
    6
    """
    if mississippi == 1:
        return mississippi
    elif mississippi == 2:
        return 2 + mississippi
    elif mississippi == 3:
        return 3 + mississippi


def two(two):
    """
    >>> two(5)
    15
    >>> two(6)
    18
    """
    one = two
    three = one
    two = three
    return three + two + one

def three(num):
    """
    >>> three(5)
    15
    >>> three(6)
    21
    """
    i, sum = 0, 0
    while num >= i:
        sum += i
        i += 1
    return sum

def four(num):
    """
    >>> four(5)
    16
    >>> four(6)
    32
    """
    if num == 1:
        return num
    return four(num - 1) + four(num - 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
