class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #Solution1, works, space complexity is good, but time complexity is bad...
    def detectCycle(self, head):
        def checkCycle(head):
            first = second = head
            while first and first.next:
                first = first.next.next
                second = second.next
                if first == second:
                    return first
            return None
        
        in_cycle_node = checkCycle(head)
        if in_cycle_node is None:
            return None
        p1, p2 = head, in_cycle_node
        while p1 != p2:
            p2 = p2.next
            if p2 == in_cycle_node:
                p1 = p1.next
        return p1

    #Solution2, using Floyd's cycle-finding algorithm, assume the distance from head to start of cycle is x, distance from start of cycle to the meet point which slow travels is y, distance from meeting point to the start of cycle is z, then we know that slow has covered distance d = x + y, fast has covered distance 2 * d = x + y + z + y => we have x = z. Thus, after getting meeting point if one pointer is placed to the beginning, then moving both with equal distance, they will meet at the start of loop
    def detectCycle2(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow2 = head
                while slow2 != slow:
                    slow2 = slow2.next
                    slow = slow.next
                return slow
        return None

if __name__ == "__main__":
    Node1 = ListNode(1)
    Node2 = ListNode(2)
    Node3 = ListNode(3)
    Node4 = ListNode(4)

    Node1.next = Node2
    Node2.next = Node3
    Node3.next = Node4
    Node4.next = Node1

    sol = Solution()
    print sol.detectCycle2(Node1).val
