class Solution(object):
    def strStr(self, s, sub_s):
        for i in xrange(len(s) - len(sub_s) + 1):
            j = 0
            while j < len(sub_s):
                if s[i+j] != sub_s[j]:
                    break
                j += 1
            if j == len(sub_s):
                return i
        return -1


sol = Solution()
print sol.strStr('abcdefg', '')
                
            
