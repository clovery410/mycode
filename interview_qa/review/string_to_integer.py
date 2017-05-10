def stringToInteger(s):
    INT_MAX = 2 ** 31 - 1
    INT_MIN = - 2 ** 31
    s.lstrip(" ")
    sign = 1
    num = 0
    for c in s:
        if c == '-':
            sign = -1
        if c == '+' or c == ' ':
            continue
        else:
            num = num * 10 + int(c)
    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX
    return num

print stringToInteger('123')


123
321
0
-123
0123

Overflow

123xbdsalk

0b100010
0xcdef
0123

1e6
1e-6
        
