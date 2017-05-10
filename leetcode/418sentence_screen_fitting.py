class Solution(object):
    #solution1, brute-force
    def wordsTyping(self, sentence, rows, cols):
        count = 0
        i, j = 0, 0
        while True:
            for word in sentence:
                length = len(word)
                
                if length > cols:
                    return 0
                if cols - j >= length:
                    j += length + 1
                else:
                    i += 1
                    j = length + 1
                    
                # Exit
                if j >= cols:
                    j = 0
                    i += 1
                if i > rows or i == rows and j > 0:
                    return count
                    
            count += 1

if __name__ == "__main__":
    sol = Solution()
    sentence = ["try", "to", "be", "better"]
    print sol.wordsTyping(sentence, 10000, 9001)
                    
