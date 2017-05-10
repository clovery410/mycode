class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #Solution1, recursion with extra O(n) space
    def flatten(self, root):
        def dfs(node):
            if node is None:
                return
            node_list.append(node)
            dfs(node.left)
            dfs(node.right)
        node_list = []
        dfs(root)
        for i in xrange(1, len(node_list)):
            node_list[i-1].left = None
            node_list[i-1].right = node_list[i]

    #Solution2, Morris Algorithm
    def flatten(self, root):
        cur_node = root
        while cur_node:
            if cur_node.left:
                pre = cur_node.left
                while pre.right:
                    pre = pre.right
                pre.right = cur_node.right
                cur_node.right = cur_node.left
                cur_node.left = None
            cur_node = cur_node.right
