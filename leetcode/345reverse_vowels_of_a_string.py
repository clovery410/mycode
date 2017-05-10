class Solution(object):
    def reverseVowels(self, s):
        temp = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s, e = 0, len(temp) - 1
        while s < e:
            if temp[s] in vowels and temp[e] in vowels:
                temp[s], temp[e] = temp[e], temp[s]
                s += 1
                e -= 1
            elif temp[s] in vowels:
                e -= 1
            elif temp[e] in vowels:
                s += 1
            else:
                s += 1
                e -= 1
                
        return ''.join(temp)
