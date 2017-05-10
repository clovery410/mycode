class Solution(object):
    #Solution1, brute-force, running time is O(n*k)
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if nums is None or len(nums) <= 1 or k <= 0:
            return False

        for i in xrange(len(nums) - 1):
            d = 1
            while d <= k:
                j = i + d
                if j < len(nums):
                    if abs(nums[i] - nums[j]) <= t:
                        return True
                    d += 1
                else:
                    break
        return False

    #Solution2, improved a little bit running time to O(n*logk), but needs O(k) space, however still TLE
    def containsNearbyAlmostDuplicate2(self, nums, k, t):
        if nums is None or len(nums) <= 1 or k <= 0:
            return False
        while True:
            curr_nums = sorted(nums[i:i+k+1])
            for s in xrange(len(curr_nums) - 1):
                if abs(curr_nums[s] - curr_nums[s+1]) <= t:
                    return True
            i += 1
            if i + k >= len(nums):
                return False
        return False

    #Solution3, learned from discuss forum, ind is an array of the indexes of sorted nums. Iterate through ind to check if nums are within t and ind are within k. This running time is O(n*t), but since t is small, it is almost O(n).
    def containsNearbyAlmostDuplicate3(self, nums, k, t):
        ind = sorted(xrange(len(nums)), key = lambda x: nums[x])
        for i in xrange(len(nums) - 1):
            j = i + 1
            while j < len(nums) and abs(nums[ind[j]] - nums[ind[i]]) <= t:
                if abs(ind[j] - ind[i]) <= k:
                    return True
                j += 1
        return False
        
    #Solution4, learned from discuss forum, the idea is like bucket sort.
    def containsNearbyAlmostDuplicate4(self, nums, k, t):
        if t < 0: return False
        d = {}
        n = len(nums)
        w = t + 1
        for i in xrange(n):
            m = nums[i] / w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m-1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m+1]) < w:
                return True
            d[m] = nums[i]
            if i >= k:
                del d[nums[i-k]/w]
        return False
        
if __name__ == "__main__":
    nums = [2, 5, 0, 2, -4]
    sol = Solution()
    print sol.containsNearbyAlmostDuplicate(nums, 3, 0)
    print sol.containsNearbyAlmostDuplicate2(nums, 3, 0)
                        
            
            
