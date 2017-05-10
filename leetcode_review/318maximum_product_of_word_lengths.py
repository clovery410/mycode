class Solution(object):
    # solution1, TLE
    def maxProduct(self, words):
        res = 0
        for i, w1 in enumerate(words):
            for j in xrange(i+1, len(words)):
                w2 = words[j]
                if not set(w1) & set(w2):
                    res = max(res, len(w1) * len(w2))
        return res

    # solution2, bit manipulation
    def maxProduct2(self, words):
        res, combinations = 0, []
        for word in words:
            combination = 0
            for c in word:
                combination |= 1 << (ord(c) - ord('a'))
            combinations.append(combination)

        for i, w1 in enumerate(words):
            for j in xrange(i+1, len(words)):
                w2 = words[j]
                if combinations[i] & combinations[j] == 0:
                    res = max(res, len(w1) * len(w2))
        return res
            

if __name__ == "__main__":
    sol = Solution()
    words = ['abcw', 'baz', 'foo', 'bar', 'xtfn', 'abcdef']
    print sol.maxProduct(words)
            
