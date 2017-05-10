from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        res = []
        queue = deque([root]) if root else []
        while queue:
            length = len(queue)
            cur_level = []
            for x in xrange(length):
                cur = queue.popleft()
                cur_level.append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            res.append(cur_level)
        return res
