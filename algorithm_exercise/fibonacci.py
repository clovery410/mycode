def fib(n):
    if n <= 1:
        return 1
    pre = curr = 1
    for i in xrange(2, n + 1):
        temp = pre + curr
        pre = curr
        curr = temp
    return curr
