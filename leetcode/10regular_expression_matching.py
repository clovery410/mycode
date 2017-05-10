class Solution(object):
    def isMatch(self, s, p):
        def helper(s_idx, p_idx):
            if s_idx == -1 and p_idx == -1:
                return True
            if s_idx >= 0 and p_idx == -1:
                return False
            if s_idx == -1:
                if p[p_idx] == '*' and helper(s_idx, p_idx - 2):
                    return True
                else: return False

            cur_s, cur_p = s[s_idx], p[p_idx]
            if cur_p == '*':
                if helper(s_idx, p_idx - 2): return True
                if (cur_s == p[p_idx-1] or p[idx_p-1] == '.') and (helper(s_idx - 1, p_idx) or helper(s_idx - 1, p_idx - 2)):
                    return True
                else: return False
            elif cur_p == '.' and helper(s_idx - 1, p_idx - 1):
                return True
            else:
                return (cur_s == cur_p) and helper(s_idx - 1, p_idx - 1)
        return helper(len(s) - 1, len(p) - 1)

    #solution2
    def isMatch2(self, s, p):
        dp = [[False for x in xrange(len(p)+1)] for x in xrange(len(s)+1)]
        dp[0][0] = True
        for j in xrange(1, len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2] if j >= 2 else True
        for i in xrange(1, len(s)+1):
            for j in xrange(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                if p[j-1] == '*':
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2]
        return dp[-1][-1]

        
            
                
                

            
