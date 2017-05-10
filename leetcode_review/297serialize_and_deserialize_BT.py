class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if node is None:
                serial.append("#")
            else:
                serial.append(str(node.val))
                preorder(node.left)
                preorder(node.right)

        if root is None:
            return ''
        serial = []
        preorder(root)
        return ','.join(serial)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        
        serial = data.split(',')
        root = TreeNode(int(serial[0]))
        
        stack = [(root, 0)]
        for i in xrange(1, len(serial)):
            c = serial[i]
            if c == '#':
                top_node, top_status = stack.pop()
                if top_status == 0:
                    stack.append((top_node, 1))
                else:
                    while stack:
                        temp_node, temp_status = stack.pop()
                        if temp_status == 0:
                            stack.append((temp_node, 1))
                            break
            else:
                new_node = TreeNode(int(c))
                top_node, top_status = stack[-1]
                if top_status == 0:
                    top_node.left = new_node
                else:
                    top_node.right = new_node
                stack.append((new_node, 0))
        return root
        
