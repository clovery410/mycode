class Solution(object):
    def removeInvalidParentheses(self, s):
        def generate(idx, count, left_count, cur_sol, all_sols):
            if idx >= len(s):
                if left_count == 0:
                    if count == self.min_count:
                        all_sols.add(''.join(cur_sol))
                    elif count < self.min_count:
                        self.min_count = count
                        all_sols.clear()
                        all_sols.add(''.join(cur_sol))
                return

            c = s[idx]
            if c == '(':
                cur_sol.append(c)
                generate(idx + 1, count, left_count + 1, cur_sol, all_sols)
                cur_sol.pop()
                generate(idx + 1, count + 1, left_count, cur_sol, all_sols)
            elif c == ')':
                generate(idx + 1, count + 1, left_count, cur_sol, all_sols)
                if left_count > 0:
                    cur_sol.append(c)
                    generate(idx + 1, count, left_count - 1, cur_sol, all_sols)
                    cur_sol.pop()
            else:
                cur_sol.append(c)
                generate(idx + 1, count, left_count, cur_sol, all_sols)
                cur_sol.pop()

        res = set()
        self.min_count = len(s) + 1
        generate(0, 0, 0, [], res)
        return list(res)

if __name__ == "__main__":
    sol = Solution()
    s = "()())()"
    print sol.removeInvalidParentheses(s)
