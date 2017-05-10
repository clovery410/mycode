class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        def getFirst(node):
            while node and not node.left and not node.right:
                node = node.next
            return node
        
        if root is None:
            return
        cur_node = root
        while cur_node:
            frist_parent = getFirst(cur_node)
            if first_parent:
                cur_node = first_parent.left if first_parent.left else first_parent.right
            else:
                cur_node = None
                
            while first_parent:
                if first_parent.right:
                    if first_parent.left:
                        first_parent.left.next = first_parent.right
                    pre = first_parent.right
                else:
                    pre = first_parent.left
                second_parent = getFirst(first_parent.next)
                if second_parent:
                    if second_parent.left:
                        pre.next = second_parent.left
                    else:
                        pre.next = second_parent.right
                first_parent = second_parent

    #Solution2, make use of a dummy node
    def connect2(self, root):
        if root is None:
            return
        curr = root
        while curr:
            dummy = TreeLinkNode(0)
            pre = dummy
            start = curr
            while start:
                if start.left:
                    pre.next = start.left
                    pre = pre.next
                if start.right:
                    pre.next = start.right
                    pre = pre.next
                start = start.next
            curr = dummy.next
            
                    
