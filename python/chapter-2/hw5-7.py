def interval(a, b):
    return (a, b)

def lower_bound(x):
    return x[0]

def upper_bound(x):
    return x[1]

def str_interval(x):
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and any vaule in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    lower = lower_bound(x) - upper_bound(y)
    upper = upper_bound(x) - lower_bound(y)
    return interval(lower, upper)

def quadratic(x, a, b, c):
    """Return the interval that is the range the quadratic defined by a, b and c, for domain interval x.

    This is the less accurate version which treats each instance of t as a difference value from the interval. See the extra for experts question for exploring why this is not_really_correct and to write a more precise version.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-9 to 5'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '-6 to 16'
    """    
    first = mul_interval(interval(a, a), mul_interval(x, x))
    second = mul_interval(interval(b, b), x)
    final = add_interval(add_interval(first, second), interval(c, c))
    return final

if __name__ == "__main__":
    import doctest
    doctest.testmod()
