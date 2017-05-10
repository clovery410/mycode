class Solution(object):
    def rob(self, nums):
        nums = [0, 0] + nums
        n = len(nums)
        dp = [0] * n
        for i in xrange(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]
