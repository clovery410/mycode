class Solution(object):
    def merge(self, nums1, m, nums2, n):
        l = m + n
        idx1, idx2 = m-1, n-1
        for i in reversed(xrange(l)):
            cur1 = nums1[idx1] if idx1 >= 0 else None
            cur2 = nums2[idx2] if idx2 >= 0 else None
            if cur2 == None or cur1 >= cur2:
                nums1[i] = cur1
                idx1 -= 1
            else:
                nums1[i] = cur2
                idx2 -= 1
