class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []
        else:
            ans = []
            queue = []
            queue.append(root)
            queue.append('right')
            while queue:
                first = queue.pop(0)
                if first == 'right' and pre_node == 'right':
                    break
                if first == 'right':
                    ans.append(pre_node)
                    queue.append('right')
                    pre_node = 'right'
                else:
                    pre_node = first.val
                    if first.left:
                        queue.append(first.left)
                    if first.right:
                        queue.append(first.right)

        return ans
    

class Solution2(object):
    def __init__(self):
        self.ans = []

    def dfs(self, node, depth):
        if node is None:
            return
        else:
            if len(self.ans) <= depth:
                self.ans.append(node.val)
            else:
                self.ans[depth] = node.val
                
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)

    def rightSideView(self, root):
        self.dfs(root, 0)
        return self.ans

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3
    node2.right = node5
    node3.right = node4

    s = Solution2()
    print s.rightSideView(node1)
