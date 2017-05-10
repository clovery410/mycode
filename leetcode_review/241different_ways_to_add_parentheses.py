class Solution(object):
    def diffWaysToCompute(self, input):
        def helper(start, end):
            if (start, end) in cache:
                return cache[(start, end)]
            if input[start:end].isdigit():
                cache[(start, end)] = [int(input[start:end])]
            else:
                curr_res = []
                for i in xrange(start, end):
                    op = input[i]
                    if op in "+-*":
                        left_total = helper(start, i)
                        right_total = helper(i+1, end)
                        for left_res in left_total:
                            for right_res in right_total:
                                total = ops[op](left_res, right_res)
                                curr_res.append(total)
                cache[(start, end)] = curr_res
            return cache[(start, end)]
        
        ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}
        cache = {}
        return helper(0, len(input))

    #Solution, more consice version
    def diffWaysToCompute2(self, input):
        def helper(inputs):
            if inputs not in cache:
                if inputs.isdigit():
                    return [int(inputs)]
                else:
                    curr_res = []
                    for i, c in enumerate(inputs):
                        if c in "+-*":
                            for left_op in helper(inputs[:i]):
                                for right_op in helper(inputs[i+1:]):
                                    curr_res.append(ops[c](left_op, right_op))
                    cache[inputs] = curr_res
            return cache[inputs]
        ops = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y}
        cache = {}
        return helper(input)

if __name__ == "__main__":
    input = "2*3-4*5"
    sol = Solution()
    print sol.diffWaysToCompute(input)
    print sol.diffWaysToCompute2(input)
