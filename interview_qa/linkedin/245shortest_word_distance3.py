class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        min_dis = len(words)
        # same word condition
        if word1 == word2:
            pre = -1
            for i, word in enumerate(words):
                if word == word1:
                    if pre >= 0:
                        min_dis = min(min_dis, i - pre)
                    pre = i

        # two different words condition
        else:
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
    word1, word2 = "makes", "coding"
    print sol.shortestWordDistance(words, word1, word2)
            
                        
