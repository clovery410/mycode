import math
class Solution(object):
    def convertToTitle(self, n):
        if n == 1: return 'A'

        digits, cur = 1, 26
        while cur < n:
            digits += 1
            cur += pow(26, digits)
            
        res = [0] * digits
        for i in xrange(digits):
            if n > 26:
                res[i] = (n-1) / pow(26, digits-i-1)
                n = n - res[i] * pow(26, digits-i-1)
            else:
                res[i] = n
        return ''.join(chr(i+64) for i in res)

    #solution2, learned from discuss
    def convertToTitle2(self, n):
        capitals = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        res = []
        while n > 0:
            res.append(capitals[(n-1) % 26])
            n = 

if __name__ == "__main__":
    sol = Solution()
    print sol.convertToTitle(7)
