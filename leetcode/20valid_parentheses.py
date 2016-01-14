class Solution(object):
    def isValid(self, s):
        n = len(s)
        if n <= 0:
            return True
        if n % 2 != 0:
            return False
        
        s_copy = s
        while s_copy:
            i, j = 0, 1
            _l = len(s_copy)
            while j < _l:
                pre, pos = s_copy[i], s_copy[j]
                if pre == '(' and pos == ')' or pre == '[' and pos == ']' or pre == '{' and pos == '}':
                    s_copy = s_copy[:i] + s_copy[j+1:]
                    break
                i += 1
                j += 1
            if _l == len(s_copy):
                return False
        return True
