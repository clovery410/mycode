class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        res = []

        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return res

    #Solution2, use haspmap
    def intersect2(self, nums1, nums2):
        cache = {}
        res = []
        for num in nums1:
            cache[num] = cache.get(num, 0) + 1
        for num in nums2:
            cache[num] = cache.get(num, 0) - 1
            if cache[num] >= 0:
                res.append(num)
        return res

if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    sol = Solution()
    print sol.intersect(nums1, nums2)
    print sol.intersect2(nums1, nums2)
