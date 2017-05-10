class Solution(object):
    def rob_easy(self, nums):
        nums = [0,0] + nums
        n = len(nums)
        dp = [0] * n
        for i in xrange(2, n):
            dp[i] = max((dp[i - 2] + nums[i]), dp[i - 1])
        return dp[-1]

    # 0 stolen, 1, n-1 remove
    # 0 not stolen, [1...n-1]
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        return max((nums[0] + self.rob_easy(nums[2:-1])), self.rob_easy(nums[1:]))
