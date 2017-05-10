class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        weight = 0
        while m != n:
            m >>= 1
            n >>= 1
            weight += 1
        return m << weight

if __name__ == "__main__":
    sol = Solution()
    print sol.rangeBitwiseAnd(5, 8)
