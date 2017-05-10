class Solution(object):
    def strStr(self, haystack, needle):
        if haystack == needle:
            return 0
        
        l = len(needle)
        for i in xrange(len(haystack)-l+1):
            if haystack[i:i+l] == needle:
                return i
        return -1
