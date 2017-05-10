class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        if len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        elif len(b) < len(a):
            b = '0' * (len(a) - len(b)) + b
        i, new_l= -1, len(a)
        carryon = 0
        while i >= -new_l:
            curr_bit, carryon = self.adder(int(a[i]), int(b[i]), carryon)
            res = str(curr_bit) + res
            i -= 1
        if carryon:
            res = '1' + res
        return res
    
    
    def adder(self, bit_a, bit_b, carry):
        res = (bit_a + bit_b + carry) % 2
        carry = (bit_a + bit_b + carry) / 2
        return res, carry
