class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0]) if len(obstacleGrid) > 0 else 0
        if m == 0 or n == 0:
            return 0
        
        dp = [0] * n
        j = 0
        while j < len(dp) and obstacleGrid[0][j] == 0:
            dp[j] = 1
            j += 1
        
        blocked = False
        for i in xrange(1, m):
            if obstacleGrid[i][0] == 1:
                blocked = True
            if blocked:
                dp[0] = 0
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j-1]
        return dp[-1]
