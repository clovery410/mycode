class Solution(object):
    def restoreIpAddresses(self, s):
        def generate(idx, cur_s, cur_sol, all_sols):
            if idx >= len(s):
                if len(cur_sol) == 4 and cur_s == '':
                    all_sols.append('.'.join(cur_sol))
                return
            new_s = cur_s + s[idx]
            if 0 <= int(new_s) <= 255:
                cur_sol.append(new_s)
                generate(idx+1, '', cur_sol, all_sols)
                cur_sol.pop()
                if new_s[0] != '0':
                    generate(idx+1, new_s, cur_sol, all_sols)

        if len(s) < 4 or len(s) > 12: return []
        res = []
        generate(0, '', [], res)
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.restoreIpAddresses("255255110135")
