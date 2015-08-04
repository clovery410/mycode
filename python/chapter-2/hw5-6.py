def interval(a, b):
    return (a, b)

def lower_bound(x):
    return x[0]

def upper_bound(x):
    return x[1]

def str_interval(x):
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))


def make_center_percent(c, p):
    """Construct an interval from center and percentage tolerance.

    >>> str_interval(make_center_percent(2, 50))
    '1.0 to 3.0'
    """
    return interval(c - (c * p / 100), c + (c * p / 100))

def center(x):
    return (upper_bound(x) + lower_bound(x)) / 2

def percent(x):
    """Return the percentage tolerance of interval x.

    >>> percent(interval(1, 3))
    50.0
    """
    dif = (upper_bound(x) - lower_bound(x)) / 2
    return dif / center(x) * 100

if __name__ == "__main__":
    import doctest
    doctest.testmod()
