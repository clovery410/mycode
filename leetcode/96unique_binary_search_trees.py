class Solution(object):
    def numTrees(self, n):
        dp = [1] * (n+1)
        for i in xrange(2, n+1):
            dp[i] = sum(dp[j] * dp[i-j-1] for j in xrange(i))
        return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.numTrees(4)
                                                        
        
