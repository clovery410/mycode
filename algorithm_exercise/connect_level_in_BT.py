class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.pre = None
        self.next = None

class Solution(object):
    def connect(self, root):
        def dfs(node, level, record):
            if node is None:
                return
            if len(record) <= level:
                record.append([node,])
            else:
                record[level].append(node)
            if node.left is not None:
                dfs(node.left, level+1, record)
            if node.right is not None:
                dfs(node.right, level+1, record)

        record = []
        dfs(root, 0, record)
        for item in record:
            i , j = 0, 1
            while j < len(item):
                item[i].next = item[j]
                item[j].pre = item[i]
                i += 1
                j += 1

        

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6

sol = Solution()
sol.connect(node1)
print node1.next
