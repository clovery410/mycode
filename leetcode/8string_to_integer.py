import re
class Solution(object):
    #My first ugly solution
    def myAtoi(self, string):
        sign = 1
        MIN, MAX = -2147483648, 2147483647
        string = string.lstrip()
        if not string or string[0] not in '+-0123456789':
            return 0
        if string[0] in '+-':
            if string[0] == '-':
                sign = -1
            string = string[1:]
            
        i = 0
        curr_total = 0
        for c in string:
            if curr_total * sign < MIN or curr_total * sign > MAX:
                break
            elif c not in '0123456789':
                break
            else:
                curr_total = curr_total * 10 + ord(c) - ord('0')
        if curr_total * sign < MIN:
            return MIN
        elif curr_total * sign > MAX:
            return MAX
        else:
            return curr_total * sign

    #Solution2, try to compact the code
    def myAtoi2(self, string):
        string = string.lstrip()
        if not string or not string[0] not in '=-1234567890': return 0
        MIN, MAX = -2147483648, 2147483647
        sign, res = 1, 0
        if string[0] in '+-':
            sign = 44 - ord(string[0])
            string = string[1:]
        for c in string:
            if c.isdigit():
                res = res * 10 + ord(c) - ord('0')
            else:
                return res * sign
            if res > MAX:
                return MAX if sign == 1 else MIN
        return res * sign

    #Solution3, use regex
    def myAtoi3(self, string):
        m = re.match(r' *([+-]?\d+).*', string)
        if m:
            return max(-2147483648, min(2147483647, int(m.group[1])))
        return 0
