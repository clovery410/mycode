class Solution(object):
    # This dfs solution time limit exceeded (learnt from leetcode forum)
    def dfs(self, string, wordDict):
        if string == '':
            return True
        for i in xrange(len(string)):
            if string[:i+1] in wordDict:
                if self.dfs(string[i+1:], wordDict):
                    return True
        return False
    
    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict)

    # DP solution: runs really fast, also learnt from leetcode forum
    def dp_solution(self, s, wordDict):
        len_s = len(s)
        dp = [False for x in xrange(len_s + 1)]
        dp[0] = True
        for i in xrange(len_s):
            j = i
            while j >= 0:
                if s[j:i+1] in wordDict and dp[j]:
                    dp[i+1] = True
                    break
                j -= 1

        return dp[-1]
                    
        
if __name__ == '__main__':
    s = 'leetcode'
    word_dict = ['leet', 'code']

    sol = Solution()
    print sol.wordBreak(s, word_dict)
    print sol.dp_solution(s, word_dict)
