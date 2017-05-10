class Solution(object):
    #solution1, basic recursive solution
    def isMatch(self, s, p):
        def helper(s_i, p_i):
            if (s_i, p_i) in cache:
                return False
            if s_i == len(s) and p_i == len(p):
                return True
            elif p_i == len(p):
                return False
            elif s_i == len(s):
                if p[p_i] == '*' and helper(s_i, p_i + 1):
                    return True
                else: return False
            cur_s, cur_p = s[s_i], p[p_i]
            if cur_p == '?' and helper(s_i + 1, p_i + 1):
                return True
            elif cur_p == '*' and (helper(s_i, p_i + 1) or helper(s_i + 1, p_i)):
                return True
            elif cur_s == cur_p and helper(s_i + 1, p_i + 1):
                return True
            else:
                cache.add((s_i, p_i))
                return False
        cache = set()
        return helper(0, 0)

    #solution2, dp solution, filling a 2D DP table, use m * n extra space
    def isMatch2(self, s, p):
        if len(s) < len(p) - p.count('*'):    #Avoid TLE
            return False

        dp = [[False for x in xrange(len(p)+1)] for x in xrange(len(s)+1)]
        dp[0][0] = True
        j = 0
        while j < len(p) and p[j] == '*':
            dp[0][j+1] = True
            j += 1

        for i in xrange(1, len(s)+1):
            for j in xrange(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        return dp[-1][-1]

    #solution3, dp solution, same 2D DP table, but filling the dp table backward
    def isMatch3(self, s, p):
        if len(s) < len(p) - p.count('*'):    #Avoid TLE
            return False
        
        dp = [[False for x in xrange(len(p)+1)] for x in xrange(len(s)+1)]
        dp[-1][-1] = True
        j = len(p) - 1
        while j >= 0 and p[j] == '*':
            dp[-1][j] = True
            j -= 1

        for i in reversed(xrange(len(s))):
            for j in reversed(xrange(len(p))):
                if s[i] == p[j] or p[j] == '?':
                    dp[i][j] = dp[i+1][j+1]
                if p[j] == '*':
                    dp[i][j] = dp[i][j+1] or dp[i+1][j+1] or dp[i+1][j]
        return dp[0][0]

    #solution4, same dp solution, but reduce the 2d space into 1d
    def isMatch4(self, s, p):
        m, n = len(s), len(p)
        if m < n - p.count('*'):   # Avoid TLE here
            return False
        
        dp = [True] + [False] * n
        for i in xrange(n):
            if p[i] != '*': break
            else: dp[i+1] = True
            
        for i in xrange(m):
            pre, dp[0] = dp[0], False
            for j in xrange(1, n+1):
                temp = dp[j]
                if p[j-1] == '*':
                    dp[j] = dp[j] or dp[j-1]
                else:
                    dp[j] = pre and (s[i] == p[j-1] or p[j-1] == '?')
                pre = temp
        return dp[-1]

    #solution5, learned from discuss
    def isMatch5(self, s, p):
        pre_s, pre_astroid = 0, -1
        i = j = 0
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                pre_s = i
                pre_astroid = j
                j += 1
            elif pre_astroid >= 0:
                pre_s += 1
                i, j = pre_s, pre_astroid + 1
            else: return False
        while j < len(p) and p[j] == '*':
            j += 1
        return True if j == len(p) else False
        
if __name__ == "__main__":
    sol = Solution()
    print sol.isMatch2("aabc", "*b*")
    print sol.isMatch3("aabc", "*b*")
    print sol.isMatch4("aabc", "*b*")
    print sol.isMatch5("aabc", "*b*")
        
