class Solution(object):
    def countBits(self, num):
        bits = [0 for x in xrange(num + 1)]
        if num < 1:
            return bits
        
        bits[1] = 1
        for i in xrange(2, num + 1):
            quotient = i / 2
            remainder = i % 2
            bits[i] = bits[quotient] + bits[remainder]
        return bits
