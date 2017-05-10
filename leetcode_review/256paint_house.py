class Solution(object):
    def minCost(self, costs):
        n = len(costs)
        if n == 0:
            return 0

        dp = [costs[0], [0] * 3]
        for i in xrange(1, n):
            for j in xrange(3):
                dp[1][j] = min(dp[0][(j+1)%3], dp[0][(j+2)%3]) + costs[i][j]
            for j in xrange(3):
                dp[0][j] = dp[1][j]
        return min(dp[0])

if __name__ == "__main__":
    sol = Solution()
    costs = [[17,2,17],[16,16,5],[14,3,19]]
    print sol.minCost(costs)
