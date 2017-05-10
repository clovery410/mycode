class Solution(object):
    def searchInsert(self, nums, target):
        s, e = 0, len(nums)
        while s < e:
            mid = (e - s) / 2 + s
            if nums[mid] >= target and (mid == 0 or nums[mid-1] < target):
                return mid
            if nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        return s

if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,5,6]
    print sol.searchInsert(nums, 5)
