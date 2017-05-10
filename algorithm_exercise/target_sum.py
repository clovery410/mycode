#Question: 123456789 = 100
#Adding '+' or '-' at certain places to make the equation valid

class Solution(object):
    def targetSum(self):
        def helper(idx, pre_num, sign, total, cur_solution, all_solutions):
            # exit
            if idx == 10:
                if pre_num > 0 and total + pre_num * sign == 100:
                    cur_solution.append(str(pre_num))
                    all_solutions.append(''.join(cur_solution))
                    cur_solution.pop()
                return

            pre_num = pre_num * 10 + idx
            # not adding sign
            helper(idx+1, pre_num, sign, total, cur_solution, all_solutions)

            # add '+'
            cur_solution.append(str(pre_num))
            cur_solution.append('+')
            helper(idx+1, 0, 1, total + pre_num * sign, cur_solution, all_solutions)
            cur_solution.pop()
            
            # add '-'
            cur_solution.append('-')
            helper(idx+1, 0, -1, total + pre_num * sign, cur_solution, all_solutions)
            cur_solution.pop()
            cur_solution.pop()

        res1, res2 = [], []
        helper(1, 0, 1, 0, [], res1)
        helper(1, 0, -1, 0, [], res2)
        return res1 + res2

if __name__ == "__main__":
    sol = Solution()
    print sol.targetSum()
                
