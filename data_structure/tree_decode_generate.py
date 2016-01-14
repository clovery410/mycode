class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeManipulate(object):
    def tree_decode_recurse(self, root):
        def _decode(root):
            if root is None:
                array.append('null')
            else:
                array.append(root.val)
                _decode(root.left)
                _decode(root.right)

        array = list()
        _decode(root)
        return array

    def tree_generate_recursive(self, array):
        def _generate(array):
            if len(array) > 0:
                if array[0] == 'null':
                    return None
                else:
                    new_node = TreeNode(array[0])
                    array.pop(0)
                    new_node.left = _generate(array)
                    array.pop(0)
                    new_node.right = _generate(array)
                    return new_node

        if array[0] == 'null':
            return None
        else:
            root = TreeNode(array[0])
            array.pop(0)
            root.left = _generate(array)
            array.pop(0)
            root.right = _generate(array)
            return root

        
if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.left = node8
    node6.right = node9

    tree = TreeManipulate()
    array = tree.tree_decode_recurse(node1)
    cons_t = tree.tree_generate_recursive(array)
    re_decode = tree.tree_decode_recurse(cons_t)
    print re_decode
