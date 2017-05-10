import collections
class Solution(object):
    #solution1, backtracing, TLE
    def wordBreak(self, s, wordDict):
        def helper(idx, word, cur_solution, all_solutions):
            if idx >= len(s):
                if word in wordDict:
                    cur_solution.append(word)
                    all_solutions.append(' '.join(cur_solution))
                    cur_solution.pop()
                return
            if word in wordDict:
                cur_solution.append(word)
                helper(idx + 1, s[idx], cur_solution, all_solutions)
                cur_solution.pop()
            helper(idx + 1, word + s[idx], cur_solution, all_solutions)

        res = []
        helper(0, '', [], res)
        return res

    #solution2, no memo, so also TLE
    def wordBreak2(self, s, wordDict):
        dp = [0] * len(s) + [1]
        res = collections.defaultdict(list)
        for i in reversed(xrange(len(s))):
            for word in wordDict:
                l = len(word)
                if s[i:i+l] == word and dp[i+l] == 1:
                    dp[i] = 1
                    if i+l not in res:
                        res[i].append(s[i:i+l])
                    else:
                        res[i].extend([s[i:i+l] + ' ' + p for p in res[i+l]])
        return res[0]

    #solution3, try dfs + memoization, but for big input cases, it fails, maybe should change memo array to dictionary
    def wordBreak3(self, s, wordDict):
        def helper(s):
            s_len = len(s)
            if memo[s_len]:
                return memo[s_len]

            res = []
            for word in wordDict:
                l = len(word)
                if s[-l:] == word:
                    prev = helper(s[:-l])
                    res += [c + [word] for c in prev]
            memo[s_len] = res
            return res
            
        memo = [None] * (len(s) + 1)
        memo[0] = [[]]
        ans = helper(s)
        return [' '.join(elem) for elem in ans]

    #solution4, correct DFS + memoization, changed array into dictionary
    def wordBreak4(self, s, wordDict):
        def helper(s):
            if s in memo:
                return memo[s]
            if s == '':
                return [[]]
            
            res = []
            for word in wordDict:
                l = len(word)
                if s[:l] == word:
                    pos = helper(s[l:])
                    res += [[word] + c for c in pos]
            memo[s] = res
            return res
        
        memo = {}
        ans = helper(s)
        return [' '.join(elem) for elem in ans]

if __name__ == "__main__":
    wordDict = {"cat", "cats", "and", "sand", "dog"}
    s = "catsanddog"
    sol = Solution()
    print sol.wordBreak3(s, wordDict)
    print sol.wordBreak4(s, wordDict)
