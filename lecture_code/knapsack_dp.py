w = [0, 1, 1, 2, 4, 12]
v = [0, 1, 2, 2, 4, 10]
W = 15

# best_value = 14

'''
f(i, j) = first i items, take no more than j weight, best value

f(i, j) = if not put item i
          f(i - 1, j)
          if put item i
          f(i - 1, j - w[i]) + v[i]
f(i, j) = 0, if i == 0
'''

dp = {}
def f(i, j):
    if i == 0:
        return 0
    if (i, j) not in dp:
        dp[i, j] = f(i - 1, j)
        if j - w[i] >= 0:
            dp[i, j] = max(dp[i, j], f(i - 1, j - w[i]) + v[i])
    return dp[i, j]

print f(5, W)
