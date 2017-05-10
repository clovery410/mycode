# "the sky is blue"
# "eulb si yks eht"

class Solution(object):
    def reverseWords(self, s):
        s = s[::-1]
        i, j = 0, 1
        while j < len(s):
            if s[j] == ' ':
                print s[i:j]
                s = s[:i] + s[i:j:-1] + s[j:]
                print s[:i], s[i:j:-1], s[j:]
                i = j + 1
            j += 1
        print s

if __name__ == '__main__':
    sol = Solution()
    sol.reverseWords(['the sky is blue'])
