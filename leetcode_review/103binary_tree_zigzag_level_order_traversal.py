import time
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        queue = deque([root])
        res = []
        level = 1
        while queue:
            cur_level = []
            length = len(queue)
            for i in xrange(length):
                top = queue.popleft()
                cur_level.append(top.val)
                if top.left: queue.append(top.left)
                if top.right: queue.append(top.right)
            if level % 2 == 1:
                res.append(cur_level)
            else:
                res.append(cur_level[::-1])
            level += 1
        return res

    #Solution2, use list comprehansion
    def zigzagLevelOrder2(self, root):
        if root is None:
            return []
        queue = [[root]]
        for level in queue:
            level_nodes = []
            for node in level:
                if node.left: level_nodes.append(node.left)
                if node.right: level_nodes.append(node.right)
            if level_nodes:
                queue.append(level_nodes)
        for i, level in enumerate(queue):
            if i % 2 == 1:
                level.reverse()
        return [[node.val for node in level] for level in queue]

if __name__ == "__main__":
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    sol = Solution()
    time1 = time.time()
    print sol.zigzagLevelOrder(node1)
    print "solution1 --- %s second ---" % (time.time() - time1)
    time2 = time.time()
    print sol.zigzagLevelOrder2(node1)
    print "solution2 --- %s second ---" % (time.time() - time2)
