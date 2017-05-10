class Solution(object):
    def findMin(self, nums):
        s, e = 0, len(nums) - 1
        while s < e:
            mid = (e - s) / 2 + s
            if nums[mid] == nums[e] == nums[s]:
                s += 1
                e -= 1
            elif nums[mid] > nums[e]:
                s = mid + 1
            else:
                e = mid
        return nums[s]

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 1, 1, 0, 1]
    print sol.findMin(nums)
