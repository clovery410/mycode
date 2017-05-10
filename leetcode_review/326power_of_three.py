class Solution(object):
    """
    First power of three means n^3
    """
    # trivial recursive solution
    def isPowerOfThree(self, n):
        return n > 0 and (n == 1 or (n % 3 == 0 and self.isPowerOfThree(n / 3)))

    # trivial iterative solution
    def isPowerOfThree2(self, n):
        if n > 1:
            while n % 3 == 0:
                n /= 3
        return n == 1

    # math solution, find the maximum integer that is a power of 3 and check if it is a multiple of the given input.
    def isPowerOfThree3(self, n):
        return n > 0 and (1162261467 % n == 0)

    
    
