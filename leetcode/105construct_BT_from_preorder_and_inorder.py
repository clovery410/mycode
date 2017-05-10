class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    # Iterative version
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        i, j = 1, 0
        while i < len(preorder) and j < len(inorder):
            curr_node = TreeNode(preorder[i])
            top = None
            while len(stack) > 0 and stack[-1].val == inorder[j]:
                top = stack.pop()
                j += 1
            if not top:
                stack[-1].left = curr_node
            else:
                top.right = curr_node
            stack.append(curr_node)
            i += 1

        return root

    # Recursive version
    def buildTree2(self, preorder, inorder):
        if len(inorder) > 0:
            idx = inorder.index(preorder[0])
            root = TreeNode(preorder[0])
            preorder.pop(0)
            root.left = self.buildTree2(preorder, inorder[:idx])
            root.right = self.buildTree2(preorder, inorder[idx+1:])
            return root
        
                
