class Solution(object):
    #Solution1, use dp, O(n) time, O(n) space
    def rob(self, nums):
        if len(nums) <= 3:
            return max(nums) if len(nums) > 0 else 0
        
        dp1 = [0 for x in xrange(len(nums) - 1)]
        dp2 = [0 for x in xrange(len(nums) - 1)]
        #from 0 -> n-2
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        for i in xrange(2, len(nums) - 1):
            curr = nums[i]
            dp1[i] = max(dp1[i-1], dp1[i-2] + curr)
        #from 1 -> n-1
        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])
        for i in xrange(2, len(nums) - 1):
            curr = nums[i+1]
            dp2[i] = max(dp2[i-1], dp2[i-2] + curr)

        return max(dp1[-1], dp2[-1])

    #Solution2, optimize space complexity to O(1)
    def rob2(self, nums):
        if len(nums) <= 3:
            return max(nums) if len(nums) > 0 else 0

        prev1, curr1 = nums[0], nums[1]
        for i in xrange(2, len(nums) - 1):
            prev1, curr1 = max(curr1, prev1), max(curr1, prev1 + nums[i])

        prev2, curr2 = nums[1], nums[2]
        for i in xrange(3, len(nums)):
            prev2, curr2 = max(curr2, prev2), max(curr2, prev2 + nums[i])

        return max(curr1, curr2)

if __name__ == "__main__":
    house = [1,3,1,3,100]
    sol = Solution()
    print sol.rob(house)
    print sol.rob2(house)
