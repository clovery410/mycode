class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        def reverseSublist(head, tail):
            prev, curr = head, head.next
            while curr != tail:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            curr.next = prev
            return tail, head

        if k <= 1:
            return head
        
        dummy = ListNode(0)
        pre = dummy
        pre.next = head
        curr = head
        while curr:
            for i in xrange(k-1):
                curr = curr.next
                if not curr:
                    return dummy.next
            next_head = curr.next
            new_head, new_tail = reverseSublist(pre.next, curr)
            pre.next = new_head
            new_tail.next = next_head
            pre = new_tail
            curr = next_head
        return dummy.next
            
                
