class Solution(object):
    # solution1, dp solution
    def wordBreak(self, name, periodic_table):
        """
        input name is a string
        input periodic_table is a set of element names
        output should be a boolean
        """
        dp = [True] + [False] * len(name)
        for i in xrange(1, len(dp)):
            for word in periodic_table:
                l = len(word)
                if i - l >= 0 and dp[i-l] and name[i-l:i] == word:
                    dp[i] = True
                    break
        return dp[-1]

    # solution2, recursion + memo
    def wordBreak2(self, name, periodic_table):
        def recurse(s):
            if s in memo:
                return False
            if s in periodic_table:
                return True

            res = False
            for word in periodic_table:
                length = len(word)
                if s[:length+1] == word and recurse(s[length+1:]):
                    res = True
                    break
            memo[s] = res
            return res

        # pre check whether name has any characters that not in periodic_table
        characters = set()
        for word in periodic_table:
            for c in word:
                characters.add(c)
        for c in name:
            if c not in characters:
                return False
            
        memo = {}
        return recurse(name)

    # variation, if just need to return all the substring that can be matched by the dictionary, return a list of such substrings, should use trie, make a trie for the periodic table, then search each substring
    def wordBreak3(self, name, periodic_table):
        # build Trie
        trie = {}
        for word in periodic_table:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['_end_'] = '_end_'

        # do the search
        res = []
        for start in xrange(len(name)):
            t, j = trie, start
            while j < len(name) and name[j] in t:
                t = t[name[j]]
                if '_end_' in t:
                    res.append(name[start:j+1])
                j += 1
                
        return res

if __name__ == "__main__":
    sol = Solution()
    name = "BreakingBadKrillAnn"
    table = {"Ba", "Br", "Au", "Zn", "Ar", "Kr", "Kl", "Se", "Te", "Sb", "Sn"}
    print sol.wordBreak(name, table)
    print sol.wordBreak3(name, table)
