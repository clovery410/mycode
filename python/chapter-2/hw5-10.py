def interval(a, b):
    return (a, b)

def lower_bound(x):
    return x[0]

def upper_bound(x):
    return x[1]

def str_interval(x):
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
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
    lower = lower_bound(x) - upper_bound(y)
    upper = upper_bound(x) - lower_bound(y)
    return interval(lower, upper)

def accurate_quadratic(x, a, b, c):
    """Return the interval that is the range the quadratic defined by a, b and c, for domain interval x.

    >>> str_interval(accurate_quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(accurate_quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    assert a != 0

    def f(t):
        return a * t * t + b * t + c

    extreme_point = (-b) / (2 * a)
    if lower_bound(x) <= extreme_point <= upper_bound(x):
        if a < 0:
            return interval(min(f(lower_bound(x)), f(upper_bound(x))), f(extreme_point))
        return interval(f(extreme_point), max(f(lower_bound(x)), f(upper_bound(x))))

    elif extreme_point < lower_bound(x):
        if a < 0:
            return interval(f(upper_bound(x)), f(lower_bound(x)))
        return interval(f(lower_bound(x)), f(upper_bound(x)))

    else:
        if a < 0:
            return interval(f(lower_bound(x)), f(upper_bound(x)))
        return interval(f(upper_bound(x)), f(lower_bound(x)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
