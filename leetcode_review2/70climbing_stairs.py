class Solution(object):
    def climbStairs(self, n):
        if n <= 1:
            return n
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in xrange(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

    #solution2, constanct space
    def climbStairs2(self, n):
        if n <= 1:
            return n

        pre, cur = 1, 2
        for i in xrange(2, n):
            pre, cur = cur, pre + cur
        return cur
