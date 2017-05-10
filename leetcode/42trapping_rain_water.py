class Solution(object):
    #Solution1, too complicated...
    def trap(self, height):
        if len(height) == 0:
            return 0
        left = 0
        while left < len(height) and height[left] == 0:
            left += 1
        right = left + 1
        stack = []
        res = 0
        while right < len(height):
            print stack
            curr_height = height[right]
            if len(stack) == 0:
                if curr_height >= height[left]:
                    left = right
                else:
                    stack.append(curr_height)
            else:
                if curr_height <= stack[-1]:
                    stack.append(curr_height)
                elif curr_height < height[left]:
                    count = 0
                    while len(stack) > 0 and stack[-1] < curr_height:
                        top = stack.pop()
                        res += (curr_height - top)
                        count += 1
                    while count >= 0:
                        stack.append(curr_height)
                        count -= 1
                else:
                    while len(stack) > 0:
                        top = stack.pop()
                        res += (height[left] - top)
                    left = right
            right += 1
        return res

    #Solution2, learned from discuss, two pointers begins at each side, approach against eath other
    def trap2(self, height):
        left, right = 0, len(height) - 1
        maxLeft = maxRight = 0
        res = 0
        while left <= right:
            if height[left] < height[right]:
                if height[left] < maxLeft:
                    res += maxLeft - height[left]
                else:
                    maxLeft = height[left]
                left += 1
            else:
                if height[right] < maxRight:
                    res += maxRight - height[right]
                else:
                    maxRight = height[right]
                right -= 1
        return res
    
if __name__ == "__main__":
    height = [5,2,1,2,1,5]
    sol = Solution()
    print sol.trap(height)
    print sol.trap2(height)                    

                    
            
