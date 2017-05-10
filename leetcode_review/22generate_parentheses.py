class Solution(object):
    def generateParenthesis(self, n):
        def helper(n):
            if n == 0:
                return ['']
            prev = helper(n-1)
            res = set()
            for p in prev:
                for i in xrange(len(p)):
                    if p[i] == '(':
                        res.add(p[:i+1] + '()' + p[i+1:])
                res.add(p + '()')
            return res
        return list(helper(n))

if __name__ == "__main__":
    sol = Solution()
    print sol.generateParenthesis(4)
