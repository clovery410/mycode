class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findLeaves(self, root):
        def dfs(node):
            left_depth = dfs(node.left) if node.left else 0
            right_depth = dfs(node.right) if node.right else 0
            cur_depth = max(left_depth, right_depth)
            if len(res) > cur_depth:
                res[cur_depth].append(node.val)
            else:
                res.append([node.val])
            return cur_depth + 1

        res = []
        if root:
            dfs(root)
        return res

if __name__ == "__main__":
    sol = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    
    print sol.findLeaves(node1)
