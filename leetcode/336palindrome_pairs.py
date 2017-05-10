class Solution(object):
    def palindromePairs(self, words):
        indices = {}
        res = []
        for i, word in enumerate(words):
            indices[word] = i

        for idx, word in enumerate(words):
            for i in xrange(1, len(word) + 1):
                if self.isPalindrome(word[:i]):
                    prefix = word[i:][::-1]
                    if prefix in indices and indices[prefix] != idx:
                        res.append([indices[prefix], idx])
            for j in xrange(-1, len(word)):
                if self.isPalindrome(word[j+1:]):
                    suffix = word[:j+1][::-1]
                    if suffix in indices and indices[suffix] != idx:
                        res.append([idx, indices[suffix]])
        return res

    def isPalindrome(self, word):
        return word == word[::-1]

if __name__ == "__main__":
    sol = Solution()
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    words2 = ["a", ""]
    print sol.palindromePairs(words)
