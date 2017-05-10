class Solution(object):
    def calculate(self, s):
        num = ''
        res = temp = 0
        op = '+'
        
        for c in s + '+':
            if c == ' ':
                continue
            if c.isdigit():
                num += c
            else:
                if op == '+':
                    res += temp
                    temp = int(num)
                elif op == '-':
                    res += temp
                    temp = -int(num)
                elif op == '*':
                    temp *= int(num)
                else:
                    temp = int(temp / float(num))
                op = c
                num = ''
        return res + temp
