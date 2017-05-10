class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # Solution 1, recursive version
    def buildTree(self, inorder, postorder):
        if len(inorder) > 0:
            idx = inorder.index(postorder[-1])
            root = TreeNode(postorder[-1])
            postorder.pop()
            root.right = self.buildTree(inorder[idx+1:], postorder)
            root.left = self.buildTree(inorder[:idx], postorder)
            return root

    # Solution 2, iterative version
    def buildTree2(self, inorder, postorder):
        i, j = 0, 0
        stack = []
        curr_node = None
        while j < len(postorder):
            if len(stack) > 0 and stack[-1].val == postorder[j]:
                stack[-1].right = curr_node
                curr_node = stack.pop()
                j += 1
            else:
                stack.append(TreeNode(inorder[i]))
                stack[-1].left = curr_node
                curr_node = None
                i += 1
        return curr_node


if __name__ == "__main__":
    sol = Solution()
    inorder = [4, 2, 5, 1, 3, 6]
    postorder = [4, 5, 2, 6, 3, 1]
    print sol.buildTree2(inorder, postorder).left.right.val
