class Solution(object):
    def mySqrt(self, x):
        if x <= 1:
            return x
        
        s, e = 1, x
        while s < e:
            mid = (e - s) / 2 + s
            cur, pos = mid * mid, (mid+1) * (mid+1)
            if cur <= x and pos > x:
                return mid
            if cur < x:
                s = mid + 1
            else:
                e = mid - 1
        return s
            
