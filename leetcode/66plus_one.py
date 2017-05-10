class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)
        for digit in reversed(xrange(l)):
            if digits[digit] == 9:
                digits[digit] = 0
            else:
                digits[digit] += 1
                break
        if digits[0] == 0:
            digits[0] = 1
            digits.append(0)
        return digits

