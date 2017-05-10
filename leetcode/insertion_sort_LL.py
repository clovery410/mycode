class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertion_sort_ll(self, head):
        if head is None or head.next is None:
            return head

        new_head = ListNode(-1)
        new_head.next = head
        tail = head
        current = head.next
        while current:
            if current.val >= tail.val:
                tail = current
                current = current.next
            else:
                pre_node = new_head
                start = pre_node.next
                while start.val < current.val:
                    start = start.next
                    pre_node = pre_node.next
                next_node = current.next
                pre_node.next, current.next = current, start
                tail.next, current = next_node, next_node

        s = new_head.next
        while s:
            print s.val
            s = s.next
        return new_head.next

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node2.next = node1
    node1.next = node5
    node5.next = node3
    node3.next = node4

    sol = Solution()
    sol.insertion_sort_ll(node2)
