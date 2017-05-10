class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dic = {}
        for item in dictionary:
            length = len(item)
            if length > 2:
                key = item[0]+str(length - 2) + item[-1]
            else:
                key = item
            if key not in self.dic:
                self.dic[key] = item
            elif self.dic[key] != item:
                self.dic[key] = 1
                
    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        print self.dic
        word_len = len(word)
        if word_len > 2:
            key = word[0] + str(word_len - 2) + word[-1]
        else:
            key = word
        if key not in self.dic or self.dic[key] == word:
            return True
        else:
            return False

vwa = ValidWordAbbr(['deer','door','cake','card','hello'])
print vwa.isUnique("dear")
print vwa.isUnique("door")
print vwa.isUnique("cart")
print vwa.isUnique("cake")
print vwa.isUnique("hello")
