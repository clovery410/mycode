class Solution(object):
    # solution1, use math trick
    def missingNumber(self, nums):
        total = 0
        for num in nums:
            total += num
        
        n = len(nums)    
        return n * (n+1) / 2 - total

    
