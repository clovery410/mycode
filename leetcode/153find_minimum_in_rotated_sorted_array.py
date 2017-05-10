class Solution(object):
    def findMin(self, nums):
        s, e = 0, len(nums) - 1
        while s < e:
            mid = (e - s) / 2 + s
            if nums[mid] > nums[e]:
                s = mid + 1
            else:
                e = mid
        return nums[s]
