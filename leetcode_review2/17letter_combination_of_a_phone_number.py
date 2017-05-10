class Solution(object):
    def letterCombinations(self, digits):
        def generate(idx):
            if idx >= len(digits):
                return ['']
            cur_digit = digits[idx]
            next_res = generate(idx+1)
            cur_res = []
            for c in phone[cur_digit]:
                for next_c in next_res:
                    cur_res.append(c + next_c)
            return cur_res

        if len(digits) == 0 or '0' in digits:
            return []
        phone = {'1': "", '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        return generate(0)

if __name__ == "__main__":
    sol = Solution()
    digits = "23"
    print sol.letterCombinations(digits)
