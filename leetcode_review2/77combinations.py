class Solution(object):
    #solution1, TLE
    def combine(self, n, k):
        def generate(count, num, cur_sol, all_sols):
            if count == 0:
                all_sols.append(list(cur_sol))
                return
            
            for cur_num in xrange(num, n+1):
                cur_sol.append(cur_num)
                generate(count - 1, cur_num + 1, cur_sol, all_sols)
                cur_sol.pop()

        res = []
        generate(k, 1, [], res)
        return res

    #solution2, backtraing with return value + memoization
    def combine2(self, n, k):
        def generate(start, end, count):
            if count == 0:
                return [[]]
            if (start, end, count) in memo:
                return memo[(start, end, count)]
            
            res = []
            for num in xrange(start, end):
                res += [[num] + x for x in generate(num+1, end, count-1)]

            memo[(start, end, count)] = res
            return res

        memo = {}
        return generate(1, n+1, k)
            
if __name__ == "__main__":
    sol = Solution()
    # print sol.combine(20, 16)
    print sol.combine(20, 16)
