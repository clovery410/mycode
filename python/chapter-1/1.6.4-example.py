def square(x):
    return x * x

def successor(x):
    return x + 1

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h

def f(x):
    """A function named f that is never called."""
    return -x

add_one_and_square = compose1(square,successor)

result = add_one_and_square(12)

print (result)
