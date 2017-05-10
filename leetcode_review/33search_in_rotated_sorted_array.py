class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return -1

        s, e = 0, len(nums) - 1
        while s <= e:
            mid = (e - s) / 2 + s
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[e] and target < nums[s]:
                s = mid + 1
            elif nums[mid] < nums[s] and target > nums[e]:
                e = mid - 1
            elif nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    print sol.search(nums, 0)
