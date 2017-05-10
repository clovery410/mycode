class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        def dfs(cur_num, root):
            if root.left is None and root.right is None:
                self.total += cur_num * 10 + root.val
                return
            new_num = cur_num * 10 + root.val
            if root.left:
                dfs(new_num, root.left)
            if root.right:
                dfs(new_num, root.right)
        if root is None:
            return 0
        self.total = 0
        dfs(0, root)
        return self.total

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.right = node4
    node3.left = node5

    sol = Solution()
    print sol.sumRootToLeaf(node1)
