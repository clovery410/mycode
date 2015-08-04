def skipped(f):
    def g():
        return f
    return g

def composed(f, g):
    def h(x):
        return f(g(x))
    return h

def added(f, g):
    def h(x):
        return f(x) + g(x)
    return h

def square(x):
    return x * x

def two(x):
    return 2

"""
skipped(f)()(x) = g()(x) = f(x)
added(f, g)(x) = h(x) = f(x) + g(x)
composed(f, g)(x) = h(x) = f(g(x))
"""

result = composed(square, two)(7)
print(result)
result1 = skipped(added(square, two))()(3)
print(result1)
result2 = added(square, two)(3)
print(result2)
result3 = composed(two, square)(2)
print(result3)
