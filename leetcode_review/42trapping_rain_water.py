class Solution(object):
    # wrong solution... want to use stack at first, but fail to include some cases
    def trap(self, height):
        stack = []
        res = 0
        lowest = 0
        for i, h in enumerate(height):
            print stack
            if h == 0:
                continue
            while len(stack) > 0 and h >= height[stack[-1]]:
                pre_idx = stack.pop()
                pre_h = height[pre_idx]
                res += (i - pre_idx - 1) * (pre_h - lowest)
                lowest = pre_h

            while len(stack) > 0 and i - stack[-1] > 1:
                res += (i - stack[-1] - 1) * (h - lowest)
                lowest = h
            else:
                stack.append(i)
                lowest = 0

        return res
    
    # reviewed the solution learned from discuss in last round
    def trap2(self, height):
        left, right = 0, len(height) - 1
        res = 0
        left_max = right_max = 0
        while left <= right:
            l_h, r_h = height[left], height[right]
            if l_h < r_h:
                if l_h < left_max:
                    res += (left_max - l_h)
                else:
                    left_max = l_h
                left += 1
            else:
                if r_h < right_max:
                    res += (right_max - r_h)
                else:x
                    right_max = r_h
                right -= 1
        return res
        

if __name__ == "__main__":
    sol = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height1 = [4,2,3]
    print sol.trap2(height)
