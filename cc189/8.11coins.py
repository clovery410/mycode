class Solution(object):
    #solution1, just recursive
    # recurse through each coins from large to small, for each kind of coin iterative through the maximum amount it can use to 0, then recurse it to next coin
    def coinChangeWays1(self, coins, n):
        def makeChange(idx, remain):
            if idx >= len(coins):
                if remain == 0:
                    return 1
                return 0
            res = 0
            for i in xrange(remain/coins[idx] + 1):
                res += makeChange(idx+1, remain - i * coins[idx])
            return res
        
        coins.sort(reverse = True)
        return makeChange(0, n)

    #solution2, optimize solution1 by adding memoization
    def coinChangeWays2(self, coins, n):
        def makeChange(idx, remain):
            if idx >= len(coins):
                if remain == 0:
                    return 1
                return 0

            if (idx, remain) in memo:
                return memo[(idx, remain)]
            res = 0
            for i in xrange(remain/coins[idx] + 1):
                res += makeChange(idx+1, remain - i * coins[idx])
            memo[(idx, remain)] = res
            return res

        coins.sort(reverse = True)
        memo = {}
        return makeChange(0, n)

if __name__ == "__main__":
    sol = Solution()
    coins = [1, 5, 10, 25]
    print sol.coinChangeWays1(coins, 29)
    print sol.coinChangeWays2(coins, 29)
                    
