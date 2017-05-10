class Solution(object):
    #Solution1, brute-force solution, running time is O(n^2), TLE
    def maxProduct(self, nums):
        all_product = nums[:]
        for i in xrange(1, len(nums)):
            if all_product[i-1] != 0:
                all_product[i] *= all_product[i-1]
        largest = max(all_product)
        for i in xrange(len(nums)):
            temp = nums[i]
            if temp != 0:
                for j in xrange(i+1, len(nums)):
                    if all_product[j] == 0:
                        break
                    all_product[j] /= temp
                largest = max(largest, max(all_product))
        return largest

    #Solution2, optimized dp version, maintain 2 states, maximum product including current element and minimum product including current element, so that can handle negative condition.
    def maxProduct2(self, nums):
        n = len(nums)
        curr_max, curr_min = nums[0], nums[0]
        dp = [curr_max, curr_min]
        for i in xrange(1, n):
            dp[0], dp[1] = max(nums[i], dp[0] * nums[i], dp[1] * nums[i]), min(nums[i], dp[0] * nums[i], dp[1] * nums[i])
            curr_max = max(curr_max, dp[0])
            curr_min = min(curr_min, dp[1])
        return curr_max
    
if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, -2, 4, -5]
    print sol.maxProduct(nums)
    print sol.maxProduct2(nums)
            
