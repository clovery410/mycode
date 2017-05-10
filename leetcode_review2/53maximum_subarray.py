class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]

        res = nums[0]
        for i in xrange(1, len(nums)):
            cur_num = nums[i]
            dp[i] = max(cur_num + dp[i-1], cur_num)
            res = max(res, dp[i])

        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print sol.maxSubArray(nums)
                
