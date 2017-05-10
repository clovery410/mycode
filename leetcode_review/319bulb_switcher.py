class Solution(object):
    def bulbSwitch(self, n):
        if n <= 0:
            return 0
        return int(math.sqrt(n))
