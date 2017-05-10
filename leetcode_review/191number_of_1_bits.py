class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in xrange(32):
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count

    #solution2
    def hammingWeight2(self, n):
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count
