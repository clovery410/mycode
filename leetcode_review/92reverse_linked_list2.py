class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        if head is None or head.next is None or m == n:
            return head

        dummy = ListNode(0)
        pre = dummy
        curr = head
        index = 1

        while index < m:
            pre.next = curr
            pre = pre.next
            curr = curr.next
            index += 1
        left, right = curr, curr.next
        index += 1
        while index <= n:
            temp = right.next
            right.next = left
            left = right
            right = temp
            index += 1
        curr.next = right
        pre.next = left
        return dummy.next

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    sol = Solution()
    new_head = sol.reverseBetween(node1, 2, 4)
    print new_head.val, new_head.next.val, new_head.next.next.val, new_head.next.next.next.val, new_head.next.next.next.next
