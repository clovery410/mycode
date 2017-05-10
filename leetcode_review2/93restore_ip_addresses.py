class Solution(object):
    def restoreIpAddresses(self, s):
        def generate(idx, cur_sol, all_sols):
            if len(cur_sol) == 4:
                if idx == len(s):
                    all_sols.append('.'.join(cur_sol))
                return

            for d in xrange(1, 4):
                if idx + d > len(s):
                    break
                if d == 1 or (s[idx] != '0' and int(s[idx:idx+d]) <= 255):
                    cur_sol.append(s[idx:idx+d])
                    generate(idx + d, cur_sol, all_sols)
                    cur_sol.pop()

        if len(s) > 12: return []
        res = []
        generate(0, [], res)
        return res

if __name__ == "__main__":
    sol = Solution()
    s = "234516523"
    print sol.restoreIpAddresses(s)
            
