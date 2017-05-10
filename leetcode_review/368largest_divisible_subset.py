class Solution(object):
    def largestDivisibleSubset(self, nums):
        if len(nums) <= 1:
            return nums
        
        nums.sort()
        dp = [1] * len(nums)
        indices = range(len(nums))
        for i in xrange(1, len(nums)):
            cur_max_count = 1
            num = nums[i]
            for j in xrange(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    indices[i] = j

        res = []
        idx = dp.index(max(dp))
        while indices[idx] != idx:
            res.append(nums[idx])
            idx = indices[idx]
        res.append(nums[idx])
        return res[::-1]

    # solution2, use set union
    def largestDivisibleSubset2(self, nums):
        nums.sort()
        records = {1: set()}
        for num in nums:
            candidate_len = -1
            candidate = set()
            for key, val in records.items():
                if num % key == 0 and len(val) > candidate_len:
                    candidate_len = len(val)
                    candidate = val
            records[num] = candidate | {num}
        return list(max(records.values(), key = len))
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,4,8,9,72]
    print sol.largestDivisibleSubset(nums)




