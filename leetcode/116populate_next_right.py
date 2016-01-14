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
        while start.left:
            curr = start
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                else:
                    curr.right.next = None
                curr = curr.next
            start = start.left

            
            
            
