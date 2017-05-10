class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def invert_linked_list(self, head):
        if head is None or head.next is None:
            return head
        first_head = head
        second_head = head.next
        head.next = None
        
        while second_head:
            temp = second_head.next
            second_head.next = first_head
            first_head = second_head
            second_head = temp

        return first_head

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

sol = Solution()
new_head = sol.invert_linked_list(node1)
print new_head.val, new_head.next.val, new_head.next.next.val, new_head.next.next.next.val
