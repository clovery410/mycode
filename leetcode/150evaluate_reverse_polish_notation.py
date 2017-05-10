class Solution(object):
    def evalRPN(self, tokens):
        ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: int(float(x) / float(y))}
        stack = []
        for token in tokens:
            if token in '+-*/':
                second = stack.pop()
                first = stack.pop()
                stack.append(ops[token](first, second))
            else:
                stack.append(int(token))
        return stack[-1]

if __name__ == "__main__":
    ins = ["4", "5", "-13", "/", "+"]
    sol = Solution()
    print (sol.evalRPN(ins))
