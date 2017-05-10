class Solution(object):
    def climbStairs(self, n):
        a, b = 1, 1
        for i in xrange(2, n+1):
            b, a = a + b, b
        return b


print Solution().climbStairs(10)
