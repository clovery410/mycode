class Solution(object):
    # This solution records all the binary representation of the sequence
    def grayCode(self, n):
        row = pow(2, n)
        res = []
        ans = [[None for x in xrange(n)] for x in xrange(row)]
        def getNext(digit, revert, start, end, all_solution):
            if digit >= n:
                return

            mid = (start + end) / 2
            if not revert:
                for i in xrange(start, mid + 1):
                    all_solution[i][digit] = 0
                for i in xrange(mid + 1, end + 1):
                    all_solution[i][digit] = 1
                getNext(digit + 1, False, start, mid, all_solution)
                getNext(digit + 1, True, mid + 1, end, all_solution)
            else:
                for i in xrange(start, mid + 1):
                    all_solution[i][digit] = 1
                for i in xrange(mid + 1, end + 1):
                    all_solution[i][digit] = 0
                getNext(digit + 1, False, start, mid, all_solution)
                getNext(digit + 1, True, mid + 1, end, all_solution)

        getNext(0, False, 0, row - 1, ans)
        for item in ans:
            curr, weight = 0, 1
            for i in reversed(xrange(n)):
                curr += item[i] * weight
                weight *= 2
            res.append(curr)
        print ans
        print res

    # This solution is the simplified version of above one
    def grayCode2(self, n):
        row = pow(2, n)
        res = [0 for x in xrange(row)]
        def populate(digit, revert, start, end, all_solution):
            if digit < 0:
                return
            mid = (start + end) / 2
            if not revert:
                for i in xrange(mid + 1, end + 1):
                    all_solution[i] += pow(2, digit)
            else:
                for i in xrange(start, mid + 1):
                    all_solution[i] += pow(2, digit)
            populate(digit - 1, False, start, mid, all_solution)
            populate(digit - 1, True, mid + 1, end, all_solution)
        populate(n - 1, False, 0, row - 1, res)

        return res

    # ********Solution from Discuss, really clever algorithm and clear logic
    def concise_recursion(self, n):
        if n < 1:
            return [0]
        if n == 1:
            return [0, 1]
        res = self.concise_recursion(n - 1)
        x = pow(2, n - 1)
        for i in xrange(x - 1, -1, -1):
            res.append(res[i] + x)
        return res
    
if __name__ == '__main__':
    sol = Solution()
    sol.grayCode2(4)
    print sol.concise_recursion(4)
