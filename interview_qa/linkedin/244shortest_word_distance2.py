import collections
class WordDistance(object):
    def __init__(self, words):
        self.position = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.position[word].append(i)

    def shortest(self, word1, word2):
        indices1 = self.position[word1]
        indices2 = self.position[word2]
        i = j = 0
        min_dis = abs(indices1[0] - indices2[0])
        while i < len(indices1) and j < len(indices2):
            idx1 = indices1[i]
            idx2 = indices2[j]
            min_dis = min(min_dis, abs(idx1 - idx2))
            if idx1 < idx2:
                i += 1
            else:
                j += 1
        return min_dis

if __name__ == "__main__":
    wd = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    print wd.shortest("coding", "practice")
            
