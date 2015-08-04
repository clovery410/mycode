def falling_fac(n, k):
    curr, prod, count = n, 1, 0
    while count < k:
        curr, prod = curr - 1, prod * curr
        count += 1
    return prod


result = falling_fac(10, 3)
print(result)


#Solution
def falling(n, k):
    total, stop = 1, n - k
    while n > stop:
        total, n = total * n, n - 1
    return total
