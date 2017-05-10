import sys
class Solution(object):
    def maxProduct(self, nums):
        max_val = min_val = nums[0]
        res = nums[0]
        for num in nums[1:]:
            if num >= 0:
                max_val = max(num, max_val * num)
                min_val = min(num, min_val * num)
            else:
                temp = max_val
                max_val = max(num, min_val * num)
                min_val = min(num, temp * num)
            res = max(res, max_val)

        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, -2, -4]
    print sol.maxProduct(nums)
