class Solution(object):
    def toHex(self, num):
        hex_map = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        res = []
        for i in xrange(8):
            cur_four = num & 15
            if cur_four >= 10:
                res.append(hex_map[cur_four])
            else:
                res.append(str(cur_four))
            num >>= 4

        while res and res[-1] == '0':
            res.pop()
        return ''.join(reversed(res)) if res else '0'
