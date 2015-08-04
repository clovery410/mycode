def map_to_range(start, end, f):
    while start < end:
        print(f(2, start))
        start = start + 1

def curry2(f):
    """Return a curried version of the given two-argument function."""
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    """Return a two-argument version of the given curried function."""
    def f(x, y):
        return g(x)(y)
    return f

b = uncurry2(curry2(pow))

result = map_to_range(0, 10, b)
