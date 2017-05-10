class Solution(object):
    def removeInvalidParentheses(self, s):
        def helper(idx, left_count, curr_solution, all_solutions, total, max_total):
            if idx >= len(s):
                if left_count == 0:
                    if total == max_total[0]:
                        all_solutions.add(curr_solution)
                    elif total > max_total[0]:
                        max_total[0] = total
                        all_solutions.clear()
                        all_solutions.add(curr_solution)
            elif s[idx] != '(' and s[idx] != ')':
                helper(idx + 1, left_count, curr_solution + s[idx], all_solutions, total, max_total)
            else:
                if s[idx] == '(':
                    helper(idx + 1, left_count + 1, curr_solution + '(', all_solutions, total + 1, max_total)
                elif s[idx] == ')' and left_count > 0:
                    helper(idx + 1, left_count - 1, curr_solution + ')', all_solutions, total + 1, max_total)
                helper(idx + 1, left_count, curr_solution, all_solutions, total, max_total)

        res = set()
        helper(0, 0, '', res, 0, [0])
        return list(res)

    def removeInvalid2(self, s):
        #from left to right
        count = 0
        left_res = right_res = ''
        for i in xrange(len(s)):
            if s[i] == '(':
                left_res += s[i]
                count += 1
            elif s[i] == ')':
                if count > 0:
                    count -= 1
                    left_res += s[i]
            else:
                left_res += s[i]
        if count > 0:
            left_res = ''
        #from right to left
        count = 0
        for i in reversed(xrange(len(s))):
            if s[i] == ')':
                right_res = s[i] + right_res
                count += 1
            elif s[i] == '(':
                if count > 0:
                    count -= 1
                    right_res = s[i] + right_res
            else:
                right_res = s[i] + right_res
        if count > 0:
            right_res = ''

        print left_res, right_res
        if left_res == '':
            return right_res
        elif right_res == '':
            return left_res
        else:
            if left_res != right_res:
                return [left_res, right_res]
            return left_res
                
                    
if __name__ == '__main__':
    sol = Solution()
    print sol.removeInvalidParentheses('(a)())()')
    print sol.removeInvalidParentheses('()())()')
    print sol.removeInvalidParentheses(')(')
    print sol.removeInvalidParentheses('()')
    print sol.removeInvalid2('(a)())()')
                    
