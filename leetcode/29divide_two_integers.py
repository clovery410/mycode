import sys
class Solution(object):
    def divide(self, dividend, divisor):
        if divisor == 0:
            return sys.maxint
        neg = ((dividend < 0) != (divisor < 0))
        dividend = left = abs(dividend)
        divisor = div = abs(divisor)
        res = 0
        q = 1
        while left >= divisor:
            left -= div
            res += q
            q += q
            div += div
            if left < div:
                div = divisor
                q = 1

        if neg:
            return max(-res, -sys.maxint)
        else:
            return min(res, sys.maxint)
            
        
