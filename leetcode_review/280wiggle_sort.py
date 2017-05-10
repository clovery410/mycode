class Solution(object):
    def wiggleSort(self, nums):
        for i in xrange(1, len(nums)):
            pre, cur = nums[i-1], nums[i]
            if i % 2 == 1 and pre > cur:
                nums[i-1], nums[i] = nums[i], nums[i-1]
            elif i % 2 == 0 and pre < cur:
                nums[i-1], nums[i] = nums[i], nums[i-1]

        return nums

if __name__ == "__main__":
    sol = Solution()
    nums = [3, 5, 2, 1, 6, 4]
    print sol.wiggleSort(nums)
                
