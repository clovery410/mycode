class Solution(object):
    def isPerfectSquare(self, num):
        start, end = 1, num
        while start <= end:
            mid = (end - start) / 2 + start
            if mid * mid == num:
                return True
            elif mid * mid > num:
                end = mid - 1
            else:
                start = mid + 1
        return False
