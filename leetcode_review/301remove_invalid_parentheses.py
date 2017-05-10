import time
class Solution(object):
    max_count = 0
    max_total = 0
    #Solution1, use backtracing
    def removeInvalidParentheses(self, s):
        def helper(idx, cnt_lp, cur_solution, all_solutions):
            if idx == len(s):
                if cnt_lp == 0:
                    if len(cur_solution) == self.max_count:
                        all_solutions.add(cur_solution)
                    elif len(cur_solution) > self.max_count:
                        all_solutions.clear()
                        all_solutions.add(cur_solution)
                        self.max_count = len(cur_solution)
            else:
                cur_elem = s[idx]
                if cur_elem == "(":
                    helper(idx+1, cnt_lp + 1, cur_solution + "(", all_solutions)
                    helper(idx+1, cnt_lp, cur_solution, all_solutions)
                elif cur_elem == ")":
                    if cnt_lp > 0:
                        helper(idx+1, cnt_lp - 1, cur_solution + ")", all_solutions)
                    helper(idx+1, cnt_lp, cur_solution, all_solutions)
                else:
                    helper(idx+1, cnt_lp, cur_solution + cur_elem, all_solutions)

        res = set()
        helper(0, 0, "", res)
        return list(res)

    #Solution2,
    def removeInvalidParentheses2(self, s):
        def dfs(idx, cnt_lp, cur_solution, all_solutions):
            if idx >= len(s):
                if cnt_lp == 0 and len(cur_solution) >= self.max_total:
                    if len(cur_solution) > self.max_total:
                        all_solutions.clear()
                        self.max_total = len(cur_solution)
                    all_solutions.add("".join(cur_solution))
            else:
                cur_elem = s[idx]
                if cur_elem not in "()":
                    cur_solution.append(cur_elem)
                    dfs(idx+1, cnt_lp, cur_solution, all_solutions)
                    cur_solution.pop()
                else:
                    dfs(idx+1, cnt_lp, cur_solution, all_solutions)
                    cur_solution.append(cur_elem)
                    if cur_elem == "(":
                        dfs(idx+1, cnt_lp + 1, cur_solution, all_solutions)
                    elif cur_elem == ")" and cnt_lp > 0:
                        dfs(idx+1, cnt_lp - 1, cur_solution, all_solutions)
                    cur_solution.pop()
        res = set()
        dfs(0, 0, [], res)
        return list(res)

if __name__ == "__main__":
    p = "()())()"
    p2 = "(a)())()"
    sol = Solution()
    time1 = time.time()
    print sol.removeInvalidParentheses(p2)
    print "solution1 --- %s second ---" % (time.time() - time1)
    time2 = time.time()
    print sol.removeInvalidParentheses2(p2)
    print "solution2 --- %s second ---" % (time.time() - time2)
