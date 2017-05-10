class Solution(object):
    def minEdit(self, s):
        l = len(s)
        dp = [[0 for x in xrange(l)] for x in xrange(l)]

        for diff in xrange(1, l):
            for i in xrange(l-diff):
                j = i + diff
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i+1][j]) + 1
                    
        return dp[0][-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.minEdit("anuja")
