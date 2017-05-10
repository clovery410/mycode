cclass Solution(object):
    def minCost(self, costs):
        dp = [[0 for x in xrange(3)] for x in xrange(len(costs))]
        dp[0] = costs[0]
        
        for i in xrange(1, len(costs)):
            for j in xrange(3):
                dp[i][j] = min(dp[i-1][(j-1)%3], dp[i-1][(j-2)%3]) + costs[i][j]
                
        return min(dp[-1])

    # solution2, optimize the space complexity
    def minCost2(self, costs):
        dp = [costs[0], [0] * 3]
        for i in xrange(1, len(costs)):
            for j in xrange(3):
                dp[1][j] = min(dp[0][(j-1)%3], dp[0][(j-2)%3]) + costs[i][j]
            for j in xrange(3):
                dp[0][j] = dp[1][j]
                
        return min(dp[0])

if __name__ == "__main__":
    sol = Solution()
    costs = [[1,2,3],[3,2,1],[4,3,2],[7,4,5]]
    print sol.minCost(costs)
