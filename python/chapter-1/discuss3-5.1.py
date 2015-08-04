# 1. Write a function cube_root that computes the cube root of the input numner x.(Hint: Use newtowns_method with a function that is zero at the cube root of the input.)
def cube(x):
    return x * x * x

def approx_deriv(fn, x, dx=0.00001):
    return (fn(x + dx) - fn(x)) / dx

def newtons_method(fn, guess=1, max_iterations=100):
    ALLOWED_ERROR_MARGIN = 0.0000001
    i = 1
    while abs(fn(guess)) > ALLOWED_ERROR_MARGIN and i <= max_iterations:
        guess = guess - fn(guess) / approx_deriv(fn, guess)
        i += 1
    return guess

def find_root(f):
    return newtons_method(f)

def cube_root(x):
    return find_root(lambda y: cube(y) - x)

print(cube_root(8))
print(cube_root(27))
