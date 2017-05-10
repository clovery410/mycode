def isPalindromeNumber(num):
    if num < 0:
        return False
    
    k = num
    lo = hi = 1
    while k > 10:
        hi *= 10
        k /= 10
    while hi > lo:
        hi_digit = num / hi % 10
        lo_digit = num / lo % 10
        if hi_digit != lo_digit:
            return False
        hi /= 10
        lo *= 10
    return True

print isPalindromeNumber(123421)
