class Solution(object):
    #Solution with backtracing, remember to pop the last added item
    def combinationSum(self, candidates, target):
        ans = []
        candidates.sort()
        n = len(candidates)
        
        def _findSolution(current_solution, index, value, all_solution):
            if value == 0:
                all_solution.append(current_solution[:])    #Here use[:] since variable itself is only a reference
                return
            elif index >= n:
                return
            
            current_val = candidates[index]
            if current_val <= value:
                current_solution.append(current_val)
                _findSolution(current_solution, index, value - current_val, all_solution)
                current_solution.pop()
                _findSolution(current_solution, index+1, value, all_solution)
                
        _findSolution([], 0, target, ans)
        return ans

if __name__ == '__main__':
    candi = [2,3,6,7]
    target = 7
    sol = Solution()
    print sol.combinationSum(candi, target)
