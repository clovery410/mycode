class Solution(object):
    def integerBreak(self, n):
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        dp = [0] * (n+1)
        dp[2], dp[3] = 2, 3
        for i in xrange(4, n+1):
            dp[i] = max(dp[j] * dp[i-j] for j in xrange(1, i/2 + 1))
        return dp[-1]

    #Solution2, O(n) running time
    def integerBreak2(self, n):
        if n == 2 or n == 3:
            return n - 1

        if n % 3 == 0:
            return 3 ** (n/3)
        if n % 3 == 1:
            return 3 ** ((n-4)/3) * 4
        if n % 3 == 2:
            return 3 ** (n/3) * 2
    
if __name__ == "__main__":
    sol = Solution()
    print sol.integerBreak(30)
    print sol.integerBreak2(30)
