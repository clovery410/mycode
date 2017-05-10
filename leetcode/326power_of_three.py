import math
class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        
        x = round(math.log(n, 3))
        if pow(3, x) != n:
            return False
        else:
            return True
