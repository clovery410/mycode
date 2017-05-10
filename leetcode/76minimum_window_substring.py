import sys
class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ''

        t_set = {}
        for c in t:
            if c not in t_set:
                t_set[c] = 0
            t_set[c] += 1

        count, d = len(t), sys.maxint
        begin = end = head = 0
        while end < len(s):
            if s[end] in t_set and t_set[s[end]] > 0:
                t_set[s[end]] -= 1
                count -= 1
            end += 1

            while count == 0:
                if end - begin < d:
                    d = end - begin
                    head = begin
                    print head, d
                old_begin = s[begin]
                begin += 1

                while s[begin] not in t_set:
                    begin += 1
                if s[begin] != old_begin:
                    count += 1
                    t_set[old_begin] += 1

        if d < sys.maxint:
            return s[head:head + d]
        return ''

if __name__ == '__main__':
    sol = Solution()
    s = 'ADOBECODECANB'
    t = 'ABC'
    print sol.minWindow(s, t)
                

            

            
