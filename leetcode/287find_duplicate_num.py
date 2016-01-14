class Solution(object):
    def findDuplicate(self, nums):
        def _findDup(nums, start, end):
            median = (end + start) / 2
            less_n = 0
            equal_n = 0
            more_n = 0
            for item in nums:
                if item >= start and item < median:
                    less_n += 1
                elif item == median:
                    equal_n += 1
                elif item > median and item <= end:
                    more_n += 1
            if equal_n > 1:
                return median
            else:
                if less_n > median - start:
                    return _findDup(nums, start, median - 1)
                else:
                    return _findDup(nums, median + 1, end)

        return _findDup(nums, 1, len(nums) - 1)

if __name__ == '__main__':
    nums = [14,16,12,1,16,17,6,8,5,19,16,13,16,3,11,16,4,16,9,7]
    sol = Solution()
    print sol.findDuplicate(nums)
