class Solution(object):
    def decodeString(self, s):
        stack = []
        count = ''
        for c in s:
            if c.isdigit():
                count += c
            elif c == '[':
                stack.append(count)
                count = ''
            elif c == ']':
                sub_s = ''
                while stack and stack[-1].isalpha():
                    sub_s = stack.pop() + sub_s
                stack.append(int(stack.pop()) * sub_s)
            else:
                stack.append(c)
        return ''.join(stack)

if __name__ == "__main__":
    sol = Solution()
    s = "3[a2[c]]"
    print sol.decodeString(s)
                    
            
