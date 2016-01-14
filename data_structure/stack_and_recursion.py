class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeMulti(object):
    def __init__(self, x, n):
        
class Manipulate(object):
    def preorder_stack(self, root):
        if root is None:
            return
        stack, ans = [], []
        start = root
        stack.append(start)

        while stack:
            top = stack.pop()
            ans.append(top.val)
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)

        return ans

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

    s = Manipulate()
    print s.preorder_stack(node1)
