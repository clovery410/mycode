class Solution(object):
    def combine(self, n, k):
        def generate(num, cur_sol, all_sols):
            if len(cur_sol) == k:
                all_sols.append(list(cur_sol))
                return
            if len(cur_sol) + n - num + 1 < k:
                return
            if num <= n:
                cur_sol.append(num)
                generate(num+1, cur_sol, all_sols)
                cur_sol.pop()
                generate(num+1, cur_sol, all_sols)
        res = []
        generate(1, [], res)
        return res

    #solution2, use recursion and list comprehension
    def combine2(self, n, k):
        if k == 1:
            return [[x] for x in range(1, n+1)]
        if n > k:
            return [r + [n] for r in self.combine2(n-1, k-1)] + self.combine2(n-1, k)
        else:
            return [r + [n] for r in self.combine2(n-1, k-1)]

if __name__ == "__main__":
    sol = Solution()
    print sol.combine(20, 16)
    print sol.combine2(20, 16)
