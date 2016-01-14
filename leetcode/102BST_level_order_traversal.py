class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        out = list()
        if root is None:
            return out

        s = []
        t = []
        level_node_s = []
        level_node_t = []
        s.append(root)
        while s or t:
            while s:
                top = s.pop()
                level_node_s.append(top.val)
                if top.left:
                    t.insert(0, top.left)
                if top.right:
                    t.insert(0, top.right)
            if level_node_s:
                out.append(level_node_s)
            while t:
                top = t.pop()
                level_node_t.append(top.val)
                if top.left:
                    s.insert(0, top.left)
                if top.right:
                    s.insert(0, top.right)
            if level_node_t:
                out.append(level_node_t)

        return out


if __name__ == '__main__':
    sol = Solution()
                
            
