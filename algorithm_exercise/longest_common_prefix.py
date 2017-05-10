def longest_common_prefix(s):
    j = 0
    prefix = ''
    n = len(s)
    while True:
        if j >= len(s[0]):
            return prefix
        base = s[0][j]
        for i in xrange(1, n):
            if j >= len(s[i]) or s[i][j] != base :
                return prefix
        prefix += base
        j += 1

string = ['adbc', '', 'abcd']
print longest_common_prefix(string)
