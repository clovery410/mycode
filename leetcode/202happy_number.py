class Solution(object):
    def isHappy(self, n):
        start = n
        count = []
        while start != 1:
            res = 0
            while start > 0:
                res += pow(start % 10, 2)
                start /= 10
            start = res
            if start in count:
                return False
            count.append(start)
        return True
