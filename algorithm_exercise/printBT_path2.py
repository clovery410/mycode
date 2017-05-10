# Review, try with three different solutions
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    # Top Down
    def printPath1(self, root):
        def helper(node):
            if node.left is None and node.right is None:
                return [[node.val],]
            else:
                paths = []
                if node.left:
                    paths.extend(helper(node.left))
                if node.right:
                    paths.extend(helper(node.right))
            return [[node.val,] + p for p in paths]

        return helper(root)

    #Bottom up, pass solution by making a copy
    def printPath2(self, root):
        def helper(node, curr_solution, all_solutions):
            if node.left is None and node.right is None:
                all_solutions.append(curr_solution + [node.val,])
            else:
                if node.left:
                    helper(node.left, curr_solution + [node.val,], all_solutions)
                if node.right:
                    helper(node.right, curr_solution + [node.val,], all_solutions)
        res = []
        helper(root, [], res)
        return res

    #Bottom up, direct pass, then pop out after finishing
    def printPath3(self, root):
        def helper(node, curr_solution, all_solutions):
            if node is None:
                return

            curr_solution.append(node.val)
            if node.left is None and node.right is None:
                all_solutions.append(curr_solution[:])
            else:
                helper(node.left, curr_solution, all_solutions)
                helper(node.right, curr_solution, all_solutions)
            curr_solution.pop()
        res = []
        helper(root, [], res)
        return res

if __name__ == '__main__':
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
    print sol.printPath1(node1)
    print sol.printPath2(node1)
    print sol.printPath3(node1)
