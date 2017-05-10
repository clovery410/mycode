class Solution(object):
    def maxArea(self, height):
        s, e = 0, len(height) - 1
        area = 0
        while s < e:
            h1, h2 = height[s], height[e]
            area = max(area, min(h1, h2) * (e - s))
            if h1 <= h2:
                s += 1
            else:
                e -= 1
        return area

if __name__ == "__main__":
    sol = Solution()
    print sol.maxArea([1, 2, 3, 6, 2, 1])
