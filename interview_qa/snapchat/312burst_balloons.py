class Solution(object):
    def maxCoins(self, nums):
        def recurse(start, end):
            if start + 1 == end:
                return 0
            if (start, end) in memo:
                return memo[(start, end)]
            
            max_coin = 0
            for idx in xrange(start+1, end):
                cur_profit = recurse(start, idx) + nums[start] * nums[idx] * nums[end] + recurse(idx, end)
                max_coin = max(max_coin, cur_profit)
                
            memo[(start, end)] = max_coin
            return max_coin

        nums = [1] + nums + [1]
        memo = {}
        return recurse(0, len(nums) - 1)

if __name__ == "__main__":
    sol = Solution()
    nums = [3, 1, 5, 8]
    print sol.maxCoins(nums)
