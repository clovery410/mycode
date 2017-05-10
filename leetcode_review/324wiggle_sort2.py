class Solution(object):
    #solution1, sort it, then reorder, O(n logn) running time
    def wiggleSort(self, nums):
        nums.sort()
        res = []
        n = len(nums)
        for i in reversed(xrange((n+1) / 2)):
            j = i + n / 2
            res.append(nums[i])
            if j >= (n + 1) / 2:
                res.append(nums[j])
        for i in xrange(n):
            nums[i] = res[i]

if __name__ == "__main__":
    sol = Solution()
    nums = [1,5,1,1,6,4]
    print sol.wiggleSort(nums)
