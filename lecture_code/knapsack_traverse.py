w = [1, 1, 2, 4, 12]
v = [1, 2, 2, 4, 10]
W = 15

# 2^n, each item put or not put
# 0-1 knapsack
# 5 = 00101
# s = 0 to 2^5 - 1
# 1<<5   100000

# 17 = 10001


best_value = 0

for s in xrange(0, (1<<5)):
    taken = 0
    value = 0
    print s, '------------'
    for p in xrange(0, 5):
        if (s & (1<<p)) != 0:
            print p
            taken += w[p]
            value += v[p]
    print 'taken', taken, 'value', value
    if taken <= W:
        best_value = max(best_value, value)


print 'best_value', best_value
