class Solution(object):
    #solution1, dp solution
    def numDecodings(self, s):
        if len(s) == 0 or s[0] == '0': return 0
        
        dp = [1] + [0] * (len(s))
        dp[1] = 1
        
        for i in xrange(2, len(dp)):
            cur = s[i-1]
            if cur == '0':
                if s[i-2] not in '12': return 0
                dp[i] = dp[i-2]
            else:
                dp[i] += dp[i-1]
                if s[i-2] == '1' or (s[i-2] == '2' and cur <= '6'):
                    dp[i] += dp[i-2]
        return dp[-1]

    #solution2, recursion + memoization
    def numDecodings2(self, s):
        def helper(s):
            if s in memo:
                return memo[s]

            if len(s) <= 1:
                if len(s) == 0 or s != '0':
                    memo[s] = 1
                    return 1
                memo[s] = 0
                return 0

            if s[0] == '0':
                memo[s] = 0
                return 0

            count = 0
            if s[0] == '1' or s[0] == '2' and s[1] == '6':
                count += helper(s[2:])
            count += helper(s[1:])
            memo[s] = count
            return count

        memo = {}
        return helper(s)
        
if __name__ == "__main__":
    sol = Solution()
    print sol.numDecodings("17")
    print sol.numDecodings2("17")
