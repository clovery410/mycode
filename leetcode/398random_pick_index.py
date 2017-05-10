class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res, n = None, 1
        nums = self.nums
        for i, num in enumerate(nums):
            if num == target:
                if random.randrange(n) == 0:
                    res = i
                n += 1
        return res
