class Solution(object):
    #this solution does not work in python, since python uses "unlimited" bits to represent integer(just think of python don't have problem of int overflow, since it can automatically converted to long type). However, in Java and Cpp, they use fixed bit length for primitive types, so this solution only works in java and cpp.
    def getSum(self, a, b):
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1  # this is used for denote whether there is a carry, 0 << 1 is 0, 1 << 1 is 2.
        return a

    #solution2, try to check when we already shifted 32 bits, whether a is largert than the limit of int
    def getSum2(self, a, b):
        for _ in xrange(32):
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a if a & 0x80000000 else a & 0xffffffff
    
if __name__ == "__main__":
    sol = Solution()
    print sol.getSum2(-1, -1)
