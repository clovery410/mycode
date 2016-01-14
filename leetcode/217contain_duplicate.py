class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) <= 0:
            return False
        dup = {}
        for item in nums:
            if item in dup:
                return False
            else:
                dup[item] = 1
        return True


if __name__ == '__main__':
    sol = Solution()
    nums = [0]
    print sol.containsDuplicate(nums)
