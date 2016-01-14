class Solution(object):

    def maxProfit_dp(self, prices):
        profit = [0 for x in xrange(len(prices))]
        if (len(prices) == 0):
            return 0
        minimum = prices[0]
        for i in xrange(1, len(prices)):
            if (prices[i] < minimum):
                minimum = prices[i]
            profit[i] = max(profit[i-1], prices[i] - minimum)

        return profit[-1]

    def maxProfit_multiple(self, prices):
        profit = []
        total_profit = 0
        if (len(prices) <= 1):
            return 0
        for i in xrange(len(prices) - 1):
            profit.append(prices[i+1] - prices[i])
        for i in xrange(len(profit)):
            if profit[i] > 0:
                total_profit += profit[i]
        return total_profit

    # This is brute-force, running time not good, using dp with memorization in 123sell_stock.py
    def maxProfit_mostTwo(self, prices):
        profit = 0
        for k in xrange(len(prices)):
            profit = max(profit, (self.maxProfit_dp(prices[:k+1]) + self.maxProfit_dp(prices[k+1:])))
        return profit
        
            

if __name__ == '__main__':
    prices = [5, 3, 7, 10, 2, 7, 4, 10]
    test = Solution()
    result = test.maxProfit_multiple(prices)
    result2 = test.maxProfit_mostTwo(prices)
    print result
    print result2
