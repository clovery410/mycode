class Solution(object):
    def calculate(self, s):
        n = len(s)
        if n <= 0:
            return 0
        res, sign = 0, 1
        stack = []
        i = 0
        while i < n:
            if self.isDigit(s[i]):
                digit_val = int(s[i])
                while i + 1 < n and self.isDigit(s[i+1]):
                    digit_val = digit_val * 10 + int(s[i+1])
                    i += 1
                res += digit_val * sign
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif s[i] == ')':
                res = res * stack.pop() + stack.pop()
            i += 1
        return res

    def isDigit(self, c):
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            return True
        return False


if __name__ == '__main__':
    sol = Solution()
    exp = "(1-(4+5+2)+3) + (6+8)"
    print sol.calculate(exp)
