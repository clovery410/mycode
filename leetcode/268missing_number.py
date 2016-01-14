class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        total = n * (n + 1) / 2

        _total = 0
        for item in nums:
            _total += item

        return total - _total


if __name__ == '__main__':
    nums = [0, 1, 3, 5, 2]
    sol = Solution()
    print sol.missingNumber(nums)
