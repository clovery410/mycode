class Solution(object):
    # #solution1, add last pair based on n-1 pairs permutation, then check dup
    def parens1(self, n):
        def helper(n, cache):
            if n == 0:
                return []
            if n == 1:
                return ['()']
            res = []
            prev = helper(n-1, cache)
            for p in prev:
                for i in xrange(len(p) + 1):
                    if i == len(p) or p[i] == '(':
                        cur = p[:i+1] + '()' + p[i+1:]
                        if cur not in cache:
                            res.append(cur)
                            cache.add(cur)
            return res
        return helper(n, set())
                            
    #solution2, build from scratch, only build valid
    def parens2(self, n):
        def helper(cur_solution, all_solutions, left):
            if len(cur_solution) == 2 * n:
                if left == 0 and cur_solution[-1] == ')':
                    all_solutions.append(cur_solution)
                return
            if left > 0:
                helper(cur_solution + ')', all_solutions, left - 1)
            helper(cur_solution + '(', all_solutions, left + 1)
        res = []
        helper('', res, 0)
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.parens(5)
    print sol.parens2(5)
