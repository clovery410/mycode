class Solution(object):
    #backtracing solution
    def permutations(self, s):
        def helper(cur_solution, all_solutions, candidates):
            if len(candidates) == 0:
                all_solutions.append(cur_solution)
                return
            for i in xrange(len(candidates)):
                c = candidates[i]
                helper(cur_solution + c, all_solutions, candidates[:i] + candidates[i+1:])
        res = []
        helper('', res, s)
        return res

    #recursive solution, building from permutations of first n-1 characters, find the right position to insert
    def permutations2(self, s):
        if len(s) == 0:
            return ['']
        prev = self.permutations2(s[1:])
        res = []
        for elem in prev:
            for i in xrange(len(s)):
                cur = elem[:i] + s[0] + elem[i:]
                res.append(cur)
        return res

    #recursive solution, building from permutations of all n-1 character substrings, just append the remaining character into the end to form a n character substring
    def permutations3(self, s):
        if len(s) == 0:
            return ['']
        res = []
        for i in xrange(len(s)):
            prev = self.permutations3(s[:i] + s[i+1:])
            res.extend([c + s[i] for c in prev])
        return res

if __name__ == "__main__":
    sol = Solution()
    print len(sol.permutations3("abcde"))
