class Solution(object):
    def getHint(self, secret, guess):
        bulls = cows = 0
        records = collections.defaultdict(int)
        for i in xrange(len(secret)):
            if secret[i] != guess[i]:
                records[secret[i]] += 1

        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            elif records[guess[i]] > 0:
                records[guess[i]] -= 1
                cows += 1
        return str(bulls) + 'A' + str(cows) + 'B'
                    
            
