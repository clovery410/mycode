class Solution(object):
    def rob(self, nums):
        if len(nums) <= 3:
            return max(nums) if len(nums) > 0 else 0

        include_pre, include_cur = nums[0], max(nums[0], nums[1])
        exclude_pre, exclude_cur = nums[1], max(nums[1], nums[2])
        for i in xrange(2, len(nums) - 1):
            include_pre, include_cur = include_cur, max(include_cur, include_pre + nums[i])
        for j in xrange(3, len(nums)):
            exclude_pre, exclude_cur = exclude_cur, max(exclude_cur, exclude_pre + nums[j])

        return max(include_cur, exclude_cur)

if __name__ == "__main__":
    nums = [2,5,2,1,9,5,7,0,8]
    sol = Solution()
    print sol.rob(nums)

    
        
