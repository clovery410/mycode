import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMin(self, root):
        def dfs(node):
            if node.left is None and node.right is None:
                return node.val if node.val != root.val else sys.maxint
            if node.val != root.val:
                return node.val

            cur_min = sys.maxint
            if node.left:
                cur_min = min(cur_min, dfs(node.left))
            if node.right:
                cur_min = min(cur_min, dfs(node.right))
            return cur_min

        if not root:
            return None
        res = dfs(root)
        return res if res != sys.maxint else None

if __name__ == "__main__":
    node1 = TreeNode(2)
    node2 = TreeNode(2)
    node3 = TreeNode(7)
    node4 = TreeNode(5)
    node5 = TreeNode(2)
    node6 = TreeNode(8)
    node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    
    sol = Solution()
    print sol.findSecondMin(node1)
                              
            
