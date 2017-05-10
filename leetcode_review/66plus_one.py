class Solution(object):
    def plusOne(self, digits):
        carry = 1
        for i in reversed(xrange(len(digits))):
            res = digits[i] + carry
            digits[i] = res % 10
            carry = res / 10

        return [carry] + digits if carry > 0 else digits
            
