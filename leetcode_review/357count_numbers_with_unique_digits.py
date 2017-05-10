class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        dp = [1] * (n + 1)
        for i in xrange(1, n+1):
            dp[i] = dp[i-1]
            res = base = 9
            for j in xrange(1, i):
                res *= base
                base -= 1
            dp[i] += res
            
        return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.countNumbersWithUniqueDigits(0)
