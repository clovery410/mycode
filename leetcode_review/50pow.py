class Solution(object):
    def myPow(self, x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        elif n == -1:
            return 1.0 / x
        if n % 2 == 0:
            return self.myPow(x * x, n / 2)
        else:
            return x * self.myPow(x * x, n / 2)

if __name__ == "__main__":
    sol = Solution()
    print sol.myPow(0, -3)
        
