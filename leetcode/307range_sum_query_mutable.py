class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.totals = [0] + [x for x in nums]
        for i in xrange(1, len(self.totals)):
            self.totals[i] += self.totals[i-1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff = val - (self.totals[i+1] - self.totals[i])
        print diff
        for idx in xrange(i+1, len(self.totals)):
            self.totals[idx] += diff

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.totals[j+1] - self.totals[i]

if __name__ == "__main__":
    na = NumArray([-1])
    print na.sumRange(0, 0)
    na.update(0, 1)
    print na.sumRange(0, 0)
