class Solution(object):
    def wordPattern(self, pattern, _str):
        words = _str.split(" ")
        if len(pattern) != len(words):
            return False
        
        table = {}
        word_set = set()
        
        for i, word in enumerate(words):
            p = pattern[i]
            if p not in table and word not in word_set:
                table[p] = word
                word_set.add(word)
            elif p not in table or word not in word_set:
                return False
            elif table[p] != word:
                return False
        return True
