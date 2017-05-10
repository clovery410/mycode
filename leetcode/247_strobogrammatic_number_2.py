class Solution(object):
    #Solution by Maomao
    def findStrobogrammatic(self, n):
        if n == 2:
            return [ "11","69","88","96"]

        def _sol(n, all_count):
            if n == 1:
                return ['0', '1', '8']
            elif n == 2:
                return ["00", "11","69","88","96"]
            else:
                results = []

                smaller_results = _sol(n-2, all_count)
                for result in smaller_results:
                    results.append('1' + result + '1')
                    results.append('8' + result + '8')
                    results.append('6' + result + '9')
                    results.append('9' + result + '6')
                    if n != all_count:
                        results.append('0' + result + '0')

                return results

        return sorted(_sol(n, n))

    #Solution by me, (learn how to write recursion)
    def findStrobogrammatic2(self, n):
        if n == 2:
            return ['11', '69', '88', '96']
        
        def helper(n, total_count):
            if n == 1:
                return ['0', '1', '8']
            elif n == 2:
                return ['11','69','88','96', '00']
            pre_result = helper(n - 2, total_count)
            curr_result = []
            for result in pre_result:
                curr_result.append('1' + result + '1')
                curr_result.append('8' + result + '8')
                curr_result.append('6' + result + '9')
                curr_result.append('9' + result + '6')
                if n != total_count:
                    curr_result.append('0' + result + '0')
            return curr_result
        return sorted(helper(n, n))

    #Solution3, the first recursion + backtracing I tried, now finish it.
    def findStrobogrammatic3(self, n):
        def _construct(n, total_n, curr_solution, all_solutions):
            if n == 0:
                all_solutions.append(curr_solution[:])
            elif n == 1:
                l = len(curr_solution)
                for result in curr_solution:
                    all_solutions.append(result[:l/2] + '0' + reuslt[l/2:])
                    all_solutions.append(result[:l/2] + '1' + result[l/2:])
                    all_solutions.append(result[:l/2] + '8' + result[l/2:])

            else:
                for result in curr_solution:
                    l = len(result)
                    _construct(n-2, total_n, (result[:l/2] + '11' + reuslt[l/2:]), all_solutions)
                    _construct(n-2, total_n, (result[:l/2] + '88' + reuslt[l/2:]), all_solutions)
                    _construct(n-2, total_n, (result[:l/2] + '69' + reuslt[l/2:]), all_solutions)
                    _construct(n-2, total_n, (result[:l/2] + '96' + reuslt[l/2:]), all_solutions)
                    if n != total_n:
                        _construct(n-2, total_n, (result[:l/2] + '00' + reuslt[l/2:]), all_solutions)

        all_solutions = []
        _construct(n, n, [], all_solutions)
        print all_solutions
                    

sol = Solution()
# print sol.findStrobogrammatic(4)
# print sol.findStrobogrammatic2(4)
print sol.findStrobogrammatic3(1)

                
