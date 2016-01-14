class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        if root is None:
            return
        
        start = root
        while True:
            if start.left or start.right:
                curr = start
                if curr.left:
                    head = curr.left
                    explored = True
                    start = start.left
                else:
                    head = curr.right
                    curr = curr.next
                    explored = False
                    start = start.right
                while curr:
                    if explored:
                        if curr.right:
                            tail = curr.right
                            head.next = tail
                            head = tail
                        curr = curr.next
                        explored = False
                    else:
                        if curr.left:
                            tail = curr.left
                            head.next = tail
                            head = tail
                        explored = True
                
            elif start.next:
                start = start.next
            else:
                break            


if __name__ == '__main__':
    node1 = TreeLinkNode(1)
    node2 = TreeLinkNode(2)
    node3 = TreeLinkNode(3)
    node4 = TreeLinkNode(4)
    node5 = TreeLinkNode(5)
    node7 = TreeLinkNode(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
#    node2.right = node5
    node3.right = node7

    sol = Solution()
    new_link_node = sol.connect(node1)
    print node4.next.val
