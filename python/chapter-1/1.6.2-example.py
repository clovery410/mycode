def square(x):
    return x * x

def successor(x):
    return x + 1

def improve(update, isclose, guess=1):
    while not isclose(guess):
        guess = update(guess)
    return guess

def near(x, f, g):
    return approx_eq(f(x), g(x))

def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance

def golden_update(guess):
    return 1/guess + 1

def square_near_successor(guess):
    return near(guess, square, successor)

phi = 1/2 + pow(5, 1/2) / 2

def near_test():
    assert near(phi, square, successor), 'phi * phi is not near phi + 1'

def improve_test():
    approx_phi = improve(golden_update, square_near_successor)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'


if __name__ == "__main__":
    import doctest
    doctest.testmod()
