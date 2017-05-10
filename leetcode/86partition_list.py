class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        if head is None or head.next is None:
            return head

        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        curr = head
        s_prev = dummy1
        ge_prev = dummy2

        while curr:
            if curr.val < x:
                s_prev.next = curr
                s_prev = s_prev.next
            else:
                ge_prev.next = curr
                ge_prev = ge_prev.next
            curr = curr.next
        s_prev.next = dummy2.next
        gr_prev.next = None
        return dummy1.next

    
                
