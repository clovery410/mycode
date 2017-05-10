class Solution(object):
    #solution1, TLE, too slow
    def maxProfit(self, prices):
        def helper(idx, hold, hold_price):
            if idx >= len(prices):
                return 0
            if (idx, hold, hold_price) in cache:
                return cache[(idx, hold, hold_price)]
            if hold:
                hold_profit = helper(idx+1, True, hold_price)
                sell_profit = helper(idx+2, False, 0) + prices[idx] - hold_price
                cache[(idx, hold, hold_price)] = max(hold_profit, sell_profit)
            else:
                buy_profit = helper(idx+1, True, prices[idx])
                look_profit = helper(idx+1, False, hold_price)
                cache[(idx, hold, hold_price)] = max(buy_profit, look_profit)
            return cache[(idx, hold, hold_price)]

        cache = {}
        return helper(0, False, 0)

    #solution2, learned from forum, a little trick here
    #profit1[i] = max profit on day i if I sell
    #profit2[i] = max profit on day i if I do nothing
    #1. profit1[i+1] means I must sell on day i+1, and there are 2 cases:
    #a. If I just sold on day i, then I have to buy again on day i and sell on day i+1
    #b. If I did nothing on day i, then I have to buy today and sell today
    #Taking both cases into account, profit1[i+1] = max(profit1[i]+prices[i+1]-prices[i], profit2[i])
    #2. profit2[i+1] means I do nothing on day i+1, so it will be max(profit1[i], profit2[i])
    def maxProfit2(self, prices):
        profit1, profit2 = 0, 0
        for i in xrange(1, len(prices)):
            profit1, profit2 = max(profit1 + prices[i] - prices[i-1], profit2), max(profit1, profit2)
        return max(profit1, profit2)

    #solution3, also learned from forum. There can be 3 states and 5 edges for state transition in total, 3 states are hold, notHold, notHold_cooldown, transition model are as follow:
    # hold -----do nothing----->hold
    # hold -----sell----->notHold_cooldown
    # notHold -----do nothing -----> notHold
    # notHold -----buy-----> hold
    # notHold_cooldown -----do nothing----->notHold
    def maxProfit3(self, prices):
        notHold, hold, notHold_cooldown = 0, float('-inf'), float('-inf')
        for price in prices:
            notHold, hold, notHold_cooldown = max(notHold, notHold_cooldown), max(hold, notHold - price), hold + price
        return max(notHold, hold, notHold_cooldown)
