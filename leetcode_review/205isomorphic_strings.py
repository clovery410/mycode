class Solution(object):
    def isIsomorphic(self, s, t):
        char_map = {}
        used_t = set()
        for i in xrange(len(s)):
            c1, c2 = s[i], t[i]
            if c1 in char_map:
                if char_map[c1] != c2:
                    return False
            elif c2 in used_t:
                return False
            else:
                char_map[c1] = c2
                used_t.add(c2)
        return True
                    
