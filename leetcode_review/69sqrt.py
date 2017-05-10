class Solution(object):
    #Solution1, bassic binary search solution
    def mySqrt(self, x):
        start, end = 1, x
        while start <= end:
            mid = (end - start) / 2 + start
            if mid > x / mid:
                end = mid - 1
            elif (mid+1) > x / (mid+1):
                return mid
            else:
                start = mid + 1
        return 0

    #Solution2, use Newton's method
    def mySqrt2(self, x):
        r = x
        while r * r > x:
            r = r + (x - r * r) / (2 * r)
        return r
