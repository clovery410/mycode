class Solution(object):
    # First version, DFS, without memorization
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in xrange(len(s)-1):
            if s[i] == s[i+1] == '+':
                if not self.canWin(s[:i] + '--' + s[i+2:]):
                    return True
        return False


    # Second version, DFS, with memorization, speed up greatly!
    _cache = {}
    def canWin2(self, s):
        cache = self._cache
        
        if s not in cache:
            for i in xrange(len(s) - 1):
                if s[i] == s[i+1] == '+':
                    if not self.canWin2(s[:i] + '--' + s[i+2:]):
                        cache[s] = True
                        return cache[s]
                    
            cache[s] = False
        return cache[s]
