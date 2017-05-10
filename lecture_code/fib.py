def fib(n):
    a, b = 1, 1
    for i in xrange(3, n+1):
        b, a = a + b, b
        #i = 3, b = 1 + 1
        #at last i = n, b = f(n)
    return b

print fib(100)
