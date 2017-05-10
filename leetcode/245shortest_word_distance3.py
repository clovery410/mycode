class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        if word1 == word2:
            pre = -1
            res = len(words)
            for i, word in enumerate(words):
                if word == word1:
                    if pre >= 0:
                        res = min(res, i - pre)
                    pre = i
            return res
        else:
            res = len(words)
            idx1, idx2 = -1, -1
            for i, word in enumerate(words):
                if word == word1:
                    idx1 = i
                    if idx2 >= 0: res = min(res, i - idx2)
                if word == word2:
                    idx2 = i
                    if idx1 >= 0: res = min(res, i - idx1)
            return res
                
