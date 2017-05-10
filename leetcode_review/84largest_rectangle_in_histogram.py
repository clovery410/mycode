class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(-1)
        
        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                top_idx = stack.pop()
                max_area = max(max_area, (i - stack[-1] - 1) * heights[top_idx] if len(stack) > 0 else i * heights[top_idx])
            stack.append(i)

        return max_area

if __name__ == "__main__":
    sol = Solution()
    heights = [2,1,2]
    print sol.largestRectangleArea(heights)
