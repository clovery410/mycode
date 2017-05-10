class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        def dfs(node):
            if node.left is None and node.right is None:
                return node, node
            new_root, new_parent = dfs(node.left)
            new_parent.left = node.right
            new_parent.right = node
            node.left = node.right = None
            return new_root, node

        if root is None:
            return None
        new_root, new_parent = dfs(root)
        return new_root

if __name__ == "__main__":
    sol = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    
    root = sol.upsideDownBinaryTree(node1)
    print root.val, root.right.val, root.right.right.val, root.right.right.right
