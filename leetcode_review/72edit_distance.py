class Solution(object):
    #solution1, recursive + memoization
    def minDistance(self, word1, word2):
        def helper(w1, w2):
            if w1 == w2:
                return 0
            l1, l2 = len(w1), len(w2)
            if l1 == 0 or l2 == 0:
                return l1 or l2
            
            if (w1, w2) in cache:
                return cache[(w1, w2)]
            
            if w1[0] == w2[0]:
                cache[(w1, w2)] = helper(w1[1:], w2[1:])
            else:
                cache[(w1, w2)] = min(helper(w1, w2[1:]), helper(w1[1:], w2), helper(w1[1:], w2[1:])) + 1
            return cache[(w1, w2)]
        
        cache = {}
        return helper(word1, word2)

    #solution2, dp
    #dp[i][j] means minimum steps convert word1[0...i-1] to word2[0...j-1]
    #boundary case: dp[i][0] = i, dp[0][j] = j
    #general case: two conditions
    #   (1). if word1[i-1] == word2[j-1], dp[i][j] = dp[i-1][j-1]
    #   (2). else: get minimum of following
    #            (A). Replace word1[i-1] by word2[j-1], => dp[i][j] = dp[i-1][j-1] + 1
    #            (B). Delete word1[i-1] and word1[0...i-2] = word2[0...j-1], => dp[i][j] = dp[i-1][j] + 1
    #            (C). Insert word2[j-1] to word1[0...i-1] and word1[0...i-1] + word2[j-1] = word2[0...j-1], => dp[i][j] = dp[i][j-1] + 1
    def minDistance2(self, word1, word2):
        l1, l2 = len(word1), len(word2)
        if l1 == 0 or l2 == 0:
            return l1 or l2
        if word1 == word2:
            return 0

        dp = [[0 for x in xrange(l2+1)] for x in xrange(l1+1)]
        for i in xrange(l1+1):
            dp[i][0] = i
        for j in xrange(l2+1):
            dp[0][j] = j

        for i in xrange(1, l1+1):
            for j in xrange(1, l2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[-1][-1]

    
if __name__ == "__main__":
    sol = Solution()
    print sol.minDistance("aabc", "abcd")
    print sol.minDistance2("aabc", "abcd")
    
