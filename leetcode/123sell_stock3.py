class Solution(object):

    def maxProfit_dp(self, prices):
        n = len(prices)
        profit = [[0 for x in xrange(n)] for x in xrange(2)]
        re_prices = list(reversed(prices))

        if (n == 0):
            return None
        
        minimum = prices[0]
        maximum = re_prices[0]
        profit[0][0] = 0
        profit[1][0] = 0
        for i in xrange(1, n):
            if (prices[i] < minimum):
                minimum = prices[i]
            if (re_prices[i] > maximum):
                maximum = re_prices[i]
            profit[0][i] = max(profit[0][i-1], prices[i] - minimum)
            profit[1][i] = max(profit[1][i-1], maximum - re_prices[i])

        return profit

    def maxProfit_mostTwo(self, prices):
        n = len(prices)
        profit = self.maxProfit_dp(prices)
        two_trans = 0
        if profit is None:
            return 0
        for k in xrange(n):
            two_trans = max(two_trans, (profit[0][k] + profit[1][n-k-1]))
        return two_trans

if __name__ == '__main__':
    prices = [2, 1, 2, 0, 1]
    solution = Solution()
    result = solution.maxProfit_dp(prices)
    result1 = solution.maxProfit_mostTwo(prices)
    print result1
