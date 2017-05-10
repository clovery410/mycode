def  krakenCount(m, n):
    if m == 0 or n == 0: return 0
    dp = [[1 for x in xrange(n)] for x in xrange(m)]
    for i in xrange(1, m):
        for j in xrange(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]
    return dp[-1][-1]

