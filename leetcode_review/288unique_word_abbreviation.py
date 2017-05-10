import collections
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        self.table = collections.defaultdict(set)
        for word in dictionary:
            l = len(word)
            if l > 2:
                self.table[word[0] + str(l-2) + word[-1]].add(word)
                
    def isUnique(self, word):
        l = len(word)
        if l <= 2: return True
        
        abbrev_s = word[0] + str(l-2) + word[-1]
        if abbrev_s in self.table:
            if len(self.table[abbrev_s]) > 1 or word not in self.table[abbrev_s]:
                return False
        return True
