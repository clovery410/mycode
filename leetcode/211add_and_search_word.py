from collections import defaultdict
class WordDictionary(object):
    def __init__(self):
        self.root = defaultdict()

    def addWord(self, word):
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        current['_end_'] = {}

    def search(self, word):
        def _search(root, word):
            if word == '':
                return True if '_end_' in root else False
            if word[0] == '.':
                for x in root.values():
                    if _search(x, word[1:]): return True
                return False
            if word[0] not in root: return False
            return _search(root[word[0]], word[1:])
        return _search(self.root, word)
        # current = self.root
        # for letter in word:
        #     if letter not in current:
        #         return False
        #     current = current[letter]
        # return True if '_end_' in current else False

#try to write it again
class WordDictionary2(object):
    def __init__(self):
        self.root = defaultdict(dict)

    def addWord(self, word):
        current = self.root
        for letter in word:
            current[letter] = defaultdict(dict)
            current = current[letter]
        current['_end_'] = '_end_'

    def search(self, word):
        def bfs(root, word):
            if word == '':
                return True if '_end_' in root else False
            c = word[0]
            if c == '.':
                for child in root.values():
                    if bfs(child, word[1:]): return True
                return False
            elif c in root:
                return bfs(root[c], word[1:])
            else:
                return False
        return bfs(self.root, word)
    
if __name__ == "__main__":
    wordDict = WordDictionary2()
    wordDict.addWord("ran")
    print wordDict.search(".an.")
    wordDict.addWord("wird")
    print wordDict.search("w..d")
    print wordDict.search("wh.d")
