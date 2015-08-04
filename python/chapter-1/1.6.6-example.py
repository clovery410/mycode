def compose1(f, g):
    return lambda x: f(g(x))

f = compose1(lambda x: x * x, lambda x: x + 1)

result = f(12)

print(result)
