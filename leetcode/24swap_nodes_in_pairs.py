class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        #Corner case
        if head is None or head.next is None:
            return head
        new_head = head.next
        next_head = head.next.next
        tail = pre_tail = head
        new_head.next = head
        while next_head:
            if next_head.next:
                pre_tail.next = next_head.next
                temp = next_head.next.next
                next_head.next.next = next_head
                next_head.next = temp
                tail = next_head
                next_head = temp
            else:
                pre_tail.next = next_head
                tail = next_head
                break
        tail.next = None
        return new_head

    #Second solution, more concised version
    def swapPairs2(self, head):
        dummy_head = ListNode(0)
        dummy_head.next = head
        pre_tail, next_head = dummy_head, head
        
        while next_head:
            if next_head.next:
                temp = next_head.next.next
                pre_tail.next, next_head.next.next = next_head.next, next_head
                next_head.next = temp
                pre_tail, next_head = next_head, temp
            else:
                pre_tail.next = next_head
                break
        return dummy_head.next

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    # node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    # node3.next = node4

    sol = Solution()
    new_head = sol.swapPairs(node1)
    print new_head.val
    print new_head.next.val
    print new_head.next.next.val
    print new_head.next.next.next
    
