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
        def dfs(node, serial):
            print serial
            if node is None:
                serial.append('#')
                return
            serial.append(str(node.val))
            dfs(node.left, serial)
            dfs(node.right, serial)
        serial = []
        dfs(root, serial)
        return ''.join(serial)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def dfs(data, idx):
            if idx[0] >= len(data):
                return None
            if data[idx[0]] == '#':
                return None
            curr_val = data[idx[0]]
            curr_node = TreeNode(int(curr_val))
            idx[0] += 1
            curr_node.left = dfs(data, idx)
            idx[0] += 1
            curr_node.right = dfs(data, idx)
            return curr_node
        idx = [0]
        root = dfs(data, idx)
        return root


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    seria = Codec()
    print seria.serialize(node1)
