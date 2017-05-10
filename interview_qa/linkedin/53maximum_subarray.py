class Solution(object):
    def maxSubArray(self, nums):
        cur_sum = max_sum = nums[0]
        for i in xrange(1, len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum

if __name__ == "__main__":
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print sol.maxSubArray(nums)
