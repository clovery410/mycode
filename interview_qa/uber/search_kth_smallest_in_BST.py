class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.count = 1
        self.left = None
        self.right = None

class Solution(object):
    def findKthElement(self, root, k):
        self.updateCount(root)
        cur_node = root
        while cur_node:
            left_count = cur_node.left.count if cur_node.left else 0
            if left_count + 1 == k:
                return cur_node.val
            if left_count >= k:
                cur_node = cur_node.left
            else:
                k = k - left_count - 1
                cur_node = cur_node.right

    def updateCount(self, root):
        def dfs(node):
            if node is None:
                return 0
            total_count = dfs(node.left) + dfs(node.right) + 1
            node.count = total_count
            return total_count

        dfs(root)

if __name__ == "__main__":
    node1 = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(8)
    node4 = TreeNode(1)
    node5 = TreeNode(4)
    node6 = TreeNode(6)
    node7 = TreeNode(9)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    sol = Solution()
    print sol.findKthElement(node1, 7)
