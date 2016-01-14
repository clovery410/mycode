class Solution(object):
    def removeElement(self, nums, val):
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                nums.remove(nums[i])
                n -= 1
                i -= 1
            i += 1
            
        return n
