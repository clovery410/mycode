class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        def ladder(beginWords, endWords):
            if len(endWords) == 0:
                return dictLen
            for word in beginWords | endWords:
                wordList.discard(word)
                
            temp = set()
            done = False
            for word in beginWords:
                length = len(word)
                for pos in xrange(length):
                    for c in string.lowercase:
                        new_word = word[:pos] + c + word[pos+1:]
                        if new_word in endWords:
                            done = True
                        elif not done and new_word in wordList:
                            temp.add(new_word)
            if done:
                return 1
            return 1 + ladder(endWords, temp)

        beginWords = {beginWord}
        endWords = {endWord}
        dictLen = len(wordList)
        res = ladder(beginWords, endWords)
        if res >= dictLen:
            return 0
        return res + 1
