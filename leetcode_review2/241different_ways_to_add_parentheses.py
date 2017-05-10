class Solution(object):
    def diffWaysToCompute(self, input):
        def evaluate(expression):
            if len(expression) == 1:
                return [int(expression[0])]
            res = []
            for i in xrange(len(expression)):
                c = expression[i]
                if c in '+-*':
                    pre_res = evaluate(expression[:i])
                    pos_res = evaluate(expression[i+1:])
                    for pre_val in pre_res:
                        for pos_val in pos_res:
                            res.append(op[c](pre_val, pos_val))
            return res
        num = ''
        inputs = []
        i = 0
        while True:
            if i == len(input):
                inputs.append(num)
                break
            c = input[i]
            if c == ' ':
                continue
            if c.isdigit():
                num += c
            elif c in '+-*':
                inputs.append(num)
                inputs.append(c)
                num = ''
            i += 1
                
        print inputs
        op = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}
        return evaluate(inputs)

    # solution2, try to not first convert into array
    def diffWaysToCompute2(self, input):
        def evaluate(start, end):
            if input[start:end].isdigit():
                return [int(input[start:end])]
            
            res = []
            for i in xrange(start, end):
                c = input[i]
                if c in '+-*':
                    pre_res = evaluate(start, i)
                    pos_res = evaluate(i+1, end)
                    for pre_val in pre_res:
                        for pos_val in pos_res:
                            res.append(op[c](pre_val, pos_val))
            return res
        op = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}
        return evaluate(0, len(input))
                
if __name__ == "__main__":
    sol = Solution()
    print sol.diffWaysToCompute("2-1-1-1")
    print sol.diffWaysToCompute2("2-1-1-1")
