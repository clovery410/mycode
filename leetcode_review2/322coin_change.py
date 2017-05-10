class Solution(object):
    # solution1, TLE
    def coinChange(self, coins, amount):
        dp = [0] + [amount+1] * amount
        coins.sort()

        for i in xrange(1, len(dp)):
            for coin in coins:
                if coin > i:
                    break
                dp[i] = min(dp[i], dp[i-coin] + 1)
                
        return dp[-1] if dp[-1] < amount + 1 else -1

    # solution2, change the loop order of dp solution
    def coinChange2(self, coins, amount):
        dp = [0] + [amount+1] * amount
        coins.sort()

        for coin in coins:
            for a in xrange(coin, amount+1):
                dp[a] = min(dp[a], dp[a-coin] + 1)
                
        return dp[-1] if dp[-1] < amount + 1 else -1

    # solution3, bfs solution
    def coinChange3(self, coins, amount):
        if amount == 0:
            return 0
        
        import collections
        queue = collections.deque(coins)
        visited = set()
        count = 1
        coins.sort()
        
        while queue:
            length = len(queue)
            for i in xrange(length):
                cur_money = queue.popleft()
                if cur_money == amount:
                    return count
                
                for coin in coins:
                    if coin + cur_money > amount:
                        break
                    if coin + cur_money not in visited:
                        visited.add(coin + cur_money)
                        queue.append(coin + cur_money)
            count += 1
        return -1
                    
