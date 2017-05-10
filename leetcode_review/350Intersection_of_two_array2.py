class Solution(object):
    # if array already sorted
    def intersect(self, nums1, nums2):
        def binarySearch(s, target):
            e = len(nums2) - 1
            while s <= e:
                mid = (e - s) / 2 + s
                if nums2[mid] >= target:
                    e = mid - 1
                else:
                    s = mid + 1
            return s
            
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        res = []
        idx1 = idx2 = 0
        while idx1 < len(nums1):
            target = nums1[idx1]
            idx2 = binarySearch(idx2, target)
            if idx2 >= len(nums2):
                break
            if nums2[idx2] != target:
                idx1 += 1
            else:
                while idx1 < len(nums1) and idx2 < len(nums2) and nums1[idx1] == nums2[idx2]:
                    res.append(nums1[idx1])
                    idx1 += 1
                    idx2 += 1
        return res

    # solution2, if the arrays are not sorted or the elements of nums2 are stored on disk, then we can precalculate the count of chars in nums1 first and store them in hashmap
    def intersect2(self, nums1, nums2):
        count = collections.defaultdict(int)
        for num in nums1:
            count[num] += 1

        res = []
        for num in nums2:
            if count[num] > 0:
                res.append(num)
                count[num] -= 1
        return res
                    
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,1,1,2,2,3,3,4,5,5,6,7,8]
    nums2 = [2,2,3,4,4,5,6,7,8,8,9]
    print sol.intersect(nums1, nums2)
