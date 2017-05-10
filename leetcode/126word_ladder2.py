from collections import deque, defaultdict
import string
import time
class Solution(object):
    min_total = 0
    def findLadders(self, beginWord, endWord, wordList):
        def helper(count, cur_solution, all_solutions):
            if cur_solution[-1] == endWord:
                if len(cur_solution) == self.min_total:
                    all_solutions.append(cur_solution[:])
                elif len(cur_solution) < self.min_total:
                    all_solutions[:] = [cur_solution[:]]
                    self.min_total = len(cur_solution)
            elif count < len(wordList):
                last_word = cur_solution[-1]
                if self.isOneEdit(last_word, endWord):
                    cur_solution.append(endWord)
                    helper(count+1, cur_solution, all_solutions)
                    cur_solution.pop()
                else:
                    flag = True
                    for word in wordList:
                        if self.isOneEdit(last_word, word):
                            cur_solution.append(word)
                            helper(count+1, cur_solution, all_solutions)
                            cur_solution.pop()
                            flag = False
                    if flag:
                        helper(count+1, cur_solution, all_solutions)
        res = []
        self.min_total = len(wordList) + 2
        helper(0, [beginWord], res)
        return res
    
    def isOneEdit(self, s1, s2):
        for i in xrange(len(s1)):
            if s1[i] != s2[i]:
                return s1[i+1:] == s2[i+1:]
        return False

    #Solution2
    def findLadders2(self, beginWord, endWord, wordList):
        candidate = set(wordList)
        queue = deque([[beginWord]])
        res = []
        while queue:
            size = len(queue)
            flag = False
            temp = set()
            for i in xrange(size):
                cur_solution = queue.popleft()
                last_word = cur_solution[-1]
                if self.isOneEdit(last_word, endWord):
                    cur_solution.append(endWord)
                    res.append(cur_solution[:])
                    flag = True
                else:
                    for word in candidate:
                        if self.isOneEdit(last_word, word):
                            cur_solution.append(word)
                            queue.append(cur_solution[:])
                            temp.add(word)
                            cur_solution.pop()
            if flag:
                return res
            for word in temp:
                candidate.remove(word)
        return res

    #Solution3, two end bfs
    def findLadders3(self, beginWord, endWord, wordList):
        def searchLadders(startWords, endWords, flip):
            flip = not flip
            if len(startWords) == 0: return False
            if len(startWords) > len(endWords): return searchLadders(endWords, startWords, flip)
            for word in startWords: wordList.discard(word)
            for word in endWords: wordList.discard(word)
            intermediate = set([])
            done = False
            for word in startWords:
                for p in xrange(word_len):
                    for char in string.lowercase:
                        newWord = word[:p] + char + word[p+1:]
                        if newWord in endWords:
                            done = True
                            if flip: children[newWord].append(word)
                            else: children[word].append(newWord)
                        elif not done and newWord in wordList:
                            intermediate.add(newWord)
                            if flip: children[newWord].append(word)
                            else: children[word].append(newWord)
            return done or searchLadders(endWords, intermediate, flip)

        def genLadders(startWord, endWord, children, ladder, ladders):
            if startWord == endWord:
                ladders.append(ladder[:])
                return
            for child in children[startWord]:
                ladder.append(child)
                genLadders(child, endWord, children, ladder, ladders)
                ladder.pop()
                
        ladders = []
        startWords = set([beginWord])
        endWords = set([endWord])
        word_len = len(beginWord)
        children = defaultdict(list)
        flip = True
        if searchLadders(startWords, endWords, flip):
            print children
            genLadders(beginWord, endWord, children, [beginWord], ladders)
        return ladders

    #Solution4, use above idea, but implement it with queue
    def findLadders4(self, beginWord, endWord, wordList):
        
        
if __name__ == "__main__":
    # beginWord = "ta"
    # endWord = "if"
    # wordList = ["ts", "sc", "ph", "ca", "jr", "hf", "to", "if", "ha", "is", "io", "cf", "ta"]
    beginWord = "red"
    endWord = "tax"
    wordList = set(["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"])
    sol = Solution()
    time1 = time.time()
    print sol.findLadders(beginWord, endWord, wordList)
    print "solution1 --- %s second ---" % (time.time() - time1)
    time2 = time.time()
    print sol.findLadders2(beginWord, endWord, wordList)
    print "solution2 --- %s second ---" % (time.time() - time2)
    time3 = time.time()
    print sol.findLadders3(beginWord, endWord, wordList)
    print "solution3 --- %s second ---" % (time.time() - time3)
                                      
