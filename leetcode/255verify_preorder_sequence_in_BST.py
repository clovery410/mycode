class Solution(object):
    def verifyPreorder(self, preorder):
        if len(preorder) <= 2:
            return True
        target = preorder[0]
        for mid in xrange(1, len(preorder)):
            if mid == len(preorder) - 1:
                return self.verifyPreorder(preorder[1:])
            if preorder[mid] > target > preorder[mid+1]:
                return False
            if preorder[mid] < target < preorder[mid+1]:
                left = preorder[1:mid]
                right = preorder[mid+1:]
                if all(x < target and y > target for x in left for y in right):
                    return self.verifyPreorder(left) and self.verifyPreorder(right)

    # Follow-up, use constanct space, but this solution TLE
    def verifyPreorder2(self, preorder):
        def checkValid(start, end):
            if end - start <= 1:
                return True
            
            target = preorder[start]
            i = start + 1
            mid = end + 1
            left_finished = False
            while i <= end:
                if preorder[i] < target and left_finished:
                    return False
                if (i - 1 == start or preorder[i-1] < target) and preorder[i] > target:
                    mid = i
                    break
                if preorder[i] > target:
                    left_finished = True
                i += 1
            if checkValid(start + 1, mid - 1) and checkValid(mid, end):
                return True
            else:
                return False
        return checkValid(0, len(preorder) - 1)

    # solution3, linear running time and linear space
    def verifyPreorder3(self, preorder):
        import sys
        stack = []
        lo_val = -sys.maxint - 1
        for val in preorder:
            if val <= lo_val:
                return False
            while stack and val > stack[-1]:
                lo_val = stack.pop()
            stack.append(val)
        return True

if __name__ == "__main__":
    sol = Solution()
    order = [1, 3, 4, 5, 6, 8, 9]
    print sol.verifyPreorder(order)
    print sol.verifyPreorder2(order)
    print sol.verifyPreorder3(order)
        
