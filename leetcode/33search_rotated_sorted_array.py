class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        start, end = 0, n - 1
        while start <= end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            if nums[start] == nums[mid] and nums[end] == nums[mid]:
                while nums[start] == nums[mid]:
                    start += 1
                while nums[end] == nums[mid]:
                    end -= 1
            elif nums[mid] <= nums[start] and target > nums[end]: # There is a inversion in first half
                end = mid - 1
            elif nums[mid] >= nums[end] and target < nums[start]:
                start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

sol = Solution()
print sol.search([1,3,1,1,1], 3)
