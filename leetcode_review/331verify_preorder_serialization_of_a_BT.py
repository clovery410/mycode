class Solution(object):
    # solution1, O(n) extra space and O(n) running time
    def isValidSerialization(self, preorder):
        stack = []
        preorder_list = preorder.split(",")
        for c in preorder_list:
            if c == '#':
                while len(stack) > 1 and stack[-1] == '#' and stack[-2] != '#':
                    stack.pop()
                    stack.pop()
                stack.append('#')
            else:
                stack.append(c)
        return True if stack == ['#'] else False

    # solution2, more sophiscated one
    def isValidSerialization2(self, preorder):
        stack = []
        preorder_list = preorder.split(",")
        for i, c in enumerate(preorder_list):
            if c == '#':
                if not stack:
                    return False
                top_val, top_lable = stack.pop()
                if top_lable == 0:
                    stack.append((top_val, 1))
                else:
                    while stack and stack[-1][1] == 1:
                        stack.pop()
                    if stack:
                        stack.append((stack.pop()[0], 1))
                    elif i < len(preorder_list) - 1:
                        return False
            else:
                stack.append((c, 0))
        return False if stack else True

if __name__ == "__main__":
    sol = Solution()
    # preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    preorder = "#,#,#,#"
    print sol.isValidSerialization(preorder)
    print sol.isValidSerialization2(preorder)
        
        
