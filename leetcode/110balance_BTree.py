class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs_depth(self, node):
        if node is None:
            return 0
        left_depth = self.dfs(node.left)
        right_depth = self.dfs(node.right)
        if abs(left_depth - right_depth) > 1 or left_depth == -1 or right_depth == -1:
            return -1
        return max(left_depth, right_depth) + 1

    def isBalanced(self, root):
        if self.dfs_depth(root) == -1:
            return False
        return True


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node3.right = node6
    node4.left = node7
    

    node8.left = node9
    sol = Solution()
    print sol.isBalanced(node1)
