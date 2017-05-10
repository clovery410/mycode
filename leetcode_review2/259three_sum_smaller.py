class Solution(object):
    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0
        for i in xrange(len(nums)-2):
            first = nums[i]
            s, e = i + 1, len(nums) - 1
            while s < e:
                if nums[s] + nums[e] < target - first:
                    count += e - s
                    s += 1
                else:
                    e -= 1
        return count
                
