class Solution(object):
    def canPartition(self, nums):
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        half_sum = total_sum / 2

        dp = [True] + [False] * half_sum
        for num in nums:
            if num > half_sum:
                return False
            
            for i in reversed(xrange(len(dp))):
                if i < num:
                    break
                if dp[i-num] == True:
                    dp[i] = True
                    
        return True if dp[-1] == True else False

    # solution2, use 2d array, dp[i][j] means whether the specific sum j can be gotten from the first i numbers. If we can pick such a series of numbers from 0-i whose sum is j, dp[i][j] is true, otherwise it is false.
    def canPartition2(self, nums):
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        half_sum = total_sum / 2
        dp = [[False for x in xrange(half_sum+1)] for x in xrange(len(nums)+1)]
        dp[0][0] = True
        for i in xrange(1, len(nums)+1):
            for j in xrange(1, half_sum+1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]
        return dp[-1][-1]

if __name__ == "__main__":
    sol = Solution()
    nums = [2,2,3,5]
    print sol.canPartition(nums)
    print sol.canPartition2(nums)
