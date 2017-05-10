class Solution(object):
    # solution1, recursive solution
    def isMatch(self, s, p):
        def check(s_i, p_i):
            if s_i == len(s) and p_i == len(p):
                return True
            elif s_i < len(s) and p_i == len(p):
                return False
            elif s_i == len(s):
                if p[p_i] == '*' and check(s_i, p_i+1):
                    return True
                return False
            
            cur_s, cur_p = s[s_i], p[p_i]
            if cur_p == '?' or cur_s == cur_p:
                return check(s_i+1, p_i+1)
            if cur_p == '*' and (check(s_i + 1, p_i) or check(s_i, p_i + 1)):
                return True
                
            return False
        
        return check(0, 0)

    # solution2, dp solution
    def isMatch2(self, s, p):
        # pre-check, avoid TLE
        if len(s) < len(p) - p.count('*'):
            return False
        
        # initialization
        dp = [[False for x in xrange(len(p)+1)] for x in xrange(len(s)+1)]
        dp[0][0] = True
        j = 1
        while j <= len(p) and p[j-1] == '*':
            dp[0][j] = True
            j += 1

        # fill up the dp table
        for i in xrange(1, len(s)+1):
            for j in xrange(1, len(p)+1):
                cur_s, cur_p = s[i-1], p[j-1]
                if cur_s == cur_p or cur_p == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif cur_p == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                    
        return dp[-1][-1]
            
            

if __name__ == "__main__":
    sol = Solution()
    s = "aab"
    p = "?*a"
    print sol.isMatch(s, p)
    print sol.isMatch2(s, p)
