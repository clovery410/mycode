def count1(n):
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    return count

def count2(n):
    count = 0
    while n > 0:
        n &= (n-1)
        count += 1
    return count

print count1(127)
print count2(127)
