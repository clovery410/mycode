class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, total):
        def dfs(root, cur_sum):
            new_sum = cur_sum + root.val
            if root.left is None and root.right is None:
                return True if total == new_sum else False
            elif (root.left and dfs(root.left, new_sum)) or (root.right and dfs(root.right, new_sum)):
                return True
            else:
                return False

        if root is None:
            return False
        return dfs(root, 0)

if __name__ == "__main__":
    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(8)
    node4 = TreeNode(11)
    node5 = TreeNode(13)
    node6 = TreeNode(4)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node3.right = node6

    sol = Solution()
    print sol.hasPathSum(node1, 20)
