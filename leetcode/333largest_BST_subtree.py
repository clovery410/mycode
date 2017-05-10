class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # Bottom-up solution for the Binary Search Tree Problem, O(n) running time
    def largestBSTSubtree(self, root):
        def checkBST(node):
            left_min, left_max, left_count =  checkBST(node.left) if node.left else [node.val, None, 0]
            right_min, right_max, right_count = checkBST(node.right) if node.right else [None, node.val, 0]

            # print node.val, left_min, left_max, left_count, right_min, right_max, right_count
            if left_max and (left_count == 0 or left_max >= node.val):
                return [left_min, right_max, 0]
            
            elif right_min and (right_count == 0 or right_min <= node.val):
                return [left_min, right_max, 0]

            else:
                nodes_count = left_count + right_count + 1
                self.max_count = max(self.max_count, nodes_count)
                return [left_min, right_max, nodes_count]
                
        self.max_count = 0
        if root:
            checkBST(root)
        return self.max_count

    # Top-down solution for the Binary Search Tree Problem, for this prolem , worst case is O(n^2)
    def largestBSTSubtree2(self, root):
        def checkBST(node, min_val, max_val):
            if node is None:
                return 0
            if min_val != None and node.val <= min_val:
                return -1
            if max_val != None and node.val >= max_val:
                return -1
            left_count = checkBST(node.left, min_val, node.val)
            right_count = checkBST(node.right, node.val, max_val)
            return left_count + right_count + 1 if left_count >= 0 and right_count >= 0 else -1

        res = checkBST(root)
        if res >= 0:
            return res
        else :
            return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))
