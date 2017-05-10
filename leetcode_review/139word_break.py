class Solution(object):
    #solution1, recursion + memoization
    def wordBreak(self, s, wordDict):
        def recurse(s):
            if s in memo:
                return memo[s]
            if s in wordDict:
                return True

            res = False
            for word in wordDict:
                length = len(word)
                if s[:length] == word and recurse(s[length:]):
                    res = True
            memo[s] = res
            return res
        
        #pre check whether s has characters that not in any words in wordDict
        characters = set()
        for word in wordDict:
            for c in word:
                characters.add(c)
        for c in s:
            if c not in characters: return False
            
        memo = {}
        return recurse(s)

    #solution2, dp
    def wordBreak2(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in xrange(len(s)):
            j = i
            while j >= 0:
                if s[j:i+1] in wordDict and dp[j]:
                    dp[i+1] = True
                    break
                j -= 1
        return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    d = {"car", "ca", "rs"}
    print sol.wordBreak("cars", d)
    print sol.wordBreak2("cars", d)
