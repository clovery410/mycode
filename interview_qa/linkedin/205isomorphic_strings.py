class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        maps = {}
        used_t = set()
        for i, char_s in enumerate(s):
            char_t = t[i]
            if char_s not in maps:
                if char_t not in used_t:
                    maps[char_s] = char_t
                    used_t.add(char_t)
                else:
                    return False
            elif maps[char_s] != char_t:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    s = "paper"
    t = "titie"
    print sol.isIsomorphic(s, t)
                
                
