class Solution(object):
    def moveZeroes(self, nums):
        pre_idx = -1
        for i, num in enumerate(nums):
            if num == 0:
                continue
            pre_idx += 1
            if i > pre_idx:
                nums[i], nums[pre_idx] = nums[pre_idx], nums[i]

