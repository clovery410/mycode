class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[1 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.uniquePaths(7, 3)
