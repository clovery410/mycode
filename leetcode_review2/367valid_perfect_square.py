class Solution(object):
    def isPerfectSquare(self, num):
        def binarySearch(s, e):
            while s <= e:
                mid = (e - s) / 2 + s
                if mid * mid == num:
                    return True
                if mid * mid > num:
                    e = mid - 1
                else:
                    s = mid + 1
            return False
        
        return binarySearch(1, num)
