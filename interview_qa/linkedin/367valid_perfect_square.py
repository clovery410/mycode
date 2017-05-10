class Solution(object):
    def isPerfectSquare(self, num):
        s, e = 1, num
        while s <= e:
            mid = (e - s) / 2 + s
            prod = mid * mid
            if prod == num:
                return True
            elif prod < num:
                s = mid + 1
            else:
                e = mid - 1
        return False
