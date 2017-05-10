class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.total = [x for x in nums]
        for i in xrange(1, len(nums)):
            self.total[i] += self.total[i-1]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.total[j]
        else:
            return self.total[j] - self.total[i-1]
