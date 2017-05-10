class Solution(object):
    def reverseString(self, s):
        s_list = list(s)
        start, end = 0, len(s_list) - 1
        while start < end:
            s_list[start], s_list[end] = s_list[end], s_list[start]
            start += 1
            end -= 1
        return ''.join(s_list)
