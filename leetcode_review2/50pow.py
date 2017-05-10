class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 2:
            return x * x
        
        if n % 2 == 0:
            return self.myPow(x * x, n / 2)
        else:
            return x * self.myPow(x, n-1)

if __name__ == "__main__":
    sol = Solution()
    print sol.myPow(8, 7)
