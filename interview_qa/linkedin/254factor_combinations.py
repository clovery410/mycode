import math
class Solution(object):
    def getFactors(self, n):
        def generate(remain):
            res = []
            for i in xrange(2, int(math.sqrt(remain)) + 1):
                if remain % i == 0:
                    middle = generate(remain / i)
                    # print remain, i, middle
                    res.extend([[i, remain / i]])
                    res.extend([[i] + x for x in middle if x[0] >= i])
            return res

        return generate(n)

if __name__ == "__main__":
    sol = Solution()
    print sol.getFactors(12)
        
