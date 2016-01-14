class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        stack = []
        path = {}
        final_path = []

        if root is None:
            return final_path
        
        path[root] = str(root.val)
        stack.append(root)
        
        while stack:
            top = stack.pop()
            left_node = top.left
            right_node = top.right
            if left_node is None and right_node is None:
                final_path.append(path[top])
            if left_node:
                path[left_node] = path[top] + '->' + str(left_node.val)
                stack.append(left_node)
            if right_node:
                path[right_node] = path[top] + '->' + str(right_node.val)
                stack.append(right_node)

        return final_path
        

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5

    sol = Solution()
    print sol.binaryTreePaths(node1)
