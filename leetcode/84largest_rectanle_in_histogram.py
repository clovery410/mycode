class Solution(object):
    # O(n^2) solution, hit TLE
    def largestRectangleArea(self, heights):
        if len(heights) == 0:
            return 0
        res = 0
        for i in range(len(heights)):
            cur_max = cur_low = heights[i]
            for j in range(i+1, len(heights)):
                if heights[j] < cur_low:
                    cur_low = heights[j]
                cur_max = max(cur_max, cur_low * (j-i+1))
            res = max(res, cur_max)
        return res

    #Solution2
    def largestRectangleArea2(self, heights):
        i = 0
        res = 0
        stack = []
        heights.append(-1)
        while i < len(heights):
            if len(stack) == 0 or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[top] if len(stack) > 0 else i * heights[top])
        return res
                    
                
if __name__ =="__main__":
    heights = [2,1,5,6,2,3]
    sol = Solution()
    print sol.largestRectangleArea(heights)
    print sol.largestRectangleArea2(heights)
