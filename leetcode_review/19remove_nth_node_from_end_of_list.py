class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        pre = dummy
        pre.next = head
        fast = head
        for i in xrange(n-1):
            fast = fast.next
        slow = head
        while fast and fast.next:
            fast = fast.next
            pre, slow = pre.next, slow.next
        pre.next = pre.next.next
        return dummy.next
