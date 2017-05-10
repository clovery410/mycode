class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        
        pre, cur = head, head.next
        while cur:
            if cur.val > pre.val:
                pre.next = cur
                pre = cur
            cur = cur.next
        pre.next = None

        return head
        
