class Solution(object):
    def generateAbbreviations(self, word):
        def generate(idx, count, cur_sol, all_sols):
            if idx >= len(word):
                if count > 0:
                    cur_sol += str(count)
                all_sols.append(cur_sol)
                return
            cur_s = word[idx]
            generate(idx+1, count+1, cur_sol, all_sols)
            if count > 0:
                cur_sol += str(count)
            generate(idx+1, 0, cur_sol + cur_s, all_sols)

        res = []
        generate(0, 0, '', res)
        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.generateAbbreviations("word")
