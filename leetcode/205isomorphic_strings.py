class Solution(object):
    #Solution1, running time is O(nlogn) since did a sort
    def isIsomorphic(self, s, t):
        s_mark, t_mark = {}, {}
        for i, ch in enumerate(s):
            if ch in s_mark:
                s_mark[ch].append(i)
            else:
                s_mark[ch] = [i]
        for i, ch in enumerate(t):
            if ch in t_mark:
                t_mark[ch].append(i)
            else:
                t_mark[ch] = [i]
        s_res = sorted(s_mark.values())
        t_res = sorted(t_mark.values())
        return s_res == t_res

    #Solution2, running time is O(n)
    def isIsomorphic2(self, s, t):
        def helper(s, t):
            mark = {}
            for i in xrange(len(s)):
                curr_s, curr_t = s[i], t[i]
                if curr_s in mark and mark[curr_s] != curr_t:
                    return False
                elif curr_s not in mark:
                    mark[curr_s] = curr_t
            return True

        if len(s) != len(t):
            return False
        return helper(s, t) and helper(t, s)
    
if __name__ == "__main__":
    sol = Solution()
    print sol.isIsomorphic("egg", "aad")
