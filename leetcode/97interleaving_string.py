import time
class Solution(object):
    #Solution1, recursive + memoization
    def isInterleave(self, s1, s2, s3):
        def helper(idx1, idx2, idx3):
            if (idx1, idx2, idx3) in memo:
                return memo[(idx1, idx2, idx3)]
            if idx3 == len(s3):
                memo[(idx1, idx2, idx3)] = True
                return True
            c3 = s3[idx3]
            if idx1 < len(s1) and s1[idx1] == c3:
                if helper(idx1+1, idx2, idx3+1):
                    memo[(idx1, idx2, idx3)] = True
                    return True
            if idx2 < len(s2) and s2[idx2] == c3:
                if helper(idx1, idx2+1, idx3+1):
                    memo[(idx1, idx2, idx3)] = True
                    return True
            memo[(idx1, idx2, idx3)] = False
            return False
        memo = {}
        if len(s1) + len(s2) != len(s3):
            return False
        return helper(0, 0, 0)

    #solution2, improve the code style of above recursive solution
    def isInterleave2(self, s1, s2, s3, memo = {}):
        if len(s1) + len(s2) != len(s3):
            return False
        if not s1 and not s2 and not s3:
            return True
        if (s1,s2,s3) in memo:
            return memo[s1,s2,s3]
        memo[s1,s2,s3] = (len(s1) > 0 and s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:])) or (len(s2) > 0 and s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:]))
        return memo[s1,s2,s3]

        
    #Solution3, dp, think of a m X n grid, you can only go right or down, try to find a maximum path
    #recursive equation is: dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
    def isInterleave3(self, s1, s2, s3):
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        #initialize
        dp[0][0] = True
        for i in xrange(1, m+1):
            if dp[i-1][0] and s1[i-1] == s3[i-1]:
                dp[i][0] = True
        for j in xrange(1, n+1):
            if dp[0][j-1] and s2[j-1] == s3[j-1]:
                dp[0][j] = True
                
        for i in range(1, m+1):
            for j in range(1, n+1):
                if (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1]):
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        return dp[-1][-1]
                
    # solution4, optimize solution 3 by improving the space complexcity, since we only need the above row info
    def isInterleave4(self, s1, s2, s3):
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        if n < m:
            return self.isInterleave(s2, s1, s3)
        
        dp = [True] * (n+1)
        for j in xrange(1, n+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]

        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                dp[j] = (dp[j-1] and s2[j-1] == s3[i+j-1]) or (dp[j] and s1[i-1] == s3[i+j-1])

        return dp[-1]

if __name__ =="__main__":
    sol = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    s33 = "aadbbbaccc"
    time1 = time.time()
    print sol.isInterleave3(s1, s2, s33)
    print "solution1 --- %s second ---" % (time.time() - time1)
    time2 = time.time()
    print sol.isInterleave4(s1, s2, s33)
    print "solution2 --- %s second ---" % (time.time() - time2)
