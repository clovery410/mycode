class Solution(object):
    def wordPattern(self, pattern, _str):
        words = _str.split(" ")
        patterns = list(pattern)
        d1, d2 = {}, {}

        if len(words) != len(patterns):
            return False
        
        for i in xrange(len(words)):
            if patterns[i] not in d1:
                d1[patterns[i]] = words[i]
            elif d1[patterns[i]] != words[i]:
                return False
            if words[i] not in d2:
                d2[words[i]] = patterns[i]
            elif d2[words[i]] != patterns[i]:
                return False
        return True

if __name__ == "__main__":
    pattern = "aabb"
    string = "dog dog cat cat"
    sol = Solution()
    print sol.wordPattern(pattern, string)
