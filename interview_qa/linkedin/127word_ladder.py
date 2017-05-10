class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        def searchLadder(begin_words, end_words):
            if len(begin_words) == 0:
                return length_of_word_list + 2
            
            for word in begin_words | end_words:
                wordList.discard(word)

            intermediate = set()
            for word in begin_words:
                word_len = len(word)
                for i in xrange(word_len):
                    for c in string.lowercase:
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in end_words:
                            return 1
                        elif new_word in wordList:
                            intermediate.add(new_word)
                            
            return 1 + searchLadder(end_words, intermediate)

        if beginWord == endWord:
            return 1
        begin_words = {beginWord}
        end_words = {endWord}
        length_of_word_list = len(wordList)
        wordList = set(wordList)
        ladder_length = searchLadder(begin_words, end_words)
        return 1 + ladder_length if ladder_length <= length_of_word_list + 1 else 0
