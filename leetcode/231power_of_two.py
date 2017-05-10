class Solution(object):
    def isPowerOfTwo(self, n):
        # need to consider 0 seperately
        if n == 0:
            return False
        
        return False if n & (n-1) else True
