class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return max(nums) if len(nums) > 0 else 0
        
        pre, cur = nums[0], max(nums[0], nums[1])
        for i in xrange(2, len(nums)):
            tmp = max(pre + nums[i], cur)
            pre = cur
            cur = tmp
        return cur

    
