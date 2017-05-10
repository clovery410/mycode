# nums = [-2, 0, 1, 3]
# 2-sums = [(-2, 0), (0, 1), (1, 3)]
class Solution(object):
    #First solution, time complexity is O(n^3)
    def threeSumSmaller(self, nums, target):
        res = 0
        l = len(nums)
        for i in xrange(l):
            for j in xrange(i+1, l):
                for k in xrange(j+1, l):
                    if nums[i] + nums[j] + nums[k] < target:
                        res += 1

        return res

    #Solution2, running time is O(n^2)
    def threeSumSmaller2(self, nums, target):
        res = 0
        nums = sorted(nums)
        for i in xrange(len(nums) - 2):
            new_target = target - nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[j] + nums[k] < new_target:
                    res += (k - j)
                    j += 1
                else:
                    k -= 1
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 1, 0, -2]
    target = 4
    print sol.threeSumSmaller(nums, target)
    print sol.threeSumSmaller2(nums, target)
