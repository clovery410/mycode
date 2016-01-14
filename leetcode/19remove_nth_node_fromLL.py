class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        start_node = head
        if n == 0:
            return head
        if head is None or head.next is None:
            return None

        i = 1
        while i <= n:
            start_node = start_node.next
            i += 1
        if start_node is None:
            return head.next

        second_node = head
        while start_node.next is not None:
            start_node = start_node.next
            second_node = second_node.next
        second_node.next = second_node.next.next

        return head
