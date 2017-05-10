class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        s, e = 0, l-1
        while s <= e:
            mid = (e - s) / 2 + s
            if l - mid == citations[mid]:
                return l - mid
            if l - mid > citations[mid]:
                s = mid + 1
            else:
                e = mid - 1
        return l - s
