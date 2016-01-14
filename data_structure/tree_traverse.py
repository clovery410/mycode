class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Recursive(object):
    def pre_order(self, root):
        if root is not None:
            print root.val
            self.pre_order(root.left)
            self.pre_order(root.right)

    def in_order(self, root):
        if root is not None:
            self.in_order(root.left)
            print root.val
            self.in_order(root.right)

    def pos_order(self, root):
        if root is not None:
            self.pos_order(root.left)
            self.pos_order(root.right)
            print root.val


class Iterative(object):
    def pre_order(self, root):
        s = list()
        if root is not None:
            s.append(root)
            while len(s) != 0:
                top = s.pop()
                print top.val
                if top.right is not None:
                    s.append(top.right)
                if top.left is not None:
                    s.append(top.left)

    def pos_order(self, root):
        s = list()
        if root is not None:
            s.append(root)
            while len(s) != 0:
                top = s.pop()
                if type(top) != int:
                    s.append(top.val)
                    if top.right is not None:
                        s.append(top.right)
                    if top.left is not None:
                        s.append(top.left)
                else:
                    print top

    def in_order(self, root):
        s = list()
        if root is not None:
            s.append(root)
            while len(s) != 0:
                top = s.pop()
                if type(top) != int:
                    if top.right is not None:
                        s.append(top.right)
                    s.append(top.val)
                    if top.left is not None:
                        s.append(top.left)
                else:
                    print top
                        

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
    
    # t = Recursive()
    # t.pre_order(node1)
    # print '\n'
    # t.in_order(node1)
    # print '\n'
    # t.pos_order(node1)

    s = Iterative()
    s.in_order(node1)
