class Solution(object):
    #solution1, use O(n) extra space dp
    def maxProduct(self, nums):
        if len(nums) == 0: return 0
        dp = [(nums[0], nums[0])] * len(nums)
        max_num = nums[0]
        for i in xrange(1, len(nums)):
            last_min, last_max = dp[i-1]
            cur_num = nums[i]
            cur_min = min(cur_num, last_min * cur_num, last_max * cur_num)
            cur_max = max(cur_num, last_min * cur_num, last_max * cur_num)
            max_num = max(max_num, cur_max)
            dp[i] = (cur_min, cur_max)
        return max_num

    #solution2, figured out that could only use two variables which is O(1) space dp
    def maxProduct2(self, nums):
        if len(nums) == 0: return 0
        cur_min = cur_max = res = nums[0]
        for i in xrange(1, len(nums)):
            cur_min, cur_max = min(nums[i], cur_min * nums[i], cur_max * nums[i]), max(nums[i], cur_min * nums[i], cur_max * nums[i])
            res = max(res, cur_max)
        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [2,3,-2,4,-8]
    print sol.maxProduct(nums)
    print sol.maxProduct2(nums)
        
