class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        stack = []
        
        i = 1
        start = head
        while i < m:
            mid_head = start
            start = start.next
            i += 1
            
        j = i
        while j < n:
            stack.append(start)
            start = start.next
            j += 1
            
        pos_head = start.next
        if m == 1:
            new_head = current = start
        else:
            new_head = head
            mid_head.next = current = start
            
        while stack:
            top = stack.pop()
            current.next = top
            current = top
        current.next = pos_head
        
        return new_head
