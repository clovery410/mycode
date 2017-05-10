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
    #Solution1, this solution constructs the BST recursively, but it changes the original list although it runs really fast
    def sortedListToBST(self, head):
        #Corner case
        if head is None:
            return None
        #use slow-fast pointer to get the middle node
        pre = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        if pre is None:
            head = None
        else:
            pre.next = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root

    #Solution2, O(n) time, 3 steps
    def sortedListToBST2(self, head):
        #Check None
        if head is None:
            return None
        #First, calculate the length of linked list
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        #pre-order traverse to construct BST
        root = self.makeTree(length)

        #in-order dfs traverse to assign the node value
        self.inorder(root, head)
        return root

    #This makeTree function called recursivly
    def makeTree(self, n):
        if n == 0:
            return None
        root = TreeNode(0)
        left_length = (n - 1) / 2
        right_length = n - 1 - left_length
        root.left = self.makeTree(left_length)
        root.right = self.makeTree(right_length)
        return root

    #This makeTree function is iterative, O(n)
    def makeTree2(self, n):
        root = TreeNode(0)
        queue = deque([root])
        n -= 1
        while True:
            if n == 0:
                break
            curr_node = queue.popleft()
            left_child = TreeNode(0)
            n -= 1
            curr_node.left = left_child
            queue.append(left_child)
            if n == 0:
                break
            right_child = TreeNode(0)
            n -= 1
            curr_node.right = right_child
            queue.append(right_child)
            if n == 0:
                break
        return root

    def inorder(self, root, list_node):
        if root.left is not None:
            list_node = self.inorder(root.left, list_node)
        root.val = list_node.val
        list_node = list_node.next
        if root.right is not None:
            list_node = self.inorder(root.right, list_node)
        return list_node
            
        
        
            
