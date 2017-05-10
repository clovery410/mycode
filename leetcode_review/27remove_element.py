class Solution(object):
    def removeElement(self, nums, val):
        pre, cur = -1, 0
        while cur < len(nums):
            if nums[cur] != val:
                pre += 1
                if cur > pre:
                    nums[cur], nums[pre] = nums[pre], nums[cur]
            cur += 1
        return pre + 1
