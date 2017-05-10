class Solution(object):
    def searchInsert(self, nums, target):
        s, e = 0, len(nums) - 1
        while s <= e:
            mid = (e - s) / 2 + s
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                s = mid + 1
            else:
                e = mid - 1
        return s

if __name__ == "__main__":
    nums = [1,3,5,6]
    sol = Solution()
    print sol.searchInsert(nums, 0)
