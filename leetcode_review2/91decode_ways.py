class Solution(object):
    def numDecodings(self, s):
        if len(s) == 0 or s[0] == '0':
            return 0
        dp = [1, 1]  + [0] * (len(s) - 1)
        for i in xrange(2, len(dp)):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if s[i-2] == '1' or (s[i-2] == '2' and '0' <= s[i-1] <= '6'):
                dp[i] += dp[i-2]
        return dp[-1]

    # solution2, recursion + memoization
    def numDecodings2(self, s):
        def checkDecode(s):
            if s == '':
                return 1
            if s in cache:
                return cache[s]
            count = 0

            if s[0] == '0':
                count = 0
            else:
                count += checkDecode(s[1:])
                if 10 <= int(s[:2]) <= 26:
                    count += checkDecode(s[2:])
            cache[s] = count
            return count
         
        if len(s) == 0:
            return 0
        cache = {}
        return checkDecode(s)

if __name__ == "__main__":
    sol = Solution()
    print sol.numDecodings('12')
        
