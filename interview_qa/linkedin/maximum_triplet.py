import sys
class Solution(object):
    def findMaximumTriplet(self, nums):
        if len(nums) < 3:
            return 0
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        positive_cnt = sum(1 for x in nums if x > 0)
        # all numbers are non-positive
        if positive_cnt == 0 or positive_cnt >= 3:
            candidate1 = candidate2 = candidate3 = -sys.maxint - 1
            for num in nums:
                if num > candidate1:
                    candidate3 = candidate2
                    candidate2 = candidate1
                    candidate1 = num
                elif num > candidate2:
                    candidate3 = candidate2
                    candidate2 = num
                elif num > candidate3:
                    candidate3 = num
            return candidate1 * candidate2 * candidate3

        else:
            pos_candidate, neg_candidate1, neg_candidate2 = -sys.maxint-1, sys.maxint, sys.maxint
            for num in nums:
                if num > pos_candidate:
                    pos_candidate = num
                if num < neg_candidate1:
                    neg_candidate2 = neg_candidate1
                    neg_candidate1 = num
                elif num < neg_candidate2:
                    neg_candidate2 = num
            return pos_candidate * neg_candidate1 * neg_candidate2
                    

if __name__ == "__main__":
    sol = Solution()
    nums = [-2,-4,-3,9]
    print sol.findMaximumTriplet(nums)
            
