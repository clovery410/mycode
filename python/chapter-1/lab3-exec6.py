def curry2(f):
    return lambda x: lambda y: f(x, y)

def divide(x, y):
    return x / y

def inverse_curry2(g):
    def f(x, y):
        return g(x)(y)
    return f

result = inverse_curry2(curry2(divide))(4, 2)
print(result)
