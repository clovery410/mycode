class Solution(object):
    #this solution only calculate the maximum length
    def largestDivisibleSubset(self, nums):
        #initialize
        n = len(nums)
        nums.sort()
        dp = [[1] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[i][j] = max(dp[i][k] + 1 if nums[j] % nums[k] == 0 else 1 for k in range(i, j))
        return dp[0][-1]

    #
    def largestDivisibleSubset2(self, nums):
        if len(nums) == 0:
            return []
        n = len(nums)
        nums.sort()
        dp = [1] * n
        indices = [0] * n
        for i in xrange(1, n):
            cur_max, idx = 1, -1
            for j in xrange(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > cur_max:
                    cur_max, idx = dp[j] + 1, j
            dp[i], indices[i] = cur_max, idx

        max_len = max(dp)
        tail = dp.index(max_len)
        res = []
        for i in range(max_len):
            res.append(nums[tail])
            tail = indices[tail]
        return res[::-1]

    #smart solution learned from discuss
    def largestDivisibleSubset3(self, nums):
        S = {-1: set()}
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key = len) | {x}
        return list(max(S.values(), key = len))

    #wrote above code again by self in a an easiler understanding way
    def largestDivisibleSubset4(self, nums):
        records = {1: set()}
        nums.sort()
        for num in nums:
            max_len = 0
            for d in records.keys():
                if num % d == 0 and len(records[d]) + 1 > max_len:
                    records[num] = records[d] | {num}
                    max_len = len(records[num])
        return list(max(records.values(), key = len))
        
if __name__ =="__main__":
    nums = [3,20,10,9,30,70,60,90]
    sol = Solution()
    print sol.largestDivisibleSubset2(nums)
    print sol.largestDivisibleSubset3(nums)
    
        
