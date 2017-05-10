class Solution(object):
    def isOneEditDistance(self, s, t):
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        for i, c in enumerate(s):
            if c != t[i]:
                return s[i+1:] == t[i+1:] or s[i:] == t[i+1:]
            
        return len(t) - len(s) == 1

if __name__ == "__main__":
    sol = Solution()
    print sol.isOneEditDistance("a", "ba")
