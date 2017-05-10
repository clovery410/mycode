class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #Solution 1, most original version
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

    #Solution2, second try with dfs
    def levelOrder2(self, root):
        def dfs(node, level, res):
            if node is None:
                return
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            dfs(node.left, level + 1, res)
            dfs(node.right, level + 1, res)
        res = []
        dfs(root, 0, res)
        return res

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3

    sol = Solution()
    print sol.levelOrder2(node1)
            
