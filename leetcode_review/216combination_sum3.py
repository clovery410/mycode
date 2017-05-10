class Solution(object):
    def combinationSum(self, k, n):
        def helper(cur_val, remain, cur_solution, all_solutions):
            if remain == 0:
                if len(cur_solution) == k:
                    all_solutions.append(cur_solution[:])
                return
            if cur_val > 9 or len(cur_solution) > k:
                return
            if cur_val <= remain:
                cur_solution.append(cur_val)
                helper(cur_val + 1, remain - cur_val, cur_solution, all_solutions)
                cur_solution.pop()
                helper(cur_val + 1, remain, cur_solution, all_solutions)

        res = []
        helper(1, n, [], res)
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.combinationSum(0, 9)

                    
