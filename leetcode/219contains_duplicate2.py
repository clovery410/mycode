class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        if len(nums) == 0:
            return False

        e = 0
        dup = {}
        while e < len(nums) and e < k:
            if nums[e] in dup:
                return True
            dup.add(nums[e])
            e += 1

        s = 0
        while e < len(nums):
            if nums[e] in dup:
                return True
            dup.add(nums[e])
            dup.remove(nums[s])
            s += 1
            e += 1
        return False
