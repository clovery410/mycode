import sys
class Solution(object):
    #solution1
    def maxProfit(self, prices):
        if len(prices) <= 2:
            return max(prices[1] - prices[0], 0) if len(prices) == 2 else 0

        #divide into 3 manipulations: buy, sell, cooldown; and 2 stages: hold & unhold
        hold = [0] * len(prices)
        unhold = [0] * len(prices)
        hold[0], unhold[0] = -prices[0], 0
        hold[1], unhold[1] = max(-prices[0], -prices[1]), max(prices[1] - prices[0], 0)

        for i in range(2, len(prices)):
            hold[i] = max(hold[i-1], unhold[i-2] - prices[i])
            unhold[i] = max(unhold[i-1], hold[i-1] + prices[i])
        return unhold[-1]

    #Solution2, review previous solution2
    def maxProfit2(self, prices):
        #divide into 3 state and 5 transitions, hold, notHold, notHold_cooldown
        hold, notHold, notHold_cooldown = -sys.maxint - 1, 0, 0
        for price in prices:
            hold = max(hold, notHold - price)
            notHold = max(notHold, notHold_cooldown)
            notHold_cooldown = hold + price
        return max(notHold, notHold_cooldown)

    #Solution3, review previous solution3, every day, only consider two manipulations, sell or do nothing
    def maxProfit3(self, prices):
        #use profit1 denote on that day, the maximum profit I can get if I sell, use profit2 denote on that day, the maximum profit I can get if I do nothing
        profit1, profit2 = 0, 0
        for i in range(1, len(prices)):
            profit1, profit2 = max(profit1 + prices[i] - prices[i-1], profit2), max(profit1, profit2)
        return max(profit1, profit2)
        
if __name__ == "__main__":
    prices = [9,5,7,4,2,4,1,6,4]
    prices2 = [6,1,6,4,3,0,2]
    sol = Solution()
    print sol.maxProfit2(prices)
    print sol.maxProfit3(prices)
