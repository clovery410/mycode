class Solution(object):
    def plusOne(self, digits):
        i = len(digits) - 1
        while i >= 0 and digits[i] == 9:
            i -= 1

        for j in xrange(i+1, len(digits)):
            digits[j] = 0
        if i >= 0:
            digits[i] += 1
            return digits
        else:
            return [1] + digits
