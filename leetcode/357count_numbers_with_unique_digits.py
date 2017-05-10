from collections import defaultdict
import math
class Solution(object):
    #dp solution with combinatorics
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        dp = [10] * n
        for i in xrange(1, n):
            dp[i] = dp[i-1] + 9 * math.factorial(9) / math.factorial(9 - i)
        return dp[-1]

    #if not use factorial function
    def countNumbersWithUniqueDigits2(self, n):
        if n == 0:
            return 1
        dp = [10] * n
        base = total = 9
        for i in xrange(1, n):
            total *= base
            base -= 1
            dp[i] = dp[i-1] + total
        return dp[-1]

    #further reduce the space complexity to O(1)
    def countNumbersWithUniqueDigits3(self, n):
        if n == 0:
            return 1
        res = 10
        base = total = 9
        for i in xrange(1, n):
            total *= base
            base -= 1
            res += total
        return res

    #Solution4, backtracing
    def countNumbersWithUniqueDigits4(self, n):
        def helper(cur_num, isHighest):
            self.res += 1
            if cur_num == 0:
                return
            for i in xrange(1, 10) if isHighest else xrange(10):
                if used[i] == 0:
                    used[i] = 1
                    helper(cur_num - 1, False)
                    used[i] = 0
        self.res = 0
        used = defaultdict(int)
        helper(n, True)
        return self.res


if __name__ =="__main__":
    sol = Solution()
    print sol.countNumbersWithUniqueDigits3(3)
    print sol.countNumbersWithUniqueDigits4(3)
