class Solution(object):
    #solution1, brute-force
    def shortestPalindrome(self, s):
        def isPalindrome(string):
            if string == string[::-1]:
                return True
            else:
                return False
            
        for i in reversed(xrange(len(s)+1)):
            if isPalindrome(s[:i]):
                return s[i:][::-1] + s

    #solution2, use python library startswith to speed up checking whether a string is start with another string.
    def shortestPalindrome2(self, s):
        r = s[::-1]
        for i in xrange(len(r)+1):
            if s.startswith(r[i:]):
                return r[:i] + s

    #solution3
    def shortestPalindrome3(self, s):
        j = 0
        for i in reversed(xrange(len(s))):
            if s[j] == s[i]:
                j += 1
        if j == len(s):
            return s
        suffix = s[j:]
        return suffix[::-1] + self.shortestPalindrome3(s[:j]) + suffix

if __name__ == "__main__":
    sol = Solution()
    print sol.shortestPalindrome3("aacecaaa")
            
