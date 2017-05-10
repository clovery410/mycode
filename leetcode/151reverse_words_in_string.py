class Solution(object):
    def reverseWords(self, s):
        # s_list = s.split()
        # s_list.reverse()
        # return ' '.join(s_list)
        return ' '.join(reversed(s.split()))

    #Solution2, do not use library functions
    def reverseWords2(self, s):
        res = ''
        s = ' ' + s
        l = len(s)
        j = l - 1
        while s[j] == ' ':
            j -= 1
        i = j
        while i >= 0:
            if s[i] == ' ' or i == 0:
                res += s[i:j+1]
                j = i - 1
                while j >= 0 and s[j] == ' ':
                    j -= 1
                i = j
            i -= 1
        return res[1:]
            
if __name__ == "__main__":
    sol = Solution()
    s = "  the   sky  is blue   "
    print sol.reverseWords2(s)
