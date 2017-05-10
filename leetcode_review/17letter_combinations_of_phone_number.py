class Solution(object):
    def letterCombinations(self, digits):
        phone = {'1': [''], '2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'],
                 '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r','s'],
                 '8': ['t','u','v'], '9': ['w','x','y','z']}
        def helper(digits):
            if digits == '':
                return [[]]
            res = []
            for c in phone[digits[0]]:
                res += [[c] + x for x in helper(digits[1:])]
            return res
        
        if len(digits) == 0 or '0' in digits: return []
        ans = helper(digits)
        return [''.join(x for x in elem) for elem in ans]

        # for i, elem in enumerate(ans):
        #     ans[i] = ''.join(elem)
        # return ans

    #solution2, classic backtracing solution
    def letterCombinations2(self, digits):
        def helper(idx, cur_sol, all_sols):
            if idx >= len(digits):
                all_sols.append(cur_sol)
                return
            for c in phone[digits[idx]]:
                helper(idx+1, cur_sol + c, all_sols)
                
        phone = {'1': [''], '2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'],
                 '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r','s'],
                 '8': ['t','u','v'], '9': ['w','x','y','z']}
        res = []
        helper(0, '', res)
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.letterCombinations('123')
    print sol.letterCombinations2('123')
