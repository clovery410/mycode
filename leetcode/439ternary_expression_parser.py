class Solution(object):
    def parseTernary(self, expression):
        def evaluate(expression):
            if expression == 'T' or expression == 'F' or expression.isdigit():
                return expression

            count = 1
            start = end = 2
            while end < len(expression):
                c = expression[end]
                if c == ':':
                    count -= 1
                elif c == '?':
                    count += 1
                if count == 0:
                    break
                end += 1
            if expression[0] == 'T':
                return evaluate(expression[start:end])
            else:
                return evaluate(expression[end+1:])
        return evaluate(expression)

if __name__ == "__main__":
    sol = Solution()
    expression = "T?T?F:5:3"
    expression2 = "F?1:T?4:5"
    print sol.parseTernary(expression2)
                
