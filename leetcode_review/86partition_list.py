class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        pre1 = dummy1
        pre2 = dummy2

        cur = head
        while cur:
            if cur.val < x:
                pre1.next = cur
                pre1 = pre1.next
            else:
                pre2.next = cur
                pre2 = pre2.next
            cur = cur.next
            
        pre2.next = None
        pre1.next = dummy2.next
        return dummy1.next
