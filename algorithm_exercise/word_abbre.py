class Trie(object):
    def __init__(self):
        self.root = {}
        self.END = '/'
        self.count = 0

    def makeTrie(self, words):
        for word in words:
            node = self.root
            for c in word:
                node = node.setdefault(c, {'count': 0})

    def markTrie(self, words):
        for word in words:
            node = self.root
            for c in word:
                node[c]['count'] += 1
                node = node[c]

    def search(self, word):
        res = []
        node = self.root
        for c in word:
            if c in node:
                res.append(c)
                if node[c]['count'] == 1:
                    res.append(str(len(word)))
                    if len(res) < len(word):
                        return ''.join(res)
                node = node[c]
        return word

def compressWords(words):
    # create dictionary which has compressed words as key, and original word as value
    dic = {}
    for word in words:
        length = len(word)
        if length > 2:
            key = word[0] + str(length - 2) + word[-1]
        else:
            key = word
        if key not in dic:
            dic[key] = [word,]
        else:
            dic[key].append(word)
            
    res = []
    trie = Trie()
    temp_words = []
    flip_word = lambda x: x[-1] + x[:len(x) - 1]
    flip_back = lambda x: x[1:] + x[0]
    for word in words:
        if word:
            temp_words.append(flip_word(word))
        else:
            temp_words.append(word)
    trie.makeTrie(temp_words)
    trie.markTrie(temp_words)
    for word in temp_words:
        if word:
            flip_back(word)
            res.append(flip_back(word))
        else:
            res.append(word)
    return res

    
if __name__ == '__main__':
    words = ["internal", "intrunal", "inal", "a", ""]
    print compressWords(words)
