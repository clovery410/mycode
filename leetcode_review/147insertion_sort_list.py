class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        curr_node = head
        next_node = head.next

        while next_node:
            if next_node.val >= curr_node.val:
                curr_node = curr_node.next
                next_node = next_node.next
            else:
                temp = next_node.next
                prev_node, scan_node = dummy, dummy.next
                while scan_node.val < next_node.val:
                    prev_node = scan_node
                    scan_node = scan_node.next
                prev_node.next = next_node
                next_node.next = scan_node

                curr_node.next = temp
                next_node = temp
        return dummy.next

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node3.next = node2
    node2.next = node1

    sol = Solution()
    new_head = sol.insertionSortList(node3)
    print new_head.val, new_head.next.val, new_head.next.next.val, new_head.next.next.next
                
        
