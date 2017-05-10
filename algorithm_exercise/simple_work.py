class Solution(object):
    def simple_word(self, words):
        wordDict = set(words)
        res = []
        for i in xrange(len(words)):
            curr_word = words[i]
            wordDict.remove(curr_word)
            dp = [False for x in xrange(len(curr_word) + 1)]
            dp[0] = True
            for j in xrange(len(curr_word)):
                k = j
                while k >= 0:
                    if curr_word[k:j+1] in wordDict and dp[k] == True:
                        dp[j+1] = True
                        break
                    k -= 1
            if dp[-1] == False:
                res.append(curr_word)
            wordDict.add(curr_word)
        return res

if __name__ == "__main__":
    sol = Solution()
    sentence = ['chat', 'ever', 'snapchat', 'snap', 'salesperson', 'per', 'person', 'sales', 'son', 'whatsoever', 'what', 'so']
    print sol.simple_word(sentence)
                
