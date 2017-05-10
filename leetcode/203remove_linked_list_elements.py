class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0)
        prev = dummy
        curr = head

        while curr:
            if curr.val != val:
                prev.next = curr
                prev = prev.next
            curr = curr.next

        prev.next = None
        return dummy.next
