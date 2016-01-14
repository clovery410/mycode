class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        def _recursive(root):
            if root is not None:
                left_node = root.left
                right_node = root.right
                root.left = right_node
                root.right = left_node
                _recursive(root.left)
                _recursive(root.right)

        if root is None:
            return None
        _recursive(root)
        return root


# if __name__ == '__main__':
    
