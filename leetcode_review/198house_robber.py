class Solution(object):
    def rob(self, nums):
        if len(nums) <= 2:
            return max(nums) if len(nums) > 0 else 0
        
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in xrange(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,2,0,5]
    print sol.rob(nums)
