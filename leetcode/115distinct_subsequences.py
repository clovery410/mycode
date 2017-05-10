class Solution(object):
    def __init__(self):
        self.count = 0

    #Solution1, brute-force recursive
    def numDistinct(self, s, t):
        def isKthAway(ori_s, sub_s, k):
            if not sub_s:
                self.count += 1
            elif k == 0:
                if ori_s == sub_s:
                    self.count += 1
                return
            else:
                if ori_s[0] == sub_s[0]:
                    isKthAway(ori_s[1:], sub_s[1:], k)
                isKthAway(ori_s[1:], sub_s, k-1)

        if len(s) < len(t): return 0
        k = len(s) - len(t)
        isKthAway(s, t, k)
        return self.count

    #Solution2, optimized recursive, use index instead of string itself, get rid of copy time
    def numDistinct2(self, s, t):
        def checkMatch(s_i, t_i, k):
            if t_i >= len(t):
                self.count += 1
            elif k == 0:
                if s[s_i:] == t[t_i:]:
                    self.count += 1
            else:
                if s[s_i] == t[t_i]:
                    checkMatch(s_i+1, t_i+1, k)
                checkMatch(s_i+1, t_i, k-1)
        if len(s) < len(t): return 0
        k = len(s) - len(t)
        checkMatch(0, 0, k)
        return self.count

    #Solution3, third version recursion, use memorization
    def numDistinct3(self, s, t):
        def helper(s_i, t_i):
            if (s_i, t_i) in cache:
                return cache[(s_i, t_i)]
            if t_i < 0:
                cache[(s_i, t_i)] = 1
            elif s_i < 0:
                cache[(s_i, t_i)] = 0
            else:
                if s[s_i] == t[t_i]:
                    cache[(s_i, t_i)] = helper(s_i - 1, t_i - 1) + helper(s_i - 1, t_i)
                else:
                    cache[(s_i, t_i)] = helper(s_i - 1, t_i)
            return cache[(s_i, t_i)]

        if len(t) > len(s): return 0
        cache = {}
        return helper(len(s)-1, len(t)-1)
                    
    #Solution4, since this is a dp problem, we can optimize it with dp solution, Time O(m*n), Space O(m*n)
    def numDistinct4(self, s, t):
        s_l, t_l = len(s), len(t)
        dp = [[1] * (s_l + 1)] + [[0 for x in xrange(s_l + 1)] for x in xrange(t_l)]
        for i in xrange(1, t_l + 1):
            for j in xrange(1, s_l + 1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

    #Solution5, optimize the space complexity in dp solution, Time O(m*n), Space O(m), here m = len(t), n = len(s)
    def numDistinct5(self, s, t):
        s_l, t_l = len(s), len(t)
        dp = [1] + [0 for x in xrange(t_l)]
        for j in xrange(1, s_l+1):
            pre = 1
            for i in xrange(1, t_l+1):
                temp = dp[i]
                if t[i-1] == s[j-1]:
                    dp[i] += pre
                pre = temp
        return dp[-1]

    #Solution6, continue optimize from solution5, get rid of two temprary variables by fill the array backward
    def numDistinct6(self, s, t):
        s_l, t_l = len(s), len(t)
        dp = [1] + [0 for x in xrange(t_l)]
        for j in xrange(1, s_l+1):
            for i in reversed(xrange(1, t_l+1)):
                if t[i-1] == s[j-1]:
                    dp[i] += dp[i-1]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    print sol.numDistinct3("aaa", "aa")
    print sol.numDistinct5("aaa", "aa")
    print sol.numDistinct6("aaa", "aa")
#    print sol.count
