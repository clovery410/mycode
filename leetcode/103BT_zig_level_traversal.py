class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def treeLevelOrder(self, root):
        if root is None: return []
        queue = [[root]]
        for level in queue:
            level_nodes = []
            for node in level:
                if node.left: level_nodes.append(node.left)
                if node.right: level_nodes.append(node.right)
            if level_nodes:
                queue.append(level_nodes)
        return [[x.val for x in level_nodes] for level_nodes in queue]
        
    def zigzagLevelOrder(self, root):
        if root is None: return []
        queue = [[root]]
        for level in queue:
            level_nodes = []
            for node in level:
                if node.left: level_nodes.append(node.left)
                if node.right: level_nodes.append(node.right)
            if level_nodes:
                queue.append(level_nodes)
        for (i, level) in enumerate(queue):
            if i % 2 == 1:
                level.reverse()
        return [[x.val for x in level] for level in queue]

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3

    sol = Solution()
    print sol.zigzagLevelOrder(node1)
        
