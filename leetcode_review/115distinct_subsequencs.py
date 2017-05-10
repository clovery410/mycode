class Solution(object):
    #first dp solution, but its O(n^2) running time, and O(n^2) space complexcity
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        dp = [[0] * (n+1) for x in xrange(m+1)]
        for i in xrange(m+1):
            dp[i][0] = 1

        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]
                # if i > 1 and s[i-2] == t[j-1]:
                #     dp[i][j] += dp[i-1][j]
        return dp[-1][-1]

    #try to come up a O(n) space dp
    def numDistinct2(self, s, t):
        m, n = len(s), len(t)
        dp = [1] + [0] * n

        for i in xrange(m):
            pre = dp[0]
            for j in xrange(1, n+1):
                temp = dp[j]
                if s[i] == t[j-1]:
                    dp[j] += pre
                pre = temp
        return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.numDistinct("rabbbit", "rabbit")
    print sol.numDistinct2("aacaacca", "ca")
