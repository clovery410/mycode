class Solution(object):
    def numTrees(self, n):
        dp = [1] * (n+1)
        for i in xrange(2, n+1):
            res = 0
            for mid in xrange(1, i+1):
                res += dp[mid-1] * dp[i-mid]
            dp[i] = res
        return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.numTrees(3)
