class Solution(object):
    def generateParenthesis(self, n):
        def generate(left_count, right_count, cur_sol, all_sols):
            if left_count < 0 or right_count < 0:
                return
            if left_count == right_count == 0:
                all_sols.append(cur_sol)
                return

            generate(left_count-1, right_count, cur_sol + '(', all_sols)
            if left_count < right_count:
                generate(left_count, right_count-1, cur_sol + ')', all_sols)

        res = []
        generate(3, 3, '', res)
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.generateParenthesis(3)
