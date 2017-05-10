class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #Solution1, use O(n) extra space to do inorder traversal
    def validate(self, root):
        def dfs(node):
            if node.left:
                dfs(node.left)
            inorder.append(node.val)
            if node.right:
                dfs(node.right)

        inorder = []
        if root:
            dfs(root)
        for i in xrange(len(inorder) - 1):
            if inorder[i+1] <= inorder[i]:
                return False
        return True

    #Solution2, use O(log n) extra space to do it recursively
    def validate2(self, root):
        def dfs(node):
            if node.left is None and node.right is None:
                return (node.val, node.val)
            cur_lo = cur_hi = node.val
            if node.left:
                left_lo, left_hi = dfs(node.left)
                if left_hi >= node.val:
                    self.isValid = False
                cur_lo = left_lo
            if node.right:
                right_lo, right_hi = dfs(node.right)
                if right_lo <= node.val:
                    self.isValid = False
                cur_hi = right_hi
            return (cur_lo, cur_hi)

        self.isValid = True
        if root:
            dfs(root)
        return self.isValid

if __name__ == "__main__":
    node1 = TreeNode(6)
    node2 = TreeNode(4)
    node3 = TreeNode(8)
    node4 = TreeNode(5)
    node5 = TreeNode(9)

    node1.left = node2
    node1.right = node3
    node2.right = node4
    node3.left = node5

    sol = Solution()
    print sol.validate(node1)
    print sol.validate2(node1)
