class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #Solution1, recursive solution using index
    def buildTree(self, preorder, inorder):
        def helperBuild(s1, e1, s2, e2):
            if e1 < s1:
                return None
            cur_root = TreeNode(preorder[s1])
            idx = inorder.index(preorder[s1])
            cur_root.left = helperBuild(s1+1, idx-s2+s1, s2, idx-1)
            cur_root.right = helperBuild(idx-s2+s1+1, e1, idx+1, e2)
            return cur_root
            
        return helperBuild(0, len(preorder) - 1, 0, len(inorder) - 1)

    #Solution2, try it iteratively using stack
    def buildTree2(self, preorder, inorder):
        i = j = len(preorder) - 1 
        stack = []
        pre_node = None
        while i >= 0:
            if len(stack) > 0 and stack[-1].val == preorder[i]:
                stack[-1].left = pre_node
                pre_node = stack.pop()
                i -= 1
            else:
                stack.append(TreeNode(inorder[j]))
                stack[-1].right = pre_node
                pre_node = None
                j -= 1
        return pre_node

    #Solution3, second try of iterative stack
    def buildTree3(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        i, j = 1, 0
        stack = [root]
        while i < len(preorder) and j < len(inorder):
            top = None
            while len(stack) > 0 and stack[-1].val == inorder[j]:
                top = stack.pop()
                j += 1
            new_node = TreeNode(preorder[i])
            if top is None:
                stack[-1].left = new_node
            else:
                top.right = new_node
            stack.append(new_node)
            i += 1
        return root

if __name__ == "__main__":
    preorder = [1,2,4,5,3,6]
    inorder = [4,2,5,1,6,3]
    sol = Solution()
    print sol.buildTree3(preorder, inorder).left.right.val
                    
                    
        
                
                    
                
            

