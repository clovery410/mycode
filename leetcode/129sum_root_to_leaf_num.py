class TreeNode(object):
    def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None

class Solution(object):
    def __init__(self):
        self.ans = 0

    def dfs(self, node, total):
        if node is None:
            return
        
        total += node.val
        if node.left is None and node.right is None:
            self.ans += total
        if node.left:
            self.dfs(node.left, total * 10)
        if node.right:
            self.dfs(node.right, total * 10)
            
    def sumNumbers(self, root):
        self.dfs(root, 0)
        return self.ans

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    
    sol = Solution()
    print sol.sumNumbers(node1)
