class Stock(object):
    def singleTransaction(self, prices):
        """
        find the maximum profit with only one buy and one sell, return the profit
        """
        profits = [0 for x in xrange(len(prices))]
        min_price = prices[0]
        for i in xrange(1, len(prices)):
            profits[i] = max(profits[i-1], prices[i] - min_price)
            min_price = min(min_price, prices[i])
        print profits
        return profits[-1]
    
    def multipleTransaction(self, prices):
        """
        You may buy one and sell one share of stock multiple times, but you may not engage in multiple transactions at the same time
        """
        profits = []
        for i in xrange(1, len(prices)):
            profits.append(prices[i] - prices[i-1])

        max_profit = sum([profit for profit in profits if profit > 0])
        return max_profit

    def unlimitedWithCommission(self, prices, cost):
        profits = []
        for i in xrange(1, len(prices)):
            profits.append(prices[i] - prices[i-1])
        max_profit = 0
        for profit in profits:
            

if __name__ == '__main__':
    s = Stock()
    print s.singleTransaction([20, 40, 52, 15, 30, 50, 10, 25])
    print s.multipleTransaction([20, 40, 52, 15, 30, 50, 10, 25])
