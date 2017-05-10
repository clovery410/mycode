class Solution(object):
    #make one number divide by two, another number multiply by 2 through bit manipulation. Need to check whether the smaller number is even or odd, if odd, need to add one bigger number to the result
    def recursive_multiply(self, a, b):
        if a > b:
            return self.recursive_multiply(b, a)
        if a == 0: return 0
        if a == 1: return b
        if a % 2 == 0:
            return self.recursive_multiply(a >> 1, b << 1)
        else:
            return b + self.recursive_multiply(a >> 1, b << 1)

    #solution2, minor modification to solution1 if have the problem of big number multiplication
    def recursive_multiply(self, a, b):
        if a > b:
            return self.recursive_multiply(b, a)
        if a == 0: return 0
        if a == 1: return b
        half = self.recursive_multiply(a >> 1, b)
        if a % 2 == 0:
            return half + half
        else:
            return half + half + b

if __name__ == "__main__":
    sol = Solution()
    print sol.recursive_multiply(6, 4)
