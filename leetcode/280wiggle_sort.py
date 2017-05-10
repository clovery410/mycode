class Solution(object):
    def wiggleSort(self, nums):
        for i in xrange(len(nums)):
            print i, i + 2, nums[i:i+2]
            nums[i:i+2] = sorted(nums[i:i+2], reverse = i % 2)

        print nums

sol = Solution()
sol.wiggleSort([1,1,1,1,2])
