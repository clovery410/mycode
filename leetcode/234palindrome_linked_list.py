class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second_head = self.reverseLinkedList(slow.next)
        curr1, curr2 = head, second_head
        while curr2:
            if curr1.val != curr2.val:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        return True

    def reverseLinkedList(self, head):
        if head is None or head.next is None:
            return head
        prev_node, curr_node = head, head.next
        prev_node.next = None
        while curr_node:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp
        return prev_node
