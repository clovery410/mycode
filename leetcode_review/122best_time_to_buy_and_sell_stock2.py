class Solution(object):
    def maxProfit(self, prices):
        profits = [prices[i] - prices[i-1] for i in xrange(1, len(prices))]
        return sum([profit for profit in profits if profit > 0])

if __name__ == "__main__":
    prices = [1]
    sol = Solution()
    print sol.maxProfit(prices)
