class Solution(object):
    def titleToNumber(self, s):
        result = i = 0
        for item in reversed(s):
            result += pow(26, i) * (ord(item) - 64)
            i += 1
        return result


if __name__ == '__main__':
    nums = 'AAA'
    sol = Solution()
    print sol.titleToNumber(nums)
