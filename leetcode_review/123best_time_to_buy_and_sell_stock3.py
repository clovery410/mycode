class Solution(object):
    #Solution1, TLE
    def maxProfit(self, prices):
        def profit_dp(start, end):
            max_profit, min_cost = 0, prices[start]
            for i in xrange(start+1, end):
                min_cost = min(min_cost, prices[i])
                max_profit = max(max_profit, prices[i] - min_cost)
            return max_profit
        res = 0
        for i in xrange(len(prices)-1):
            res = max(res, profit_dp(0, i) + profit_dp(i, len(prices)))
        return res

    #Solution2,
    def maxProfit2(self, prices):
        def profit_dp(start, end):
            min_cost, max_cost = prices[start], prices[end]
            for i in xrange(start, end+1):
                j = len(prices) - i - 1
                if i > start:
                    min_cost = min(min_cost, prices[i])
                    profits[0][i] = max(profits[0][i-1], prices[i] - min_cost)
                if j < end:
                    max_cost = max(max_cost, prices[j])
                    profits[1][j] = max(profits[1][j+1], max_cost - prices[j])
        n, res = len(prices), 0
        if n <= 1:
            return 0
        
        profits = [[0] * n for _ in xrange(2)]
        profit_dp(0, n-1)

        for i in xrange(n):
            res = max(res, profits[0][i] + profits[1][i])
        return res

if __name__ == "__main__":
    sol = Solution()
    prices = [1,2,9,5,4,8]
    print sol.maxProfit(prices)
    print sol.maxProfit2(prices)
