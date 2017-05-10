class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        if len(nums) < 4:
            return []
        res = set()
        for i in xrange(len(nums)-3):
            first = nums[i]
            for j in xrange(i+1, len(nums)-2):
                second = nums[j]
                new_target = target - first - second
                s, e = j + 1, len(nums) - 1
                while s < e:
                    if nums[s] + nums[e] == new_target:
                        res.add((first, second, nums[s], nums[e]))
                    if nums[s] + nums[e] <= new_target:
                        s += 1
                    else:
                        e -= 1
        return [list(elem) for elem in res]

if __name__ == "__main__":
    sol = Solution()
    nums = [1,0,-1,0,-2,2]
    target = 0
    print sol.fourSum(nums, target)
