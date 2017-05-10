class Solution(object):
    def longestPalindrome(self, s):
        counter = collections.defaultdict(int)
        for c in s:
            counter[c] += 1

        max_len = 0
        odd = False
        for cnt in counter.values():
            if cnt % 2 == 0:
                max_len += cnt
            else:
                max_len += cnt - 1
                odd = True
        return max_len + 1 if odd else max_len
        
