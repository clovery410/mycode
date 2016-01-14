class Solution(object):
    def combinationSum3(self, k, n):
        ans = []
        
        def _findNext(current_solution, current_val, count, total, all_solution):
            if count == k and total == n:
                all_solution.append(current_solution[:])
                return
            elif count > k or total > n or current_val > 9:
                return
            
            current_solution.append(current_val)
            _findNext(current_solution, current_val + 1, count + 1, total + current_val, all_solution)
            current_solution.pop()
            _findNext(current_solution, current_val + 1, count, total, all_solution)

        if pow(9, k) < n or k > n:
            return ans
        
        _findNext([], 1, 0, 0, ans)
        return ans

if __name__ == '__main__':
    sol = Solution()
    print sol.combinationSum3(3, 20)
