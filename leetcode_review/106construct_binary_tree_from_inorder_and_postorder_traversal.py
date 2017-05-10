class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #Solution1, do it recursively using index
    def buildTree(self, inorder, postorder):
        def helper(s1, e1, s2, e2):
            if e2 < s2:
                return None
            root_val = postorder[e2]
            idx = inorder.index(root_val)
            cur_root = TreeNode(root_val)
            cur_root.left = helper(s1, idx-1, s2, e2-e1+idx-1)
            cur_root.right = helper(idx+1, e1, e2-e1+idx, e2-1)
            return cur_root
        return helper(0, len(inorder) - 1, 0, len(postorder) - 1) if len(inorder) > 0 else None

    #Solution2, use stack to do it iteratively
    def buildTree2(self, inorder, postorder):
        i, j= 0, 0
        stack = []
        pre_node = None
        while j < len(postorder):
            if len(stack) > 0 and stack[-1].val == postorder[j]:
                stack[-1].right = pre_node
                pre_node = stack.pop()
                j += 1
            else:
                stack.append(TreeNode(inorder[i]))
                stack[-1].left = pre_node
                pre_node = None
                i += 1
        return pre_node
    
if __name__ == "__main__":
    sol = Solution()
    inorder = [4,2,5,1,6,3]
    postorder = [4,5,2,6,3,1]
    print sol.buildTree(inorder, postorder).right.left.val
    print sol.buildTree2(inorder, postorder).right.left.val
