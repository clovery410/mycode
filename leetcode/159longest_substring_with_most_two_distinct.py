from collections import deque
class Solution(object):
    #First solution by me, a little bit ugly...
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        
        freq = []
        pre = curr = s[0]
        count = 1
        for i in xrange(1, len(s)):
            curr = s[i]
            if curr != pre:
                freq.append((pre, count))
                pre = curr
                count = 1
            else:
                count += 1
        freq.append((curr, count))
        
        queue = deque()
        curr_count = max_count = 0
        for i in xrange(len(freq)):
            if freq[i][0] in queue:
                curr_count += freq[i][1]
            elif len(queue) < 2:
                queue.append(freq[i][0])
                curr_count += freq[i][1]
            else:
                max_count = max(max_count, curr_count)
                if freq[i-1][0] == queue[1]:
                    queue.popleft()
                else:
                    queue.pop()
                queue.append(freq[i][0])
                curr_count = freq[i-1][1] + freq[i][1]
        return max(max_count, curr_count)

    #second solution
    def lengthOfLongestSubstringTwoDistinct2(self, s):
        if len(s) <= 2:
            return len(s)
        visited = {}
        start = tmp = 0
        max_count = diff = 0
        
        for i in xrange(len(s)):
            if s[i] not in visited:
                if diff == 2:
                    max_count = max(max_count, i-start)
                    start = tmp
                    visited = {}
                    visited[s[i-1]] = True
                else:
                    diff += 1
                visited[s[i]] = True
                tmp = i
            elif s[i] != s[i-1]:
                tmp = i
                
        return max(max_count, i + 1 -start)
