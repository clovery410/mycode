class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):    
    def preorderTraversal(self, root):
        stack = list()
        out = list()
        if root is not None:
            stack.append(root)
            while len(stack) != 0 :
                top = stack.pop()
                out.append(top.val)
                if top.right is not None:
                    stack.append(top.right)
                if top.left is not None:
                    stack.append(top.left)

        return out

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.right = node2
    node2.left = node3

    sol = Solution()
    print sol.preorderTraversal(node1)