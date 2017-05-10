class Solution(object):
    def minSubArrayLen(self, s, nums):
        if len(nums) == 0:
            return 0
        
        min_len = len(nums) + 1
        slow = fast = 0
        total = nums[0]
        while fast < len(nums):
            if total >= s:
                min_len = min(min_len, fast - slow + 1)
                total -= nums[slow]
                slow += 1
            else:
                fast += 1
                if fast < len(nums):
                    total += nums[fast]
                
        return min_len if min_len <= len(nums) else 0
                

    
