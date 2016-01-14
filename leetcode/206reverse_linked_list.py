class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        first_node = head
        tail = head.next

        while head and tail:
            temp = tail.next
            tail.next = head
            head = tail
            tail = temp

        first_node.next = None

        return head

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    sol = Solution()
    new_head = sol.reverseList(node1)
    print new_head.val
            
