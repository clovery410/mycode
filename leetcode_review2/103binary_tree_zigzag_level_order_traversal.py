class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        res = []
        cur_level = [root] if root else []

        while cur_level:
            next_level = []
            cur_res = []
            for node in reversed(cur_level):
                cur_res.append(node.val)
                if len(res) % 2 == 0:
                    if node.left: next_level.append(node.left)
                    if node.right: next_level.append(node.right)
                else:
                    if node.right: next_level.append(node.right)
                    if node.left: next_level.append(node.left)
            res.append(cur_res)
            cur_level = next_level
        return res

                        
