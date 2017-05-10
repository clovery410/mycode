class Solution(object):
    def calculate(self, s):
        #First remove the space in the string
        s = s.replace(" ", "")
        stack = []
        curr_num, curr_i = self.getNext(s, 0)
        stack.append(curr_num)
        while curr_i < len(s):
            op = s[curr_i]
            curr_num, curr_i = self.getNext(s, curr_i+1)
            if op == '+':
                stack.append(curr_num)
            elif op == '-':
                stack.append(-curr_num)
            elif op == '*':
                stack[-1] *= curr_num
            elif op == '/':
                stack[-1] = stack[-1] / curr_num if stack[-1] >= 0 else -((-stack[-1]) / curr_num)
        return sum(stack)
    
    def getNext(self, s, idx):
        res = 0
        while idx < len(s) and s[idx] not in '+-*/':
            res = res * 10 + int(s[idx])
            idx += 1
        return (res, idx)

    #Solution2, to optimize the space complexity
    def calculate2(self, s):
        s = s.replace(' ', '') + ' '
        num, op = '', '+'
        temp, res = 0, 0
        for c in s:
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
                elif op == '/':
                    if temp < 0: temp = -((-temp) / int(num))
                    else: temp /= int(num)
                op = c
                num = ''
        return res + temp

if __name__ == "__main__":
    sol = Solution()
    s = "16/2 + 10"
    print sol.calculate2(s)
