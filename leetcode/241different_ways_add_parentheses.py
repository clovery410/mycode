class Solution(object):
    # Solution from the Leetcode forum
    def diffWaysToCompute(self, inputs):
        ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}
        def helper(s, cache):
            if s not in cache:
                res = []
                for i, c in enumerate(s):
                    if c in '+-*':
                        for pre in helper(s[:i], cache):
                            for pos in helper(s[i+1:], cache):
                                res.append(ops[c](pre, pos))
                if not res:
                    res.append(int(s))
                cache[s] = res
            return cache[s]
        return helper(inputs, {})

    # Learn it by intimating
    def diffWaysToCompute2(self, inputs):
        ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}
        def dp(inputs, cache):
            if inputs not in cache:
                if inputs.isdigit():
                    return [int(inputs)]
                res = []
                for i, c in enumerate(inputs):
                    if c in '+-*':
                        for left_op in dp(inputs[:i], cache):
                            for right_op in dp(inputs[i+1:], cache):
                                res.append(ops[c](left_op, right_op))
                cache[inputs] = res
            return cache[inputs]
        return dp(inputs, {})
                

if __name__ == '__main__':
    sol = Solution()
    inputs = "2*3-4*5"
    print sol.diffWaysToCompute(inputs)
    print sol.diffWaysToCompute2(inputs)
