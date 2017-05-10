class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #Solution1
    def countNodes(self, root):
        self.count = 0
        def dfs(node):
            if node is None:
                return
            left_height = self.getHeight(node.left)
            right_height = self.getHeight(node.right)
            if left_height == right_height:
                self.count += pow(2, left_height)
                node = node.right
            else:
                self.count += pow(2, right_height)
                node = node.left
            dfs(node)
            
        dfs(root)
        return 0 if root is None else self.count
    
    def getHeight(self, root):
        if root is None:
            return 0
        return 1 + self.getHeight(root.left)

    #Solution2
    def countNodes2(self, root):
        if root is None:
            return 0
        height = self.getHeight(root)
        count = 1
        node = root
        while node:
            if self.getHeight(node.left) == self.getHeight(node.right):
                if node.right:
                    count = count * 2 + 1
                node = node.right
            else:
                count *= 2
                node = node.left
        return count
                    
        

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6

    sol = Solution()
    print sol.countNodes(node1)
