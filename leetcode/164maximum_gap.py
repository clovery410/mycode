class Solution(object):
    def maximumGap(self, nums):
        s_nums = self.radixSort(nums)
        res = 0
        for i in xrange(1, len(s_nums)):
            res = max(res, s_nums[i] - s_nums[i-1])

        #can also use following to calculate max, but not that necessarily quick
        # return max([b - a for a, b in zip(s_nums, s_nums[1:])] or [0])
        return res

    #solution1, radix sort according to digit
    def radixSort(self, nums):
        for k in xrange(10):
            s = [[] for x in xrange(10)]
            for num in nums:
                s[num/(10**k) % 10].append(num)
            nums = [a for b in s for a in b]
        return nums

    #solution2, use the bit to do radix sort, instead of digit
    def radixSort2(self, nums):
        for i in xrange(32):
            zeros, ones = [], []
            for num in nums:
                if num & (1 << i):
                    ones.append(num)
                else:
                    zeros.append(num)
            nums = zeros + ones
        return nums

if __name__ == "__main__":
    sol = Solution()
    nums = [170,45,75,90,802,2,24,66]
    print sol.maximumGap(nums)
