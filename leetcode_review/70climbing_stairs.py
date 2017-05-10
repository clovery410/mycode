class Solution(object):
    def climbStairs(self, n):
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in xrange(2, n):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[-1]

if __name__ =="__main__":
    sol = Solution()
    print sol.climbStairs(10)
