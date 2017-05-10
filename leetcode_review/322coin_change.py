import sys, time
from collections import deque
class Solution(object):
    #Solution1, TLE
    def coinChange(self, coins, amount):
        def helper(amount):
            if amount in changes:
                return True
            if amount < coins[0]:
                return False
            if amount in coins:
                return True
            else:
                res = False
                minimum = sys.maxint
                for coin in coins:
                    if helper(amount-coin):
                        res = True
                        minimum = min(minimum, changes[amount-coin] + 1)
                        changes[amount] = minimum
                return res

        coins.sort()
        changes = {x: 1 for x in coins}
        changes[0] = 0
        helper(amount)
        return changes[amount] if amount in changes else -1

    #Solution2, still TLE, problem is inner for loop is O(amount), much slower than O(n) if amount is very large
    def coinChange2(self, coins, amount):
        dp = [-1] * (amount+1)
        for coin in coins:
            dp[coin] = 1
        for i in range(2, amount+1):
            if dp[i] != 1:
                minimum = sys.maxint
                for j in range(1, i):
                    if dp[j] != -1 and dp[i-j] != -1:
                        minimum = min(dp[j] + dp[i-j], minimum)
                        dp[i] = minimum
        return 0 if amount == 0 else dp[amount]

    #Solution3, modify the inner loop to O(n), which just iterate through coins
    def coinChange3(self, coins, amount):
        dp = [0] + [amount+1] * amount
        coins.sort()
        for i in xrange(1, amount+1):
            for coin in coins:
                if coin > i:
                    break
                else:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        return -1 if dp[-1] == amount + 1 else dp[-1]

    #Solution4, modify the outer loop to O(n), inner loop to O(amount)
    def coinChange4(self, coins, amount):
        dp = [0] + [amount+1] * amount
        for coin in coins:
            for a in xrange(coin, amount+1):
                dp[a] = min(dp[a], dp[a-coin] + 1)
        return -1 if dp[-1] > amount else dp[-1]
    
    #Solution5, use bfs
    def coinChange5(self, coins, amount):
        visited = set()
        queue = deque([0])
        count = 0
        while len(queue) > 0:
            length = len(queue)
            for i in range(length):
                pre = queue.popleft()
                if pre == amount:
                    return count
                for coin in coins:
                    cur = pre + coin
                    if cur <= amount and cur not in visited:
                        visited.add(cur)
                        queue.append(cur)
            count += 1
        return -1

    #Stefan's bfs version
    def coinChange6(self, coins, amount):
        level = seen = {0}
        count = 0
        while level:
            if amount in level:
                return count
            level = {a + c for a in level for c in coins if a + c <= amount} - seen
            seen |= level
            count += 1
        return -1
    

if __name__ == "__main__":
    sol = Solution()
    # print sol.coinChange([186, 419, 83, 408], 6249)
    time1 = time.time()
    print sol.coinChange2([186, 419, 83, 408], 6249)
    print "solution 2 --- %s seconds ---" % (time.time() - time1)
    time2 = time.time()
    print sol.coinChange3([186, 419, 83, 408], 6249)
    print "solution 3 --- %s seconds ---" % (time.time() - time2)
    time3 = time.time()
    print sol.coinChange4([186, 419, 83, 408], 6249)
    print "solution 4 --- %s seconds ---" % (time.time() - time3)
    time4 = time.time()
    print sol.coinChange5([186, 419, 83, 408], 6249)
    print "solution 5 --- %s seconds ---" % (time.time() - time4)
