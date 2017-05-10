class Solution(object):
    def print3sum(self, nums):
        n = len(nums)
        nums.sort()
        res = []
        print nums
        pre_i = nums[-1] + 1
        for i in xrange(n):
            if nums[i] == pre_i:
                continue
            target = 0 - nums[i]
            j = i + 1
            k = n - 1
            pre_j = nums[-1] + 1
            while j < k:
                if nums[j] == pre_j:
                    j += 1
                elif nums[j] + nums[k] == target:
                    res.append((nums[i], nums[j], nums[k]))
                    pre_j = nums[j]
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < target:
                    pre_j = nums[j]
                    j += 1
                else:
                    k -= 1
            pre_i = nums[i]
        return res

if __name__ == '__main__':
    sol = Solution()
    print sol.print3sum([-1, 2, 3, 4, -3, -5, 6, 3, 3, 2, 2])
    print sol.print3sum([0, 0, 0, 0])
