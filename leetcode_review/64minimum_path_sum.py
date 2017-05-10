class Solution(object):
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0]) if len(grid) > 0 else 0
        if m == 0 or n == 0:
            return 0
        dp = [grid[0][0]] * n
        for j in xrange(1, n):
            dp[j] = dp[j-1] + grid[0][j]
        for i in xrange(1, m):
            for j in xrange(n):
                if j == 0: dp[j] += grid[i][0]
                else:
                    dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[-1]

if __name__ =="__main__":
    sol = Solution()
    matrix = [[2,3,5],[1,7,3],[4,5,6]]
    print sol.minPathSum(matrix)
