def improve(update, isclose, guess):
    while not isclose(guess):
        guess = update(guess)
    return guess

def approx_derivative(f, x, delta = 1e-5):
    df = f(x + delta) - f(x)
    return df / delta

def newton_update(f):
    def update(x):
        return x - f(x) / approx_derivative(f, x)
    return update

def find_root(f, initial_guess = 10):
    def close_to_zero(x):
        def approx_eq(f, y, tolerance = 1e-3):
            return f(x) - y < tolerance
        return approx_eq(f(x), 0)
    return improve(newton_update(f), close_to_zero, initial_guess)

def sqrt(a):
    return find_root(lambda x: lambda x: (x * x) - a)

def logarithm(a, base=2):
    return find_root(lambda x: pow(base, x) - a)

result1 = sqrt(16)
result2 = logarithm(32, 2)

print(result1)
print(result2)
