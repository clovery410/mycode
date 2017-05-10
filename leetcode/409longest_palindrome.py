import collections
class Solution(object):
    def longestPalindrome(self, s):
        counts = collections.defaultdict(int)
        res = 0
        odd = False
        for c in s:
            counts[c] += 1

        for count in counts.values():
            if count % 2 == 0:
                res += count
            if count % 2 == 1:
                odd = True
                res += count - 1
                
        return res + 1 if odd else res

if __name__ == "__main__":
    sol = Solution()
    s = "abccccdd"
    print sol.longestPalindrome(s)
