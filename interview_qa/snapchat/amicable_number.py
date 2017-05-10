import math
class Solution(object):
    def findAmicableNumber(self, start, end):
        def getFactorial(num):
            fact_sum = 1
            for i in xrange(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    fact_sum += i + num / i
            return fact_sum

        cache = [0] * (end - start + 1)
        res = []
        for x in xrange(start, end+1):
            y = getFactorial(x)
            cache[x-start] = y
            if start <= y <= end:
                if not cache[y-start]:
                    cache[y-start] = getFactorial(y)
                if cache[y-start] == x and x < y:
                    res.append((x, y))

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print sol.findAmicableNumber(1, 100000)
    
