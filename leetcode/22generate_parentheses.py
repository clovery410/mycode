class Solution(object):
    def __init__(self):
        self.ans = []

    def dfs(self, n, pre, pos, curr):
        if curr and len(curr) == n * 2:
            self.ans.append(curr)
            return

        if pre == pos:
            self.dfs(n, pre+1, pos, curr + '(')
        else:
            if pre < n:
                self.dfs(n, pre+1, pos, curr + '(')
            if pos < n:
                self.dfs(n, pre, pos+1, curr + ')')

    def generateParenthesis(self, n):
        if n <= 0:
            return None
        self.dfs(n, 1, 0, '(')
        return self.ans

    # This version pass a list as parameter, running time beats above one since Python is pass by reference, while string is immutable, which works as copy a new string instead of modifying the original one. However, list is not immutable, as pass by reference, the call function will directly modify the original list.
    def more_efficient_version(self, n):
        def _getNext(current_solution, pre, pos, all_solution):
            if len(current_solution) == n * 2:
                all_solution.append(''.join(current_solution))
                return

            if pre < n:
                current_solution.append('(')
                _getNext(current_solution, pre+1, pos, all_solution)
                current_solution.pop()

            if pos < pre:
                current_solution.append(')')
                _getNext(current_solution, pre, pos+1, all_solution)
                current_solution.pop()
        res = []
        _getNext([], 0, 0, res)
        return res
    
if __name__ == '__main__':
    sol = Solution()
    print sol.generateParenthesis(4)
    print sol.more_efficient_version(4)
