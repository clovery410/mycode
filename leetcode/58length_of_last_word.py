class Solution(object):
    def lengthOfLastWord(self, s):
        last = curr = i = 0
        for item in s:
            if item != ' ':
                curr += 1
            else:
                if curr == 0:
                    continue
                last = curr
                curr = 0
                
        if curr == 0:
            return last
        return curr
