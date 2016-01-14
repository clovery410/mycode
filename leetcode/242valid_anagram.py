class Solution(object):
    def isAnagram(self, s, t):
        char_list = [0 for x in xrange(26)]
        for item in s:
            char_list[ord(item) - ord('a')] += 1
        for item in t:
            char_list[ord(item) - ord('a')] -= 1
        is_anagram = True
        for i in xrange(26):
            if char_list[i] != 0:
                is_anagram = False

        return is_anagram


if __name__ == '__main__':
    sol = Solution()
    s = "rat"
    t = "tar"
    print sol.isAnagram(s, t)
