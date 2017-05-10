class Permutation(object):
    #Solution 1
    def permutation(self, n):
        def _construct(n):
            if n == 1:
                return [[1,]]
            all_results = []
            pre_results = _construct(n-1)
            for result in pre_results:
                for j in xrange(len(result) + 1):
                    all_results.append(result[:j] + [n,] + result[j:])
            return all_results

        ret = _construct(n)
        return ret

    #Solution2
    def permutation2(self, n):
        def _construct(curr_solution, all_solutions, available_num):
            if len(available_num) <= 0:
                all_solutions.append(curr_solution[:])
            else:
                for num in available_num:
                    curr_solution.append(num)
                    available_num.remove(num)
                    _construct(curr_solution, all_solutions, available_num)
                    curr_solution.pop()
                    available_num.add(num)
        available = set(xrange(1, n+1))
        all_solutions = []
        _construct([], all_solutions, available)
        return all_solutions

sol = Permutation()
print sol.permutation(4)
print sol.permutation2(4)
