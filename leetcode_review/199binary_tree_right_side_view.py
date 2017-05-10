from collections import deque
import time
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #Solution1, bfs, but slower than solution2 since this copys whole list at each iteration
    def rightSideView(self, root):
        if root is None:
            return []
        stack = [root]
        res = []
        while stack:
            next_check = []
            res.append(stack[-1].val)
            for node in stack:
                if node.left: next_check.append(node.left)
                if node.right: next_check.append(node.right)
            stack = next_check
        return res

    #Solution2, bfs
    def rightSideView2(self, root):
        if root is None:
            return []
        res = []
        queue = deque(["#", root])
        while queue:
            top = queue.popleft()
            if top == "#":
                if len(queue) == 0 or queue[0] == "#":
                    return res
                else:
                    res.append(queue[0].val)
                    queue.append("#")
            else:
                if top.right:
                    queue.append(top.right)
                if top.left:
                    queue.append(top.left)
        return res

    #Solution3, dfs
    def rightSideView3(self, root):
        def dfs(node, level):
            if node is None:
                return
            if level > len(res):
                res.append(node.val)
            dfs(node.right, level+1)
            dfs(node.left, level+1)
        res = []
        dfs(root, 1)
        return res

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node1.left = node2
    node1.right = node3
    node2.right = node5
    node3.right = node4
    node5.left = node6

    sol = Solution()
    time1 = time.time()
    print sol.rightSideView(node1)
    print "solution1 --- %s seconds ---" % (time.time() - time1)
    time2 = time.time()
    print sol.rightSideView2(node1)
    print "solution2 --- %s second ---" % (time.time() - time2)
    time3 = time.time()
    print sol.rightSideView3(node1)
    print "solution3 --- %s second ---" % (time.time() - time3)


                
            
