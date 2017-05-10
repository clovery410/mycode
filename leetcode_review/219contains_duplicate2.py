class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dups = collections.defaultdict(int)
        l = len(nums)
        i = 0
        while i < min(k+1, l):
            cur_num = nums[i]
            dups[cur_num] += 1
            if dups[cur_num] > 1:
                return True
            i += 1

        for j in xrange(i, l):
            cur_num = nums[j]
            dups[nums[j-k-1]] -= 1
            dups[cur_num] += 1
            if dups[cur_num] > 1:
                return True
        return False

    #solution2
    def containsNearbyDuplicate2(self, nums, k):
        dups = {}
        for i, num in enumerate(nums):
            if num in dups:
                if i - dups[num] <= k:
                    return True
            dups[num] = i
        return False
            
