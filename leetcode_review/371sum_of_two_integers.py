class Solution(object):
    def getSum(self, a, b):
        for i in xrange(32):
            carry = a & b
            a ^= b
            b = carry << 1
        return a if a & 0x80000000 else a & 0xffffffff

if __name__  == "__main__":
    sol = Solution()
    print sol.getSum(12, 23)
            
