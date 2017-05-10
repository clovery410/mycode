class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenthese = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if len(stack) > 0 and c in parenthese and parenthese[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return True if len(stack) == 0 else False
