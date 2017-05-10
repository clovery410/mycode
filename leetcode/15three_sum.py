class Solution(object):
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        pre1 = nums[0] - 1
        for i in xrange(len(nums)-2):
            first = nums[i]
            if first == pre1:
                continue
            s, e = i + 1, len(nums) - 1
            pre2, pre3 = nums[s] - 1, nums[e] + 1
            while s < e:
                second, third = nums[s], nums[e]
                if second == pre2:
                    s += 1
                    continue
                if third == pre3:
                    e -= 1
                    continue
                if second + third == -first:
                    res.append([first, second, third])
                    pre2, pre3 = second, third
                    s += 1
                    e -= 1
                elif second + third < -first:
                    pre2 = second
                    s += 1
                else:
                    pre3 = third
                    e -= 1
                pre2, pre3 = second, third
            pre1 = first
        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print sol.threeSum(nums)
