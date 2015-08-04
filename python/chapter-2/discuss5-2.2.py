from operator import getitem
def rational(n, d):
    return (n, d)

def numer(x):
    return getitem(x, 0)

def denom(x):
    return getitem(x, 1)

def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def approx_e(iter=100):
    total = rational(0, 1)
    for k in range(iter):
        total = add_rationals(total, rational(1, factorial(k)))
    return total


def approx_e_1(iter=100):
    i, e = 0, rational(0, 1)
    while i < iter:
        e = add_rationals(e, rational(1, factorial(i)))
        i = i + 1
    return e


print(approx_e(10))
print(approx_e_1(10))

def inverse_rational(x):
    """Return the inverse of the given non-zero rational number"""
    return rational(denom(x), numer(x))

def div_rationals(x, y):
    """Return x / y fot given rational x and non-zero rational y"""
    return mul_rationals(x, inverse_rational(y))
