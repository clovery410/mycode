class Solution(object):
    def restoreIpAddresses(self, s):
        def helper(pre_str, idx, curr_solution, all_solutions):
            if idx >= len(s) and pre_str == '' and len(curr_solution) == 4:
                all_solutions.append('.'.join(curr_solution[:]))
                return
            elif idx >= len(s) or len(curr_solution) > 4:
                return
            else:
                curr_str = pre_str + s[idx]
                helper(curr_str, idx+1, curr_solution, all_solutions)
                if int(curr_str) <= 255 and (len(curr_str) == 1 or curr_str[0] != '0'):
                    curr_solution.append(curr_str)
                    helper('', idx+1, curr_solution, all_solutions)
                    curr_solution.pop()

        res = []
        if len(s) <= 12:
            helper('', 0, [], res)
        return res

    # Solution2, improve the string copy part, to avoid copying each time, just use index
    # After running, turns out that running time is similar......
    def restoreIpAddresses2(self, s):
        def helper(start, end, curr_solution, all_solutions):
            if end >= len(s) and start == end and len(curr_solution) == 4:
                all_solutions.append('.'.join(curr_solution[:]))
                return
            elif end >= len(s) or len(curr_solution) > 4:
                return
            else:
                curr_str = s[start:end+1]
                helper(start, end+1, curr_solution, all_solutions)
                if int(curr_str) <= 255 and not (end > start and s[start] == '0'):
                    curr_solution.append(curr_str)
                    helper(end+1, end+1, curr_solution, all_solutions)
                    curr_solution.pop()
        res = []
        if len(s) <= 12:
            helper(0, 0, [], res)
        return res
                

if __name__ == "__main__":
    s = "25525511135"
    s2 = "0100310"
    sol = Solution()
    print sol.restoreIpAddresses(s)
    print sol.restoreIpAddresses(s2)
    print sol.restoreIpAddresses2(s2)

