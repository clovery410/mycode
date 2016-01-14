class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        n = len(candidates)
        
        def _findNext(current_solution, index, value, all_solution):
            if value == 0 and current_solution not in all_solution:
                all_solution.append(current_solution[:])
                return
            elif index >= n:
                return
            
            current_val = candidates[index]
            if current_val <= value:
                current_solution.append(current_val)
                _findNext(current_solution, index + 1, value - current_val, all_solution)
                current_solution.pop()
                _findNext(current_solution, index + 1, value, all_solution)
                
        _findNext([], 0, target, ans)
        return ans

if __name__ == '__main__':
    candi = [10,1,2,7,6,1,5]
    target = 8
    sol = Solution()
    print sol.combinationSum2(candi, target)
