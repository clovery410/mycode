class TrieNode(object):
    def __init__(self):
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                new_child = TrieNode()
                current.children[letter] = new_child
            current = current.children[letter]
        current.children['_end_'] = '_end_'
        
    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        if '_end_' in current.children: return True
        return False

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True

import collections
class TrieNode2(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode2)
        self.isWord = False

class Trie2(object):
    def __init__(self):
        self.root = TrieNode2()

    def insert(self, word):
        current = self.root
        for c in word:
            current = current.children[c]
        current.isWord = True

    def search(self, word):
        current = self.root
        for c in word:
            if c not in current.children: return False
            current = current.children[c]
        return current.isWord

    def startsWith(self, prefix):
        current = self.root
        for c in prefix:
            if c not in current.children: return False
            current = current.children[c]
        return True
    
if __name__ == "__main__":
    trie = Trie()
    trie.insert("somestring")
    print trie.search("some")
    print trie.startsWith("some")
    trie.insert("hello")
    print trie.search("helloo")

    trie2 = Trie2()
    trie2.insert("somestring")
    print trie2.search("some")
    print trie2.startsWith("some")
    trie2.insert("hello")
    print trie2.search("helloo")
