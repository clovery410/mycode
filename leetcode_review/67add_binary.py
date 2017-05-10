class Solution(object):
    def addBinary(self, a, b):
        m, n = len(a), len(b)
        if m > n: return self.addBinary(b, a)

        carry = 0
        res = []
        for i in xrange(1, m + 1):
            res.append(int(a[-i]) ^ int(b[-i]) ^ carry)
            carry = (int(a[-i]) & int(b[-i])) | (int(a[-i]) & carry) | (int(b[-i]) & carry)

        for j in xrange(i+1, n + 1):
            res.append(int(b[-j]) ^ carry)
            carry = int(b[-j]) & carry
            
        if carry:
            res.append(carry)
            
        return ''.join([str(x) for x in reversed(res)])

if __name__ == "__main__":
    sol = Solution()
    print sol.addBinary("11", "1")
