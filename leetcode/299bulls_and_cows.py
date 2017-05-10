class Solution(object):
    def getHint(self, secret, guess):
        bull_count = cow_count = 0
        bulls = [0] * 10
        cows = [0] * 10
        for i in xrange(len(secret)):
            num1, num2 = int(secret[i]), int(guess[i])
            if num1 == num2:
                bull_count += 1
            else:
                bulls[num1] += 1
                cows[num2] += 1
        for i in xrange(len(bulls)):
            if bulls[i] and cows[i]:
                cow_count += min(bulls[i], cows[i])
        return str(bull_count) + 'A' + str(cow_count) + 'B'
                
