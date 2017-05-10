class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current['_end_'] = {}

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def bfs(root, word):
            if word == '':
                return True if '_end_' in root else False
            
            c = word[0]
            if c == '.':
                for child in root.values():
                    if bfs(child, word[1:]):
                        return True
                return False
            elif c in root:
                return bfs(root[c], word[1:])
            else:
                return False

        current = self.root
        return bfs(current, word)

if __name__ == "__main__":
    wd = WordDictionary()
    # wd.addWord("ran")
    # wd.addWord("rune")
    # wd.addWord("runner")
    # wd.addWord("runs")
    # wd.addWord("add")
    # wd.addWord("adds")
    # wd.addWord("adder")
    # wd.addWord("addee")
    # print wd.search("r.n")
    # print wd.search("ru.n.e")
    # print wd.search("add")
    # print wd.search("add.")
    # print wd.search("adde.")
    # print wd.search(".an.")
    # print wd.search("...s")
    # print wd.search("....e.")
    # print wd.search(".......")
    # print wd.search("..n.r")
    wd.addWord("a")
    print wd.search("a.")
