class Solution(object):
    def firstBadVersion(self, n):
        s, e = 1, n
        while s <= e:
            mid = (e - s) / 2 + s
            if not isBadVersion(mid):
                if isBadVersion(mid+1):
                    return mid + 1
                s = mid + 1
            else:
                e = mid - 1
        return s
