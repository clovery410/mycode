class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution(object):
    # solution1, use topological sort to do this
    def findLeaves(self, root):
        pre_nodes = collections.defaultdict(list)
        pos_nodes = collections.defaultdict(int)
        nodes = [root] if root else []
        sinks = collections.deque([])
        res = []
        while nodes:
            cur_node = nodes.pop()
            if not cur_node.left and not cur_node.right:
                sinks.append(cur_node)
            if cur_node.left:
                left_node = cur_node.left
                pre_nodes[left_node].append(cur_node)
                pos_nodes[cur_node] += 1
                nodes.append(left_node)
            if cur_node.right:
                right_node = cur_node.right
                pre_nodes[right_node].append(cur_node)
                pos_nodes[cur_node] += 1
                nodes.append(right_node)

        while sinks:
            length = len(sinks)
            cur_level = []
            for i in xrange(length):
                cur_leaf = sinks.popleft()
                cur_level.append(cur_leaf.val)
                for parent in pre_nodes[cur_leaf]:
                    pos_nodes[parent] -= 1
                    if pos_nodes[parent] == 0:
                        sinks.append(parent)
            res.append(cur_level)

        return res

    # solution2
    def findLeaves2(self, root):
        def dfs(node):
            if node is None:
                return -1
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            cur_depth = max(left_depth, right_depth) + 1
            if cur_depth >= len(level_nodes):
                level_nodes.append([node.val])
            else:
                level_nodes[cur_depth].append(node.val)
            return cur_depth
        
        level_nodes = []
        dfs(root)
        return level_nodes

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
    print sol.findLeaves(node1)
    print sol.findLeaves2(node1)
