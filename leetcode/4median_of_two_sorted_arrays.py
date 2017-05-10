class Solution(object):
    #Solution1
    def findMedianSortedArrays(self, nums1, nums2):
        def findKthSmallest(s1, s2, k):
            if s1 >= m:
                return nums2[s2+k-1] / 1.0
            if s2 >= n:
                return nums1[s1+k-1] / 1.0
            if k == 1:
                return min(nums1[s1], nums2[s2]) / 1.0
            p1 = min(k/2-1, m-1-s1)
            p2 = k - p1 - 2
            if nums1[s1+p1] == nums2[s2+p2]:
                return nums1[s1+p1] / 1.0
            elif nums1[s1+p1] > nums2[s2+p2]:
                return findKthSmallest(s1, s2+p2+1, k-p2-1)
            else:
                return findKthSmallest(s1+p1+1, s2, k-p1-1)
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        if (m+n) % 2 == 1:
            return findKthSmallest(0, 0, (m+n)/2+1)
        else:
            first = findKthSmallest(0, 0, (m+n)/2)
            second = findKthSmallest(0, 0, (m+n)/2+1)
            return (first+second) / 2.0
            

if __name__ == "__main__":
    nums1 = [1,2,3]
    nums2 = [3,4,6,7]
    sol = Solution()
    print sol.findMedianSortedArrays(nums1, nums2)
            
