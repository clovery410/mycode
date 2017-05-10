class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #Solution1, 3-way partition quicksort
    def sortList1(self, head):
        #Base case
        if head is None or head.next is None:
            return head

        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        prev1 = dummy1
        prev2 = dummy2
        curr = head.next
        prev = head

        while curr:
            if curr.val < head.val:
                prev1.next = curr
                prev1 = prev1.next
            elif curr.val > head.val:
                prev2.next = curr
                prev2 = prev2.next
            else:
                prev.next = curr
                prev = prev.next
            curr = curr.next

        prev.next = prev1.next = prev2.next = None
        dummy1.next = self.sortList1(dummy1.next)
        dummy2.next = self.sortList1(dummy2.next)

        prev1 = dummy1
        while prev1.next:
            prev1 = prev1.next
        prev1.next = head
        prev.next = dummy2.next

        return dummy1.next

    #Solution2, using bottom-up merge sort
        

if __name__ == "__main__":
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(-1)
    node4 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    sol = Solution()
    new_head = sol.sortList(node1)
    print new_head.val, new_head.next.val, new_head.next.next.val, new_head.next.next.next.val
    
                
                
