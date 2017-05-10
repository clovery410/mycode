class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(-1)
        tail = dummy
        pre, cur = head, head.next
        
        while cur:
            if cur.val == pre.val:
                while cur and cur.val == pre.val:
                    cur = cur.next
                pre = cur
                if cur: cur = cur.next
                continue
            else:
                tail.next = pre
                tail = tail.next
                pre = pre.next
                cur = cur.next
                
        tail.next = pre
        return dummy.next
