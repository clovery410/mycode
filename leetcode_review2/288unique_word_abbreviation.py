class Solution(object):
    def __init__(self, dictionary):
        self.abbr = collections.defaultdict(list)
        for word in dictionary:
            l = len(word)
            if l > 2:
                self.abbr[word[0] + str(l-2) + word[-1]].append(word)

    def isUnique(self, word):
        l = len(word)
        if l <= 2: return True
        
        key = word[0] + str(l-2) + word[-1]
        if key in self.abbr:
            if len(self.abbr[key]) > 1 or self.abbr[key][0] != word:
                return False
        return True
