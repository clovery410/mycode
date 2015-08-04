def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)

print(sum(5))

def ab_plus_c(a, b, c):
    if a == 0:
        return c
    return ab_plus_c(a-1, b, c) + b

print(ab_plus_c(2, 3, 5))

def summation(n, term):
    if n == 0:
        return term(0)
    return term(n) + summation(n-1, term)


