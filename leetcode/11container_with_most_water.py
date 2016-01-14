class Solution(object):
    #This running time is n^2, time limit exceeded
    def maxArea(self, height):
        n = len(height)
        curr_max = 0
        for i in xrange(n):
            for j in xrange(i+1, n):
                curr = min(height[i], height[j]) * (j - i)
                if curr > curr_max:
                    curr_max = curr
                    
        return curr_max

    # This solution misunderstands the question, which fullfills each bar
    def recurse_help(self, height, left, right):
        if left >= right:
            return 0
        elif right - left == 1:
            return min(height[left], height[right])
        
        curr_i, curr_min = left, height[left]
        for i in xrange(left+1, right+1):
            if height[i] < curr_min:
                curr_i, curr_min = i, height[i]
        left_max = self.recurse_help(height, left, curr_i-1)
        right_max = self.recurse_help(height, curr_i+1, right)

        return max(left_max, right_max, curr_min * (right - left))
    
    def second_solution(self, height):
        n = len(height)

        return self.recurse_help(height, 0, n-1)

    # This algorithem works, AC version
    def correct_solution(self, height):
        n = len(height)
        i, j = 0, n-1
        ans = min(height[0], height[-1]) * (n - 1)
        
        while j > i:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            curr_max = min(height[i], height[j]) * (j - i)
            ans = max(ans, curr_max)

        return ans
    
if __name__ == '__main__':
    sol = Solution()
    array = [1,7,1,3,4,5,2]

#    print sol.second_solution(array)
    print sol.correct_solution(array)
