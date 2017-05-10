class Solution(object):
    # solution1, if sort by value, then for each number, only need to compare at most t times
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        new_nums = [(num, i) for i, num in enumerate(nums)]
        new_nums.sort()

        for i in xrange(len(new_nums)):
            j = i + 1
            while j < len(new_nums) and new_nums[j][0] - new_nums[i][0] <= t:
                if abs(new_nums[j][1] - new_nums[i][1]) <= k:
                    return True
                j += 1
        return False
