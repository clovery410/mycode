class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
class BinaryTree(object):

#    class TreeNode(object):
#        def __init__(self, key):
#            self.key = key
#            self.left = None
#            self.right = None
            
    def __init__(self, root):
        self.root = root

    def insert_left(self, val):
        if self.left is None:
            self.left = BinaryTree(val)
        else:
            sub_tree = BinaryTree(val)
            sub_tree.left = self.left
            self.left = sub_tree

    def insert_right(self, val):
        if self.right is None:
            self.right = BinaryTree(val)
        else:
            sub_tree = BinaryTree(val)
            sub_tree.right = self.right
            self.right = sub_tree


    def traverse_in_order(self):
        def _traverse_in_order(tNode):
            if tNode is not None:
                _traverse_in_order(tNode.left)
                print(tNode.key)
                _traverse_in_order(tNode.right)

        _traverse_in_order(self.root)

    def traverse_pre_order(self):
        def _traverse_pre_order(tNode):
            if tNode is not None:
                print(tNode.key)
                _traverse_pre_order(tNode.left)
                _traverse_pre_order(tNode.right)

        _traverse_pre_order(self.root)

    def traverse_post_order(self):
        def _traverse_post_order(tNode):
            if tNode is not None:
                _traverse_post_order(tNode.left)
                _traverse_post_order(tNode.right)
                print(tNode.key)

        _traverse_post_order(self.root)

    def in_order_search(self, val):
        def _in_order_search(tNode):
            if tNode is None:
                return None
            else:
                if tNode.key == val:
                    return tNode
                elif tNode.key > val:
                    return _in_order_search(tNode.left)
                else:
                    return _in_order_search(tNode.right)

        return _in_order_search(self.root)

    def in_order_insert(self, val):
        def _in_order_insert(tNode):
            if tNode is None:
                new_root = TreeNode(val)
                tNode = new_root
                return
            if val < tNode.key and tNode.left is None:
                left_child = TreeNode(val)
                tNode.left = left_child
                return
            if val > tNode.key and tNode.right is None:
                right_child = TreeNode(val)
                tNode.right = right_child
                return
            if val < tNode.key and tNode.left is not None:
                return _in_order_insert(tNode.left)
            if val > tNode.key and tNode.right is not None:
                return _in_order_insert(tNode.right)
            else:
                raise ValueError('Non valid input')

        _in_order_insert(self.root)
        
    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setNodeValue(self, val):
        self.root = val

    def getNodeValue(self):
        return self.root

    def print_tree(self, ):
        current = self.root
        if current is not None:
           self.print_tree(self.getLeftChild())
           print(current.getNodeValue())
           self.print_tree(self.getRightChild())

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
    node10 = TreeNode(10)

#    my_tree = BinaryTree(node5)
#    node5.left = node3
#    node5.right = node9
#    node3.left = node1
#    node3.right = node4
#    node9.left = node7
#    node9.right = node10
#    node7.right = node8

    my_tree = BinaryTree(node7)
    my_tree.in_order_insert(1)
    my_tree.in_order_insert(3)
    my_tree.in_order_insert(9)
    my_tree.in_order_insert(4)
    my_tree.in_order_insert(10)
    my_tree.in_order_insert(8)
    my_tree.in_order_insert(5)
    my_tree.traverse_in_order()
    print'\n'
    my_tree.traverse_pre_order()
    print '\n'
    my_tree.traverse_post_order()
    print '\n'
    my_tree.in_order_insert(6)
    result = my_tree.in_order_search(6)
    if result:
        print('%s\n' % result.key)
    else:
        print('Node not in the tree')
    my_tree.traverse_in_order()
