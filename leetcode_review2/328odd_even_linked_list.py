class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        pre1, pre2 = dummy1, dummy2
        cur1, cur2 = head, head.next

        while True:
            pre1.next = cur1
            pre1 = cur1
            pre2.next = cur2
            pre2 = cur2
            if cur2 is None or cur2.next is None:
                break
            cur1 = cur2.next
            cur2 = cur2.next.next
            
        pre1.next = dummy2.next
        return dummy1.next

        
