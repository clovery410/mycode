class Solution(object):
    def titleToNumber(self, s):
        weight = 1
        res = 0

        for c in reversed(s):
            res += (ord(c) - ord('A') + 1) * weight
            weight *= 26

        return res

if __name__ == "__main__":
    sol = Solution()
    print sol.titleToNumber("AJHX")
