class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        res_sum = nums[0] + nums[1] + nums[2]
        i = 0
        while i < len(nums) - 2:
            s, e = i + 1, len(nums) - 1
            while s < e:
                cur_sum = nums[i] + nums[s] + nums[e]
                if cur_sum == target:
                    return cur_sum
                if abs(cur_sum - target) < abs(res_sum - target):
                    res_sum = cur_sum
                if cur_sum < target:
                    s += 1
                    while s < e and nums[s] == nums[s-1]:
                        s += 1
                else:
                    e -= 1
                    while e > s and nums[e] == nums[e+1]:
                        e -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i-1]:
                i += 1
        return res_sum
