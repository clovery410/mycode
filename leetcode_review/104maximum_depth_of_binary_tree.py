class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        def dfs(node, height):
            if node is None:
                return height
            return max(dfs(node.left, height+1), dfs(node.right, height+1))
        return dfs(root, 0)

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    node1.left = node2
    node2.left = node3
    node3.left = node4

    sol = Solution()
    print sol.maxDepth(node1)
    
