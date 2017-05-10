class Solution(object):
    def shortestDistance(self, words, word1, word2):
        res = len(words) - 1
        i = 0
        while i < len(words):
            if words[i] == word1:
                first, second = word1, word2
                pre = i
                break
            if words[i] == word2:
                first, second = word2, word1
                pre = i
                break
            i += 1
        j = i + 1
        while j < len(words):
            if words[j] == first:
                pre = j
            if words[j] == second:
                res = min(res, j - pre)
                second, first = first, second
                pre = j
            j += 1
        return res

    #solution2, simplify solution1
    def shortestDistance2(self, words, word1, word2):
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

if __name__ == "__main__":
    sol = Solution()
    words = ["practice", "makes", "perfect", "coding", "makes"]
    print sol.shortestDistance2(words, "coding", "practice")
    print sol.shortestDistance2(words, "makes", "coding")
                
            
                
