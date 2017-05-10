class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: int(x * 1.0 / y)}

        stack = []
        for token in tokens:
            if token in op:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(op[token](operand1, operand2))
            else:
                stack.append(int(token))
        return stack[0]
