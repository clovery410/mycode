class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.first = None
        self.second = None
        self.prev = TreeNode(-sys.maxint-1)
        
    def recoverTree(self, root):
        def dfs(root):
            if root.left is None and root.right is None:
                return (root, root)

            left_min, left_max = dfs(root.left) if root.left else (root, root)
            right_min, right_max = dfs(root.right) if root.right else (root, root)
            if left_max.val > root.val > right_min.val:
                left_max.val, right_min.val = right_min.val, left_max.val
            elif root.val > left_max.val > right_min.val:
                left_max.val, root.val, right_min.val = right_min.val, left_max.val, root.val
            elif left_max.val > right_min.val > root.val:
                left_max.val, root.val, right_min.val = root.val, right_min.val, left_max.val
            elif left_max.val > root.val:
                left_max.val, root.val = root.val, left_max.val
            elif right_min.val < root.val:
                right_min.val, root.val = root.val, right_min.val

            min_node = left_min if left_min.val < left_max.val else left_max
            max_node = right_max if right_max.val > right_min.val else right_min
            return (min_node, max_node)

        height = self.getHeight(root)
        for i in xrange(height):
            dfs(root)

    def getHeight(self, root):
        if root is None:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    #Solution2, learned from discuss
    def recoverTree2(self, root):
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            if self.first is None and root.val < self.prev.val:
                self.first = self.prev
                self.second = root
            if self.first is not None and root.val < self.prev.val:
                self.second = root
            self.prev = root
            inorder(root.right)

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
if __name__ == "__main__":
    node1 = TreeNode(1)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)

    node5.left = node4
    node5.right = node8
    node4.left = node1
    node4.right = node6
    node8.left = node7
    node8.right = node9

    sol = Solution()
    sol.recoverTree(node5)
    print node5.val
    
                

        
