class Solution(object):
    def integerBreak(self, n):
        dp = [0, 0, 1, 2, 4, 6, 9]
        for i in xrange(7, n+1):
            dp[i].append(max([x * dp[i-x] for x in range(1, i)]))
            
        return dp[n]
