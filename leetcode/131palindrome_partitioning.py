class Solution(object):
    #solution1, classic backtracing, no memoization
    def partition(self, s):
        def helper(idx, cur_subs, cur_solution, all_solutions):            
            if idx >= len(s):
                if cur_subs == '':
                    all_solutions.append(cur_solution[:])
                return

            cur_subs = cur_subs + s[idx]

            if cur_subs == cur_subs[::-1]:
                cur_solution.append(cur_subs)
                helper(idx+1, '', cur_solution, all_solutions)
                cur_solution.pop()

            helper(idx+1, cur_subs, cur_solution, all_solutions)

        res = []
        helper(0, '', [], res)
        return res

    #solution2, try to optimize solution1 by adding memo
    #1. cut s into two part (from backend to start), if backend is palindrome then solve the sub problem of prefix.
    #2. use a memo to avoid the repeated calling.
    def partition2(self, s):
        def helper(s):
            n = len(s)
            if memo[n]:
                return memo[n]
            res = []
            for i in range(n-1, -1, -1):
                cur = s[i:]
                if cur == cur[::-1]:
                    pre_res = helper(s[:i])
                    res += [r + [cur] for r in pre_res]
            memo[n] = res
            return res
        memo = [None] * (len(s) + 1)
        memo[0] = [[]]
        return helper(s)

if __name__ == "__main__":
    sol = Solution()
    print sol.partition("aab")
    print sol.partition2("aab")
