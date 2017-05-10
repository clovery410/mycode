class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #Solution1, use recursion, O(log n) extra space
    def recoverTree1(self, root):
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            if self.prev and self.prev.val >= node.val:
                if self.first is None:
                    self.first = self.prev
                self.second = node
            self.prev = node
            dfs(node.right)

        self.first = None
        self.second = None
        self.prev = None
        dfs(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    #Solution2, use Morris Traversal, O(1) extra space
    def recoverTree2(self, root):
        prev = None
        first = None
        second = None
        cur_node = root
        while cur_node:
            if cur_node.left:
                pre_node = cur_node.left
                while pre_node.right and pre_node.right != cur_node:
                    pre_node = pre_node.right
                if pre_node.right is None:
                    pre_node.right = cur_node
                    cur_node = cur_node.left
                else:
                    if prev and prev.val >= cur_node.val:
                        if first is None:
                            first = prev
                        second = cur_node
                    pre_node.right = None
                    prev = cur_node
                    cur_node = cur_node.right
            else:
                if prev and prev.val >= cur_node.val:
                    if first is None:
                        first = prev
                    second = cur_node
                prev = cur_node
                cur_node = cur_node.right
        first.val, second.val = second.val, first.val

if __name__ == "__main__":
    node1 = TreeNode(6)
    node2 = TreeNode(8)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node2.right = node4
    node3.left = node5

    sol = Solution()
    print node1.left.val
    sol.recoverTree2(node1)
    print node1.left.val
    
