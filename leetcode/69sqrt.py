class Solution(object):
    def mySqrt(self, x):
        start, end = 1, x
        while start <= end:
            mid = (end - start) / 2 + start
            if mid * mid <= x and (mid+1) * (mid+1) > x:
                return mid
            elif mid * mid > x:
                end = mid - 1
            else:
                start = mid + 1
        return 0
