class Solution(object):
    def numberOfOneBits(self, num):
        bit_sum = 0
        for i in xrange(32):
            bit_sum += ((1 << i) & num) >> i

        return bit_sum

    def hammingWeight(self, n):
        count = 0
        while n:
            count += 1
            n &= (n - 1)
        return count

if __name__ == '__main__':
    n = 7
    sol = Solution()
    print sol.numberOfOneBits(n)
    print sol.hammingWeight(n)
