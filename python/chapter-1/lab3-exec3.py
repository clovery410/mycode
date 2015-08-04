def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def repeated(f, n):
    if n == 0:
        return lambda x: f(x)
    return compose1(f, repeated(f, n - 1))

def double(x):
    return x * 2

result = repeated(double, 3)(2)
print(result)
