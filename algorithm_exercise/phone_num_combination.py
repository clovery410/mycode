class Solution(object):
    def combination(self, s):
        nums = list(s)
        dic = {'2': ['A', 'B', 'C'], '3': ['D', 'E', 'F'], '4': ['G', 'H', 'I'], '5': ['J', 'K', 'L'], '6': ['M', 'N', 'O'], '7': ['P', 'Q', 'R', 'S'], '8': ['T', 'U', 'V'], '9': ['W', 'X', 'Y', 'Z']}

        def helper(idx):
            if idx == 0:
                return dic[str(nums[0])]

            pre_solutions = helper(idx - 1)
            all_solutions = []
            for c in dic[str(nums[idx])]:
                for solution in pre_solutions:
                    all_solutions.append(solution + c)
            return all_solutions

        return helper(len(nums) - 1)


if __name__ == '__main__':
    sol = Solution()
    print sol.combination('234')
    
