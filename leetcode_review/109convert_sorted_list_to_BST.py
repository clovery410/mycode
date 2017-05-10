from collections import deque
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        if head is None:
            return None
        n = 0
        node = head
        while node:
            node = node.next
            n += 1
        root = self.makeTree(0, n-1)
        self.inorder(root, head)
        return root

    def makeTree(self, s, e):
        if s <= e:
            mid = (e - s) / 2 + s
            node = TreeNode(0)
            node.left = self.makeTree(s, mid-1)
            node.right = self.makeTree(mid+1, e)
            return node
        else:
            return None

    def inorder(self, node, llNode):
        if node is None:
            return llNode
        cur_ll = self.inorder(node.left, llNode)
        node.val = cur_ll.val
        cur_ll = cur_ll.next
        return self.inorder(node.right, cur_ll)

    #Solution2, use fast and slow two pointers
    def sortedListToBST(self, head):
        if head is None:
            return None
        

if __name__ == "__main__":
    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln3 = ListNode(3)
    ln4 = ListNode(4)
    ln5 = ListNode(5)

    ln1.next = ln2
    ln2.next = ln3
    ln3.next = ln4
    ln4.next = ln5

    sol = Solution()
    print sol.sortedListToBST(ln1).val
