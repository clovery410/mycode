import collections
class Solution(object):
    def shortestWord(self, wordList, word1, word2):
        words = collections.defaultdict(list)
        for i, word in enumerate(wordList):
            words[word].append(i)

        res = len(wordList)
        if word1 == word2:
            cur_list = words[word1]
            for i in xrange(1, len(cur_list)):
                res = min(res, cur_list[i] - cur_list[i-1])
        else:
            s1, s2 = 0, 0
            cur_list1 = words[word1]
            cur_list2 = words[word2]
            while s1 < len(cur_list1) and s2 < len(cur_list2):
                res = min(res, abs(cur_list2[s2] - cur_list1[s1]))
                if cur_list1[s1] < cur_list2[s2]:
                    s1 += 1
                else:
                    s2 += 1
        return res

    #solution2, actually, there is no need to allocate extra space
    def shortestWord2(self, wordList, word1, word2):
        if word1 == word2:
            res = len(wordList)
            pre = -1
            for i, word in enumerate(wordList):
                if word == word1:
                    if pre >= 0:
                        res = min(res, i - pre)
                    pre = i
            return res
        else:
            res = len(wordList)
            idx1, idx2 = -1, -1
            for i, word in enumerate(wordList):
                if word == word1:
                    idx1 = i
                    if idx2 >= 0: res = min(res, i - idx2)
                if word == word2:
                    idx2 = i
                    if idx1 >= 0: res = min(res, i - idx1)
            return res
                        
                    

if __name__ == "__main__":
    sol = Solution()
    wordList = ["make", "perfect", "also", "make"]
    word1 = "make"
    word2 = "perfect"
    print sol.shortestWord(wordList, word1, word2)
    print sol.shortestWord2(wordList, word1, word2)
                
        
