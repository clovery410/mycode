import sys
class Solution(object):
    #correct dp solution
    def getMoneyAmount(self, n):
        dp = [[0 for x in xrange(n+1)] for x in xrange(n+1)]
        for i in reversed(xrange(1, n+1)):
            for j in xrange(i+1, n+1):
                if j == i + 1:
                    dp[i][j] = i
                else:
                    count = sys.maxint
                    for k in xrange(i+1, j):
                        count = min(count, max(dp[i][k-1], dp[k+1][j]) + k)
                    dp[i][j] = count
        return dp[1][-1]

    #more concise version, learned from discuss
    def getMoneyAmount2(self, n):
        dp = [[0] * (n+1) for _ in range(n+1)]
        for lo in range(n, 0, -1):
            for hi in range(lo+1, n+1):
                dp[lo][hi] = min(x + max(dp[lo][x-1], dp[x+1][hi]) for x in range(lo, hi))
        return dp[1][n]
    
if __name__ == "__main__":
    sol = Solution()
    print sol.getMoneyAmount(50)
    print sol.getMoneyAmount2(50)
