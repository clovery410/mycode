class Solution(object):
    def reverseVowels(self, s):
        s_list = list(s)
        start, end = 0, len(s_list) - 1
        while start < end:
            c1, c2 = s_list[start], s_list[end]
            if c1.lower() in 'aeiou' and c2.lower() in 'aeiou':
                s_list[start], s_list[end] = s_list[end], s_list[start]
                start += 1
                end -= 1
            if c1.lower() not in 'aeiou':
                start += 1
            if c2.lower() not in 'aeiou':
                end -= 1
        return ''.join(s_list)

            
