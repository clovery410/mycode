class Solution(object):
    # this solution will TLE
    def wordBreak(self, s, wordDict):
        def generate(idx, cur_sol, all_sols):
            if idx >= len(s):
                all_sols.append(' '.join(cur_sol))
                return
            for end in xrange(idx, len(s)):
                if s[idx:end+1] in wordDict:
                    cur_sol.append(s[idx:end+1])
                    generate(end+1, cur_sol, all_sols)
                    cur_sol.pop()
        res = []
        generate(0, [], res)
        return res

    # solution2, use backtracing + memo
    def wordBreak2(self, s, wordDict):
        def generate(s, memo):
            if s == '':
                return [[]]
            if s in memo:
                return memo[s]

            res = []
            for word in wordDict:
                length = len(word)
                cur_res = []
                if s[:length] == word:
                    for following_res in generate(s[length:], memo):
                        res.append([word] + following_res)
                    # pos = generate(s[length:], memo)
                    # res += [[word] + x for x in pos]
            memo[s] = res
            return res
        
        ret = generate(s, {})
        return [' '.join(x) for x in ret]

    # solution3, use dp + dfs
    def wordBreak3(self, s, wordDict):
        def construct(idx, cur_sol, all_sols):
            if idx == 0:
                all_sols.append(' '.join(reversed(cur_sol)))
                return
            for pre_idx in dp[idx]:
                cur_sol.append(s[pre_idx:idx])
                construct(pre_idx, cur_sol, all_sols)
                cur_sol.pop()
                
        maxLen = len(max(wordDict, key = len)) if wordDict else 0
        dp = [[] for x in xrange(len(s)+1)]
        dp[0] = [-1]
        for i in xrange(1, len(dp)):
            for j in xrange(max(0, i-maxLen), i):
                if not dp[j]:
                    continue
                word = s[j:i]
                if word in wordDict:
                    dp[i].append(j)
        ret = []
        construct(len(dp) - 1, [], ret)
        return ret

if __name__ == "__main__":
    sol = Solution()
    d = {"cat", "cats", "and", "sand", "dog"}
    print sol.wordBreak("catsanddog", d)
    print sol.wordBreak2("catsanddog", d)
    print sol.wordBreak3("catsanddog", d)
                
                
