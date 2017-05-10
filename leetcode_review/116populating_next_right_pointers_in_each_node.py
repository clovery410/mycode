class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        cur_node = root
        while cur_node.left:
            start_node = cur_node
            while start_node:
                start_node.left.next = start_node.right
                if start_node.next:
                    start_node.right.next = start_node.next.left
                start_node = start_node.next
            cur_node = cur_node.left
            




            
