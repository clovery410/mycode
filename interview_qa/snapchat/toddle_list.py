class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class Solution(object):
    def __init__(self):
        self.cache = {}
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def toddle(self, t):
        for num in t:
            if num in self.cache:
                rm_node = self.cache[num]
                pre_node, pos_node = rm_node.prev, rm_node.next
                pre_node.next = pos_node
                pos_node.prev = pre_node
                del self.cache[num]

            else:
                new_node = ListNode(num)
                last_node = self.tail.prev
                last_node.next = new_node
                new_node.prev = last_node
                new_node.next = self.tail
                self.tail.prev = new_node
                self.cache[num] = new_node

    def getSelectedList(self):
        res = []
        cur_node = self.head.next
        while cur_node != self.tail:
            res.append(cur_node.val)
            cur_node = cur_node.next
        return res

if __name__ == "__main__":
    sol = Solution()
    sol.toddle(['a', 'b', 'a', 'c'])
    print sol.getSelectedList()
    sol.toddle(['a'])
    print sol.getSelectedList()
    
    
