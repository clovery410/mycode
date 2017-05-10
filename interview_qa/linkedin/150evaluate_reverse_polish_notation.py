class Solution(object):
    def evalRPN(self, tokens):
        op = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: int(x * 1.0 / y)}
        
        stack = []
        for token in tokens:
            if token in op:
                print token
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(op[token](operand1, operand2))
            else:
                stack.append(int(token))
        return stack[0]

if __name__ == "__main__":
    sol = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print sol.evalRPN(tokens)
