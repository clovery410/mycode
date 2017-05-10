class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        min_cost, max_profit = prices[0], 0
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_cost)
            min_cost = min(min_cost, price)
        return max_profit

if __name__ =="__main__":
    prices = [7,6,4,3,1]
    sol = Solution()
    print sol.maxProfit(prices)
