class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n <= 0:
            return 0
        elif n == 1:
            return k
        
        c = [0 for x in xrange(n)]
        c[0], c[1] = k, k * k
        for i in xrange(2, n):
            c[i] = c[i-1] * (k - 1) + c[i-2] * (k - 1)
        return c[-1]
