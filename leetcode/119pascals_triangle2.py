class Solution(object):
    #Solution1, recursive
    def getRow(self, rowIndex):
        def helper(idx, solution):
            if idx == 0:
                return solution
            new_solution = helper(idx-1, solution)
            new_solution.append(1)
            for i in reversed(xrange(1, len(new_solution) - 1)):
                new_solution[i] = new_solution[i] + new_solution[i-1]
            return new_solution
        return helper(rowIndex, [1]) if rowIndex >= 0 else []

    #Solution2, iterative
    def getRow2(self, rowIndex):
        res = [1]
        while rowIndex > 0:
            res.append(1)
            for i in reversed(xrange(1, len(res) - 1)):
                res[i] += res[i-1]
            rowIndex -= 1
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.getRow(8)
    print sol.getRow2(8)


            
