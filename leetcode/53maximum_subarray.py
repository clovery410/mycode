class Solution(object):
    def maxSubArray(self, nums):
        if nums == []:
            return 0
        n = len(nums)
        solution = [0 for x in xrange(n)]
        solution[0] = start = curr_total = nums[0]
        
        for i in xrange(1, n):
            curr = nums[i]
            if curr > curr_total + curr:
                start = curr_total = curr
            else:
                curr_total += curr
            solution[i] = max(solution[i-1], curr_total)
        return solution[-1]

    # Following solution runs in O(n) time and O(1) space, really quick!! Learnt form Discuss
    def quick_dp(self, nums):
        if nums == []:
            return None
        curr_max = curr_total = nums[0]
        n = len(nums)

        for i in xrange(1, n):
            if curr_total < 0:
                curr_total = 0
            curr_total += nums[i]
            curr_max = max(curr_max, curr_total)

        return curr_max

if __name__ == '__main__':
    sol = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print sol.quick_dp(nums)
