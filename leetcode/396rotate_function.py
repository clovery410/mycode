class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Recursive equation is:
        # F(x) = F(x-1) - (n-1) * A[-x] + sum - A[-x]
        # F(x) = F9x-1) + sum - n * A[-x]
        
        pre = _sum = 0
        n = len(A)
        
        for i, num in enumerate(A):
            pre += i * num
            _sum += num
        
        res = pre
        for i in xrange(1, n):
            cur = pre + _sum - n * A[-i]
            res = max(res, cur)
            pre = cur
        
        return res
