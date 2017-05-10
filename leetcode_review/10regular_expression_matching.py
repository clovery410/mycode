class Solution(object):
    # recursive solution
    def isMatch(self, s, p):
        def checkRegExp(s_idx, p_idx):
            if s_idx >= len(s) and p_idx >= len(p):
                return True
            elif p_idx >= len(p):
                return False
            elif s_idx >= len(s):
                if p_idx < len(p) - 1 and p[p_idx+1] == '*' and checkRegExp(s_idx, p_idx + 2):
                    return True
                else:
                    return False

            cur_s = s[s_idx]
            cur_p = p[p_idx]
            next_p = p[p_idx+1] if p_idx + 1 < len(p) else None
            if next_p == '*':
                if checkRegExp(s_idx, p_idx + 2):
                    return True
                elif (cur_s == cur_p or cur_p == '.') and checkRegExp(s_idx + 1, p_idx):
                    return True
                else:
                    return False
            elif (cur_s == cur_p or cur_p == '.') and checkRegExp(s_idx + 1, p_idx + 1):
                return True
            else:
                return False

        return checkRegExp(0, 0)

    # # dp solution
    # def isMatch(self, s, p):
    #     dp = 

if __name__ == "__main__":
    sol = Solution()
    print sol.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
            
