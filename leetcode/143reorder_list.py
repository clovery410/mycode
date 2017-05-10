class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #Solution1, brute-force solution
    def reorderList1(self, head):
        if head is None or head.next is None or head.next.next is None:
            return

        curr = head
        while curr.next and curr.next.next:
            pre_tail, tail = head, head.next
            while tail.next:
                tail = tail.next
                pre_tail = pre_tail.next
            curr.next, tail.next = tail, curr.next
            pre_tail.next = None
            curr = curr.next.next

    #Solution2,
    def reorderList2(self, head):
        if head is None or head.next is None or head.next.next is None:
            return
        
        #calculate length
        tail = head
        length = 1
        while tail.next:
            length += 1
            tail = tail.next
        mid = length / 2
        
        #locate the start of second half
        curr = head
        for i in xrange(mid):
            curr = curr.next
            
        #reverse right half
        right_pre, right_head = curr, curr.next
        right_pre.next = None
        
        while right_head:
            temp = right_head.next
            right_head.next = right_pre
            right_pre = right_head
            right_head = temp
            
        #combine two halfs
        left_curr = head
        right_curr = right_pre
        while right_curr.next and right_curr != left_curr:
            left_next = left_curr.next
            right_next = right_curr.next
            left_curr.next = right_curr
            right_curr.next = left_next
            left_curr = left_next
            right_curr = right_next

            
