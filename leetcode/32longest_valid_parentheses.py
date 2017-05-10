class Solution(object):
    #Solution1, recursive + memoization solution, but still TLE
    def longestValidParentheses(self, s):
        def helper(idx, pre, count):
            if pre == 0:
                self.max_count = max(self.max_count, count)
            if idx == len(s):
                return 
            if (idx, pre, count) not in memo:
                cur = s[idx]
                if cur == '(':
                    helper(idx+1, pre+1, count+1)
                elif pre > 0:
                    helper(idx+1, pre-1, count+1)
                helper(idx+1, 0, 0)
                memo.add((idx, pre, count))

        self.max_count = 0
        memo = set()
        helper(0, 0, 0)
        return self.max_count

    #Solution2, try to come up with a dp solution, recursive equation is:
    # if s[i] == '(': longest[i] = 0
    # if s[i] == ')':
    #     (1) if s[i-1] == '(': longest[i] = longest[i-2] + 2
    #     (2) if i - longest[i-1] - 1 > 0 && s[i-longest[i-1]-1] == '(': longest[i] = longest[i-1] + 2 + longest[i-longest[i-1]-2]    
    def longestValidParentheses2(self, s):
        longest = [0] * len(s)
        max_count = 0
        for i in xrange(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    longest[i] = longest[i-2] + 2 if i >= 2 else 2
                elif i - longest[i-1] - 1 >= 0 and s[i-longest[i-1]-1] == '(':
                    longest[i] = longest[i-1] + 2 + (longest[i-longest[i-1]-2] if i-longest[i-1]-2 >= 0 else 0)
                    # if i - longest[i-1] - 2 >= 0: longest[i] += longest[i-longest[i-1]-2]
                    max_count = max(max_count, longest[i])
        return max_count

    #Solution3, use stack, same idea as 84largest_rectangle_in_histogram, push index into stack
    def longestValidParentheses3(self, s):
        stack = []
        max_count = 0
        for i in xrange(len(s)):
            if  s[i] == ')' and len(stack) > 0 and s[stack[-1]] == '(':
                stack.pop()
                max_count = max(max_count, i - stack[-1] if len(stack) > 0 else i + 1)
            else:
                stack.append(i)
        return max_count
                
if __name__ == "__main__":
    sol = Solution()
    p1 = ")()())"
    p2 = "(())"
    p3 = "()(()"
    p4 = "()(())"
    print sol.longestValidParentheses2(p4)
    print sol.longestValidParentheses3(p4)
