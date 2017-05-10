class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def helper(word1, word2, cache):
            if word1 == '':
                cache[(word1, word2)] = len(word2)
                return len(word2)
            if word2 == '':
                cache[(word1, word2)] = len(word1)
                return len(word1)
            if (word1, word2) not in cache:
                if word1[0] == word2[0]:
                    cache[(word1, word2)] = helper(word1[1:], word2[1:], cache)
                else:
                    cache[(word1, word2)] = 1 + min(helper(word1[1:], word2[1:], cache), helper(word1, word2[1:], cache), helper(word1[1:], word2, cache))
            return cache[(word1, word2)]
        
        n1, n2 = len(word1), len(word2)
        return helper(word1, word2, {})
