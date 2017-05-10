class Solution(object):
    def firstBadVersion(self, n):
        s, e = 1, n
        while s <= e:
            mid = (e - s) / 2 + s
            if isBadVersion(mid):
                e = mid - 1
            else:
                s = mid + 1
        return s
