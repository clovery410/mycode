# First version solution, inspired by the forum discussion
class Solution(object):
    def getHeight(self, node):
        h = 0
        while node:
            h += 1
            node = node.left
        return h
    
    def countNodes(self, root):
        if root is None:
            return 0
        count = 1
        curr_node = root
        while curr_node:
            if self.getHeight(curr_node.left) > self.getHeight(curr_node.right):
                count = count * 2
                curr_node = curr_node.left
            else:
                if curr_node.right:
                    count = count * 2 + 1
                curr_node = curr_node.right
        return count
