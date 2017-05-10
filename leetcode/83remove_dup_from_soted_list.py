class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return None
    
        record = {}
        record[head.val] = 1
        start, tail = head.next, head
        
        while start:
            if start.val in record:
                tail.next = start.next
            else:
                record[start.val] = 1
                tail = tail.next
            start = start.next
        return head
