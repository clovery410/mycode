class Solution(object):
    def divide(self, dividend, divisor):
        if divisor == 0:
            return sys.maxint
        if dividend == 0:
            return 0

        neg = (dividend < 0) != (divisor < 0)
        left = abs(dividend)
        divisor = right = abs(divisor)
        res = 0
        q = 1
        while left >= divisor:
            left -= right
            res += q
            q += q
            right += right
            if left < right:
                right = divisor
                q = 1

        if neg:
            res = -res
        return sys.maxtint if res < -sys.maxint-1 or res > sys.maxint else res        
