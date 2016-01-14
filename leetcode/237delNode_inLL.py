class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        next_node = node.next
        if next_node is None:
            node = None
        else:
            node.val = next_node.val
            node.next = next_node.next
