class Solution(object):
    def addOperators(self, num, target):
        def helper(idx, curr_num, flag, curr_solution, all_solutions):
            if idx == n:
                curr_solution.append(curr_num)
                all_solutions.append(curr_solution[:])
                curr_solution.pop()
            else:
                if not curr_num or curr_num[-1] != '0':
                    helper(idx+1, curr_num + num[idx], True, curr_solution, all_solutions)
                if flag:
                    for op in '+-*':
                        curr_solution.append(curr_num)
                        curr_solution.append(op)
                        helper(idx, '', False, curr_solution, all_solutions)
                        curr_solution.pop()
                        curr_solution.pop()
        expressions, res = [], []
        n = len(num)
        if n > 0:
            helper(0, '', False, [], expressions)
        for expression in expressions:
            if self.calculate(expression) == target:
                res.append(expression)
        return [''.join(x) for x in res]

    def calculate(self, expression):
        stack = []
        for c in expression:
            if c == '+':
                continue
            elif c not in '-*':
                if stack and stack[-1] == '-':
                    stack.pop()
                    stack.append(0 - int(c))
                elif stack and stack[-1] == '*':
                    stack.pop()
                    pre = stack.pop()
                    stack.append(pre * int(c))
                else:
                    stack.append(int(c))
            else:
                stack.append(c)
        return sum(stack)

    #Solution2, divide and conquer, not finish....
    def addOperators2(self, num, target):
        ops = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y}
        def helper(num):
            if len(num) == 0:
                return ''
            for i in xrange(len(num)):
                left_res = helper(num[:i])
                right_res = helper(num[i:])
                for c in '+-*':
                    if ops[c](self.calculate(left_res), self.caculate(right_res)) == target:
                        res.append(left_res + c + right_res)
                    return left_res + c + right_res

    #Solution3
    def addOperators3(self, nums, target):
        def solve(target, pos, negate, prod):
            expr = []
            for i in xrange(pos, len(num)):
                if i > pos and num[pos] == "0":
                    break
                if i == len(num) - 1:
                    if negate * prod * int(num[pos:i+1]) == target:
                        expr.extend([num[pos:i+1]])
                    break

                add_expr = solve(target - prod * negate * long(num[pos:i+1]), i + 1, 1, 1)
                expr.extend([num[pos:i+1] + "+" + e for e in add_expr])

                sub_expr = solve(target - prod * negate * long(num[pos:i+1]), i + 1, -1, 1)
                expr.extend([num[pos:i+1] + "-" + e for e in sub_expr])

                mul_expr = solve(target, i + 1, 1, prod * negate * long(num[pos:i+1]))
                expr.extend([num[pos:i+1] + "*" + e for e in mul_expr])

            return expr

        return solve(target, 0, 1, 1)

    #Solution4, easy to understand version, recommend
    def addOperators4(self, num, target):
        def helper(all_solutions, pos, path, total, prod):
            if pos == len(num):
                if total == target:
                    all_solutions.append(path)
                return
            for i in xrange(pos, len(num)):
                if i != pos and num[pos] == "0":
                    break
                cur = long(num[pos:i+1])
                if pos == 0:
                    helper(all_solutions, i + 1, num[pos:i+1], cur, cur)
                else:
                    helper(all_solutions, i + 1, path + "+" + str(cur), total + cur, cur)
                    helper(all_solutions, i + 1, path + "-" + str(cur), total - cur, -cur)
                    helper(all_solutions, i + 1, path + "*" + str(cur), total - prod + prod * cur, prod * cur)
        res = []
        helper(res, 0, "", 0, 1)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    num = "123"
    print sol.addOperators(num, 6)
    print sol.addOperators3(num, 6)
    print sol.addOperators4(num, 6)
