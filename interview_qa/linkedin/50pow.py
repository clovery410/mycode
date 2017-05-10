class Solution(object):
    def myPow(self, x, n):
        print x, n
        if n == 0:
            return 1.0

        # this deals with overflow problem which might occur in Java or C++, but this line is not need in Python since Python extend int to long automatically if overlow.
        if n == -(1 << 31):
            return self.myPow(x * x, n / 2)
        
        if n < 0:
            return 1 / self.myPow(x, -n)
        return self.myPow(x * x, n / 2) if n % 2 == 0 else x * self.myPow(x, n-1)

if __name__ == "__main__":
    sol = Solution()
    print -(1 << 31)
    print sol.myPow(2.00000, -2147483648)
