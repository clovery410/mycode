class Solution(object):
    def grayCode(self, n):
        if n == 0:
            return [0]

        prev = self.grayCode(n-1)
        return prev + [x + 2 ** (n-1) for x in reversed(prev)]

