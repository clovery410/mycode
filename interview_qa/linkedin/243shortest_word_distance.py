class Solution(object):
    def shortestDistance(self, words, word1, word2):
        pre_word, pre_pos = None, -1
        min_dis = len(words)
        for i, word in enumerate(words):
            if word in [word1, word2]:
                if pre_word is None:
                    pre_pos = i
                    pre_word = word
                elif pre_word == word:
                    pre_pos = i
                else:
                    min_dis = min(min_dis, i - pre_pos)
                    pre_word = word
                    pre_pos = i
        return min_dis

    # solution2
    def shortestDistance2(self, words, word1, word2):
        min_dis = len(words)
        idx1 = idx2 = -1
        for i, word in enumerate(words):
            if word == word1:
                idx1 = i
                if idx2 >= 0: min_dis = min(min_dis, i - idx2)
            if word == word2:
                idx2 = i
                if idx1 >= 0: min_dis = min(min_dis, i - idx1)
        return min_dis

if __name__ == "__main__":
    sol = Solution()
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1, word2 = "coding", "makes"
    print sol.shortestDistance(words, word1, word2)
                    
