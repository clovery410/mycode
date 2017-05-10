class Solution(object):
    def maximumGap(self, nums):
        def radixSort(nums):
            for k in xrange(10):
                s = [[] for x in xrange(10)]
                for num in nums:
                    s[(num / 10 ** k) % 10].append(num)
                nums = [num for x in s for num in x]

        if len(nums) < 2:
            return 0
        radixSort(nums)
        res = 0
        for i in xrange(1, len(nums)):
            res = max(res, nums[i] - nums[i-1])
        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,22,7,18,9,10]
    print sol.maximumGap(nums)
        
