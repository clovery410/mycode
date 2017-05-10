class Solution(object):
    def wordBreak(self, s, wordDict):
        def checkNext(pre_word, idx):
            if (pre_word, idx) in memo:
                return False
            if idx >= len(s):
                if pre_word == "" or pre_word in wordDict:
                    return True
                return False
            
            if pre_word in wordDict and checkNext(s[idx], idx + 1):
                return True
            elif checkNext(pre_word + s[idx], idx + 1):
                return True
            else:
                memo.add((pre_word, idx))
                return False

        memo = {}
        return checkNext("", 0)

    #solution2, after reviewed last two round code, try to rewrite the dp solution
    def wordBreak2(self, s, wordDict):
        dp = [True] + [False] * len(s)
        for i in xrange(len(s)):
            j = i
            while j >= 0:
                if s[j:i+1] in wordDict and dp[j] == True:
                    dp[i+1] = True
                    break
                j -= 1
        return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    print sol.wordBreak2("leetcode", {"leet", "code"})
                
