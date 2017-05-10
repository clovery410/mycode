class Solution(object):
    def minWindow(self, s, t):
        t_count = collections.defaultdict(int)
        for c in t:
            t_count[c] += 1

        counter = len(t)
        start, end, minStart, minLen = 0, 0, 0, len(s) + 1
        while end < len(s):
            c = s[end]
            if t_count[c] > 0:
                counter -= 1
            t_count[c] -= 1

            end += 1

            while counter == 0:
                if end - start < minLen:
                    minLen = end - start
                    minStart = start
                t_count[s[start]] += 1
                if t_count[s[start]] > 0:
                    counter += 1
                start += 1

        if minLen == len(s) + 1:
            return ''
        else:
            return s[minStart:minStart+minLen]

                
                
        
            
