class Solution(object):
    def removeKdigits(self, num, k):
        if len(num) == k:
            return '0'
        stack = []
        for char in num:
            while k > 0 and len(stack) > 0 and stack[-1] > char:
                stack.pop()
                k -= 1
            stack.append(char)
            
        for _ in xrange(k):
            stack.pop()
            
        res = ''.join(stack).lstrip('0')
        return res if len(res) > 0 else '0'

if __name__ == "__main__":
    sol = Solution()
    print sol.removeKdigits('1234567890', 9)
