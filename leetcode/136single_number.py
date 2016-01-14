class Solution(object):
    def singleNumber(self, nums):
        result = nums[0]
        for num in nums[1:]:
            result = num ^ result

        return result


if __name__ == '__main__':
    nums = [1, 2, 4, 5, 2, 1, 4]
    sol = Solution()
    data = sol.singleNumber(nums)
    print data
