class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            if c != '0' or len(stack) > 0:
                stack.append(c)

        while k > 0 and stack:
            stack.pop()
            k -= 1
            
        return '0' if not stack else ''.join(stack)

if __name__ == "__main__":
    sol = Solution()
    num = "10200"
    k = 2
    print sol.removeKdigits(num, k)
                
