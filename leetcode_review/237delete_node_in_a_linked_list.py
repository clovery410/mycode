class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None:
            return
        
        pre, cur = node, node.next
        while cur:
            pre.val = cur.val
            cur = cur.next
            if not cur:
                break
            pre = pre.next
        pre.next = None

    # solution2, last round solution, O(1)
    def deleteNode2(self, node):
        next_node = node.next

        node.val = next_node.val
        node.next = next_node.next
