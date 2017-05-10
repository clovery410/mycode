import string
class Solution(object):
    #backtracing + bfs, too slow...
    def ladderLength(self, beginWord, endWord, wordList):
        def getNext(count, word, used):
            if word == endWord:
                self.res = min(self.res, count)
                return
            if count < len(wordList):
                if self.isOneEdit(word, endWord):
                    getNext(count + 1, endWord, used)
                else:
                    cur_cnt = 0
                    for nextWord in wordList:
                        if nextWord not in used and self.isOneEdit(word, nextWord):
                            cur_cnt += 1
                            used.add(nextWord)
                            getNext(count + 1, nextWord, used)
                            used.remove(nextWord)
                    if cur_cnt == 0:
                        getNext(count + 1, word, used)
        
        self.res = len(wordList) + 2
        getNext(1, beginWord, set())
        return 0 if self.res == len(wordList) + 2 else self.res

    def isOneEdit(self, w1, w2):
        for i in xrange(len(w1)):
            if w1[i] != w2[i]:
                return w1[i+1:] == w2[i+1:]
        return False

    def ladderLength2(self, beginWord, endWord, wordList):
        def searchLadders(startWords, endWords):
            if len(startWords) == 0: return False
            if len(startWords) > len(endWords): return searchLadders(endWords, startWords)
            for word in startWords: wordList.discard(word)
            for word in endWords: wordList.discard(word)
            intermediate = set([])
            done = False

            for word in startWords:
                for p in xrange(len(beginWord)):
                    for char in string.lowercase:
                        newWord = word[:p] + char + word[p+1:]
                        if newWord in endWords:
                            done = True
                        elif not done and newWord in wordList:
                            intermediate.add(newWord)
            self.count += 1
            return done or searchLadders(endWords, intermediate)

        self.count = 1
        startWords = set([beginWord])
        endWords = set([endWord])
        if searchLadders(startWords, endWords):
            return self.count
        else:
            return 0

if __name__ == "__main__":
    sol = Solution()
    beginWord = "qa"
    endWord = "sq"
    wordList = set(["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])
    print sol.ladderLength2(beginWord, endWord, wordList)
        
