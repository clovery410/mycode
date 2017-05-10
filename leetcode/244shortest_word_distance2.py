#solution1, TLE
class WordDistance(object):
    def __init__(self, words):
        self.table = {}
        for i in range(len(words)-1):
            w1 = words[i]
            for j in range(i+1, len(words)):
                w2 = words[j]
                if (w1, w2) in self.table:
                    self.table[(w1, w2)] = min(self.table[(w1, w2)], j-i)
                else:
                    self.table[(w1, w2)] = j-i
                if (w2, w1) in self.table:
                    self.table[(w2, w1)] = min(self.table[(w2, w1)], j-i)
                else:
                    self.table[(w2, w1)] = j-i
                
    def shortest(self, word1, word2):
        return self.table[(word1, word2)]

#solution2, memory limit exceed
class WordDistance2(object):
    def __init__(self, words):
        self.length = len(words)
        self.table = {}
        for d in range(1, len(words)):
            for s in range(len(words)-d):
                e = s + d
                if (words[s], words[e]) not in self.table:
                    self.table[(words[s], words[e])] = d
            
    def shortest(self, word1, word2):
        d1 = self.table[(word1, word2)] if (word1, word2) in self.table else self.length
        d2 = self.table[(word2, word1)] if (word2, word1) in self.table else self.length
        return min(d1, d2)

#solution3
import collections
class WordDistance3(object):
    def __init__(self, words):
        self.index = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.index[word].append(i)

    def shortest(self, word1, word2):
        w1, w2 = self.index[word1], self.index[word2]
        s1, s2 = 0, 0
        res = abs(w1[s1] - w2[s2])
        while s1 < len(w1) and s2 < len(w2):
            p1, p2 = w1[s1], w2[s2]
            res = min(res, abs(p1 - p2))
            if p1 < p2: s1 += 1
            else: s2 += 1
        return res
            
if __name__ == "__main__":
    w = WordDistance3(["practice", "makes", "perfect", "coding", "makes"])
    print w.shortest("coding", "practice")
    print w.shortest("makes", "coding")
