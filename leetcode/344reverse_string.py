class Solution(object):
    def reverseString(self, s):
        temp = list(s)
        start, end = 0, len(temp) - 1
        while start < end:
            temp[start], temp[end] = temp[end], temp[start]
            start += 1
            end -= 1
        return ''.join(temp)

    def reverseString2(self, s):
        temp = list(s)
        l = len(s)
        for i in xrange(l/2):
            temp[i], temp[l-1-i] = temp[l-1-i], temp[i]
        return ''.join(temp)

if __name__ == "__main__":
    sol = Solution()
    print sol.reverseString("hello")
    print sol.reverseString2("hello")
