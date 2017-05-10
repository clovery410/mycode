class Solution(object):
    def integerReplacement(self, n):
        count = 0
        mask1 = 3
        while n != 1:
            if n & 1 == 0:
                n >>= 1
            elif n & mask1 == mask1 and n != 3:
                n += 1
            else:
                n -= 1
            count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    print sol.integerReplacement(100000000)
    print "{0:b}".format(100000000)
