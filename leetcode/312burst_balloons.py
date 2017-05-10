class Solution(object):
    #Solution1, bottom up recursive of dp solution
    def maxCoins(self, nums):
        nums = [1] + [i for i in nums if i > 0] + [1]
        dp = [[0 for x in xrange(len(nums))] for x in xrange(len(nums))]

        def helper(left, right):
            if dp[left][right]:
                return dp[left][right]
            combination = []
            for i in xrange(left+1, right):
                combination.append(nums[left] * nums[i] * nums[right] + helper(left, i), helper(right, i))
            dp[left][right] = max(combination) if len(combination) > 0 else 0
            return dp[left][right]

        return helper(0, len(nums) - 1)

    #Solution2, top down dp
    def maxCoins2(self, nums):
        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)
        dp = [[0 for x in xrange(n)] for x in xrange(n)]

        for k in xrange(2, n):
            for i in xrange(n-k):
                j = i + k
                for x in xrange(i+1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[x] * nums[j] + dp[i][x] + dp[x][j]
        return dp[0][-1]
                

        
        
