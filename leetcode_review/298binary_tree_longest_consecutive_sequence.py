class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #solution1
    def longestConsecutive(self, root):
        def dfs(node):
            cur_consec = cur_global = 1
            if node.left:
                left_consec, left_global = dfs(node.left)
                if node.left.val == node.val + 1:
                    cur_consec = max(cur_consec, left_consec + 1)
                cur_global = max(cur_consec, left_global) 
            if node.right:
                right_consec, right_global = dfs(node.right)
                if node.right.val == node.val + 1:
                    cur_consec = max(cur_consec, right_consec + 1)
                cur_global = max(cur_global, cur_consec, right_global)
            return (cur_consec, cur_global)

        if root:
            return dfs(root)[1]
        return 0

    #solution2
    def longestConsecutive2(self, root):
        def dfs(node, last_num, count, longest):
            if node is None:
                return max(count, longest)
            
            if node.val == last_num + 1:
                count += 1
                longest = max(count, longest)
            else:
                count = 0
                
            left_max = dfs(node.left, node.val, count, longest)
            right_max = dfs(node.right, node.val, count, longest)
            return max(left_max, right_max)

        if root is None:
            return 0
        left_ret = dfs(root.left, root.val, 0, 0)
        right_ret = dfs(root.right, root.val, 0, 0)
        return max(left_ret, right_ret) + 1
        
            
