class Solution(object):
    def wordPatternMatch(self, pattern, _str):
        def generate(p_i, s_i, bj):
            print bj
            if p_i >= len(pattern) and s_i >= len(_str):
                return True
            if p_i >= len(pattern) or s_i >= len(_str):
                return False
            if pattern[p_i] in bj:
                word = bj[pattern[p_i]]
                l = len(word)
                if word == _str[s_i:s_i+l] and generate(p_i+1, s_i+l, bj):
                    return True
                else: return False
            else:
                for end in range(s_i, len(_str)):
                    if _str[s_i:end+1] not in matched:
                        matched.add(_str[s_i:end+1])
                        bj[pattern[p_i]] = _str[s_i:end+1]
                        if generate(p_i+1, end+1, bj):
                            return True
                        matched.remove(_str[s_i:end+1])
                        del bj[pattern[p_i]]
                return False
        matched = set()
        return generate(0, 0, dict())

if __name__ == "__main__":
    sol = Solution()
    pattern = "abab"
    s = "dogcatdogcat"
    print sol.wordPatternMatch(pattern, s)
