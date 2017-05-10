class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        
        last_odd = head
        first_even = pre_node = head.next
        curr_node = pre_node.next
        i = 3
        
        while curr_node:
            if i % 2 != 0:
                pre_node.next = curr_node.next
                last_odd.next = curr_node
                last_odd = pre_node = curr_node
                curr_node, i = curr_node.next, i + 1
            else:
                pre_node, curr_node = pre_node.next, curr_node.next
                i += 1
        last_odd.next = first_even
        return head
