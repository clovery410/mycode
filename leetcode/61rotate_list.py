class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head
        
        length = 1
        curr = head
        while curr.next:
            length += 1
            curr = curr.next
        tail = curr

        if k % length == 0:
            return head
        
        step = length - k % length
        dummy = ListNode(0)
        dummy.next = head
        new_head = head
        pre_new_head = dummy
        while step > 0:
            new_head = new_head.next
            pre_new_head = pre_new_head.next
            step -= 1

        pre_new_head.next = None
        tail.next = head
        return new_head

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    sol = Solution()
    new_head = sol.rotateRight(node1, 8)
    print new_head.val, new_head.next.val, new_head.next.next.val, new_head.next.next.next.val, new_head.next.next.next.next.val, new_head.next.next.next.next.next
