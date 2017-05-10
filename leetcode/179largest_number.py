class Solution(object):
    def largestNumber(self, nums):
        def string_compare(x, y):
            s1 = x + y
            s2 = y + x
            for i in xrange(len(s1)):
                if s1[i] == s2[i]:
                    continue
                else:
                    return ord(s2[i]) - ord(s1[i])
            return 0

        nums_str = [str(x) for x in nums]
        nums_str.sort(cmp = string_compare)
        res = ''.join(nums_str)
        return res if len(res) > 0 else '0'
                
if __name__ == "__main__":
    sol = Solution()
    nums = [3, 30, 34, 301, 5, 9, 52]
    print sol.largestNumber2(nums)
