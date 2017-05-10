class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def printPath(self, root):
        def dfs(node):
            if node.left is None and node.right is None:
                # curr_path.append(node.val)
                return [[node.val],]
            else:
                paths = []
                if node.left:
                    paths.extend(dfs(node.left))
                if node.right:
                    paths.extend(dfs(node.right))
                return [p + [node.val, ] for p in paths]

        res = []
        return dfs(root)

if __name__ == '__main__':
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
    node3.right = node6

    sol = Solution()
    print sol.printPath(node1)
