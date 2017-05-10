class Solution(object):
    def uniquePaths(self, m, n):
        dp = [1] * n
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[j] += dp[j-1]
                
        return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.uniquePaths(3, 7)
