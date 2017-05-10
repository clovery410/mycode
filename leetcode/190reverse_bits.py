class Solution(object):
    def reverseBits(self, n):
        res = 0
        for i in xrange(32):
            res = (res << 1) + (n & 1)
            n >>= 1
        return res

    #solution2, for the follow-up, can do the reverse in byte unit
    def reverseBits2(self, n):
        def reverseByte(num):
            if num in cache:
                return cache[num]
            res = 0
            tmp = num
            for i in xrange(8):
                res = (res << 1) + (num & 1)
                num >>= 1
                
            cache[tmp] = res
            return res
        
        res = 0
        byte = []
        mask = 0xff
        for i in xrange(4):
            byte.append(n & mask)
            n >>= 8

        res = 0
        cache = {}
        for i, num in enumerate(byte):
            res += reverseByte(num)
            if i < 3:
                res <<= 8
        return res
        

if __name__ == "__main__":
    sol = Solution()
    # print sol.reverseBits2(43261596)
    print sol.reverseBits2(1)
