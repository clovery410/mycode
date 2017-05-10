class Solution(object):
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if len(res) == 0 or res[-1] != nums1[i]:
                    res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res

    #Solution2, use binary search
    def intersection2(self, nums1, nums2):
        nums2.sort()
        res = []
        cache = {}

        for num in nums1:
            if num not in cache and self.inList(nums2, num):
                res.append(num)
                cache[num] = 1
        return res

    def inList(self, nums, val):
        s, e = 0, len(nums)
        while s <= e:
            mid = (e - s) / 2 + s
            if nums[mid] == val:
                return True
            elif nums[mid] < val:
                s = mid + 1
            else:
                e = mid - 1
        return False
                

if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    sol = Solution()
    print sol.intersection(nums1, nums2)
    print sol.intersection2(nums1, nums2)
    
