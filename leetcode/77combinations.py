class Solution(object):
    def combine(self, n, k):
        ans = []
        
        def _findNext(current_solution, count, current_val, all_solution):
            if current_val > n + 1:
                return
            elif count == k:
                all_solution.append(current_solution[:])
                return
            
            current_solution.append(current_val)
            _findNext(current_solution, count + 1, current_val + 1, all_solution)
            current_solution.pop()
            _findNext(current_solution, count, current_val + 1, all_solution)
            
        if k > n:
            return ans
        _findNext([], 0, 1, ans)
        return ans

    # Not quite understand this solution!!!
    def concise_recursive(self, n, k):
        if k == 1:
            print [[i+1] for i in xrange(n)]
            return [[i+1] for i in xrange(n)]

        if n > k:
            print [[n]]
            return [r + [n] for r in self.concise_recursive(n-1, k-1)] + self.concise_recursive(n-1, k)
        else:
#            print [[] + [n]]
            return [r + [n] for r in self.concise_recursive(n-1, k-1)]
        
if __name__ == '__main__':
    sol = Solution()
#    print sol.combine(4, 2)
    print sol.concise_recursive(6, 5)
