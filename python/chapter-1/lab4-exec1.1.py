def add_ten_iter(n, x):
    i, sum = 1, 0
    while i <= n:
        sum = sum + 10
        i += 1
    return sum + x

def add_ten_recur(n, x):
    if n == 0:
        return x
    elif n > 0:
        return add_ten_recur(n - 1, x) + 10
    else:
        return add_ten_recur(n + 1, x) - 10


print(add_ten_iter(3, 5))
print(add_ten_recur(3, 5))
print(add_ten_iter(-4, -2))
print(add_ten_recur(-4, -2))
