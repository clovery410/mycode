import heapq
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        if lists is None:
            return None
        
        hq = []
        dummy = ListNode(0)
        prev = dummy
        for node in lists:
            if node:
                heapq.heappush(hq, (node.val, node))
        while len(hq) > 0:
            curr_node = heapq.heappop(hq)[1]
            prev.next = curr_node
            prev = prev.next
            curr_node = curr_node.next
            if curr_node:
                heapq.heappush(hq, (curr_node.val, curr_node))
        return dummy.next

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(3)
    node1.next = node2

    node4 = ListNode(2)
    node5 = ListNode(4)
    node6 = ListNode(5)
    node4.next = node5
    node5.next = node6

    node7 = ListNode(3)
    node8 = ListNode(5)
    node9 = ListNode(6)
    node7.next = node8
    node8.next = node9

    sol = Solution()
    new_head = sol.mergeKLists([node1, node4, node7, None])
    print new_head.val, new_head.next.val, new_head.next.next.val, new_head.next.next.next.val
