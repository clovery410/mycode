class Solution(object):
    #Solution 1, time complexity is not good
    def myPow(self, x, n):
        if n == 0 or x == 1.0:
            return 1.0
        elif x == -1.0:
            return 1.0 if n % 2 == 0 else -1.0
        
        res = 1.0
        op = 1 if n > 0 else 0
        for i in xrange(abs(n)):
            if op:
                res *= x
            else:
                res /= x
            if res == 0.0:
                return res
        return res

    # Solutoin2, Binary search
    def mypow2(self, x, n):
        if n == 0:
            return 1
        if n == -1:
            return 1 / x
        return self.mypow2(x * x, n / 2) if n % 2 == 0 else self.mypow2(x * x, n / 2) * x


if __name__ == "__main__":
    sol = Solution()
    print sol.mypow2(8.88023, -3)
