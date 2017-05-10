class Solution(object):
    def intersection(self, nums1, nums2):
        return [x for x in set(nums1) & set(nums2)]
