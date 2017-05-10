class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def serialize(self, root):
        def preorder(node):
            if node is None:
                res.append("#")
            else:
                res.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        res = []
        preorder(root)
        return ','.join(res)

    # use recursive way
    def deserialize_recursive(self, s):
        def preorder():
            c = string[self.idx]
            if c == '#':
                cur_node = None
                self.idx += 1
            else:
                cur_node = TreeNode(int(c))
                self.idx += 1
                cur_node.left = preorder()
                cur_node.right = preorder()
            return cur_node

        self.idx = 0
        string = s.split(',')
        return preorder()

    # use iterative way
    def deserialize_iterative(self, s):
        string = s.split(',')
        if string[0] == '#':
            return None
        root = TreeNode(int(string[0]))
        stack = [(root, 0)]
        for i in xrange(1, len(string)):
            cur_val = string[i]
            if cur_val == '#':
                top_node, top_status = stack.pop()
                if top_status == 0:
                    stack.append((top_node, 1))
                else:
                    while stack and stack[-1][1] == 1:
                        stack.pop()
                    if stack:
                        top_node, top_status = stack.pop()
                        stack.append((top_node, 1))
            else:
                top_node, top_status = stack[-1]
                cur_node = TreeNode(int(cur_val))
                if top_status == 0:
                    top_node.left = cur_node
                else:
                    top_node.right = cur_node
                stack.append((cur_node, 0))
        return root
            
if __name__ == "__main__":
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
    print sol.serialize(node1)
    root1 = sol.deserialize_recursive("1,2,#,#,3,4,#,#,5,#,#")
    root2 = sol.deserialize_iterative("1,2,#,#,3,4,#,#,5,#,#")
    print root1.right.right.val
    print root2.right.right.val
