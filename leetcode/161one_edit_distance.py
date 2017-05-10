class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l_s, l_t = len(s), len(t)
        
        s_skip, t_skip = False, False
        if abs(l_s - l_t) > 1:
            return False
        elif abs(l_s - l_t) == 1:
            if l_s < l_t:
                t_skip = True
            else:
                s_skip = True
                
        i = j = count = 0
        while i < l_s and j < l_t:
            if count > 1:
                return False
            elif s[i] != t[j]:
                if s_skip:
                    i += 1
                    s_skip = False
                elif t_skip:
                    j += 1
                    t_skip = False
                else:
                    i += 1
                    j += 1
                count += 1
            else:
                i += 1
                j += 1
                
        if count + l_s - i + l_t - j == 1:
            return True
        return False

    #Second solution, excellent idea!
    def isOneEditDistance2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l_s, l_t = len(s), len(t)
        
        if abs(l_s - l_t) > 1 or s == t:
            return False
        if l_s > l_t:
            return self.isOneEditDistance(t, s)
    
        for i in xrange(l_s):
            if s[i] != t[i]:
                return s[i:] == t[i+1:] or s[i+1:] == t[i+1:]
        return True
