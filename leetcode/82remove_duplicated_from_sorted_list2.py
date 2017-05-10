class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)
        prev_node = dummy
        curr_node = head
        next_node = head.next

        while next_node:
            if next_node.val != curr_node.val:
                prev_node.next = curr_node
                prev_node = curr_node
                curr_node = next_node
                next_node = next_node.next
            else:
                while next_node and next_node.val == curr_node.val:
                    next_node = next_node.next
                if next_node is not None:
                    curr_node = next_node
                    next_node = next_node.next
                else:
                    prev_node.next = None
                    return dummy.next
        prev_node.next = curr_node
        return dummy.next
                
